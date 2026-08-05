#!/usr/bin/env python3
"""Build an OKF v0.2 bundle from the ScalarDB / ScalarDL documentation.

Usage
-----
    python3 tools/okf_build.py                 # sync sources and rebuild everything
    python3 tools/okf_build.py --only-new      # add versions that are not in the bundle yet
    python3 tools/okf_build.py --offline       # rebuild from the cached clones
    python3 tools/okf_build.py --products scalardb --versions 3.17,3.18

The bundle is written to okf/ and is a conformant OKF bundle: every non-reserved
.md file carries YAML frontmatter with a non-empty `type`, concepts link to each
other with ordinary Markdown links, and index.md / log.md are used for directory
listings and update history.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from okf_common import (  # noqa: E402
    GENERATOR, LIFECYCLE_LABELS, LIFECYCLE_ORDER, OKF_VERSION, now, slugify_tag,
    write_concept,
)
from okf_mdx import (  # noqa: E402
    MdxConverter, extract_description, extract_title, rewrite_links,
    split_frontmatter,
)
from okf_repo import RepoVersionBuilder, write_repo_product_index  # noqa: E402
from okf_sources import (  # noqa: E402
    PRODUCTS, PRODUCTS_BY_KEY, DocVersion, Product, classify, discover_versions,
    index_sidebar, load_sidebar, sync_repo, sync_repo_versions,
)

# Upstream page tags mix two vocabularies: which edition a feature belongs to
# and what release status the feature is in.  They are kept apart here so a
# consumer never mistakes "Deprecated" for an edition.
FEATURE_STATUS_TAGS = {"Deprecated", "Private Preview", "Public Preview"}
SKIP_DIRS = {"components", "images", "slides", "assets", "_partials"}

ROOT = Path(__file__).resolve().parent.parent


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def _is_empty(body: str, min_words: int = 12) -> bool:
    """True when a page has no prose of its own.

    A handful of upstream pages exist only to render a navigation-card
    component or to redirect to the Japanese site; they would become empty
    concepts, so the generated index.md listings stand in for them instead.
    """
    text = re.sub(r"^#.*$", "", body, flags=re.M)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return len(re.findall(r"[A-Za-z0-9_]+", text)) < min_words


@dataclass
class Page:
    """One documentation page on its way into the bundle."""

    doc_id: str                 # "scalardb-cluster/overview"
    source: Path
    out_rel: str                # "scalardb-cluster/overview.md"
    directory: str              # "scalardb-cluster"
    title: str = ""
    description: str = ""
    concept_type: str = "Documentation Page"
    phase: str = "implement"
    breadcrumb: list[str] = field(default_factory=list)
    editions: list[str] = field(default_factory=list)
    feature_status: list[str] = field(default_factory=list)


# --------------------------------------------------------------------------
# Version build
# --------------------------------------------------------------------------

class VersionBuilder:
    def __init__(self, product: Product, version: DocVersion, repo_dir: Path,
                 repo_sha: str, repo_committed_at: str, out_dir: Path):
        self.product = product
        self.version = version
        self.repo_dir = repo_dir
        self.repo_sha = repo_sha
        self.repo_committed_at = repo_committed_at
        self.out_dir = out_dir
        self.converter = MdxConverter(repo_dir, version.docs_dir, version.patch)
        self.site_base = f"{product.site}/docs/{version.url_path}"
        self.pages: list[Page] = []
        self.unresolved: set[str] = set()
        self.skipped: list[str] = []

    # -- discovery --------------------------------------------------------

    def collect(self) -> None:
        docs = self.version.docs_dir
        for path in sorted(docs.rglob("*")):
            if not path.is_file() or path.suffix not in (".md", ".mdx"):
                continue
            rel = path.relative_to(docs)
            if any(part in SKIP_DIRS for part in rel.parts[:-1]):
                continue
            if rel.name.startswith("_"):
                continue

            doc_id = str(rel.with_suffix("")).replace("\\", "/")
            directory = str(rel.parent).replace("\\", "/")
            directory = "" if directory == "." else directory
            if rel.stem == "index":
                out_rel = f"{directory}/section-home.md" if directory else "section-home.md"
            else:
                out_rel = f"{doc_id}.md"
            self.pages.append(
                Page(doc_id=doc_id, source=path, out_rel=out_rel, directory=directory)
            )

    # -- conversion -------------------------------------------------------

    def build(self) -> None:
        sidebar = index_sidebar(load_sidebar(self.version))

        # First pass: convert, and discard pages that carry no prose (redirect
        # stubs and pages whose whole body is a navigation-card component).
        converted: list[tuple[Page, str]] = []
        for page in self.pages:
            conv = self.converter.convert(page.source)
            self.unresolved |= {
                u for u in conv.unresolved
                if u not in {"Tabs", "TabItem", "CodeBlock", "DocCardList"}
            }

            upstream_fm = {}
            if conv.frontmatter:
                try:
                    upstream_fm = yaml.safe_load(conv.frontmatter) or {}
                except yaml.YAMLError:
                    upstream_fm = {}

            if _is_empty(conv.body):
                self.skipped.append(page.doc_id)
                continue

            page.breadcrumb = sidebar.get(page.doc_id, [])
            page.concept_type, page.phase = classify(page.doc_id, page.breadcrumb)
            page.title = upstream_fm.get("title") or extract_title(
                conv.body, page.doc_id.rsplit("/", 1)[-1].replace("-", " ").title()
            )
            page.description = (
                upstream_fm.get("description") or extract_description(conv.body)
            )
            raw_tags = upstream_fm.get("tags") or []
            upstream_tags = [t for t in raw_tags if isinstance(t, str)]
            page.editions = [t for t in upstream_tags if t not in FEATURE_STATUS_TAGS]
            page.feature_status = [t for t in upstream_tags if t in FEATURE_STATUS_TAGS]
            converted.append((page, conv.body))

        self.pages = [page for page, _ in converted]

        # Second pass: now that the concept set is final, resolve in-bundle links.
        to_md = {p.doc_id: p.out_rel for p in self.pages}
        for page, body in converted:
            self._emit_page(
                page, rewrite_links(body, to_md, self.site_base, page.directory)
            )

        self._emit_directory_indexes()

    def _page_url(self, page: Page) -> str:
        if page.doc_id == "index":
            return f"{self.site_base}/"
        if page.doc_id.endswith("/index"):
            return f"{self.site_base}/{page.doc_id[:-len('/index')]}/"
        return f"{self.site_base}/{page.doc_id}/"

    def _upstream_url(self, page: Page) -> str:
        rel = page.source.relative_to(self.repo_dir).as_posix()
        return f"{self.product.repo_url}/blob/{self.repo_sha}/{rel}"

    def _emit_page(self, page: Page, body: str) -> None:
        tags = [
            self.product.key,
            f"v{self.version.name}",
            f"phase:{page.phase}",
        ]
        if page.breadcrumb:
            tags += [f"section:{slugify_tag(page.breadcrumb[0])}"]
        tags += [f"edition:{slugify_tag(e)}" for e in page.editions]
        tags += [f"feature-status:{slugify_tag(s)}" for s in page.feature_status]
        if not self.version.supported:
            tags.append("unmaintained")

        fm = {
            "type": page.concept_type,
            "title": page.title,
            "description": page.description,
            "resource": self._page_url(page),
            "tags": tags,
            "status": self.version.status,
            "product": self.product.key,
            "product_title": self.product.title,
            "version": self.version.name,
        }
        if self.version.patch:
            fm["patch_version"] = self.version.patch
        fm.update({
            "doc_id": page.doc_id,
            "lifecycle_phase": page.phase,
        })
        if page.breadcrumb:
            fm["breadcrumb"] = page.breadcrumb
        if page.editions:
            fm["editions"] = page.editions
        if page.feature_status:
            fm["feature_status"] = page.feature_status
        fm["generated"] = {"by": GENERATOR, "at": now()}
        fm["sources"] = [{
            "id": self.product.repo,
            "resource": self._upstream_url(page),
            "title": f"{self.product.title} documentation source (MDX)",
            "author": f"process:scalar-labs/{self.product.repo}",
            "last_modified": self.repo_committed_at,
        }]

        write_concept(self.out_dir / page.out_rel, fm, body)

    # -- directory listings ----------------------------------------------

    def _emit_directory_indexes(self) -> None:
        by_dir: dict[str, list[Page]] = {}
        for page in self.pages:
            by_dir.setdefault(page.directory, []).append(page)

        subdirs: dict[str, set[str]] = {}
        for directory in by_dir:
            parts = directory.split("/") if directory else []
            for i in range(len(parts)):
                parent = "/".join(parts[:i])
                subdirs.setdefault(parent, set()).add("/".join(parts[: i + 1]))

        for directory, pages in sorted(by_dir.items()):
            if directory == "":
                continue  # version root index is written by ProductBuilder
            self._write_dir_index(directory, pages, sorted(subdirs.get(directory, ())))

        # Directories that only hold subdirectories still need a listing.
        for directory in sorted(subdirs):
            if directory and directory not in by_dir:
                self._write_dir_index(directory, [], sorted(subdirs[directory]))

    def _write_dir_index(self, directory: str, pages: list[Page],
                         child_dirs: list[str]) -> None:
        name = directory.rsplit("/", 1)[-1]
        title = name.replace("-", " ").title()
        lines = [f"# {title}", ""]
        lines.append(
            f"{self.product.title} {self.version.name} documentation under "
            f"`{directory}/`."
        )
        lines.append("")

        home = next((p for p in pages if p.out_rel.endswith("section-home.md")), None)
        if home:
            lines += [f"Section overview: [{home.title}](./section-home.md)", ""]

        if child_dirs:
            lines += ["## Subsections", ""]
            for child in child_dirs:
                lines.append(f"- [{child.rsplit('/', 1)[-1]}](./{child.rsplit('/', 1)[-1]}/index.md)")
            lines.append("")

        listed = [p for p in pages if p is not home]
        if listed:
            lines += ["## Concepts", ""]
            for page in sorted(listed, key=lambda p: p.title.lower()):
                target = "./" + page.out_rel.rsplit("/", 1)[-1]
                desc = f" — {page.description}" if page.description else ""
                lines.append(f"- [{page.title}]({target}){desc}")
            lines.append("")

        fm = {
            "type": "Documentation Section",
            "title": f"{self.product.title} {self.version.name} — {title}",
            "description": (
                f"Directory listing for the `{directory}` section of the "
                f"{self.product.title} {self.version.name} documentation."
            ),
            "resource": f"{self.site_base}/{directory}/",
            "tags": [self.product.key, f"v{self.version.name}", "index"],
            "status": self.version.status,
            "product": self.product.key,
            "version": self.version.name,
            "generated": {"by": GENERATOR, "at": now()},
        }
        write_concept(self.out_dir / directory / "index.md", fm, "\n".join(lines))

    # -- version root ------------------------------------------------------

    def write_version_index(self) -> None:
        root_pages = [p for p in self.pages if p.directory == ""]
        by_phase: dict[str, list[Page]] = {}
        for page in self.pages:
            by_phase.setdefault(page.phase, []).append(page)

        banner = {
            "none": "Supported release.",
            "unmaintained": "**Unmaintained release.** Prefer a supported version "
                            "for new work; kept here for systems still running it.",
        }.get(self.version.banner, self.version.banner)

        lines = [
            f"# {self.product.title} {self.version.name}",
            "",
            banner,
            "",
            "| | |",
            "|---|---|",
            f"| Product | {self.product.title} |",
            f"| Documentation version | {self.version.name} |",
        ]
        if self.version.patch:
            lines.append(f"| Newest patch release described | {self.version.patch} |")
        lines += [
            f"| Docs site | {self.site_base}/ |",
            f"| Upstream source | {self.product.repo_url} @ `{self.repo_sha[:12]}` |",
            f"| Concepts in this version | {len(self.pages)} |",
            "",
            "## By lifecycle phase",
            "",
            "Start here when you know which phase of the project you are in.",
            "",
        ]
        for phase in LIFECYCLE_ORDER:
            pages = by_phase.get(phase) or []
            if not pages:
                continue
            lines += [f"### {LIFECYCLE_LABELS[phase]} ({len(pages)})", ""]
            for page in sorted(pages, key=lambda p: (p.directory, p.title.lower()))[:400]:
                lines.append(f"- [{page.title}](./{page.out_rel})")
            lines.append("")

        dirs = sorted({p.directory.split("/")[0] for p in self.pages if p.directory})
        if dirs:
            lines += ["## Sections", ""]
            lines += [f"- [{d}](./{d}/index.md)" for d in dirs]
            lines.append("")

        if root_pages:
            lines += ["## Top-level concepts", ""]
            for page in sorted(root_pages, key=lambda p: p.title.lower()):
                desc = f" — {page.description}" if page.description else ""
                lines.append(f"- [{page.title}](./{page.out_rel}){desc}")
            lines.append("")

        fm = {
            "type": "Product Version",
            "title": f"{self.product.title} {self.version.name}",
            "description": (
                f"Documentation set for {self.product.title} {self.version.name}"
                + (f" (newest patch {self.version.patch})" if self.version.patch else "")
                + "."
            ),
            "resource": f"{self.site_base}/",
            "tags": [self.product.key, f"v{self.version.name}", "product-version"]
                    + ([] if self.version.supported else ["unmaintained"]),
            "status": self.version.status,
            "product": self.product.key,
            "product_title": self.product.title,
            "version": self.version.name,
            **({"patch_version": self.version.patch} if self.version.patch else {}),
            "url_path": self.version.url_path,
            "maintenance": "supported" if self.version.supported else "unmaintained",
            "is_latest": self.version.is_current,
            "concept_count": len(self.pages),
            "generated": {"by": GENERATOR, "at": now()},
            "sources": [{
                "id": self.product.repo,
                "resource": f"{self.product.repo_url}/tree/{self.repo_sha}",
                "title": f"{self.product.title} documentation repository",
                "author": f"process:scalar-labs/{self.product.repo}",
                "last_modified": self.repo_committed_at,
            }],
        }
        write_concept(self.out_dir / "index.md", fm, "\n".join(lines))


# --------------------------------------------------------------------------
# Bundle assembly
# --------------------------------------------------------------------------

def write_product_index(product: Product, versions: list[DocVersion],
                        out_dir: Path, repo_sha: str, committed_at: str,
                        counts: dict[str, int]) -> None:
    lines = [
        f"# {product.title}",
        "",
        product.summary,
        "",
        "## Versions",
        "",
        "| Version | Newest patch | Maintenance | Concepts | Docs |",
        "|---|---|---|---|---|",
    ]
    for v in versions:
        latest = " (latest)" if v.is_current else ""
        lines.append(
            f"| [{v.name}{latest}](./{v.name}/index.md) | {v.patch or '—'} | "
            f"{'supported' if v.supported else 'unmaintained'} | "
            f"{counts.get(v.name, 0)} | {product.site}/docs/{v.url_path}/ |"
        )
    lines += [
        "",
        "## How to pick a version",
        "",
        "1. Match the version to the ScalarDB/ScalarDL release the project actually runs.",
        "2. If the project is greenfield, use the newest supported version.",
        "3. Never mix guidance across versions — configuration keys, error codes and "
        "API signatures differ between minor releases.",
        "",
    ]

    fm = {
        "type": "Product",
        "title": product.title,
        "description": product.summary.split(".")[0] + ".",
        "resource": f"{product.site}/docs/",
        "tags": [product.key, "product"],
        "status": "stable",
        "product": product.key,
        "versions": [v.name for v in versions],
        "latest_version": next((v.name for v in versions if v.is_current), versions[0].name),
        "supported_versions": [v.name for v in versions if v.supported],
        "generated": {"by": GENERATOR, "at": now()},
        "sources": [{
            "id": product.repo,
            "resource": f"{product.repo_url}/tree/{repo_sha}",
            "title": f"{product.title} documentation repository",
            "author": f"process:scalar-labs/{product.repo}",
            "last_modified": committed_at,
        }],
    }
    write_concept(out_dir / "index.md", fm, "\n".join(lines))


def write_bundle_index(bundle: Path, summary: dict) -> None:
    lines = [
        "# ScalarDB / ScalarDL Knowledge Bundle",
        "",
        "An OKF bundle containing the ScalarDB and ScalarDL product documentation "
        "published at developers.scalar-labs.com, plus the documentation ScalarDB Saga "
        "keeps in its source repository, split by product and by version so that an AI "
        "agent can be pointed at exactly the release a project runs.",
        "",
        "## Start here",
        "",
        "- [How to use this bundle](./guides/how-ai-agents-use-this-bundle.md) — read this first.",
        "- [Choosing a product, edition and version](./guides/product-and-version-selection.md)",
        "- [Keeping the bundle current](./guides/bundle-maintenance.md)",
        "",
        "## Products",
        "",
        "| Product | Latest | Versions | Concepts |",
        "|---|---|---|---|",
    ]
    for key, info in summary["products"].items():
        product = PRODUCTS_BY_KEY[key]
        lines.append(
            f"| [{product.title}](./products/{key}/index.md) | {info['latest']} | "
            f"{', '.join(info['versions'])} | {info['concepts']} |"
        )
    lines += [
        "",
        "## Layout",
        "",
        "```",
        "products/<product>/<version>/index.md      product version concept + navigation",
        "products/<product>/<version>/<page>.md     one concept per documentation page",
        "products/<product>/<version>/<dir>/        sections keep the upstream structure",
        "guides/                                    how to consume and maintain the bundle",
        "log.md                                     update history",
        "```",
        "",
        "## Conventions",
        "",
        "Every concept carries `product`, `version`, `lifecycle_phase` and `status` in its "
        "frontmatter, plus `resource` pointing at the canonical page on the docs site and "
        "`sources[]` pointing at the exact upstream commit it was generated from. "
        "`lifecycle_phase` is one of `design`, `implement`, `operate`.",
        "",
        "ScalarDB Saga has no documentation site yet, so its concepts are generated from "
        "the Markdown and contract files in `scalar-labs/scalardb-saga`, one release "
        "branch per version; their `resource` points at the file on GitHub, pinned to the "
        "commit they were built from. A version with no GA release is marked "
        "`status: draft` and tagged `pre-release`.",
        "",
    ]
    fm = {
        "type": "Knowledge Bundle",
        "title": "ScalarDB / ScalarDL Knowledge Bundle",
        "okf_version": OKF_VERSION,
        "description": (
            "ScalarDB, ScalarDL and ScalarDB Saga documentation organised per product "
            "and per version for AI-assisted design, implementation and operations."
        ),
        "resource": "https://developers.scalar-labs.com/",
        "tags": ["scalardb", "scalardl", "scalardb-saga", "bundle-root"],
        "status": "stable",
        "concept_count": summary["total_concepts"],
        "generated": {"by": GENERATOR, "at": now()},
    }
    write_concept(bundle / "index.md", fm, "\n".join(lines))


def append_log(bundle: Path, entry: str) -> None:
    log = bundle / "log.md"
    header = (
        "---\n"
        "type: Update Log\n"
        "title: Bundle update history\n"
        "description: Every generator run that changed this bundle, newest last.\n"
        f"generated:\n  by: {GENERATOR}\n"
        "---\n\n"
        "# Update history\n\n"
    )
    if not log.exists():
        log.write_text(header, encoding="utf-8")
    with log.open("a", encoding="utf-8") as fh:
        fh.write(entry.rstrip() + "\n\n")


# --------------------------------------------------------------------------
# Guides (written once, kept in the bundle)
# --------------------------------------------------------------------------

GUIDES_DIR = Path(__file__).resolve().parent / "guides"


def copy_guides(bundle: Path) -> None:
    dest = bundle / "guides"
    dest.mkdir(parents=True, exist_ok=True)
    for src in sorted(GUIDES_DIR.glob("*.md")):
        shutil.copyfile(src, dest / src.name)


# --------------------------------------------------------------------------
# Repository-sourced products
# --------------------------------------------------------------------------

def build_repo_product(product: Product, cache: Path, bundle: Path, state: dict,
                       summary: dict, changed: list[str], *,
                       wanted_versions: set[str], only_new: bool,
                       offline: bool) -> None:
    """Build a product whose documentation lives in its source repository.

    Its versions are release branches rather than `versioned_docs/` directories,
    and a branch keeps moving until the line is released, so a version is
    rebuilt whenever the branch head has moved — not only when it is new.
    """
    versions = sync_repo_versions(product, cache, offline=offline)
    if not versions:
        print("  (no release branches found)", flush=True)
        return

    repo_dir = cache / product.repo
    known = state["products"].get(product.key, {}).get("versions", {})
    counts: dict[str, int] = {v: known.get(v, {}).get("concepts", 0) for v in known}
    built_any = False

    for version in versions:
        if wanted_versions and version.name not in wanted_versions:
            continue
        if (only_new and version.name in known
                and known[version.name].get("sha") == version.sha):
            continue

        out_dir = bundle / "products" / product.key / version.name
        if out_dir.exists():
            shutil.rmtree(out_dir)

        builder = RepoVersionBuilder(product, version, repo_dir, out_dir)
        builder.build()
        builder.write_version_index()
        counts[version.name] = len(builder.built)
        built_any = True
        tag = "new" if version.name not in known else "rebuilt"
        changed.append(
            f"{product.title} {version.name} ({tag}, {len(builder.built)} concepts)"
        )
        missing = f"  missing {len(builder.missing)} source" if builder.missing else ""
        print(f"  {version.name:<6} {len(builder.built):>4} concepts  [{tag}]{missing}",
              flush=True)

    write_repo_product_index(
        product, versions, bundle / "products" / product.key, counts,
    )
    if not built_any:
        print("  (nothing to build)", flush=True)

    head = versions[0]
    state["products"][product.key] = {
        "repo": product.repo,
        "kind": "repo",
        "repo_sha": head.sha,
        "repo_committed_at": head.committed_at,
        "latest": head.name,
        "version_order": [v.name for v in versions],
        "versions": {
            v.name: {
                "patch": v.release,
                "sha": v.sha,
                "url_path": v.name,
                "maintenance": "pre-release" if v.prerelease else "supported",
                "concepts": counts.get(v.name, 0),
            }
            for v in versions if v.name in counts
        },
    }
    summary["products"][product.key] = {
        "latest": head.name,
        "versions": [v.name for v in versions],
        "concepts": sum(counts.get(v.name, 0) for v in versions),
    }
    summary["total_concepts"] += summary["products"][product.key]["concepts"]


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(ROOT / "okf"), help="bundle root")
    ap.add_argument("--cache", default=str(ROOT / ".cache"), help="upstream clone cache")
    ap.add_argument("--state", default=str(ROOT / ".okf-state.json"))
    ap.add_argument("--products", default="", help="comma-separated product keys")
    ap.add_argument("--versions", default="", help="comma-separated version numbers")
    ap.add_argument("--only-new", action="store_true",
                    help="build only versions absent from the state file (plus the latest)")
    ap.add_argument("--offline", action="store_true", help="do not touch the network")
    args = ap.parse_args()

    bundle = Path(args.out)
    cache = Path(args.cache)
    state_path = Path(args.state)
    state = json.loads(state_path.read_text()) if state_path.exists() else {"products": {}}

    wanted_products = [p.strip() for p in args.products.split(",") if p.strip()]
    wanted_versions = {v.strip() for v in args.versions.split(",") if v.strip()}
    products = [p for p in PRODUCTS if not wanted_products or p.key in wanted_products]

    summary = {"products": {}, "total_concepts": 0}
    changed: list[str] = []
    unresolved_all: set[str] = set()

    for product in products:
        print(f"[{product.key}] syncing {product.repo} ...", flush=True)

        if product.kind == "repo":
            build_repo_product(
                product, cache, bundle, state, summary, changed,
                wanted_versions=wanted_versions, only_new=args.only_new,
                offline=args.offline,
            )
            continue

        repo_state = sync_repo(product, cache, offline=args.offline)
        repo_dir = cache / product.repo
        versions = discover_versions(product, repo_dir)
        known = state["products"].get(product.key, {}).get("versions", {})

        counts: dict[str, int] = {v: known.get(v, {}).get("concepts", 0) for v in known}
        built_any = False

        for version in versions:
            if wanted_versions and version.name not in wanted_versions:
                continue
            if args.only_new and version.name in known and not version.is_current:
                # A version transition changes previously built content: the
                # old "latest" gains a numbered URL path, and end-of-support
                # flips concepts to deprecated.  Rebuild when that happened.
                prev = known[version.name]
                maintenance = "supported" if version.supported else "unmaintained"
                if (prev.get("url_path") == version.url_path
                        and prev.get("maintenance") == maintenance):
                    continue

            out_dir = bundle / "products" / product.key / version.name
            if out_dir.exists():
                shutil.rmtree(out_dir)

            builder = VersionBuilder(
                product, version, repo_dir, repo_state.sha,
                repo_state.committed_at, out_dir,
            )
            builder.collect()
            builder.build()
            builder.write_version_index()
            counts[version.name] = len(builder.pages)
            unresolved_all |= builder.unresolved
            built_any = True
            tag = "new" if version.name not in known else "rebuilt"
            changed.append(f"{product.title} {version.name} ({tag}, {len(builder.pages)} concepts)")
            skipped = f"  skipped {len(builder.skipped)} empty" if builder.skipped else ""
            print(f"  {version.name:<6} {len(builder.pages):>4} concepts  [{tag}]{skipped}",
                  flush=True)

        write_product_index(
            product, versions, bundle / "products" / product.key,
            repo_state.sha, repo_state.committed_at, counts,
        )

        state["products"][product.key] = {
            "repo": product.repo,
            "repo_sha": repo_state.sha,
            "repo_committed_at": repo_state.committed_at,
            "latest": next((v.name for v in versions if v.is_current), versions[0].name),
            "version_order": [v.name for v in versions],
            "versions": {
                v.name: {
                    "patch": v.patch,
                    "url_path": v.url_path,
                    "maintenance": "supported" if v.supported else "unmaintained",
                    "concepts": counts.get(v.name, 0),
                }
                for v in versions if v.name in counts
            },
        }
        summary["products"][product.key] = {
            "latest": next((v.name for v in versions if v.is_current), versions[0].name),
            "versions": [v.name for v in versions],
            "concepts": sum(counts.values()),
        }
        summary["total_concepts"] += sum(counts.values())
        if not built_any:
            print(f"  (nothing to build)", flush=True)

    # A filtered run must not shrink the bundle index: products that were not
    # rebuilt this time are carried over from the recorded state.
    for key, pstate in state["products"].items():
        if key in summary["products"] or key not in PRODUCTS_BY_KEY:
            continue
        version_counts = pstate.get("versions", {})
        summary["products"][key] = {
            "latest": pstate.get("latest") or next(iter(version_counts), "?"),
            "versions": pstate.get("version_order") or list(version_counts),
            "concepts": sum(v.get("concepts", 0) for v in version_counts.values()),
        }
        summary["total_concepts"] += summary["products"][key]["concepts"]
    summary["products"] = {
        p.key: summary["products"][p.key] for p in PRODUCTS if p.key in summary["products"]
    }

    copy_guides(bundle)
    write_bundle_index(bundle, summary)

    if changed:
        append_log(bundle, "\n".join(
            [f"## {now()}", ""] + [f"- {c}" for c in changed]
        ))

    state["okf_version"] = OKF_VERSION
    state["generator"] = GENERATOR
    state["last_run"] = now()
    state_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")

    print(f"\nbundle: {bundle}")
    print(f"concepts: {summary['total_concepts']}")
    if unresolved_all:
        print(f"note: JSX components left inline: {', '.join(sorted(unresolved_all))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
