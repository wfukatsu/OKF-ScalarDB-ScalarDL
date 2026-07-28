---
type: Product Version
title: ScalarDB Community 3.4
description: Documentation set for ScalarDB Community 3.4.
resource: https://scalardb-community.scalar-labs.com/docs/3.4/
tags:
- scalardb-community
- v3.4
- product-version
- unmaintained
status: deprecated
product: scalardb-community
product_title: ScalarDB Community
version: '3.4'
url_path: '3.4'
maintenance: unmaintained
is_latest: false
concept_count: 24
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:10Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/tree/71d199cb0df1c638bd7e305b64fa09fc7236e5c4
  title: ScalarDB Community documentation repository
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# ScalarDB Community 3.4

**Unmaintained release.** Prefer a supported version for new work; kept here for systems still running it.

| | |
|---|---|
| Product | ScalarDB Community |
| Documentation version | 3.4 |
| Docs site | https://scalardb-community.scalar-labs.com/docs/3.4/ |
| Upstream source | https://github.com/scalar-labs/docs-scalardb-community @ `71d199cb0df1` |
| Concepts in this version | 24 |

## By lifecycle phase

Start here when you know which phase of the project you are in.

### 実装 / Implement (21)

- [Add ScalarDB to your build](./add-scalardb-to-your-build.md)
- [Database schema in Scalar DB](./schema.md)
- [Getting Started with Scalar DB](./getting-started-with-scalardb.md)
- [Getting Started with Scalar DB](./getting-started.md)
- [Getting Started with Scalar DB on Cassandra](./getting-started-with-scalardb-on-cassandra.md)
- [Getting Started with Scalar DB on Cosmos DB](./getting-started-with-scalardb-on-cosmosdb.md)
- [Getting Started with Scalar DB on DynamoDB](./getting-started-with-scalardb-on-dynamodb.md)
- [Getting Started with Scalar DB on JDBC databases](./getting-started-with-scalardb-on-jdbc.md)
- [Multi-storage Transactions](./multi-storage-transactions.md)
- [Requirements in the Underlining Databases of Scalar DB](./requirements.md)
- [Scalar DB design document](./design.md)
- [Scalar DB Schema Loader](./schema-loader.md)
- [Scalar DB Supported Databases](./scalardb-supported-databases.md)
- [ScalarDB Community](./section-home.md)
- [Two-phase Commit Transactions](./two-phase-commit-transactions.md)
- [ScalarDB Benchmarks](./scalardb-benchmarks/README.md)
- [ScalarDB Samples](./scalardb-samples/README.md)
- [Create a Sample Application That Supports Microservice Transactions](./scalardb-samples/microservice-transaction-sample/README.md)
- [Multi-storage Transaction Sample](./scalardb-samples/multi-storage-transaction-sample/README.md)
- [ScalarDB Sample](./scalardb-samples/scalardb-sample/README.md)
- [ScalarDB Server Sample](./scalardb-samples/scalardb-server-sample/README.md)

### 運用 / Operate (3)

- [A Guide on How to Back up and Restore Databases Integrated with Scalar DB](./backup-restore.md)
- [Scalar DB server](./scalardb-server.md)
- [ScalarDB 3.4 Release Notes](./releases/release-notes.md)

## Sections

- [releases](./releases/index.md)
- [scalardb-benchmarks](./scalardb-benchmarks/index.md)
- [scalardb-samples](./scalardb-samples/index.md)

## Top-level concepts

- [A Guide on How to Back up and Restore Databases Integrated with Scalar DB](./backup-restore.md) — Since Scalar DB provides transaction capability on top of non-transactional (possibly transactional) databases non-invasively, you need to take special care of backing up and restoring the databases in a transactionally-consistent way....
- [Add ScalarDB to your build](./add-scalardb-to-your-build.md) — The library is available on maven central repository. You can install it in your application using your build tool such as Gradle and Maven.
- [Database schema in Scalar DB](./schema.md) — Scalar DB has its own data model and schema, that maps to the implementation specific data model and schema. Also, it stores internal metadata for managing transaction logs and statuses. This document briefly explains the Scalar DB data...
- [Getting Started with Scalar DB](./getting-started-with-scalardb.md) — Here we assume Oracle JDK 8 and the underlying storage/database such as Cassandra are properly configured. If you haven't done it, please configure them first by following this.
- [Getting Started with Scalar DB](./getting-started.md) — This document briefly explains how you can get started with Scalar DB with a simple electronic money application.
- [Getting Started with Scalar DB on Cassandra](./getting-started-with-scalardb-on-cassandra.md) — This document briefly explains how you can get started with Scalar DB on Cassandra with a simple electronic money application.
- [Getting Started with Scalar DB on Cosmos DB](./getting-started-with-scalardb-on-cosmosdb.md) — This document briefly explains how you can get started with Scalar DB on Cosmos DB with a simple electronic money application.
- [Getting Started with Scalar DB on DynamoDB](./getting-started-with-scalardb-on-dynamodb.md) — This document briefly explains how you can get started with Scalar DB on DynamoDB with a simple electronic money application.
- [Getting Started with Scalar DB on JDBC databases](./getting-started-with-scalardb-on-jdbc.md) — This document briefly explains how you can get started with Scalar DB on JDBC databases with a simple electronic money application.
- [Multi-storage Transactions](./multi-storage-transactions.md) — Scalar DB transactions can span multiple storages/databases while preserving ACID property with a feature called Multi-storage Transactions. This documentation explains the feature briefly.
- [Requirements in the Underlining Databases of Scalar DB](./requirements.md) — This document explains the requirements in the underlining databases of Scalar DB to make Scalar DB applications work correctly.
- [Scalar DB design document](./design.md) — Scalar DB is a library that makes non-ACID databases/storages ACID-compliant. This design document briefly explains its background, design, and implementation.
- [Scalar DB Schema Loader](./schema-loader.md) — Scalar DB Schema Loader creates and deletes Scalar DB schemas (namespaces and tables) on the basis of a provided schema file. Also, it automatically adds the Scalar DB transaction metadata (used in the Consensus Commit protocol) to the...
- [Scalar DB server](./scalardb-server.md) — Scalar DB server is a gRPC server that implements Scalar DB interface. With Scalar DB server, you can use Scalar DB features from multiple programming languages that are supported by gRPC.
- [Scalar DB Supported Databases](./scalardb-supported-databases.md) — Scalar DB supports the following databases and the databases that are compatible with those databases. Cassandra Cosmos DB DynamoDB MySQL PostgreSQL
- [ScalarDB Community](./section-home.md) — ScalarDB is a cross-database HTAP engine. It achieves ACID transactions and real-time analytics across diverse databases to simplify the complexity of managing multiple databases.
- [Two-phase Commit Transactions](./two-phase-commit-transactions.md) — Scalar DB also supports two-phase commit style transactions called Two-phase Commit Transactions. With Two-phase Commit Transactions, you can execute a transaction that spans multiple processes/applications (e.g., Microservices).
