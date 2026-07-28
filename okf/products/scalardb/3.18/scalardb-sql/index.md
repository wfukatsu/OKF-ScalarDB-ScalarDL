---
type: Documentation Section
title: ScalarDB 3.18 — Scalardb Sql
description: Directory listing for the `scalardb-sql` section of the ScalarDB 3.18 documentation.
resource: https://scalardb.scalar-labs.com/docs/latest/scalardb-sql/
tags:
- scalardb
- v3.18
- index
status: stable
product: scalardb
version: '3.18'
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:24Z'
---

# Scalardb Sql

ScalarDB 3.18 documentation under `scalardb-sql/`.

Section overview: [ScalarDB SQL Overview](./section-home.md)

## Concepts

- [Guide of Spring Data JDBC for ScalarDB](./spring-data-guide.md) — Directly using the ScalarDB API may be difficult because you need to write a lot of code and consider how and when to call the APIs (e.g., rollback() and commit()) for transactions. Since we assume most ScalarDB users develop their...
- [How to Migrate Your Applications and Databases into a ScalarDB-Based Environment](./migration-guide.md) — This guide describes how to migrate your existing applications and relational databases into ScalarDB-based applications and ScalarDB-managed databases, respectively.
- [ScalarDB JDBC Guide](./jdbc-guide.md) — The usage of ScalarDB JDBC basically follows Java JDBC API. This guide describes several important topics that are specific to ScalarDB JDBC.
- [ScalarDB SQL API Guide](./sql-api-guide.md) — This guide describes how to use ScalarDB SQL API.
- [ScalarDB SQL Error Codes](./scalardb-sql-status-codes.md) — This page provides a list of error codes in ScalarDB SQL.
- [ScalarDB SQL Grammar](./grammar.md) — Each DDL command triggers several write operations, but these operations are not executed atomically, meaning that if the command fails midway, you may encounter inconsistent states. To resolve this inconsistency issue, you can repair the...
