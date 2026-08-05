---
type: Product
title: ScalarDB Saga
description: Saga orchestration engine for microservices.
resource: https://github.com/scalar-labs/scalardb-saga
tags:
- scalardb-saga
- product
status: draft
product: scalardb-saga
versions:
- '3.19'
latest_version: '3.19'
supported_versions:
- '3.19'
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-05T00:26:16Z'
sources:
- id: scalardb-saga
  resource: https://github.com/scalar-labs/scalardb-saga/tree/ecbd61722adae47620b2032be6974c9af593ecda
  title: ScalarDB Saga source repository
  author: process:scalar-labs/scalardb-saga
  last_modified: '2026-08-03T21:49:02Z'
---

# ScalarDB Saga

Saga orchestration engine for microservices. Coordinates eventually consistent distributed transactions across services with the Saga pattern (steps with compensations) and TCC, keeping saga state durable through ScalarDB so no message broker is needed. Runs as a server exposing REST and gRPC, or embedded as a library.

## Versions

| Version | Release | Status | Concepts | Source |
|---|---|---|---|---|
| [3.19 (latest)](./3.19/index.md) | 3.19.0-alpha.1 | pre-release | 9 | https://github.com/scalar-labs/scalardb-saga/tree/3.19 |

## How to pick a version

1. ScalarDB Saga keeps one branch per minor line, and that branch is the version here. Match it to the `com.scalar-labs:scalardb-saga-*` version the project declares, or to the tag of the `ghcr.io/scalar-labs/scalardb-saga-server` image it runs.
2. Development lines (`main`, and the next minor branch) build `-SNAPSHOT` versions that nobody runs in production, so they are not in this bundle.
3. A line marked *pre-release* has no GA release. Its API and configuration keys can still change between builds; confirm against the branch before committing to them.

## Relationship to ScalarDB

ScalarDB gives strongly consistent ACID transactions **across databases**. ScalarDB Saga coordinates operations **across services**, where a single ACID transaction is not possible, trading strong consistency for compensation-based rollback and eventual convergence. It stores its own saga state through ScalarDB, so it runs on any database ScalarDB supports and needs no message broker.

Use ScalarDB transactions where correctness requires immediate consistency, and ScalarDB Saga where eventual consistency with compensation is sufficient. See `products/scalardb/<version>/two-phase-commit-transactions.md` for the strongly consistent alternative across microservices.
