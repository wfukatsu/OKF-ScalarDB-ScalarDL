"""Build bundle concepts for a product documented inside its source repository.

ScalarDB Saga has no documentation site: what exists is the Markdown kept in
the repository (README, the getting-started walkthrough, the server image
guide) plus the files that *are* the contract — the gRPC protos, the annotated
server configuration template, and the sample saga definitions.  This module
turns that fixed set into concepts of the same shape the Docusaurus builder
emits, one release branch at a time.

The mapping is declared, not discovered: a source repository has no sidebar to
read, so which files become concepts, and what each one is, is stated in
REPO_DOCS below.  Adding a document to the upstream repository does not add a
concept until it is listed here — deliberately, so that build output does not
change shape because someone added a design note to the repository.
"""

from __future__ import annotations

import os
import posixpath
import re
from dataclasses import dataclass
from pathlib import Path

from okf_common import (
    GENERATOR, LIFECYCLE_LABELS, LIFECYCLE_ORDER, now, slugify_tag, write_concept,
)
from okf_mdx import extract_description, extract_title
from okf_sources import Product, RepoVersion, read_repo_file, repo_path_kind


@dataclass(frozen=True)
class RepoDoc:
    """One concept built from one or more files in the source repository."""

    out_rel: str                        # path under the version directory
    sources: tuple[str, ...]            # repo-relative paths, in order
    concept_type: str
    phase: str
    render: str = "markdown"            # "markdown" | "code"
    title: str = ""                     # required for code renders
    description: str = ""               # required for code renders
    intro: str = ""                     # prose placed above a code render
    optional: bool = False              # skip silently when the source is gone

    @property
    def directory(self) -> str:
        parent = posixpath.dirname(self.out_rel)
        return parent


FENCE_LANGUAGES = {
    ".proto": "protobuf",
    ".properties": "properties",
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".py": "python",
    ".xml": "xml",
}


REPO_DOCS: dict[str, list[RepoDoc]] = {
    "scalardb-saga": [
        RepoDoc(
            out_rel="overview.md",
            sources=("README.md",),
            concept_type="Concept",
            phase="design",
        ),
        RepoDoc(
            out_rel="getting-started.md",
            sources=("getting-started/README.md",),
            concept_type="Tutorial",
            phase="implement",
        ),
        RepoDoc(
            out_rel="server-deployment.md",
            sources=("server/docker/README.md",),
            concept_type="Deployment Guide",
            phase="operate",
        ),
        RepoDoc(
            out_rel="reference/saga-definitions.md",
            sources=(
                "getting-started/conf/definitions/order-saga.json",
                "getting-started/conf/definitions/order-saga-failing.json",
                "core/src/test/resources/sagas/transfer.yaml",
                "core/src/test/resources/sagas/minimal.json",
            ),
            concept_type="Reference",
            phase="implement",
            render="code",
            title="Saga definition examples",
            description=(
                "Working saga definitions from the repository: declarative service "
                "steps in JSON, and code steps (stepClass) in YAML and JSON."
            ),
            intro=(
                "A saga definition names the steps, the call each one makes and the "
                "call that undoes it. Values flow between steps through the saga "
                "context: `${...}` reads from it, and `output` captures fields of a "
                "response back into it. JSON and YAML are equally valid.\n\n"
                "Two kinds of step exist. A **declarative service step** names a "
                "`service` configured on the server and the HTTP call to make; it "
                "works in both server and embedded mode. A **code step** names a "
                "`stepClass` implemented in Java and therefore only works in "
                "embedded mode — the server rejects such a definition at startup, "
                "because an operator cannot add classes to its image.\n\n"
                "These are the definitions the repository ships, reproduced verbatim."
            ),
        ),
        RepoDoc(
            out_rel="reference/server-configuration.md",
            sources=("server/docker/conf/server.properties",),
            concept_type="Reference",
            phase="operate",
            render="code",
            title="Server configuration reference",
            description=(
                "Every scalar.db.saga.server.* property the saga server accepts, with "
                "its default and the reasoning behind it, as shipped in the image's "
                "configuration template."
            ),
            intro=(
                "The server image ships this file at "
                "`/scalardb-saga/conf/server.properties` and passes it to the process "
                "with `--config`. It is a *template*: as shipped it does not start, "
                "because a ScalarDB store, at least one saga definition and a security "
                "provider are required and cannot be guessed. Commented-out lines show "
                "each key's default value, so this file is also the authoritative list "
                "of settings and defaults.\n\n"
                "A misspelled `scalar.db.saga.server.*` key fails startup rather than "
                "being ignored. Any value under `scalar.db.saga.*` may use a secret "
                "reference — `${env:NAME}` or `${file:UTF-8:/path}`; plain "
                "`scalar.db.*` keys are resolved by ScalarDB itself, which supports "
                "`${env:...}` but not `${file:...}`."
            ),
        ),
        RepoDoc(
            out_rel="reference/grpc-saga-api.md",
            sources=("rpc/src/main/proto/saga.proto",),
            concept_type="Reference",
            phase="implement",
            render="code",
            title="Saga gRPC API",
            description=(
                "The SagaService gRPC contract — starting a saga, awaiting it, and "
                "reading its snapshot and event history — as defined in saga.proto."
            ),
            intro=(
                "`SagaService` is the gRPC rendering of the server's REST contract, "
                "served on port `12051` by default. The protobuf definition below is "
                "the contract itself, and its comments state the semantics each RPC "
                "guarantees — what a bounded wait returns, which errors travel as "
                "which `io.grpc.Status`, and what a client-supplied saga id does.\n\n"
                "The generated stubs ship as `com.scalar-labs:scalardb-saga-rpc`; the "
                "client SDK (`scalardb-saga-java-client-sdk`) wraps them and is what "
                "an application normally uses."
            ),
        ),
        RepoDoc(
            out_rel="reference/grpc-admin-api.md",
            sources=("rpc/src/main/proto/admin.proto",),
            concept_type="Reference",
            phase="operate",
            render="code",
            title="Admin gRPC API",
            description=(
                "The AdminService gRPC contract — listing, recovering, force-completing "
                "and resetting sagas that need operator intervention."
            ),
            intro=(
                "`AdminService` is the operator-facing surface: it lists sagas by "
                "status and drives the ones that cannot make progress on their own. "
                "Every route it exposes requires the `saga:admin` role under the "
                "configured security provider.\n\n"
                "Reach for it when a saga has been escalated after repeated "
                "compensation failure; the reasoning for each operation is in the "
                "comments below."
            ),
        ),
    ],
}

# Repo paths that became concepts; links pointing at them are rewritten to the
# concept.  Everything else in the repository is linked on GitHub instead.
_LINK_TARGET = re.compile(r"(\]\()([^)\s]+)(\s+\"[^\"]*\")?(\))")
_BADGE_LINE = re.compile(r"^\s*(?:\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)\s*)+$", re.M)
_GH_ALERT = re.compile(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", re.M)


def _clean_markdown(text: str) -> str:
    """Drop badge rows and render GitHub alert markers as plain Markdown."""
    text = _BADGE_LINE.sub("", text)
    text = _GH_ALERT.sub(lambda m: f"> **{m.group(1).title()}**\n>", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


class RepoVersionBuilder:
    """Write one release branch of a repository-sourced product."""

    def __init__(self, product: Product, version: RepoVersion, repo_dir: Path,
                 out_dir: Path):
        self.product = product
        self.version = version
        self.repo_dir = repo_dir
        self.out_dir = out_dir
        self.docs = REPO_DOCS[product.key]
        self.built: list[RepoDoc] = []
        self.titles: dict[str, str] = {}
        self.descriptions: dict[str, str] = {}
        self.missing: list[str] = []

    # -- helpers ----------------------------------------------------------

    def _read(self, path: str) -> str | None:
        return read_repo_file(self.repo_dir, self.version.ref, path)

    def _blob_url(self, path: str) -> str:
        return f"{self.product.repo_url}/blob/{self.version.sha}/{path}"

    def _github_url(self, path: str) -> str:
        """A repository path as a GitHub URL — blob for files, tree for dirs.

        Asked of the repository rather than guessed from the extension, so an
        extensionless file such as LICENSE still gets a blob URL.
        """
        kind = repo_path_kind(self.repo_dir, self.version.ref, path)
        segment = "tree" if kind == "tree" else "blob"
        return f"{self.product.repo_url}/{segment}/{self.version.sha}/{path}"

    # -- link rewriting ---------------------------------------------------

    def _rewrite_links(self, body: str, doc: RepoDoc, source: str) -> str:
        """Point in-repo links at the concept they became, or at GitHub."""
        source_dir = posixpath.dirname(source)
        in_bundle = {
            src: d.out_rel for d in self.docs if d in self.built for src in d.sources
        }

        def replace(m: re.Match) -> str:
            target = m.group(2)
            if target.startswith(("http://", "https://", "#", "mailto:")):
                return m.group(0)
            path, _, anchor = target.partition("#")
            if not path:
                return m.group(0)
            repo_path = posixpath.normpath(posixpath.join(source_dir, path))
            if repo_path in in_bundle:
                rel = os.path.relpath(in_bundle[repo_path], doc.directory or ".")
                rel = rel if rel.startswith(".") else f"./{rel}"
                return f"{m.group(1)}{rel}{anchor and '#' + anchor}{m.group(4)}"
            url = self._github_url(repo_path)
            return f"{m.group(1)}{url}{anchor and '#' + anchor}{m.group(4)}"

        return _LINK_TARGET.sub(replace, body)

    # -- build ------------------------------------------------------------

    def build(self) -> None:
        # First pass: read every source, so link rewriting knows which
        # documents actually exist on this branch.
        contents: dict[RepoDoc, list[tuple[str, str]]] = {}
        for doc in self.docs:
            found = [(src, text) for src in doc.sources
                     if (text := self._read(src)) is not None]
            if not found:
                self.missing.append(doc.sources[0])
                continue
            contents[doc] = found
            self.built.append(doc)

        for doc in self.built:
            body = self._render(doc, contents[doc])
            self._emit(doc, body, [src for src, _ in contents[doc]])

        self._emit_section_indexes()

    def _render(self, doc: RepoDoc, found: list[tuple[str, str]]) -> str:
        if doc.render == "markdown":
            source, text = found[0]
            body = _clean_markdown(text)
            self.titles[doc.out_rel] = extract_title(body, doc.out_rel)
            self.descriptions[doc.out_rel] = doc.description or extract_description(body)
            return self._rewrite_links(body, doc, source)

        self.titles[doc.out_rel] = doc.title
        self.descriptions[doc.out_rel] = doc.description
        lines = [f"# {doc.title}", ""]
        if doc.intro:
            lines += [doc.intro, ""]
        for source, text in found:
            language = FENCE_LANGUAGES.get(posixpath.splitext(source)[1], "")
            lines += [
                f"## `{source}`",
                "",
                f"[View on GitHub]({self._blob_url(source)})",
                "",
                f"```{language}",
                text.rstrip("\n"),
                "```",
                "",
            ]
        return "\n".join(lines)

    def _emit(self, doc: RepoDoc, body: str, sources: list[str]) -> None:
        tags = [self.product.key, f"v{self.version.name}", f"phase:{doc.phase}"]
        if doc.directory:
            tags.append(f"section:{slugify_tag(doc.directory)}")
        if self.version.prerelease:
            tags.append("pre-release")

        fm = {
            "type": doc.concept_type,
            "title": self.titles[doc.out_rel],
            "description": self.descriptions[doc.out_rel],
            "resource": self._blob_url(sources[0]),
            "tags": tags,
            "status": self.version.status,
            "product": self.product.key,
            "product_title": self.product.title,
            "version": self.version.name,
        }
        if self.version.release:
            fm["patch_version"] = self.version.release
            fm["prerelease"] = self.version.prerelease
        fm.update({
            "doc_id": doc.out_rel[: -len(".md")],
            "lifecycle_phase": doc.phase,
            "generated": {"by": GENERATOR, "at": now()},
            "sources": [{
                "id": self.product.repo,
                "resource": self._blob_url(src),
                "title": f"{self.product.title} source repository — {src}",
                "author": f"process:scalar-labs/{self.product.repo}",
                "last_modified": self.version.committed_at,
            } for src in sources],
        })
        write_concept(self.out_dir / doc.out_rel, fm, body)

    # -- listings ---------------------------------------------------------

    def _emit_section_indexes(self) -> None:
        by_dir: dict[str, list[RepoDoc]] = {}
        for doc in self.built:
            if doc.directory:
                by_dir.setdefault(doc.directory, []).append(doc)

        for directory, docs in sorted(by_dir.items()):
            title = directory.rsplit("/", 1)[-1].replace("-", " ").title()
            lines = [
                f"# {title}",
                "",
                f"{self.product.title} {self.version.name} reference material generated "
                f"from the files that define the contract in the source repository.",
                "",
                "## Concepts",
                "",
            ]
            for doc in sorted(docs, key=lambda d: self.titles[d.out_rel].lower()):
                name = doc.out_rel.rsplit("/", 1)[-1]
                desc = self.descriptions.get(doc.out_rel)
                lines.append(
                    f"- [{self.titles[doc.out_rel]}](./{name})"
                    + (f" — {desc}" if desc else "")
                )
            lines.append("")

            fm = {
                "type": "Documentation Section",
                "title": f"{self.product.title} {self.version.name} — {title}",
                "description": (
                    f"Directory listing for the `{directory}` section of the "
                    f"{self.product.title} {self.version.name} documentation."
                ),
                "resource": f"{self.product.repo_url}/tree/{self.version.sha}",
                "tags": [self.product.key, f"v{self.version.name}", "index"],
                "status": self.version.status,
                "product": self.product.key,
                "version": self.version.name,
                "generated": {"by": GENERATOR, "at": now()},
            }
            write_concept(self.out_dir / directory / "index.md", fm, "\n".join(lines))

    def write_version_index(self) -> None:
        by_phase: dict[str, list[RepoDoc]] = {}
        for doc in self.built:
            by_phase.setdefault(doc.phase, []).append(doc)

        banner = (
            "**Pre-release.** This line has no general-availability release yet; "
            "the documentation describes "
            f"`{self.version.release}`. Treat APIs, configuration keys and wire "
            "contracts as subject to change, and do not use it as the basis for a "
            "production commitment without confirming the current release."
            if self.version.prerelease else "Supported release."
        )

        lines = [
            f"# {self.product.title} {self.version.name}",
            "",
            banner,
            "",
            "| | |",
            "|---|---|",
            f"| Product | {self.product.title} |",
            f"| Version line | {self.version.name} |",
        ]
        if self.version.release:
            lines.append(f"| Release the branch builds | {self.version.release} |")
        lines += [
            f"| Source branch | `{self.version.name}` |",
            f"| Upstream source | {self.product.repo_url} @ `{self.version.sha[:12]}` |",
            f"| Concepts in this version | {len(self.built)} |",
            "",
            "## By lifecycle phase",
            "",
            "Start here when you know which phase of the project you are in.",
            "",
        ]
        for phase in LIFECYCLE_ORDER:
            docs = by_phase.get(phase) or []
            if not docs:
                continue
            lines += [f"### {LIFECYCLE_LABELS[phase]} ({len(docs)})", ""]
            for doc in sorted(docs, key=lambda d: self.titles[d.out_rel].lower()):
                lines.append(f"- [{self.titles[doc.out_rel]}](./{doc.out_rel})")
            lines.append("")

        sections = sorted({d.directory.split("/")[0] for d in self.built if d.directory})
        if sections:
            lines += ["## Sections", ""]
            lines += [f"- [{s}](./{s}/index.md)" for s in sections]
            lines.append("")

        lines += [
            "## Where this comes from",
            "",
            f"{self.product.title} has no documentation site yet. Every concept here "
            "is generated from the documentation and contract files kept in "
            f"[{self.product.repo}]({self.product.repo_url}) on branch "
            f"`{self.version.name}`, at the commit recorded in each concept's "
            "`sources[]`. The `resource` of a concept points at the file it was "
            "generated from, pinned to that commit.",
            "",
        ]

        fm = {
            "type": "Product Version",
            "title": f"{self.product.title} {self.version.name}",
            "description": (
                f"Documentation set for {self.product.title} {self.version.name}"
                + (f" (release {self.version.release})" if self.version.release else "")
                + ", generated from the source repository."
            ),
            "resource": f"{self.product.repo_url}/tree/{self.version.name}",
            "tags": [self.product.key, f"v{self.version.name}", "product-version"]
                    + (["pre-release"] if self.version.prerelease else []),
            "status": self.version.status,
            "product": self.product.key,
            "product_title": self.product.title,
            "version": self.version.name,
            **({"patch_version": self.version.release} if self.version.release else {}),
            "prerelease": self.version.prerelease,
            "url_path": self.version.name,
            "maintenance": "supported",
            "is_latest": self.version.is_current,
            "concept_count": len(self.built),
            "generated": {"by": GENERATOR, "at": now()},
            "sources": [{
                "id": self.product.repo,
                "resource": f"{self.product.repo_url}/tree/{self.version.sha}",
                "title": f"{self.product.title} source repository",
                "author": f"process:scalar-labs/{self.product.repo}",
                "last_modified": self.version.committed_at,
            }],
        }
        write_concept(self.out_dir / "index.md", fm, "\n".join(lines))


def write_repo_product_index(product: Product, versions: list[RepoVersion],
                             out_dir: Path, counts: dict[str, int]) -> None:
    head = versions[0] if versions else None
    lines = [
        f"# {product.title}",
        "",
        product.summary,
        "",
        "## Versions",
        "",
        "| Version | Release | Status | Concepts | Source |",
        "|---|---|---|---|---|",
    ]
    for v in versions:
        latest = " (latest)" if v.is_current else ""
        state = "pre-release" if v.prerelease else "released"
        lines.append(
            f"| [{v.name}{latest}](./{v.name}/index.md) | {v.release or '—'} | "
            f"{state} | {counts.get(v.name, 0)} | "
            f"{product.repo_url}/tree/{v.name} |"
        )
    lines += [
        "",
        "## How to pick a version",
        "",
        f"1. {product.title} keeps one branch per minor line, and that branch is the "
        "version here. Match it to the `com.scalar-labs:scalardb-saga-*` version the "
        "project declares, or to the tag of the "
        "`ghcr.io/scalar-labs/scalardb-saga-server` image it runs.",
        "2. Development lines (`main`, and the next minor branch) build `-SNAPSHOT` "
        "versions that nobody runs in production, so they are not in this bundle.",
        "3. A line marked *pre-release* has no GA release. Its API and configuration "
        "keys can still change between builds; confirm against the branch before "
        "committing to them.",
        "",
        "## Relationship to ScalarDB",
        "",
        "ScalarDB gives strongly consistent ACID transactions **across databases**. "
        "ScalarDB Saga coordinates operations **across services**, where a single ACID "
        "transaction is not possible, trading strong consistency for compensation-based "
        "rollback and eventual convergence. It stores its own saga state through "
        "ScalarDB, so it runs on any database ScalarDB supports and needs no message "
        "broker.",
        "",
        "Use ScalarDB transactions where correctness requires immediate consistency, and "
        "ScalarDB Saga where eventual consistency with compensation is sufficient. See "
        "`products/scalardb/<version>/two-phase-commit-transactions.md` for the "
        "strongly consistent alternative across microservices.",
        "",
    ]

    fm = {
        "type": "Product",
        "title": product.title,
        "description": product.summary.split(".")[0] + ".",
        "resource": product.repo_url,
        "tags": [product.key, "product"],
        "status": "draft" if (head and head.prerelease) else "stable",
        "product": product.key,
        "versions": [v.name for v in versions],
        "latest_version": head.name if head else "",
        "supported_versions": [v.name for v in versions],
        "generated": {"by": GENERATOR, "at": now()},
        "sources": [{
            "id": product.repo,
            "resource": f"{product.repo_url}/tree/{head.sha}" if head else product.repo_url,
            "title": f"{product.title} source repository",
            "author": f"process:scalar-labs/{product.repo}",
            "last_modified": head.committed_at if head else now(),
        }],
    }
    write_concept(out_dir / "index.md", fm, "\n".join(lines))
