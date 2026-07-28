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
- '3.18'
- '3.17'
- '3.16'
- '3.15'
- '3.14'
latest_version: '3.18'
supported_versions:
- '3.18'
- '3.17'
- '3.16'
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/tree/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a
  title: ScalarDB documentation repository
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# ScalarDB

Universal HTAP engine that provides ACID transactions and analytical queries across heterogeneous databases. Covers the core library, ScalarDB Cluster, SQL/GraphQL interfaces, Analytics, Data Loader and the surrounding Kubernetes tooling.

## Versions

| Version | Newest patch | Maintenance | Concepts | Docs |
|---|---|---|---|---|
| [3.18 (latest)](./3.18/index.md) | 3.18.0 | supported | 206 | https://scalardb.scalar-labs.com/docs/latest/ |
| [3.17](./3.17/index.md) | 3.17.3 | supported | 202 | https://scalardb.scalar-labs.com/docs/3.17/ |
| [3.16](./3.16/index.md) | 3.16.5 | supported | 204 | https://scalardb.scalar-labs.com/docs/3.16/ |
| [3.15](./3.15/index.md) | 3.15.8 | unmaintained | 193 | https://scalardb.scalar-labs.com/docs/3.15/ |
| [3.14](./3.14/index.md) | 3.14.6 | unmaintained | 178 | https://scalardb.scalar-labs.com/docs/3.14/ |

## How to pick a version

1. Match the version to the ScalarDB/ScalarDL release the project actually runs.
2. If the project is greenfield, use the newest supported version.
3. Never mix guidance across versions — configuration keys, error codes and API signatures differ between minor releases.
