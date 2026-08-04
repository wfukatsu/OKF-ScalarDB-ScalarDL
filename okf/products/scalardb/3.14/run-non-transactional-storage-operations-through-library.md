---
type: Development Guide
title: Run Non-Transactional Storage Operations Through the Core Library
description: This guide explains how to run non-transactional storage operations through the ScalarDB Core library.
resource: https://scalardb.scalar-labs.com/docs/3.14/run-non-transactional-storage-operations-through-library/
tags:
- scalardb
- v3.14
- phase:implement
- section:develop
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: run-non-transactional-storage-operations-through-library
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Non-Transactional Storage Operations
- Run Through the CRUD Interface
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/run-non-transactional-storage-operations-through-library.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Run Non-Transactional Storage Operations Through the Core Library

This guide explains how to run non-transactional storage operations through the ScalarDB Core library.

## Preparation

For the purpose of this guide, you will set up a database and ScalarDB by using a sample in the ScalarDB samples repository.

### Clone the ScalarDB samples repository

Open **Terminal**, then clone the ScalarDB samples repository by running the following command:

```console
git clone https://github.com/scalar-labs/scalardb-samples
```

Then, go to the directory that contains the necessary files by running the following command:

```console
cd scalardb-samples/scalardb-sample
```

## Set up a database

Select your database, and follow the instructions to configure it for ScalarDB.

For a list of databases that ScalarDB supports, see [Databases](./requirements.md#databases).

**MySQL**

### Run MySQL locally

You can run MySQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start MySQL, run the following command:

```console
docker compose up -d mysql
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations for ScalarDB. Please uncomment the properties for MySQL in the **database.properties** file so that the configuration looks as follows:

```properties
# For MySQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://localhost:3306/
scalar.db.username=root
scalar.db.password=mysql
```

**PostgreSQL**

### Run PostgreSQL locally

You can run PostgreSQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start PostgreSQL, run the following command:

```console
docker compose up -d postgres
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations for ScalarDB. Please uncomment the properties for PostgreSQL in the **database.properties** file so that the configuration looks as follows:

```properties
# For PostgreSQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://localhost:5432/
scalar.db.username=postgres
scalar.db.password=postgres
```

**Oracle Database**

### Run Oracle Database locally

You can run Oracle Database in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start Oracle Database, run the following command:

```console
docker compose up -d oracle
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations for ScalarDB. Please uncomment the properties for Oracle Database in the **database.properties** file so that the configuration looks as follows:

```properties
# For Oracle
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:oracle:thin:@//localhost:1521/FREEPDB1
scalar.db.username=SYSTEM
scalar.db.password=Oracle
```

**SQL Server**

### Run SQL Server locally

You can run SQL Server in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start SQL Server, run the following command:

```console
docker compose up -d sqlserver
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations for ScalarDB. Please uncomment the properties for SQL Server in the **database.properties** file so that the configuration looks as follows:

```properties
# For SQL Server
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:sqlserver://localhost:1433;encrypt=true;trustServerCertificate=true
scalar.db.username=sa
scalar.db.password=SqlServer22
```

**DynamoDB**

### Run Amazon DynamoDB Local

You can run Amazon DynamoDB Local in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start Amazon DynamoDB Local, run the following command:

```console
docker compose up -d dynamodb
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations for ScalarDB. Please uncomment the properties for Amazon DynamoDB Local in the **database.properties** file so that the configuration looks as follows:

```properties
# For DynamoDB Local
scalar.db.storage=dynamo
scalar.db.contact_points=sample
scalar.db.username=sample
scalar.db.password=sample
scalar.db.dynamo.endpoint_override=http://localhost:8000
```

**Cosmos DB for NoSQL**

To use Azure Cosmos DB for NoSQL, you must have an Azure account. If you don't have an Azure account, visit [Create an Azure Cosmos DB account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal#create-account).

### Configure Cosmos DB for NoSQL

Set the **default consistency level** to **Strong** according to the official document at [Configure the default consistency level](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-manage-consistency#configure-the-default-consistency-level).

### Configure ScalarDB

The following instructions assume that you have properly installed and configured the JDK in your local environment and properly configured your Cosmos DB for NoSQL account in Azure.

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations for ScalarDB. Be sure to change the values for `scalar.db.contact_points` and `scalar.db.password` as described.

```properties
# For Cosmos DB
scalar.db.storage=cosmos
scalar.db.contact_points=<COSMOS_DB_FOR_NOSQL_URI>
scalar.db.password=<COSMOS_DB_FOR_NOSQL_KEY>
```

:::note

You can use the primary key or the secondary key in your Azure Cosmos DB account as the value for `scalar.db.password`.

:::

**Cassandra**

### Run Cassandra locally

You can run Apache Cassandra in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start Apache Cassandra, run the following command:
```console
docker compose up -d cassandra
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations for ScalarDB. Please uncomment the properties for Cassandra in the **database.properties** file so that the configuration looks as follows:

```properties
# For Cassandra
scalar.db.storage=cassandra
scalar.db.contact_points=localhost
scalar.db.username=cassandra
scalar.db.password=cassandra
```

For a comprehensive list of configurations for ScalarDB, see [ScalarDB Configurations](./configurations.md).

## Configure ScalarDB to run non-transactional storage operations

To run non-transactional storage operations, you need to configure the `scalar.db.transaction_manager` property to `single-crud-operation` in the configuration file **database.properties**:

```properties
scalar.db.transaction_manager=single-crud-operation
```

## Create or import a schema

ScalarDB has its own data model and schema that maps to the implementation-specific data model and schema.

- **Need to create a database schema?** See [ScalarDB Schema Loader](./schema-loader.md).
- **Need to import an existing database?** See [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](./schema-loader-import.md).

## Load initial data as necessary

ScalarDB Data Loader is a utility for importing and exporting data with ScalarDB.

- **Need to import data into your database?** See [Importing data](./data-loader.md#importing-data).
- **Need to export data from your database?** See [Exporting data](./data-loader.md#exporting-data).

## Create your Java application

This section describes how to add the ScalarDB Core library to your project and how to configure it to run non-transactional storage operations by using Java.

### Add ScalarDB to your project

The ScalarDB library is available on the [Maven Central Repository](https://mvnrepository.com/artifact/com.scalar-labs/scalardb). You can add the library as a build dependency to your application by using Gradle or Maven.

Select your build tool, and follow the instructions to add the build dependency for ScalarDB to your application.

**Gradle**

To add the build dependency for ScalarDB by using Gradle, add the following to `build.gradle` in your application:

```gradle
dependencies {
    implementation 'com.scalar-labs:scalardb:3.14.6'
}
```

**Maven**

To add the build dependency for ScalarDB by using Maven, add the following to `pom.xml` in your application:

```xml
<dependency>
    <groupId>com.scalar-labs</groupId>
    <artifactId>scalardb</artifactId>
    <version>3.14.6</version>
</dependency>
```

### Use the Java API

For details about the Java API, see [ScalarDB Java API Guide](./api-guide.md).

:::note

The following limitations apply to non-transactional storage operations:

- Beginning a transaction is not supported. For more details, see [Execute transactions without beginning or starting a transaction](./api-guide.md#execute-transactions-without-beginning-or-starting-a-transaction).
- Executing multiple mutations in a single transaction is not supported.

:::

### Learn more

- [Javadoc](https://javadoc.io/doc/com.scalar-labs/scalardb/3.14.6/index.html)
