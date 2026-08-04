---
type: Concept
title: Requirements
description: This page describes the required tools and their versions to use ScalarDL correctly.
resource: https://scalardl.scalar-labs.com/docs/latest/requirements/
tags:
- scalardl
- v3.13
- phase:design
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: requirements
lifecycle_phase: design
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:59Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/docs/requirements.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Requirements

This page describes the required tools and their versions to use ScalarDL correctly.

## Client SDK

Because ScalarDL is written in Java, the easiest way to interact with ScalarDL is to use the [Java client SDK](./getting-started.md#download-the-client-sdk).

### Java

The following Java Development Kits (JDKs) are verified and supported:

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, 17, or 21 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, 17, or 21 (LTS versions)

### Other languages

ScalarDL uses gRPC, so you can create your own client by using the generated clients of your preferred languages.

## Databases

ScalarDL is middleware that runs on top of the following databases and their versions.

### Relational databases

**Oracle Database**

| Version           | Oracle Database 23ai | Oracle Database 21c | Oracle Database 19c |
|:------------------|:---------------------|:--------------------|:--------------------|
| **ScalarDL 3.13** | ✅                   | ✅                   | ✅                  |
| **ScalarDL 3.12** | ✅                   | ✅                   | ✅                  |
| **ScalarDL 3.11** | ✅                   | ✅                   | ✅                  |
| **ScalarDL 3.10** | ✅                   | ✅                   | ✅                  |

**Db2**

| Version           | Db2 12.1 | Db2 11.5 |
|:------------------|:---------|:---------|
| **ScalarDL 3.13** | ✅        | ✅        |
| **ScalarDL 3.12** | ✅        | ✅        |
| **ScalarDL 3.11** | ❌        | ❌        |
| **ScalarDL 3.10** | ❌        | ❌        |

**MySQL**

| Version           | MySQL 8.4 | MySQL 8.0 |
|:------------------|:----------|:----------|
| **ScalarDL 3.13** | ✅        | ✅         |
| **ScalarDL 3.12** | ✅        | ✅         |
| **ScalarDL 3.11** | ✅        | ✅         |
| **ScalarDL 3.10** | ✅        | ✅         |

**PostgreSQL**

| Version           | PostgreSQL 17 | PostgreSQL 16 | PostgreSQL 15 | PostgreSQL 14 | PostgreSQL 13 |
|:------------------|:--------------|:--------------|:--------------|:--------------|:--------------|
| **ScalarDL 3.13** | ✅             | ✅             | ✅             | ✅             | ✅             |
| **ScalarDL 3.12** | ✅             | ✅             | ✅             | ✅             | ✅             |
| **ScalarDL 3.11** | ✅             | ✅             | ✅             | ✅             | ✅             |
| **ScalarDL 3.10** | ✅             | ✅             | ✅             | ✅             | ✅             |

**Amazon Aurora MySQL**

| Version           | Aurora MySQL 3  | Aurora MySQL 2  |
|:------------------|:----------------|:----------------|
| **ScalarDL 3.13** | ✅              | ✅              |
| **ScalarDL 3.12** | ✅              | ✅              |
| **ScalarDL 3.11** | ✅              | ✅              |
| **ScalarDL 3.10** | ✅              | ✅              |

**Amazon Aurora PostgreSQL**

| Version           | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 |
|:------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| **ScalarDL 3.13** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDL 3.12** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDL 3.11** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDL 3.10** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |

**MariaDB**

| Version           | MariaDB 11.4  | MariaDB 10.11 |
|:------------------|:--------------|:--------------|
| **ScalarDL 3.13** | ✅            | ✅            |
| **ScalarDL 3.12** | ✅            | ✅            |
| **ScalarDL 3.11** | ✅            | ✅            |
| **ScalarDL 3.10** | ✅            | ✅            |

**TiDB**

| Version           | TiDB 8.5 | TiDB 7.5 | TiDB 6.5 |
|:------------------|:---------|:---------|----------|
| **ScalarDL 3.13** | ✅        | ✅        | ✅        |
| **ScalarDL 3.12** | ❌        | ❌        | ❌        |
| **ScalarDL 3.11** | ❌        | ❌        | ❌        |
| **ScalarDL 3.10** | ❌        | ❌        | ❌        |

**AlloyDB**

| Version           | AlloyDB 16 | AlloyDB 15 |
|:------------------|:-----------|:-----------|
| **ScalarDL 3.13** | ✅          | ✅          |
| **ScalarDL 3.12** | ❌          | ❌          |
| **ScalarDL 3.11** | ❌          | ❌          |
| **ScalarDL 3.10** | ❌          | ❌          |

**SQL Server**

| Version           | SQL Server 2022  | SQL Server 2019  | SQL Server 2017  |
|:------------------|:-----------------|:-----------------|:-----------------|
| **ScalarDL 3.13** | ✅               | ✅               | ✅               |
| **ScalarDL 3.12** | ✅               | ✅               | ✅               |
| **ScalarDL 3.11** | ✅               | ✅               | ✅               |
| **ScalarDL 3.10** | ✅               | ✅               | ✅               |

**SQLite**

| Version           | SQLite 3  |
|:------------------|:----------|
| **ScalarDL 3.13** | ✅        |
| **ScalarDL 3.12** | ✅        |
| **ScalarDL 3.11** | ✅        |
| **ScalarDL 3.10** | ✅        |

**YugabyteDB**

| Version           | YugabyteDB 2 |
|:------------------|:-------------|
| **ScalarDL 3.13** | ✅           |
| **ScalarDL 3.12** | ✅           |
| **ScalarDL 3.11** | ✅           |
| **ScalarDL 3.10** | ✅           |

### NoSQL databases

**Amazon DynamoDB**

| Version           | DynamoDB  |
|:------------------|:----------|
| **ScalarDL 3.13** | ✅        |
| **ScalarDL 3.12** | ✅        |
| **ScalarDL 3.11** | ✅        |
| **ScalarDL 3.10** | ✅        |

**Apache Cassandra**

| Version           | Cassandra 5.0  | Cassandra 4.1  | Cassandra 3.11  | Cassandra 3.0  |
|:------------------|:---------------|:---------------|:----------------|:---------------|
| **ScalarDL 3.13** | ✅             | ✅             | ✅              | ✅             |
| **ScalarDL 3.12** | ✅             | ✅             | ✅              | ✅             |
| **ScalarDL 3.11** | ✅             | ✅             | ✅              | ✅             |
| **ScalarDL 3.10** | ✅             | ✅             | ✅              | ✅             |

**Azure Cosmos DB for NoSQL**

| Version           | Cosmos DB for NoSQL  |
|:------------------|:---------------------|
| **ScalarDL 3.13** | ✅                   |
| **ScalarDL 3.12** | ✅                   |
| **ScalarDL 3.11** | ✅                   |
| **ScalarDL 3.10** | ✅                   |

:::note

ScalarDL uses ScalarDB to abstract underlying databases. For details on how to configure each database, see [Configurations for the Underlying Databases of ScalarDB](https://scalardb.scalar-labs.com/docs/latest/database-configurations).

The following list shows the versions of ScalarDB used in ScalarDL internally. This version list will help you if:

- You want to know what available backend databases you can use in ScalarDL. For details about which backend databases are supported and can be used in ScalarDL based on the version of ScalarDB, see the [list of databases that ScalarDB supports](https://scalardb.scalar-labs.com/docs/latest/requirements#databases/).
- You want to know what ScalarDB APIs are available for the `Function` feature in ScalarDL.

| ScalarDL version              | ScalarDB version |
|:------------------------------|:-----------------|
| 3.13                          | 3.17             |
| 3.12                          | 3.16             |
| 3.11                          | 3.15             |
| 3.10                          | 3.14             |

:::

## Required ports

ScalarDL requires the following ports to be accessible. These default port numbers can be configured as needed:

- **ScalarDL Ledger**
  - 50051 (normal request)
  - 50052 (privileged request)
  - 50053 (pause request)
  - 8080 (metrics)
- **ScalarDL Auditor**
  - 40051 (normal request)
  - 40052 (privileged request)
  - 40053 (pause request)
  - 8080 (metrics)
- **ScalarDL Gateway**
  - 30051 (normal request)
  - 30052 (privileged request)
  - 30053 (pause request)
  - 8080 (metrics)

## Kubernetes

ScalarDL is provided as a Pod on the Kubernetes platform in production environments. ScalarDL supports the following platforms and tools.

### Platform

- **[Kubernetes](https://kubernetes.io/):** 1.32 - 1.35
  - **[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)**
  - **[Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service)**
- **[Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift):** TBD

### Package manager

- **[Helm](https://helm.sh/):** 3.5+
