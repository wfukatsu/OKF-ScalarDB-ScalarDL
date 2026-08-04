---
type: Development Guide
title: Run Transactions Through the ScalarDB Core Library
description: This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using the ScalarDB Core library.
resource: https://scalardb.scalar-labs.com/docs/latest/run-transactions-through-scalardb-core-library/
tags:
- scalardb
- v3.19
- phase:implement
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.0
doc_id: run-transactions-through-scalardb-core-library
lifecycle_phase: implement
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:47Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/docs/run-transactions-through-scalardb-core-library.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Run Transactions Through the ScalarDB Core Library

This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using the ScalarDB Core library.

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

Follow the instructions below to configure your database for ScalarDB.

For a list of databases that ScalarDB supports, see [Databases](./requirements.md#databases).

**Relational databases**

Select your relational database.

**Db2**

### Run Db2 locally

You can run IBM Db2 in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start IBM Db2, run the following command:

```console
docker compose up -d db2
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for Db2 in the **database.properties** file so that the configuration looks as follows:

```properties
# For Db2
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:db2://localhost:50000/sample
scalar.db.username=db2inst1
scalar.db.password=db2inst1
```

**MariaDB**

### Run MariaDB locally

You can run MariaDB in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start MariaDB, run the following command:

```console
docker compose up -d mariadb
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for MariaDB in the **database.properties** file so that the configuration looks as follows:

```properties
# For MariaDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mariadb://localhost:3306
scalar.db.username=root
scalar.db.password=mariadb
```

**MySQL**

### Run MySQL locally

You can run MySQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start MySQL, run the following command:

```console
docker compose up -d mysql
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for MySQL in the **database.properties** file so that the configuration looks as follows:

```properties
# For MySQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://localhost:3306/
scalar.db.username=root
scalar.db.password=mysql
```

**Oracle Database**

### Run Oracle Database locally

You can run Oracle Database in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start Oracle Database, run the following command:

```console
docker compose up -d oracle
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for Oracle Database in the **database.properties** file so that the configuration looks as follows:

```properties
# For Oracle
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:oracle:thin:@//localhost:1521/FREEPDB1
scalar.db.username=SYSTEM
scalar.db.password=Oracle
```

**PostgreSQL**

### Run PostgreSQL locally

You can run PostgreSQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start PostgreSQL, run the following command:

```console
docker compose up -d postgres
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for PostgreSQL in the **database.properties** file so that the configuration looks as follows:

```properties
# For PostgreSQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://localhost:5432/
scalar.db.username=postgres
scalar.db.password=postgres
```

**SQL Server**

### Run SQL Server locally

You can run SQL Server in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start SQL Server, run the following command:

```console
docker compose up -d sqlserver
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for SQL Server in the **database.properties** file so that the configuration looks as follows:

```properties
# For SQL Server
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:sqlserver://localhost:1433;encrypt=true;trustServerCertificate=true
scalar.db.username=sa
scalar.db.password=SqlServer22
```

**SQLite**

### Configure ScalarDB

SQLite is an embedded, file-based database, so there is no separate server to start. ScalarDB creates the database file automatically when it is first used.

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for SQLite in the **database.properties** file so that the configuration looks as follows:

```properties
# For Sqlite
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:sqlite:scalardb-sample.sqlite3?busy_timeout=10000
scalar.db.username=
scalar.db.password=
```

**NewSQL databases**

Select your NewSQL database.

**AlloyDB**

### Run AlloyDB locally

You can run AlloyDB Omni in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start AlloyDB Omni, run the following command:

```console
docker compose up -d alloydb
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for AlloyDB in the **database.properties** file so that the configuration looks as follows:

```properties
# For AlloyDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://localhost:5432/
scalar.db.username=postgres
scalar.db.password=postgres
```

**Spanner**

### Run Spanner locally

You can run Spanner Omni in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start Spanner Omni, run the following command:

```console
docker compose up -d spanner spanner-init
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for Spanner in the **database.properties** file so that the configuration looks as follows:

```properties
# For Spanner
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:cloudspanner://localhost:15000/databases/test-db;isExperimentalHost=true;usePlainText=true
scalar.db.username=
scalar.db.password=
```

**TiDB**

### Run TiDB locally

You can run TiDB locally by using the TiUP tool. For installation instructions, see [Install TiUP](https://docs.pingcap.com/tidb/stable/tiup-overview/#install-tiup).

To start TiDB, run the following command:

```console
tiup playground v8.5 --without-monitor
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for TiDB in the **database.properties** file so that the configuration looks as follows:

```properties
# For TiDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://localhost:4000/
scalar.db.username=root
scalar.db.password=
```

**YugabyteDB**

### Run YugabyteDB locally

You can run YugabyteDB in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start YugabyteDB, run the following command:

```console
docker compose up -d yugabyte
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for YugabyteDB in the **database.properties** file so that the configuration looks as follows:

```properties
# For Yugabyte
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:yugabytedb://localhost:5433/postgres
scalar.db.username=yugabyte
scalar.db.password=yugabyte
```

**NoSQL databases**

Select your NoSQL database.

**Cassandra**

### Run Cassandra locally

You can run Apache Cassandra in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start Apache Cassandra, run the following command:

```console
docker compose up -d cassandra
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for Cassandra in the **database.properties** file so that the configuration looks as follows:

```properties
# For Cassandra
scalar.db.storage=cassandra
scalar.db.contact_points=localhost
scalar.db.username=cassandra
scalar.db.password=cassandra
```

**Cosmos DB for NoSQL**

To use Azure Cosmos DB for NoSQL, you must have an Azure account. If you don't have an Azure account, visit [Create an Azure Cosmos DB account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal#create-account).

### Configure Cosmos DB for NoSQL

Set the **default consistency level** to **Strong** according to the official document at [Configure the default consistency level](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-manage-consistency#configure-the-default-consistency-level).

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Be sure to change the values for `scalar.db.contact_points` and `scalar.db.password` as described.

```properties
# For Cosmos DB
scalar.db.storage=cosmos
scalar.db.contact_points=<COSMOS_DB_FOR_NOSQL_URI>
scalar.db.password=<COSMOS_DB_FOR_NOSQL_KEY>
```

You can use the primary key or the secondary key in your Azure Cosmos DB account as the value for `scalar.db.password`.

**DynamoDB**

### Run Amazon DynamoDB Local

You can run Amazon DynamoDB Local in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-sample` directory.

To start Amazon DynamoDB Local, run the following command:

```console
docker compose up -d dynamodb
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-sample` directory contains database configurations. Please uncomment the properties for Amazon DynamoDB Local in the **database.properties** file so that the configuration looks as follows:

```properties
# For DynamoDB Local
scalar.db.storage=dynamo
scalar.db.contact_points=sample
scalar.db.username=sample
scalar.db.password=sample
scalar.db.dynamo.endpoint_override=http://localhost:8000
```

For a comprehensive list of configurations for ScalarDB, see [ScalarDB Configurations](./configurations.md).

## Create or import a schema

ScalarDB has its own data model and schema that maps to the implementation-specific data model and schema.

- **Need to create a database schema?** See [ScalarDB Schema Loader](./schema-loader.md).
- **Need to import an existing database?** See [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](./schema-loader-import.md).

## Load initial data as necessary

ScalarDB Data Loader is a utility for importing and exporting data with ScalarDB.

- **Need to import data into your database?** See [Importing data](./data-loader.md#importing-data).
- **Need to export data from your database?** See [Exporting data](./data-loader.md#exporting-data).

## Run transactions by using Java

- **Want to run transactions by using a one-phase commit interface?** See the [ScalarDB Java API Guide](./api-guide.md#transactional-api).
- **Want to run transactions by using a two-phase commit interface?** See [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md).
