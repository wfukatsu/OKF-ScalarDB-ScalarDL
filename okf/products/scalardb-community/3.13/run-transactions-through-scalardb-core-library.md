---
type: Development Guide
title: Run Transactions Through the ScalarDB Core Library
description: This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using the ScalarDB core library.
resource: https://scalardb-community.scalar-labs.com/docs/latest/run-transactions-through-scalardb-core-library/
tags:
- scalardb-community
- v3.13
- phase:implement
status: stable
product: scalardb-community
product_title: ScalarDB Community
version: '3.13'
doc_id: run-transactions-through-scalardb-core-library
lifecycle_phase: implement
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:31Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/docs/run-transactions-through-scalardb-core-library.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# Run Transactions Through the ScalarDB Core Library

This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using the ScalarDB core library.

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

You can use a primary key or a secondary key as the value for `scalar.db.password`.

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

## Create or import a schema

ScalarDB has its own data model and schema that maps to the implementation-specific data model and schema.

- **Need to create a database schema?** See [ScalarDB Schema Loader](./schema-loader.md).
- **Need to import an existing database?** See [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](./schema-loader-import.md).

## Run transactions by using Java

- **Want to run transactions by using a one-phase commit interface?** See the [ScalarDB Java API Guide](./api-guide.md#transactional-api).
- **Want to run transactions by using a two-phase commit interface?** See [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md).
