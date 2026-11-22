---
type: Concept
title: ScalarDB PostgreSQL Frontend user documentation
description: 'Entry point of the user documentation: deployment choices and where to read about clients, SQL, transactions, security and operations.'
resource: https://github.com/scalar-labs/scalardb-postgres-frontend/blob/d28a3ad131f99cc7a8f8f92bdff9621671d1dee8/docs/user/README.md
tags:
- scalardb-postgres-frontend
- v3.20
- phase:implement
- section:user
status: stable
product: scalardb-postgres-frontend
product_title: ScalarDB PostgreSQL Frontend
version: '3.20'
patch_version: 3.20.1
prerelease: false
doc_id: user/overview
lifecycle_phase: implement
generated:
  by: process:okf-build/1.0.0
  at: '2026-11-22T03:58:44Z'
sources:
- id: scalardb-postgres-frontend
  resource: https://github.com/scalar-labs/scalardb-postgres-frontend/blob/d28a3ad131f99cc7a8f8f92bdff9621671d1dee8/docs/user/README.md
  title: ScalarDB PostgreSQL Frontend source repository — docs/user/README.md
  author: process:scalar-labs/scalardb-postgres-frontend
  last_modified: '2026-11-20T09:17:04Z'
---

# ScalarDB PostgreSQL frontend: user documentation

The PostgreSQL frontend lets psql, the PostgreSQL JDBC driver and other PostgreSQL clients run SQL as
ScalarDB transactions. It runs inside ScalarDB Cluster nodes, which is the recommended deployment, or as a
standalone server on ScalarDB core.

## Get started

- [Quick start](./quick-start.md): run a ScalarDB Cluster node with the frontend in Docker, and connect with psql.
- [Getting started with the standalone server](../getting-started.md): run the frontend on ScalarDB
  core, without ScalarDB Cluster.

## Use

- [Designing tables and queries](./schema-and-queries.md): how tables map to ScalarDB, which queries run in the
  database, and how to check them with `EXPLAIN`.
- [SQL reference](./sql-reference.md): statements, data types, functions and error codes.
- [Transactions](./transactions.md): optimistic transactions, retries, isolation levels and their differences
  from PostgreSQL.
- [Clients and tools](./clients.md): tested drivers, ORMs and tools, and what to know about each.

## Configure and operate

- [Configuration](./configuration.md): every property, session setting and fixed limit.
- [Security](./security.md): authentication, TLS, users, privileges, encryption and ABAC.
- [Operations](./operations.md): connections across nodes, sizing, monitoring, upgrades and troubleshooting.

## Reference

- [Limitations](../limitations.md): what the frontend refuses, announces with a `NOTICE`, or does
  differently from PostgreSQL.
- [Changelog](../releases/release-notes.md): changes per release; those that need you to act are marked `[BREAKING]`.
