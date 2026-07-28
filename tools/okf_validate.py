#!/usr/bin/env python3
"""Check the generated bundle against the OKF v0.2 conformance rules.

Conformance (SPEC §11) requires that every non-reserved .md file has parseable
YAML frontmatter with a non-empty `type`, and that reserved files (index.md,
log.md) are well formed.  Broken links are tolerated by the spec, so they are
reported as warnings rather than failures.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

RESERVED = {"index.md", "log.md"}
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.S)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)")

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", default=str(ROOT / "okf"))
    ap.add_argument("--strict-links", action="store_true",
                    help="treat unresolved in-bundle links as errors")
    args = ap.parse_args()

    bundle = Path(args.bundle)
    if not bundle.is_dir():
        print(f"error: bundle not found: {bundle}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    types: dict[str, int] = {}
    products: dict[str, set[str]] = {}
    total = 0

    files = sorted(bundle.rglob("*.md"))
    for path in files:
        rel = path.relative_to(bundle)
        total += 1
        text = path.read_text("utf-8", errors="replace")
        m = FRONTMATTER_RE.match(text)
        reserved = path.name in RESERVED

        if not m:
            (warnings if reserved else errors).append(f"{rel}: no YAML frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: unparseable frontmatter ({exc.__class__.__name__})")
            continue
        if not isinstance(fm, dict):
            errors.append(f"{rel}: frontmatter is not a mapping")
            continue

        concept_type = str(fm.get("type") or "").strip()
        if not concept_type:
            (warnings if reserved else errors).append(f"{rel}: empty `type`")
        else:
            types[concept_type] = types.get(concept_type, 0) + 1

        if not str(fm.get("title") or "").strip():
            warnings.append(f"{rel}: no title")
        if not str(fm.get("description") or "").strip():
            warnings.append(f"{rel}: no description")

        product = fm.get("product")
        version = fm.get("version")
        if product and version:
            products.setdefault(str(product), set()).add(str(version))

        status = fm.get("status")
        if status is not None and status not in ("draft", "stable", "deprecated"):
            errors.append(f"{rel}: invalid status {status!r}")

        body = text[m.end():]
        for target in LINK_RE.findall(body):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                warnings.append(f"{rel}: unresolved link -> {target}")

    root_index = bundle / "index.md"
    if not root_index.exists():
        errors.append("index.md: bundle root index missing")
    else:
        fm = yaml.safe_load(FRONTMATTER_RE.match(root_index.read_text("utf-8")).group(1))
        if str(fm.get("okf_version") or "") != "0.2":
            warnings.append("index.md: bundle does not declare okf_version: 0.2")
    if not (bundle / "log.md").exists():
        warnings.append("log.md: update history missing")

    link_warnings = [w for w in warnings if "unresolved link" in w]
    other_warnings = [w for w in warnings if "unresolved link" not in w]
    if args.strict_links:
        errors += link_warnings
        link_warnings = []

    print(f"bundle:   {bundle}")
    print(f"files:    {total}")
    print(f"products: " + ", ".join(
        f"{k} ({len(v)} versions)" for k, v in sorted(products.items())
    ))
    print("\nconcept types:")
    for name, count in sorted(types.items(), key=lambda kv: -kv[1]):
        print(f"  {count:>5}  {name}")

    if other_warnings:
        print(f"\nwarnings: {len(other_warnings)}")
        for w in other_warnings[:15]:
            print(f"  ! {w}")
        if len(other_warnings) > 15:
            print(f"  ... and {len(other_warnings) - 15} more")
    if link_warnings:
        print(f"\nunresolved in-bundle links: {len(link_warnings)}")
        for w in link_warnings[:10]:
            print(f"  ! {w}")
        if len(link_warnings) > 10:
            print(f"  ... and {len(link_warnings) - 10} more")

    if errors:
        print(f"\nERRORS: {len(errors)}")
        for e in errors[:30]:
            print(f"  x {e}")
        if len(errors) > 30:
            print(f"  ... and {len(errors) - 30} more")
        print("\nNOT CONFORMANT")
        return 1

    print("\nCONFORMANT (OKF v0.2)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
