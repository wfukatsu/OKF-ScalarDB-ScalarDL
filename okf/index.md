---
type: Knowledge Bundle
title: ScalarDB / ScalarDL Knowledge Bundle
okf_version: '0.2'
description: ScalarDB and ScalarDL documentation organised per product and per version for AI-assisted design, implementation and operations.
resource: https://developers.scalar-labs.com/
tags:
- scalardb
- scalardl
- bundle-root
status: stable
concept_count: 1800
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:31Z'
---

# ScalarDB / ScalarDL Knowledge Bundle

An OKF bundle containing the ScalarDB and ScalarDL product documentation published at developers.scalar-labs.com, split by product and by version so that an AI agent can be pointed at exactly the release a project runs.

## Start here

- [How to use this bundle](./guides/how-ai-agents-use-this-bundle.md) — read this first.
- [Choosing a product, edition and version](./guides/product-and-version-selection.md)
- [Keeping the bundle current](./guides/bundle-maintenance.md)

## Products

| Product | Latest | Versions | Concepts |
|---|---|---|---|
| [ScalarDB](./products/scalardb/index.md) | 3.18 | 3.18, 3.17, 3.16, 3.15, 3.14 | 983 |
| [ScalarDL](./products/scalardl/index.md) | 3.13 | 3.13, 3.12, 3.11, 3.10 | 548 |
| [ScalarDB Community](./products/scalardb-community/index.md) | 3.13 | 3.13, 3.12, 3.11, 3.10, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4 | 269 |

## Layout

```
products/<product>/<version>/index.md      product version concept + navigation
products/<product>/<version>/<page>.md     one concept per documentation page
products/<product>/<version>/<dir>/        sections keep the upstream structure
guides/                                    how to consume and maintain the bundle
log.md                                     update history
```

## Conventions

Every concept carries `product`, `version`, `lifecycle_phase` and `status` in its frontmatter, plus `resource` pointing at the canonical page on the docs site and `sources[]` pointing at the exact upstream commit it was generated from. `lifecycle_phase` is one of `design`, `implement`, `operate`.
