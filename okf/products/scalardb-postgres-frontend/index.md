---
type: Product
title: ScalarDB PostgreSQL Frontend
description: PostgreSQL-compatible SQL interface for ScalarDB.
resource: https://github.com/scalar-labs/scalardb-postgres-frontend
tags:
- scalardb-postgres-frontend
- product
status: stable
product: scalardb-postgres-frontend
versions:
- '3.20'
latest_version: '3.20'
supported_versions:
- '3.20'
generated:
  by: process:okf-build/1.0.0
  at: '2026-11-22T03:58:44Z'
sources:
- id: scalardb-postgres-frontend
  resource: https://github.com/scalar-labs/scalardb-postgres-frontend/tree/d28a3ad131f99cc7a8f8f92bdff9621671d1dee8
  title: ScalarDB PostgreSQL Frontend source repository
  author: process:scalar-labs/scalardb-postgres-frontend
  last_modified: '2026-11-20T09:17:04Z'
---

# ScalarDB PostgreSQL Frontend

PostgreSQL-compatible SQL interface for ScalarDB. psql, the PostgreSQL JDBC driver and ORMs connect over the PostgreSQL wire protocol, and their SQL runs as ScalarDB transactions on the databases ScalarDB manages. Runs inside ScalarDB Cluster nodes (recommended) or as a standalone server.

## Versions

| Version | Release | Status | Concepts | Source |
|---|---|---|---|---|
| [3.20 (latest)](./3.20/index.md) | 3.20.1 | released | 14 | https://github.com/scalar-labs/scalardb-postgres-frontend/tree/3.20 |

## How to pick a version

1. The product keeps one branch per minor line, and that branch is the version here. The line follows the ScalarDB line it is released with: `3.20` belongs with ScalarDB Cluster 3.20.
2. `main` builds against an unreleased ScalarDB (`4.0.0-SNAPSHOT`), so it is not in this bundle.
3. `patch_version` is the latest **released** patch of the line. The branch itself builds the next `-SNAPSHOT`, so documentation for an unreleased fix can appear before the release that ships it.

## Relationship to ScalarDB

ScalarDB already offers SQL through ScalarDB SQL (JDBC / Spring Data JDBC) and the Core CRUD API. The PostgreSQL frontend is a **third interface**: it lets unmodified PostgreSQL clients and tools issue SQL, which it parses, plans into ScalarDB Get / Scan / mutation operations, and runs as ScalarDB transactions. It is **not PostgreSQL**: the supported SQL subset, type handling and result differences are stated in `limitations.md` and `reference/`. Read `limitations.md` before promising PostgreSQL compatibility to anyone.

Authentication and TLS exist only when it runs inside, or in front of, ScalarDB Cluster. As a standalone server on ScalarDB core it has none and belongs on a trusted network only.
