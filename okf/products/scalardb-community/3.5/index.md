---
type: Product Version
title: ScalarDB Community 3.5
description: Documentation set for ScalarDB Community 3.5.
resource: https://scalardb-community.scalar-labs.com/docs/3.5/
tags:
- scalardb-community
- v3.5
- product-version
- unmaintained
status: deprecated
product: scalardb-community
product_title: ScalarDB Community
version: '3.5'
url_path: '3.5'
maintenance: unmaintained
is_latest: false
concept_count: 22
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:05Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/tree/71d199cb0df1c638bd7e305b64fa09fc7236e5c4
  title: ScalarDB Community documentation repository
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# ScalarDB Community 3.5

**Unmaintained release.** Prefer a supported version for new work; kept here for systems still running it.

| | |
|---|---|
| Product | ScalarDB Community |
| Documentation version | 3.5 |
| Docs site | https://scalardb-community.scalar-labs.com/docs/3.5/ |
| Upstream source | https://github.com/scalar-labs/docs-scalardb-community @ `71d199cb0df1` |
| Concepts in this version | 22 |

## By lifecycle phase

Start here when you know which phase of the project you are in.

### 実装 / Implement (19)

- [A Guide on How to Handle Exceptions](./how-to-handle-exceptions.md)
- [Add ScalarDB to Your Build](./add-scalardb-to-your-build.md)
- [Database schema in Scalar DB](./schema.md)
- [Getting Started with ScalarDB](./getting-started-with-scalardb.md)
- [Getting Started with ScalarDB by Using Kotlin](./getting-started-with-scalardb-by-using-kotlin.md)
- [Multi-Storage Transactions](./multi-storage-transactions.md)
- [Requirements and Recommendations for the Underlying Databases of ScalarDB](./requirements.md)
- [Scalar DB design document](./design.md)
- [ScalarDB Community](./section-home.md)
- [ScalarDB Configurations](./configurations.md)
- [ScalarDB Schema Loader](./schema-loader.md)
- [Supported Databases](./scalardb-supported-databases.md)
- [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md)
- [ScalarDB Benchmarking Tools](./scalardb-benchmarks/README.md)
- [ScalarDB Samples](./scalardb-samples/README.md)
- [Create a Sample Application That Supports Microservice Transactions](./scalardb-samples/microservice-transaction-sample/README.md)
- [Create a Sample Application That Supports Multi-Storage Transactions](./scalardb-samples/multi-storage-transaction-sample/README.md)
- [Create a Sample Application That Uses ScalarDB](./scalardb-samples/scalardb-sample/README.md)
- [ScalarDB Server Sample](./scalardb-samples/scalardb-server-sample/README.md)

### 運用 / Operate (3)

- [How to Back Up and Restore Databases Used Through ScalarDB](./backup-restore.md)
- [Scalar DB server](./scalardb-server.md)
- [ScalarDB 3.5 Release Notes](./releases/release-notes.md)

## Sections

- [releases](./releases/index.md)
- [scalardb-benchmarks](./scalardb-benchmarks/index.md)
- [scalardb-samples](./scalardb-samples/index.md)

## Top-level concepts

- [A Guide on How to Handle Exceptions](./how-to-handle-exceptions.md) — Handling exceptions correctly in Scalar DB is very important. If you mishandle exceptions, your data could become inconsistent. This document explains how to handle exceptions properly in Scalar DB.
- [Add ScalarDB to Your Build](./add-scalardb-to-your-build.md) — The ScalarDB library is available on the Maven Central Repository. You can add the library as a build dependency to your application by using Gradle or Maven.
- [Database schema in Scalar DB](./schema.md) — Scalar DB has its own data model and schema, that maps to the implementation specific data model and schema. Also, it stores internal metadata for managing transaction logs and statuses. This document briefly explains the Scalar DB data...
- [Getting Started with ScalarDB](./getting-started-with-scalardb.md) — This getting started tutorial explains how to configure your preferred database in ScalarDB and set up a basic electronic money application.
- [Getting Started with ScalarDB by Using Kotlin](./getting-started-with-scalardb-by-using-kotlin.md) — This getting started tutorial explains how to configure your preferred database in ScalarDB and set up a basic electronic money application by using Kotlin. Since Kotlin has Java interoperability, you can use ScalarDB directly from Kotlin.
- [How to Back Up and Restore Databases Used Through ScalarDB](./backup-restore.md) — Since ScalarDB provides transaction capabilities on top of non-transactional or transactional databases non-invasively, you need to take special care to back up and restore the databases in a transactionally consistent way.
- [Multi-Storage Transactions](./multi-storage-transactions.md) — ScalarDB transactions can span multiple storages or databases while maintaining ACID compliance by using a feature called multi-storage transactions.
- [Requirements and Recommendations for the Underlying Databases of ScalarDB](./requirements.md) — This document explains the requirements and recommendations in the underlying databases of ScalarDB to make ScalarDB applications work correctly.
- [Scalar DB design document](./design.md) — Scalar DB is a library that makes non-ACID databases/storages ACID-compliant. This design document briefly explains its background, design, and implementation.
- [Scalar DB server](./scalardb-server.md) — Scalar DB server is a gRPC server that implements Scalar DB interface. With Scalar DB server, you can use Scalar DB features from multiple programming languages that are supported by gRPC.
- [ScalarDB Community](./section-home.md) — ScalarDB is a cross-database HTAP engine. It achieves ACID transactions and real-time analytics across diverse databases to simplify the complexity of managing multiple databases.
- [ScalarDB Configurations](./configurations.md) — This page describes the available configurations for ScalarDB.
- [ScalarDB Schema Loader](./schema-loader.md) — ScalarDB has its own data model and schema that maps to the implementation-specific data model and schema. In addition, ScalarDB stores internal metadata, such as transaction IDs, record versions, and transaction statuses, to manage...
- [Supported Databases](./scalardb-supported-databases.md) — ScalarDB supports the following databases and their versions.
- [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md) — ScalarDB supports executing transactions with a two-phase commit interface. With the two-phase commit interface, you can execute a transaction that spans multiple processes or applications, like in a microservice architecture.
