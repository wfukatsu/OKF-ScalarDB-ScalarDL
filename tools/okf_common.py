"""Helpers shared by every builder that writes into the bundle.

Two builders exist: the Docusaurus one in okf_build.py, which turns a
documentation site's MDX into concepts, and the repository one in okf_repo.py,
which turns the documentation kept inside a source repository into concepts.
Both write the same concept shape, so the pieces that define that shape live
here.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

import yaml

GENERATOR = "process:okf-build/1.0.0"
OKF_VERSION = "0.2"

LIFECYCLE_LABELS = {
    "design": "設計 / Design",
    "implement": "実装 / Implement",
    "operate": "運用 / Operate",
}
LIFECYCLE_ORDER = ["design", "implement", "operate"]


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_concept(path: Path, frontmatter: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = yaml.safe_dump(
        frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False,
        width=100000,
    ).rstrip()
    path.write_text(f"---\n{fm}\n---\n\n{body.lstrip()}", encoding="utf-8")


def slugify_tag(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
