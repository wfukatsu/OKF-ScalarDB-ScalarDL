---
type: Concept
title: Requirements
description: This page outlines the requirements for using each ScalarDB component, including the programming languages and their versions, supported databases and their versions, and the necessary configurations.
resource: https://scalardb.scalar-labs.com/docs/3.17/requirements/
tags:
- scalardb
- v3.17
- phase:design
- section:about-scalardb
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.3
doc_id: requirements
lifecycle_phase: design
breadcrumb:
- About ScalarDB
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:26Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.17/requirements.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Requirements

This page outlines the requirements for using each ScalarDB component, including the programming languages and their versions, supported databases and their versions, and the necessary configurations.

## Core

ScalarDB Core is a key component of ScalarDB, providing a database manager with an abstraction layer that abstracts underlying databases. For more information, see [ScalarDB Design](./design.md).

### Languages and runtimes

ScalarDB Core provides a Java client SDK for interacting with ScalarDB. It also includes tools, such as Schema Loader and Data Loader, which run on the Java Virtual Machine (JVM).

#### Java

The ScalarDB Core library is available on the Maven Central Repository. You can add the library as a build dependency to your application by using Gradle or Maven. For more details, see [Add ScalarDB to Your Build](./add-scalardb-to-your-build.md).

For building applications that integrate with the library, the following Java Development Kits (JDKs) are verified and supported.

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, 17, or 21 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, 17, or 21 (LTS versions)

Java Runtime Environments (JREs) of these JDKs are also supported for running the tools.

### Databases

ScalarDB runs on top of the following databases and their versions.

#### Relational databases

**IBM Db2**

|      Version      | Db2 12.1 | Db2 11.5 |
| :---------------- | :------- | :------- |
| **ScalarDB 3.17** | ✅        | ✅        |
| **ScalarDB 3.16** | ✅        | ✅        |
| **ScalarDB 3.15** | ❌        | ❌        |
| **ScalarDB 3.14** | ❌        | ❌        |

:::note

Only Linux, UNIX, and Windows versions of Db2 are supported. The z/OS version is not currently supported.

:::

**MariaDB**

|      Version      | MariaDB 11.4 | MariaDB 10.11 |
| :---------------- | :----------- | :------------ |
| **ScalarDB 3.17** | ✅            | ✅             |
| **ScalarDB 3.16** | ✅            | ✅             |
| **ScalarDB 3.15** | ✅            | ✅             |
| **ScalarDB 3.14** | ✅            | ✅             |

**MySQL**

|      Version      | MySQL 8.4 | MySQL 8.0 |
| :---------------- | :-------- | :-------- |
| **ScalarDB 3.17** | ✅         | ✅         |
| **ScalarDB 3.16** | ✅         | ✅         |
| **ScalarDB 3.15** | ✅         | ✅         |
| **ScalarDB 3.14** | ✅         | ✅         |

**Oracle Database**

|      Version      | Oracle Database 23ai | Oracle Database 21c | Oracle Database 19c |
| :---------------- | :------------------- | :------------------ | :------------------ |
| **ScalarDB 3.17** | ✅                    | ✅                   | ✅                   |
| **ScalarDB 3.16** | ✅                    | ✅                   | ✅                   |
| **ScalarDB 3.15** | ✅                    | ✅                   | ✅                   |
| **ScalarDB 3.14** | ✅                    | ✅                   | ✅                   |

**PostgreSQL**

|      Version      | PostgreSQL 17 | PostgreSQL 16 | PostgreSQL 15 | PostgreSQL 14 | PostgreSQL 13 |
| :---------------- | :------------ | :------------ | :------------ | :------------ | ------------- |
| **ScalarDB 3.17** | ✅             | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.16** | ✅             | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.15** | ✅             | ✅             | ✅             | ✅             | ✅             |
| **ScalarDB 3.14** | ✅             | ✅             | ✅             | ✅             | ✅             |

**SQL Server**

|      Version      | SQL Server 2022 | SQL Server 2019 | SQL Server 2017 |
| :---------------- | :-------------- | :-------------- | :-------------- |
| **ScalarDB 3.17** | ✅               | ✅               | ✅               |
| **ScalarDB 3.16** | ✅               | ✅               | ✅               |
| **ScalarDB 3.15** | ✅               | ✅               | ✅               |
| **ScalarDB 3.14** | ✅               | ✅               | ✅               |

**SQLite**

|      Version      | SQLite 3 |
| :---------------- | :------- |
| **ScalarDB 3.17** | ✅        |
| **ScalarDB 3.16** | ✅        |
| **ScalarDB 3.15** | ✅        |
| **ScalarDB 3.14** | ✅        |

#### NewSQL databases

**AlloyDB**

| Version           | AlloyDB 16 | AlloyDB 15 |
|:------------------|:-----------|:-----------|
| **ScalarDB 3.17** | ✅          | ✅          |
| **ScalarDB 3.16** | ❌          | ❌          |
| **ScalarDB 3.15** | ❌          | ❌          |
| **ScalarDB 3.14** | ❌          | ❌          |

**Amazon Aurora MySQL**

|      Version      | Aurora MySQL 3 | Aurora MySQL 2 |
| :---------------- | :------------- | :------------- |
| **ScalarDB 3.17** | ✅              | ✅              |
| **ScalarDB 3.16** | ✅              | ✅              |
| **ScalarDB 3.15** | ✅              | ✅              |
| **ScalarDB 3.14** | ✅              | ✅              |

**Amazon Aurora PostgreSQL**

| Version           | Aurora PostgreSQL 17 | Aurora PostgreSQL 16 | Aurora PostgreSQL 15 | Aurora PostgreSQL 14 | Aurora PostgreSQL 13 |
|:------------------|:---------------------|:---------------------|:---------------------|:---------------------|:---------------------|
| **ScalarDB 3.17** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.16** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.15** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |
| **ScalarDB 3.14** | ✅                    | ✅                    | ✅                    | ✅                    | ✅                    |

**TiDB**

| Version           | TiDB 8.5 | TiDB 7.5 | TiDB 6.5 |
|:------------------|:---------|:---------|----------|
| **ScalarDB 3.17** | ✅        | ✅        | ✅        |
| **ScalarDB 3.16** | ❌        | ❌        | ❌        |
| **ScalarDB 3.15** | ❌        | ❌        | ❌        |
| **ScalarDB 3.14** | ❌        | ❌        | ❌        |

**YugabyteDB**

|      Version      | YugabyteDB 2 |
| :---------------- | :----------- |
| **ScalarDB 3.17** | ✅            |
| **ScalarDB 3.16** | ✅            |
| **ScalarDB 3.15** | ✅            |
| **ScalarDB 3.14** | ✅            |

#### NoSQL databases

**Amazon DynamoDB**

|      Version      | DynamoDB |
| :---------------- | :------- |
| **ScalarDB 3.17** | ✅        |
| **ScalarDB 3.16** | ✅        |
| **ScalarDB 3.15** | ✅        |
| **ScalarDB 3.14** | ✅        |

**Apache Cassandra**

|      Version      | Cassandra 5.0 | Cassandra 4.1 | Cassandra 3.11 | Cassandra 3.0 |
| :---------------- |:--------------|:--------------| :------------- | :------------ |
| **ScalarDB 3.17** | ✅             | ✅             | ✅              | ✅             |
| **ScalarDB 3.16** | ✅             | ✅             | ✅              | ✅             |
| **ScalarDB 3.15** | ✅             | ✅             | ✅              | ✅             |
| **ScalarDB 3.14** | ✅             | ✅             | ✅              | ✅             |

**Azure Cosmos DB for NoSQL**

|      Version      | Cosmos DB for NoSQL |
| :---------------- | :------------------ |
| **ScalarDB 3.17** | ✅                   |
| **ScalarDB 3.16** | ✅                   |
| **ScalarDB 3.15** | ✅                   |
| **ScalarDB 3.14** | ✅                   |

#### Object Storage

:::note

Object Storage support is currently in Private Preview. For more details, please [contact us](https://www.scalar-labs.com/contact) or wait for this feature to become publicly available in a future version.

:::

**Amazon S3**

|      Version      | S3 |
| :---------------- | :------------------ |
| **ScalarDB 3.17** | ✅                   |
| **ScalarDB 3.16** | ❌                   |
| **ScalarDB 3.15** | ❌                   |
| **ScalarDB 3.14** | ❌                   |

**Azure Blob Storage**

|      Version      | Blob Storage |
| :---------------- | :------------------ |
| **ScalarDB 3.17** | ✅                   |
| **ScalarDB 3.16** | ❌                   |
| **ScalarDB 3.15** | ❌                   |
| **ScalarDB 3.14** | ❌                   |

**Google Cloud Storage**

|      Version      | Cloud Storage |
| :---------------- | :------------------ |
| **ScalarDB 3.17** | ✅                   |
| **ScalarDB 3.16** | ❌                   |
| **ScalarDB 3.15** | ❌                   |
| **ScalarDB 3.14** | ❌                   |

:::note

For details on how to configure each database, see [Configurations for the Underlying Databases of ScalarDB](./database-configurations.md).

:::

### Database permission requirements

ScalarDB requires specific permissions to perform its operations on the underlying databases.

:::note

ScalarDB assumes that the same underlying database user account is used for all administrative and CRUD operations.

:::

#### Relational databases

This section describes the permission requirements for relational databases.

**IBM Db2**

If you're using Db2, the following authority must be granted.

**Db2 12.1**

- `DBADM`

**Db2 11.5**

- `DBADM`

**MariaDB**

If you're using MariaDB, the following privileges must be granted.

**MariaDB 11.4**

- `CREATE`
- `CREATE VIEW`
- `DROP`
- `INDEX`
- `ALTER`
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

**MariaDB 10.11**

- `CREATE`
- `CREATE VIEW`
- `DROP`
- `INDEX`
- `ALTER`
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

**MySQL**

If you're using MySQL, the following privileges must be granted.

**MySQL 8.4**

- `CREATE`
- `CREATE VIEW`
- `DROP`
- `INDEX`
- `ALTER`
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

**MySQL 8.0**

- `CREATE`
- `CREATE VIEW`
- `DROP`
- `INDEX`
- `ALTER`
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

**Oracle Database**

If you're using Oracle Database, the following privileges must be granted.

**Oracle Database 23ai**

- `CREATE SESSION`
- `CREATE USER`
- `DROP USER`
- `ALTER USER`
- `CREATE ANY TABLE`
- `DROP ANY TABLE`
- `CREATE ANY INDEX`
- `ALTER ANY INDEX`
- `DROP ANY INDEX`
- `ALTER ANY TABLE`
- `SELECT ANY TABLE`
- `INSERT ANY TABLE`
- `UPDATE ANY TABLE`
- `DELETE ANY TABLE`
- `CREATE ANY VIEW`
- `DROP ANY VIEW`

**Oracle Database 21c**

- `CREATE SESSION`
- `CREATE USER`
- `DROP USER`
- `ALTER USER`
- `CREATE ANY TABLE`
- `DROP ANY TABLE`
- `CREATE ANY INDEX`
- `ALTER ANY INDEX`
- `DROP ANY INDEX`
- `ALTER ANY TABLE`
- `SELECT ANY TABLE`
- `INSERT ANY TABLE`
- `UPDATE ANY TABLE`
- `DELETE ANY TABLE`
- `CREATE ANY VIEW`
- `DROP ANY VIEW`

**Oracle Database 19c**

- `CREATE SESSION`
- `CREATE USER`
- `DROP USER`
- `ALTER USER`
- `CREATE ANY TABLE`
- `DROP ANY TABLE`
- `CREATE ANY INDEX`
- `ALTER ANY INDEX`
- `DROP ANY INDEX`
- `ALTER ANY TABLE`
- `SELECT ANY TABLE`
- `INSERT ANY TABLE`
- `UPDATE ANY TABLE`
- `DELETE ANY TABLE`
- `CREATE ANY VIEW`
- `DROP ANY VIEW`

**PostgreSQL**

If you're using PostgreSQL, the following database privilege must be granted.

**PostgreSQL 17**

- `CREATE`

**PostgreSQL 16**

- `CREATE`

**PostgreSQL 15**

- `CREATE`

**PostgreSQL 14**

- `CREATE`

**PostgreSQL 13**

- `CREATE`

**SQL Server**

If you're using SQL Server, the following database permissions must be granted.

**SQL Server 2022**

- `CREATE SCHEMA`
- `CREATE TABLE`
- `CREATE VIEW`

**SQL Server 2019**

- `CREATE SCHEMA`
- `CREATE TABLE`
- `CREATE VIEW`

**SQL Server 2017**

- `CREATE SCHEMA`
- `CREATE TABLE`
- `CREATE VIEW`

#### NewSQL databases

This section describes the permission requirements for NewSQL databases.

**AlloyDB**

If you're using AlloyDB, the following database privilege must be granted.

**AlloyDB 16**

- `CREATE`

**AlloyDB 15**

- `CREATE`

**TiDB**

If you're using TiDB, the following privileges must be granted.

**TiDB 8.5**

- `CREATE`
- `CREATE VIEW`
- `DROP`
- `INDEX`
- `ALTER`
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

**TiDB 7.5**

- `CREATE`
- `CREATE VIEW`
- `DROP`
- `INDEX`
- `ALTER`
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

**TiDB 6.5**

- `CREATE`
- `CREATE VIEW`
- `DROP`
- `INDEX`
- `ALTER`
- `SELECT`
- `INSERT`
- `UPDATE`
- `DELETE`

**YugabyteDB**

If you're using YugabyteDB, the following database privilege must be granted.

- `CREATE`

#### NoSQL databases

This section describes the permission requirements for NoSQL databases.

**Amazon DynamoDB**

If you're using Amazon DynamoDB, the following actions must be granted.

- `dynamodb:ConditionCheckItem`
- `dynamodb:PutItem`
- `dynamodb:ListTables`
- `dynamodb:DeleteItem`
- `dynamodb:Scan`
- `dynamodb:Query`
- `dynamodb:UpdateItem`
- `dynamodb:DeleteTable`
- `dynamodb:UpdateContinuousBackups`
- `dynamodb:CreateTable`
- `dynamodb:DescribeTable`
- `dynamodb:GetItem`
- `dynamodb:DescribeContinuousBackups`
- `dynamodb:UpdateTable`
- `application-autoscaling:RegisterScalableTarget`
- `application-autoscaling:DeleteScalingPolicy`
- `application-autoscaling:PutScalingPolicy`
- `application-autoscaling:DeregisterScalableTarget`
- `application-autoscaling:TagResource`

**Apache Cassandra**

If you're using Apache Cassandra, the following privileges must be granted.

**Cassandra 5.0**

- `CREATE`
- `DROP`
- `ALTER`
- `SELECT`
- `MODIFY`

**Cassandra 4.1**

- `CREATE`
- `DROP`
- `ALTER`
- `SELECT`
- `MODIFY`

**Cassandra 3.11**

- `CREATE`
- `DROP`
- `ALTER`
- `SELECT`
- `MODIFY`

**Cassandra 3.0**

- `CREATE`
- `DROP`
- `ALTER`
- `SELECT`
- `MODIFY`

**Azure Cosmos DB for NoSQL**

ScalarDB requires an Azure Cosmos DB key, which has full access to Azure Cosmos DB for NoSQL, for authentication.

#### Object Storage

This section describes the permission requirements for object storage.

**Amazon S3**

If you're using Amazon S3 as Object Storage, the following actions must be granted:

- `s3:PutObject`
- `s3:GetObject`
- `s3:DeleteObject`
- `s3:ListBucket`

**Azure Blob Storage**

ScalarDB requires an access key, which has full access to Azure Blob Storage, for authentication.

**Google Cloud Storage**

If you're using Google Cloud Storage as Object Storage, the following role must be granted:

- `Storage Object Admin (roles/storage.objectAdmin)`

## Cluster

ScalarDB Cluster is a component that provides a clustering solution for the Core component to work as a clustered server. For more information, see [ScalarDB Design](./design.md).

### Languages and runtimes

ScalarDB Cluster provides Java and .NET client SDKs that wrap gRPC-generated clients for ease of use.

#### Java

The Java client SDK for ScalarDB Cluster is available on the Maven Central Repository. You can add the library as a build dependency to your application by using Gradle or Maven. For more details, see [Add ScalarDB Cluster Java Client SDK to your build](./scalardb-cluster/developer-guide-for-scalardb-cluster-with-java-api.md#add-scalardb-cluster-java-client-sdk-to-your-build).

For building applications that integrate with the library, the following Java Development Kits (JDKs) are verified and supported:

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, 17, or 21 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, 17, or 21 (LTS versions)

:::note

The ScalarDB Cluster Embedding Java Client SDK library requires Java 17 or 21 from one of the vendors listed above.

:::

#### .NET

The .NET client SDK for ScalarDB Cluster is available as a NuGet package. For more details, see [Install the SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-distributed-transactions.md#install-the-sdk).

For building applications that integrate with the library, the following .NET versions are verified and supported:

- [.NET 8.0](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)
- [.NET 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0)

#### Other languages

Since ScalarDB Cluster uses gRPC, you can also create your own client in your preferred language by using the generated clients from the proto file. If you need the proto file, please [contact support](https://www.scalar-labs.com/support).

### Databases

Since ScalarDB Cluster uses Core to interact with databases, the requirements for databases are the same as those for Core. For more information, see [Databases](#databases).

### Required ports

ScalarDB Cluster requires the following ports to be accessible. These default port numbers can be configured as needed:

- 60053 (Administrative API / Transactional API / SQL API / pause operation)
- 8080 (GraphQL)
- 9080 (metrics)

### Kubernetes

ScalarDB Cluster is provided as a cluster consisting of one or more Pods on the Kubernetes platform in production environments. ScalarDB Cluster supports the following platforms and tools.

#### Platform

- **[Kubernetes](https://kubernetes.io/):** 1.32 - 1.35
  - **[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)**
  - **[Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service)**
- **[Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift):** 4.18 - 4.21

  :::note

  - ScalarDB Cluster does not support Extended Update Support (EUS) versions of **Red Hat OpenShift**.
  - ScalarDB Cluster for Red Hat OpenShift is provided as a container image based on Red Hat Universal Base Images (UBI), which uses Red Hat Build of OpenJDK.
  - If you plan to use Red Hat OpenShift, it is your responsibility to ensure you have a valid subscription. Please contact Red Hat directly for more information. Red Hat offers various subscription options for Red Hat OpenShift, and you may also need to purchase a separate subscription for Red Hat Build of OpenJDK.

  :::

#### Package manager

- **[Helm](https://helm.sh/):** 3.5+

## Analytics

ScalarDB Analytics is a component that provides scalable analytical processing for the data managed by the Core component or managed by applications that don't use ScalarDB. For more information, see [ScalarDB Design](./design.md).

### Spark

ScalarDB Analytics uses [Apache Spark](https://spark.apache.org/) for the query engine. It supports the following versions of Spark. Cloud-managed Spark services, such as Amazon EMR, Azure Synapse Analytics, and Databricks, are also supported as long as they use the Spark versions listed in the following table.

| ScalarDB Analytics Version | Spark Versions | Scala Versions |
| :------------------------- | :------------- | :------------- |
| 3.17                       | 3.5, 3.4       | 2.13, 2.12     |
| 3.16                       | 3.5, 3.4       | 2.13, 2.12     |
| 3.15                       | 3.5, 3.4       | 2.13, 2.12     |
| 3.14                       | 3.5, 3.4       | 2.13, 2.12     |

### Languages and runtimes

ScalarDB Analytics provides a library for running federated queries on Spark. It also provides a tool called ScalarDB Analytics CLI, which runs on the Java Virtual Machine (JVM).

The library is available on the Maven Central Repository. You need to specify the library when setting up Spark. For more details, see [Set up ScalarDB Analytics in the Spark configuration](./scalardb-analytics/run-analytical-queries.md#set-up-scalardb-analytics-in-the-spark-configuration).

:::note

Since Spark and Scala may be incompatible among different minor versions, the library offers different artifacts for various Spark and Scala versions, named in the format `scalardb-analytics-spark-all-<SPARK_VERSION>_<SCALA_VERSION>`. Make sure that you select the artifact matching the Spark and Scala versions you're using. For example, if you're using Spark 3.5 with Scala 2.13, you must specify `scalardb-analytics-spark-all-3.5_2.13`.

:::

#### Java

For using the library on Spark, the following JREs are verified and supported:

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, or 17 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, or 17 (LTS versions)

:::note

The Java runtime versions available for Spark on each cloud service are based on those supported by Apache Spark. For reference, the following shows the Spark service versions and corresponding Java runtime versions on major cloud services:

- **Amazon EMR:** EMR 7.x: Spark 3.5 (Java 17); EMR 6.x: Spark 3.4 (Java 8)
- **Azure Synapse Analytics:** Spark 3.5 (Java 17); Spark 3.4 (Java 11)
- **Databricks:** Runtime 16.4 LTS: Spark 3.5 (Java 17); Runtime 15.4 LTS: Spark 3.5 (Java 8); Runtime 14.3 LTS: Spark 3.5 (Java 8); Runtime 13.3 LTS: Spark 3.4 (Java 8)

For detailed information, please refer to the documentation for the cloud service you are using.

:::

For running ScalarDB Analytics CLI, the following JREs are verified and supported:

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, 17, or 21 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, 17, or 21 (LTS versions)

### Databases

ScalarDB Analytics runs on top of the following databases and their versions.

#### ScalarDB

ScalarDB Analytics can run analytical queries on the databases managed by ScalarDB Core and Cluster. It uses the ScalarDB Core library of the same version to interact with these databases, as shown below.

| ScalarDB Analytics version | ScalarDB Core version |
| :------------------------- | :-------------------- |
| 3.17                       | 3.17                  |
| 3.16                       | 3.16                  |
| 3.15                       | 3.15                  |
| 3.14                       | 3.14                  |

For the supported databases and their versions, see [Databases](#databases).

#### Relational databases

ScalarDB Analytics can run analytical queries on the following relational databases **not** managed by ScalarDB Core and Cluster.

**Oracle Database**

|      Version                | Oracle Database 23ai | Oracle Database 21c | Oracle Database 19c |
| :-------------------------- | :------------------- | :------------------ | :------------------ |
| **ScalarDB Analytics 3.17** | ✅                   | ✅                  | ✅                  |
| **ScalarDB Analytics 3.16** | ✅                   | ❌                  | ❌                  |
| **ScalarDB Analytics 3.15** | ✅                   | ❌                  | ❌                  |
| **ScalarDB Analytics 3.14** | ✅                   | ❌                  | ❌                  |

**MySQL**

|           Version           | MySQL 8.4 | MySQL 8.0 |
| :-------------------------- | :-------- | :-------- |
| **ScalarDB Analytics 3.17** | ✅        | ✅        |
| **ScalarDB Analytics 3.16** | ❌        | ✅        |
| **ScalarDB Analytics 3.15** | ❌        | ✅        |
| **ScalarDB Analytics 3.14** | ❌        | ✅        |

**PostgreSQL**

|           Version           | PostgreSQL 18 | PostgreSQL 17 | PostgreSQL 16 |
| :-------------------------- | :------------ | :------------ | :------------ |
| **ScalarDB Analytics 3.17** | ✅            | ✅            | ✅            |
| **ScalarDB Analytics 3.16** | ❌            | ❌            | ✅            |
| **ScalarDB Analytics 3.15** | ❌            | ❌            | ✅            |
| **ScalarDB Analytics 3.14** | ❌            | ❌            | ✅            |

**SQL Server**

|           Version           | SQL Server 2022 | SQL Server 2019 | SQL Server 2017 |
| :-------------------------- | :-------------- | :-------------- | :-------------- |
| **ScalarDB Analytics 3.17** | ✅              | ✅              | ✅              |
| **ScalarDB Analytics 3.16** | ❌              | ✅              | ❌              |
| **ScalarDB Analytics 3.15** | ❌              | ✅              | ❌              |
| **ScalarDB Analytics 3.14** | ❌              | ✅              | ❌              |

#### NoSQL databases

ScalarDB Analytics can run analytical queries on the following NoSQL databases **not** managed by ScalarDB Core and Cluster.

**Amazon DynamoDB**

|           Version           | DynamoDB |
| :-------------------------- | :------- |
| **ScalarDB Analytics 3.17** | ✅        |
| **ScalarDB Analytics 3.16** | ✅        |
| **ScalarDB Analytics 3.15** | ✅        |
| **ScalarDB Analytics 3.14** | ✅        |

#### Analytical platforms

ScalarDB Analytics can run analytical queries on the following analytical platforms **not** managed by ScalarDB Core and Cluster.

**Databricks**

|           Version           | Databricks |
| :-------------------------- | :--------- |
| **ScalarDB Analytics 3.17** | ✅         |
| **ScalarDB Analytics 3.16** | ✅         |
| **ScalarDB Analytics 3.15** | ❌         |
| **ScalarDB Analytics 3.14** | ❌         |

:::note

ScalarDB Analytics supports running queries on Databricks by using both SQL warehouses and compute. For compute, all default compute policies are supported.

:::

**Snowflake**

|           Version           | Snowflake |
| :-------------------------- | :-------- |
| **ScalarDB Analytics 3.17** | ✅        |
| **ScalarDB Analytics 3.16** | ✅        |
| **ScalarDB Analytics 3.15** | ❌        |
| **ScalarDB Analytics 3.14** | ❌        |

#### ScalarDB Analytics server database

The ScalarDB Analytics server manages catalog information in its database using ScalarDB Core. You can use any database supported by ScalarDB Core for this purpose. For the supported databases and their versions, see [Databases](#databases).

### Database permission requirements

ScalarDB Analytics requires read permissions to perform its operations on the underlying databases.

For databases managed under ScalarDB Core and Cluster, the databases are already configured according to [Database permission requirements](#database-permission-requirements), so no additional configuration is required.

For databases **not** managed under ScalarDB Core and Cluster, make sure you register your data sources with users who have read permission on the data sources. For instructions on registering your data sources, see [Create your catalog](./scalardb-analytics/create-scalardb-analytics-catalog.md#create-your-catalog).

Since ScalarDB Analytics server uses ScalarDB Core to manage catalog information, you need to configure a database user for ScalarDB Analytics server according to the [Database permission requirements](#database-permission-requirements) documentation for ScalarDB Core.

### Required ports

ScalarDB Analytics requires the following ports to be accessible. These default port numbers can be configured as needed:

- 11051 (catalog service)
- 11052 (metering service)
- The port number that Apache Spark uses depends on how you deploy the Spark cluster. For details on which ports you need to make accessible, please refer to your Spark service provider's documentation.

### Kubernetes

The server component of ScalarDB Analytics (ScalarDB Analytics server) is provided as a Pod on the Kubernetes platform in production environments. ScalarDB Analytics supports the following platforms and tools.

#### Platform

- **[Kubernetes](https://kubernetes.io/):** 1.32 - 1.35
  - **[Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)**
  - **[Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/products/kubernetes-service)**
- **[Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift):** TBD

#### Package manager

- **[Helm](https://helm.sh/):** 3.5+
