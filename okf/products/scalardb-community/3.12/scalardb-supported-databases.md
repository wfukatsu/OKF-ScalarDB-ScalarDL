---
type: Concept
title: Supported Databases
description: ScalarDB supports the following databases and their versions.
resource: https://scalardb-community.scalar-labs.com/docs/3.12/scalardb-supported-databases/
tags:
- scalardb-community
- v3.12
- phase:design
- section:about-scalardb
status: stable
product: scalardb-community
product_title: ScalarDB Community
version: '3.12'
doc_id: scalardb-supported-databases
lifecycle_phase: design
breadcrumb:
- About ScalarDB
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:04Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/versioned_docs/version-3.12/scalardb-supported-databases.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# Supported Databases

ScalarDB supports the following databases and their versions.

## Amazon DynamoDB

| Version           | DynamoDB  |
|:------------------|:----------|
| **ScalarDB 3.13** | ✅        |
| **ScalarDB 3.12** | ✅        |
| **ScalarDB 3.11** | ✅        |
| **ScalarDB 3.10** | ✅        |
| **ScalarDB 3.9**  | ✅        |
| **ScalarDB 3.8**  | ✅        |
| **ScalarDB 3.7**  | ✅        |

## Apache Cassandra

:::note

For requirements when using Cassandra or Cassandra-compatible databases, see [How to configure databases to achieve the general requirements](./requirements.md#how-to-configure-databases-to-achieve-the-general-requirements).

:::

| Version           | Cassandra 4.1  | Cassandra 4.0  | Cassandra 3.11  | Cassandra 3.0  |
|:------------------|:---------------|:---------------|:----------------|:---------------|
| **ScalarDB 3.13** | ❌             | ❌             | ✅              | ✅             |
| **ScalarDB 3.12** | ❌             | ❌             | ✅              | ✅             |
| **ScalarDB 3.11** | ❌             | ❌             | ✅              | ✅             |
| **ScalarDB 3.10** | ❌             | ❌             | ✅              | ✅             |
| **ScalarDB 3.9**  | ❌             | ❌             | ✅              | ✅             |
| **ScalarDB 3.8**  | ❌             | ❌             | ✅              | ✅             |
| **ScalarDB 3.7**  | ❌             | ❌             | ✅              | ✅             |

## Azure Cosmos DB for NoSQL

| Version           | Cosmos DB for NoSQL  |
|:------------------|:---------------------|
| **ScalarDB 3.13** | ✅                   |
| **ScalarDB 3.12** | ✅                   |
| **ScalarDB 3.11** | ✅                   |
| **ScalarDB 3.10** | ✅                   |
| **ScalarDB 3.9**  | ✅                   |
| **ScalarDB 3.8**  | ✅                   |
| **ScalarDB 3.7**  | ✅                   |

## JDBC databases

:::note

For recommendations when using JDBC databases, see [Recommendations](./requirements.md#recommendations).

:::

### Amazon Aurora MySQL

| Version           | Aurora MySQL 3  | Aurora MySQL 2  |
|:------------------|:----------------|:----------------|
| **ScalarDB 3.13** | ✅              | ✅              |
| **ScalarDB 3.12** | ✅              | ✅              |
| **ScalarDB 3.11** | ✅              | ✅              |
| **ScalarDB 3.10** | ✅              | ✅              |
| **ScalarDB 3.9**  | ✅              | ✅              |
| **ScalarDB 3.8**  | ✅              | ✅              |
| **ScalarDB 3.7**  | ✅              | ✅              |

### Amazon Aurora PostgreSQL

| Version           | Aurora PostgreSQL 15  | Aurora PostgreSQL 14  | Aurora PostgreSQL 13  | Aurora PostgreSQL 12  |
|:------------------|:----------------------|:----------------------|:----------------------|:----------------------|
| **ScalarDB 3.13** | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.12** | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.11** | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.10** | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.9**  | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.8**  | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.7**  | ✅                    | ✅                    | ✅                    | ✅                    |

### MariaDB

| Version           | MariaDB 10.11 |
|:------------------|:--------------|
| **ScalarDB 3.13** | ✅            |
| **ScalarDB 3.12** | ✅            |
| **ScalarDB 3.11** | ✅            |
| **ScalarDB 3.10** | ✅            |
| **ScalarDB 3.9**  | ✅            |
| **ScalarDB 3.8**  | ✅            |
| **ScalarDB 3.7**  | ✅            |

### Microsoft SQL Server

| Version           | SQL Server 2022  | SQL Server 2019  | SQL Server 2017  |
|:------------------|:-----------------|:-----------------|:-----------------|
| **ScalarDB 3.13** | ✅               | ✅               | ✅               |
| **ScalarDB 3.12** | ✅               | ✅               | ✅               |
| **ScalarDB 3.11** | ✅               | ✅               | ✅               |
| **ScalarDB 3.10** | ✅               | ✅               | ✅               |
| **ScalarDB 3.9**  | ✅               | ✅               | ✅               |
| **ScalarDB 3.8**  | ✅               | ✅               | ✅               |
| **ScalarDB 3.7**  | ✅               | ✅               | ✅               |

### MySQL

| Version           | MySQL 8.1  | MySQL 8.0  | MySQL 5.7  |
|:------------------|:-----------|:-----------|:-----------|
| **ScalarDB 3.13** | ✅         | ✅         | ✅         |
| **ScalarDB 3.12** | ✅         | ✅         | ✅         |
| **ScalarDB 3.11** | ✅         | ✅         | ✅         |
| **ScalarDB 3.10** | ✅         | ✅         | ✅         |
| **ScalarDB 3.9**  | ✅         | ✅         | ✅         |
| **ScalarDB 3.8**  | ✅         | ✅         | ✅         |
| **ScalarDB 3.7**  | ✅         | ✅         | ✅         |

### Oracle

| Version           | Oracle 23.2.0-free  | Oracle 21.3.0-xe  | Oracle 18.4.0-xe  |
|:------------------|:--------------------|:------------------|:------------------|
| **ScalarDB 3.13** | ✅                  | ✅                | ✅                |
| **ScalarDB 3.12** | ✅                  | ✅                | ✅                |
| **ScalarDB 3.11** | ✅                  | ✅                | ✅                |
| **ScalarDB 3.10** | ✅                  | ✅                | ✅                |
| **ScalarDB 3.9**  | ✅                  | ✅                | ✅                |
| **ScalarDB 3.8**  | ✅                  | ✅                | ✅                |
| **ScalarDB 3.7**  | ✅                  | ✅                | ✅                |

### PostgreSQL

| Version           | PostgreSQL 15  | PostgreSQL 14  | PostgreSQL 13  | PostgreSQL 12  |
|:------------------|:---------------|:---------------|:---------------|:---------------|
| **ScalarDB 3.13** | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.12** | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.11** | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.10** | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.9**  | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.8**  | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.7**  | ✅             | ✅             | ✅             | ✅             |

### SQLite

| Version           | SQLite 3  |
|:------------------|:----------|
| **ScalarDB 3.13** | ✅        |
| **ScalarDB 3.12** | ✅        |
| **ScalarDB 3.11** | ✅        |
| **ScalarDB 3.10** | ✅        |
| **ScalarDB 3.9**  | ✅        |
| **ScalarDB 3.8**  | ❌        |
| **ScalarDB 3.7**  | ❌        |

### YugabyteDB

| Version           | YugabyteDB 2 |
|:------------------|:-------------|
| **ScalarDB 3.13** | ✅           |
| **ScalarDB 3.12** | ❌           |
| **ScalarDB 3.11** | ❌           |
| **ScalarDB 3.10** | ❌           |
| **ScalarDB 3.9**  | ❌           |
| **ScalarDB 3.8**  | ❌           |
| **ScalarDB 3.7**  | ❌           |
