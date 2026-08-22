---
type: Knowledge Bundle
title: ScalarDB / ScalarDL Knowledge Bundle
okf_version: '0.2'
description: ScalarDB, ScalarDL and ScalarDB Saga documentation organised per product and per version for AI-assisted design, implementation and operations.
resource: https://developers.scalar-labs.com/
tags:
- scalardb
- scalardl
- scalardb-saga
- bundle-root
status: stable
concept_count: 2159
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-22T00:59:11Z'
---

# ScalarDB / ScalarDL Knowledge Bundle

An OKF bundle containing the ScalarDB and ScalarDL product documentation published at developers.scalar-labs.com, plus the documentation ScalarDB Saga keeps in its source repository, split by product and by version so that an AI agent can be pointed at exactly the release a project runs.

## Start here

- [How to use this bundle](./guides/how-ai-agents-use-this-bundle.md) — read this first.
- [Choosing a product, edition and version](./guides/product-and-version-selection.md)
- [Keeping the bundle current](./guides/bundle-maintenance.md)
- [Pricing and licensing](./pricing/index.md) — list prices, licensing units, edition matrix. Not from the docs site; pay-as-you-go / monthly / annual list prices only.

## Products

| Product | Latest | Versions | Concepts |
|---|---|---|---|
| [ScalarDB](./products/scalardb/index.md) | 3.19 | 3.19, 3.18, 3.17, 3.16, 3.15, 3.14 | 1189 |
| [ScalarDL](./products/scalardl/index.md) | 3.14 | 3.14, 3.13, 3.12, 3.11, 3.10 | 692 |
| [ScalarDB Saga](./products/scalardb-saga/index.md) | 3.19 | 3.19 | 9 |
| [ScalarDB Community](./products/scalardb-community/index.md) | 3.13 | 3.13, 3.12, 3.11, 3.10, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4 | 269 |

## Layout

```
products/<product>/<version>/index.md      product version concept + navigation
products/<product>/<version>/<page>.md     one concept per documentation page
products/<product>/<version>/<dir>/        sections keep the upstream structure
guides/                                    how to consume and maintain the bundle
pricing/                                   commercial terms (hand-written, not upstream)
log.md                                     update history
```

## Conventions

Every concept carries `product`, `version`, `lifecycle_phase` and `status` in its frontmatter, plus `resource` pointing at the canonical page on the docs site and `sources[]` pointing at the exact upstream commit it was generated from. `lifecycle_phase` is one of `design`, `implement`, `operate`.

ScalarDB Saga has no documentation site yet, so its concepts are generated from the Markdown and contract files in `scalar-labs/scalardb-saga`, one release branch per version; their `resource` points at the file on GitHub, pinned to the commit they were built from. A version with no GA release is marked `status: draft` and tagged `pre-release`.

`pricing/` is the one section that does not come from an upstream repository. It is authored by hand from the internal Scalar price list and is not refreshed by the generator. It carries only the pay-as-you-go, monthly and annual list prices (JPY, tax excluded); three-year list prices, prepaid-credit sale prices and any discount terms are deliberately out of scope and marked 非公開. Treat it as input to a quotation, never as a binding offer, and never infer a price the bundle does not state.
