---
type: Product
title: ScalarDB
description: Universal HTAP engine that provides ACID transactions and analytical queries across heterogeneous databases.
resource: https://scalardb.scalar-labs.com/docs/
tags:
- scalardb
- product
status: stable
product: scalardb
versions:
- '3.19'
- '3.18'
- '3.17'
- '3.16'
- '3.15'
- '3.14'
latest_version: '3.19'
supported_versions:
- '3.19'
- '3.18'
- '3.17'
- '3.16'
archived_versions:
- '3.14'
generated:
  by: process:okf-build/1.0.0
  at: '2026-09-11T05:23:06Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/tree/c882c4103fe6e0aedff74e7afa67c2587a78ec9b
  title: ScalarDB documentation repository
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-09-09T05:43:01Z'
---

# ScalarDB

Universal HTAP engine that provides ACID transactions and analytical queries across heterogeneous databases. Covers the core library, ScalarDB Cluster, SQL/GraphQL interfaces, Analytics, Data Loader and the surrounding Kubernetes tooling.

## Versions

| Version | Newest patch | Maintenance | Concepts | Docs |
|---|---|---|---|---|
| [3.19 (latest)](./3.19/index.md) | 3.19.1 | supported | 203 | https://scalardb.scalar-labs.com/docs/latest/ |
| [3.18](./3.18/index.md) | 3.18.2 | supported | 206 | https://scalardb.scalar-labs.com/docs/3.18/ |
| [3.17](./3.17/index.md) | 3.17.5 | supported | 202 | https://scalardb.scalar-labs.com/docs/3.17/ |
| [3.16](./3.16/index.md) | 3.16.7 | supported | 204 | https://scalardb.scalar-labs.com/docs/3.16/ |
| [3.15](./3.15/index.md) | 3.15.9 | unmaintained | 193 | https://scalardb.scalar-labs.com/docs/3.15/ |
| [3.14](./3.14/index.md) | 3.14.6 | archived | 178 | — (removed upstream) |

## How to pick a version

1. Match the version to the ScalarDB/ScalarDL release the project actually runs.
2. If the project is greenfield, use the newest supported version.
3. Never mix guidance across versions — configuration keys, error codes and API signatures differ between minor releases.

## Archived versions

3.14 — upstream has removed these versions from the documentation site, so they are no longer regenerated and their pages on https://scalardb.scalar-labs.com now 404. The concepts kept here are the last snapshot taken before the removal; their `resource` links point at pages that no longer exist, and `sources[]` still pins the upstream commit they were built from.

Use them to investigate a system that is still running that release. **Never use them as the basis for a new design**, and say plainly that the version is archived whenever you quote one.
