---
type: Product Version
title: ScalarDB Community 3.12
description: Documentation set for ScalarDB Community 3.12.
resource: https://scalardb-community.scalar-labs.com/docs/3.12/
tags:
- scalardb-community
- v3.12
- product-version
status: stable
product: scalardb-community
product_title: ScalarDB Community
version: '3.12'
url_path: '3.12'
maintenance: supported
is_latest: false
concept_count: 34
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:04Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/tree/71d199cb0df1c638bd7e305b64fa09fc7236e5c4
  title: ScalarDB Community documentation repository
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# ScalarDB Community 3.12

Supported release.

| | |
|---|---|
| Product | ScalarDB Community |
| Documentation version | 3.12 |
| Docs site | https://scalardb-community.scalar-labs.com/docs/3.12/ |
| Upstream source | https://github.com/scalar-labs/docs-scalardb-community @ `71d199cb0df1` |
| Concepts in this version | 34 |

## By lifecycle phase

Start here when you know which phase of the project you are in.

### 設計 / Design (5)

- [Requirements](./requirements.md)
- [ScalarDB Design Document](./design.md)
- [ScalarDB Overview](./overview.md)
- [Supported Databases](./scalardb-supported-databases.md)
- [ScalarDB 3.12 Release Notes](./releases/release-notes.md)

### 実装 / Implement (25)

- [Add ScalarDB to Your Build](./add-scalardb-to-your-build.md)
- [Configurations for the Underlying Databases of ScalarDB](./database-configurations.md)
- [Develop Overview](./develop-overview.md)
- [Getting Started with ScalarDB](./getting-started-with-scalardb.md)
- [Getting Started with ScalarDB by Using Kotlin](./getting-started-with-scalardb-by-using-kotlin.md)
- [Model Your Data](./data-modeling.md)
- [Multi-Storage Transactions](./multi-storage-transactions.md)
- [Quickstart Overview](./quick-start-overview.md)
- [Run Non-Transactional Storage Operations Through the Core Library](./run-non-transactional-storage-operations-through-library.md)
- [Run Non-Transactional Storage Operations Through the Primitive CRUD Interface](./run-non-transactional-storage-operations-through-primitive-crud-interface.md)
- [Run Transactions Through the ScalarDB Core Library](./run-transactions-through-scalardb-core-library.md)
- [ScalarDB Community](./section-home.md)
- [ScalarDB Configurations](./configurations.md)
- [ScalarDB Java API Guide](./api-guide.md)
- [ScalarDB Schema Loader](./schema-loader.md)
- [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md)
- [Getting Started with ScalarDB Analytics with PostgreSQL](./scalardb-analytics-postgresql/getting-started.md)
- [How to Install ScalarDB Analytics with PostgreSQL in Your Local Environment by Using Docker](./scalardb-analytics-postgresql/installation.md)
- [ScalarDB FDW](./scalardb-analytics-postgresql/scalardb-fdw.md)
- [Schema Importer](./scalardb-analytics-postgresql/schema-importer.md)
- [ScalarDB Benchmarking Tools](./scalardb-benchmarks/README.md)
- [ScalarDB Samples](./scalardb-samples/README.md)
- [Create a Sample Application That Supports Microservice Transactions](./scalardb-samples/microservice-transaction-sample/README.md)
- [Create a Sample Application That Supports Multi-Storage Transactions](./scalardb-samples/multi-storage-transaction-sample/README.md)
- [Run Analytical Queries on Sample Data by Using ScalarDB Analytics with PostgreSQL](./scalardb-samples/scalardb-analytics-postgresql-sample/README.md)

### 運用 / Operate (4)

- [How to Back Up and Restore Databases Used Through ScalarDB](./backup-restore.md)
- [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](./schema-loader-import.md)
- [ScalarDB Error Codes](./scalardb-core-status-codes.md)
- [ScalarDB Server](./scalardb-server.md)

## Sections

- [releases](./releases/index.md)
- [scalardb-analytics-postgresql](./scalardb-analytics-postgresql/index.md)
- [scalardb-benchmarks](./scalardb-benchmarks/index.md)
- [scalardb-samples](./scalardb-samples/index.md)

## Top-level concepts

- [Add ScalarDB to Your Build](./add-scalardb-to-your-build.md) — The ScalarDB library is available on the Maven Central Repository. You can add the library as a build dependency to your application by using Gradle or Maven.
- [Configurations for the Underlying Databases of ScalarDB](./database-configurations.md) — This document explains how to configure the underlying databases of ScalarDB to make applications that use ScalarDB work correctly and efficiently.
- [Develop Overview](./develop-overview.md) — In this category, you can follow guides to help you become more familiar with ScalarDB, specifically with how to run transactions, analytical queries, and non-transactional storage operations.
- [Getting Started with ScalarDB](./getting-started-with-scalardb.md) — This getting started tutorial explains how to configure your preferred database in ScalarDB and illustrates the process of creating a sample e-commerce application, where items can be ordered and paid for with a credit card by using...
- [Getting Started with ScalarDB by Using Kotlin](./getting-started-with-scalardb-by-using-kotlin.md) — This getting started tutorial explains how to configure your preferred database in ScalarDB and set up a basic electronic money application by using Kotlin. Since Kotlin has Java interoperability, you can use ScalarDB directly from Kotlin.
- [How to Back Up and Restore Databases Used Through ScalarDB](./backup-restore.md) — Since ScalarDB provides transaction capabilities on top of non-transactional or transactional databases non-invasively, you need to take special care to back up and restore the databases in a transactionally consistent way.
- [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](./schema-loader-import.md) — You might want to use ScalarDB (e.g., for database-spanning transactions) with your existing databases. In that case, you can import those databases under the ScalarDB control using ScalarDB Schema Loader. ScalarDB Schema Loader...
- [Model Your Data](./data-modeling.md) — Data modeling (or in other words, designing your database schemas) is the process of conceptualizing and visualizing how data will be stored and used by identifying the patterns used to access data and the types of queries to be performed...
- [Multi-Storage Transactions](./multi-storage-transactions.md) — ScalarDB transactions can span multiple storages or databases while maintaining ACID compliance by using a feature called multi-storage transactions.
- [Quickstart Overview](./quick-start-overview.md) — In this category, you can follow quickstart tutorials for how to get started with running transactions and queries through ScalarDB.
- [Requirements](./requirements.md) — This page describes the required tools and their versions to use ScalarDB correctly.
- [Run Non-Transactional Storage Operations Through the Core Library](./run-non-transactional-storage-operations-through-library.md) — This guide explains how to run non-transactional storage operations through the ScalarDB core library.
- [Run Non-Transactional Storage Operations Through the Primitive CRUD Interface](./run-non-transactional-storage-operations-through-primitive-crud-interface.md) — This page explains how to run non-transactional storage operations through the primitive CRUD interface, also known as the Storage API. This guide assumes that you have an advanced understanding of ScalarDB.
- [Run Transactions Through the ScalarDB Core Library](./run-transactions-through-scalardb-core-library.md) — This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using the ScalarDB core library.
- [ScalarDB Community](./section-home.md) — ScalarDB is a cross-database HTAP engine. It achieves ACID transactions and real-time analytics across diverse databases to simplify the complexity of managing multiple databases.
- [ScalarDB Configurations](./configurations.md) — This page describes the available configurations for ScalarDB.
- [ScalarDB Design Document](./design.md) — For details about the design and implementation of ScalarDB, please see the following documents, which we presented at the VLDB 2023 conference:
- [ScalarDB Error Codes](./scalardb-core-status-codes.md) — This page provides a list of error codes in ScalarDB.
- [ScalarDB Java API Guide](./api-guide.md) — The ScalarDB Java API is mainly composed of the Administrative API and Transactional API. This guide briefly explains what kinds of APIs exist, how to use them, and related topics like how to handle exceptions.
- [ScalarDB Overview](./overview.md) — This page describes what ScalarDB is and its primary use cases.
- [ScalarDB Schema Loader](./schema-loader.md) — ScalarDB has its own data model and schema that maps to the implementation-specific data model and schema. In addition, ScalarDB stores internal metadata, such as transaction IDs, record versions, and transaction statuses, to manage...
- [ScalarDB Server](./scalardb-server.md) — ScalarDB Server is a gRPC server that implements ScalarDB interface. With ScalarDB Server, you can use ScalarDB features from multiple programming languages that are supported by gRPC.
- [Supported Databases](./scalardb-supported-databases.md) — ScalarDB supports the following databases and their versions.
- [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md) — ScalarDB supports executing transactions with a two-phase commit interface. With the two-phase commit interface, you can execute a transaction that spans multiple processes or applications, like in a microservice architecture.
