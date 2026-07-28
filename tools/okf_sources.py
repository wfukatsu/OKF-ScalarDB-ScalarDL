"""Source-side helpers: repo sync, version discovery, sidebar parsing.

The upstream documentation for developers.scalar-labs.com is authored as
Docusaurus sites in three public repositories.  This module knows how to fetch
them and how to read the metadata that the Docusaurus configuration carries
(version list, patch version, maintenance banner, sidebar hierarchy).
"""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# Product registry
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Product:
    """One documented product."""

    key: str            # bundle directory name
    title: str
    repo: str           # github repo under scalar-labs
    site: str           # public docs site the pages are served from
    summary: str

    @property
    def clone_url(self) -> str:
        return f"https://github.com/scalar-labs/{self.repo}.git"

    @property
    def repo_url(self) -> str:
        return f"https://github.com/scalar-labs/{self.repo}"


PRODUCTS: list[Product] = [
    Product(
        key="scalardb",
        title="ScalarDB",
        repo="docs-scalardb",
        site="https://scalardb.scalar-labs.com",
        summary=(
            "Universal HTAP engine that provides ACID transactions and "
            "analytical queries across heterogeneous databases. Covers the core "
            "library, ScalarDB Cluster, SQL/GraphQL interfaces, Analytics, "
            "Data Loader and the surrounding Kubernetes tooling."
        ),
    ),
    Product(
        key="scalardl",
        title="ScalarDL",
        repo="docs-scalardl",
        site="https://scalardl.scalar-labs.com",
        summary=(
            "Byzantine-fault-detection middleware that makes database state "
            "tamper-evident. Covers contracts and functions, Ledger and Auditor "
            "deployment, certificate/HMAC authentication and operations."
        ),
    ),
    Product(
        key="scalardb-community",
        title="ScalarDB Community",
        repo="docs-scalardb-community",
        site="https://scalardb-community.scalar-labs.com",
        summary=(
            "Documentation set for the community (OSS) edition of ScalarDB, "
            "kept for versions 3.4 through 3.13. Superseded by the unified "
            "ScalarDB documentation for newer releases."
        ),
    ),
]

PRODUCTS_BY_KEY = {p.key: p for p in PRODUCTS}


# --------------------------------------------------------------------------
# Repo sync
# --------------------------------------------------------------------------

def _run(args: list[str], cwd: Path | None = None) -> str:
    res = subprocess.run(
        args, cwd=cwd, capture_output=True, text=True, check=True,
    )
    return res.stdout.strip()


@dataclass
class RepoState:
    sha: str
    committed_at: str   # ISO-8601 UTC


def sync_repo(product: Product, cache_dir: Path, *, offline: bool = False) -> RepoState:
    """Clone or fast-forward the upstream docs repo into ``cache_dir``."""
    dest = cache_dir / product.repo
    if not dest.exists():
        if offline:
            raise SystemExit(
                f"{product.repo} is not cached at {dest} and --offline was given"
            )
        cache_dir.mkdir(parents=True, exist_ok=True)
        _run(["git", "clone", "--depth", "1", product.clone_url, str(dest)])
    elif not offline:
        _run(["git", "fetch", "--depth", "1", "origin"], cwd=dest)
        head = _run(["git", "symbolic-ref", "--short", "HEAD"], cwd=dest)
        _run(["git", "reset", "--hard", f"origin/{head}"], cwd=dest)

    sha = _run(["git", "rev-parse", "HEAD"], cwd=dest)
    committed_at = _run(
        ["git", "show", "-s", "--format=%cd", "--date=format-local:%Y-%m-%dT%H:%M:%SZ", "HEAD"],
        cwd=dest,
    )
    return RepoState(sha=sha, committed_at=committed_at)


# --------------------------------------------------------------------------
# docusaurus.config.js parsing
# --------------------------------------------------------------------------

_BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.S)
# A line comment, but not the "//" inside a URL scheme such as https://
_LINE_COMMENT = re.compile(r"(?<![:\"'])//.*?$", re.M)


def _strip_js_comments(text: str) -> str:
    return _LINE_COMMENT.sub("", _BLOCK_COMMENT.sub("", text))


def _extract_balanced(text: str, start: int) -> str:
    """Return the {...} block that begins at or after ``start``."""
    open_at = text.index("{", start)
    depth = 0
    for i in range(open_at, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[open_at : i + 1]
    raise ValueError("unbalanced braces in docusaurus.config.js")


@dataclass
class DocVersion:
    """One documentation version of a product."""

    name: str               # "3.17"  (the minor version users pick)
    label: str              # as shown in the version dropdown
    url_path: str           # "3.17" or "latest"
    patch: str | None       # "3.17.3" — the newest patch the docs describe
    banner: str             # "none" | "unmaintained" | ...
    is_current: bool        # True for the in-development / newest version
    docs_dir: Path = field(repr=False, default=Path())
    sidebar_file: Path | None = field(repr=False, default=None)

    @property
    def supported(self) -> bool:
        return self.banner != "unmaintained"

    @property
    def status(self) -> str:
        """OKF lifecycle status for concepts belonging to this version."""
        return "stable" if self.supported else "deprecated"


_VERSION_ENTRY = re.compile(
    r"""(?P<key>current|"(?P<num>[0-9]+\.[0-9]+)")\s*:\s*\{(?P<body>[^{}]*)\}""",
    re.S,
)


def _attr(body: str, name: str) -> str | None:
    m = re.search(rf"{name}\s*:\s*['\"]([^'\"]*)['\"]", body)
    return m.group(1) if m else None


def discover_versions(product: Product, repo_dir: Path) -> list[DocVersion]:
    """Read versions.json + docusaurus.config.js into DocVersion records."""
    config = _strip_js_comments((repo_dir / "docusaurus.config.js").read_text("utf-8"))
    block_start = config.index("versions:")
    versions_block = _extract_balanced(config, block_start)

    found: dict[str, DocVersion] = {}
    for m in _VERSION_ENTRY.finditer(versions_block):
        body = m.group("body")
        label = _attr(body, "label") or ""
        url_path = _attr(body, "path") or ""
        patch = _attr(body, "className")
        banner = _attr(body, "banner") or "none"
        is_current = m.group("key") == "current"

        # The config keeps a commented-out template; after comment stripping any
        # leftover placeholder is ignored defensively.
        if "<VERSION_NUMBER>" in label or label in ("", "X.X.X"):
            continue
        name = m.group("num") or re.sub(r"\s*\(.*\)$", "", label).strip()
        if patch in (None, "X.X.X"):
            patch = None

        docs_dir = (
            repo_dir / "docs"
            if is_current
            else repo_dir / "versioned_docs" / f"version-{name}"
        )
        sidebar_file = (
            repo_dir / "sidebars.js"
            if is_current
            else repo_dir / "versioned_sidebars" / f"version-{name}-sidebars.json"
        )
        found[name] = DocVersion(
            name=name,
            label=label,
            url_path=url_path,
            patch=patch,
            banner=banner,
            is_current=is_current,
            docs_dir=docs_dir,
            sidebar_file=sidebar_file if sidebar_file.exists() else None,
        )

    # versions.json lists every archived version; make sure none were missed.
    archived = json.loads((repo_dir / "versions.json").read_text("utf-8"))
    for name in archived:
        if name in found:
            continue
        docs_dir = repo_dir / "versioned_docs" / f"version-{name}"
        if not docs_dir.exists():
            continue
        sidebar_file = repo_dir / "versioned_sidebars" / f"version-{name}-sidebars.json"
        found[name] = DocVersion(
            name=name, label=name, url_path=name, patch=None,
            banner="unmaintained", is_current=False, docs_dir=docs_dir,
            sidebar_file=sidebar_file if sidebar_file.exists() else None,
        )

    def sort_key(v: DocVersion) -> tuple:
        parts = [int(x) for x in re.findall(r"\d+", v.name)]
        return tuple(parts)

    return sorted(found.values(), key=sort_key, reverse=True)


# --------------------------------------------------------------------------
# Sidebar parsing
# --------------------------------------------------------------------------

_SIDEBAR_JS_EXPORT = re.compile(r"const\s+sidebars\s*=\s*", re.S)


def load_sidebar(version: DocVersion) -> dict:
    """Return the English sidebar tree, or {} when unavailable.

    Versioned sidebars are plain JSON.  The ``current`` version keeps its
    sidebar in sidebars.js, which is evaluated with node.
    """
    path = version.sidebar_file
    if path is None:
        return {}
    if path.suffix == ".json":
        return json.loads(path.read_text("utf-8"))
    try:
        out = subprocess.run(
            ["node", "-e",
             f"const s=require({json.dumps(str(path))});"
             "process.stdout.write(JSON.stringify(s));"],
            capture_output=True, text=True, check=True,
        ).stdout
        return json.loads(out)
    except (subprocess.CalledProcessError, FileNotFoundError, json.JSONDecodeError):
        return {}


# Top-level sidebar category -> (OKF concept type, lifecycle phase)
SECTION_TYPES: list[tuple[re.Pattern, tuple[str, str]]] = [
    (re.compile(r"^about", re.I),        ("Concept", "design")),
    (re.compile(r"quickstart|getting started", re.I), ("Tutorial", "implement")),
    (re.compile(r"^develop", re.I),      ("Development Guide", "implement")),
    (re.compile(r"^deploy", re.I),       ("Deployment Guide", "operate")),
    (re.compile(r"^manage", re.I),       ("Operations Guide", "operate")),
    (re.compile(r"^migrate", re.I),      ("Migration Guide", "operate")),
    (re.compile(r"^troubleshoot", re.I), ("Troubleshooting", "operate")),
    (re.compile(r"^reference", re.I),    ("Reference", "implement")),
]

# Fallback rules used when a page is not reachable from the sidebar.  Each
# pattern is tried against the full path within the version and then against the
# file name alone, so `scalardb-data-loader/getting-started-import` is still
# recognised as a tutorial.
PATH_TYPES: list[tuple[re.Pattern, tuple[str, str]]] = [
    (re.compile(r"^releases/"),                       ("Release Notes", "operate")),
    (re.compile(r"^(scalar-kubernetes|helm-charts)/"), ("Deployment Guide", "operate")),
    (re.compile(r"^scalar-manager/"),                 ("Operations Guide", "operate")),
    (re.compile(r"^scalar-licensing/"),               ("Reference", "operate")),
    (re.compile(r"^(scalardb|scalardl)-samples/"),    ("Sample Application", "implement")),
    (re.compile(r"^applications/"),                   ("Sample Application", "implement")),
    (re.compile(r"^(scalardb|scalardl)-benchmarks/"), ("Benchmark Guide", "operate")),
    (re.compile(r"^ca/"),                             ("Reference", "operate")),
    (re.compile(r"error-codes|status-codes"),         ("Troubleshooting", "operate")),
    (re.compile(r"^troubleshooting"),                 ("Troubleshooting", "operate")),
    (re.compile(r"configurations?$|^configure-"),     ("Reference", "implement")),
    (re.compile(r"^getting-started|^quickstart|^try-"), ("Tutorial", "implement")),
    (re.compile(r"^how-to-|^(run|use|write)-"),       ("Development Guide", "implement")),
    (re.compile(r"^(design|features|overview|glossary|requirements|roadmap|data-modeling|consensus-commit|implementation|compatibility|learning-paths)"),
                                                      ("Concept", "design")),
    (re.compile(r"^(backup-restore|manage-|monitor|scale)"), ("Operations Guide", "operate")),
    (re.compile(r"^(install|deploy|migrate-to)"),     ("Deployment Guide", "operate")),
    (re.compile(r"^(two-phase-commit|multi-storage|transactions)"),
                                                      ("Development Guide", "implement")),
    (re.compile(r"api-guide|-reference$|^javadoc|^schema|^auth|-sdk$|^libraries"),
                                                      ("Reference", "implement")),
    (re.compile(r"-server$|^scalardb-server"),        ("Deployment Guide", "operate")),
]


def index_sidebar(tree: dict) -> dict[str, list[str]]:
    """Map a doc id to its sidebar breadcrumb (list of category labels)."""
    out: dict[str, list[str]] = {}

    def walk(items, trail: list[str]) -> None:
        for item in items or []:
            if not isinstance(item, dict):
                if isinstance(item, str):
                    out.setdefault(item, list(trail))
                continue
            kind = item.get("type")
            if kind == "category":
                label = item.get("label", "")
                link = item.get("link") or {}
                if link.get("type") == "doc" and link.get("id"):
                    out.setdefault(link["id"], list(trail) + [label])
                walk(item.get("items"), trail + [label])
            elif kind == "doc" and item.get("id"):
                out.setdefault(item["id"], list(trail))

    sidebars = {
        key: items for key, items in (tree or {}).items()
        if isinstance(items, list)
    }
    for key, items in sidebars.items():
        if "english" in key.lower() or key == "docs":
            walk(items, [])
    if not out:  # single unnamed sidebar
        for items in sidebars.values():
            walk(items, [])
    return out


def classify(doc_id: str, breadcrumb: list[str]) -> tuple[str, str]:
    """Return (OKF concept type, lifecycle phase) for a documentation page."""
    if breadcrumb:
        for pattern, result in SECTION_TYPES:
            if pattern.search(breadcrumb[0]):
                return result
    basename = doc_id.rsplit("/", 1)[-1]
    for pattern, result in PATH_TYPES:
        if pattern.search(doc_id) or pattern.search(basename):
            return result
    return ("Documentation Page", "implement")
