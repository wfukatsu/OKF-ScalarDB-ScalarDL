---
type: Development Guide
title: Run Non-Transactional Storage Operations Through the SQL Interface
description: This guide explains how to run non-transactional storage operations through the SQL interface for ScalarDB Cluster.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalardb-cluster/run-non-transactional-storage-operations-through-sql-interface/
tags:
- scalardb
- v3.16
- phase:implement
- section:develop
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.6
doc_id: scalardb-cluster/run-non-transactional-storage-operations-through-sql-interface
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Advanced Configurations and Operations
- Run Single-Operation Transactions
editions:
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:54Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.16/scalardb-cluster/run-non-transactional-storage-operations-through-sql-interface.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Run Non-Transactional Storage Operations Through the SQL Interface

This guide explains how to run non-transactional storage operations through the SQL interface for ScalarDB Cluster.

:::warning

You need to have a license key (trial license or commercial license) for ScalarDB Cluster. If you don't have a license key, please [contact us](https://www.scalar-labs.com/contact).

:::

## Preparation

For the purpose of this guide, you will set up a database and ScalarDB Cluster in standalone mode by using a sample in the ScalarDB samples repository.

:::note

ScalarDB Cluster in standalone mode is primarily for development and testing purposes.

:::

### Clone the ScalarDB samples repository

Open **Terminal**, then clone the ScalarDB samples repository by running the following command:

```console
git clone https://github.com/scalar-labs/scalardb-samples
```

Then, go to the directory that contains the necessary files by running the following command:

```console
cd scalardb-samples/scalardb-cluster-standalone-mode
```

## Set up a database

Follow the instructions below to configure your database for ScalarDB Cluster.

For a list of databases that ScalarDB supports, see [Databases](../requirements.md#databases).

**Relational databases**

Select your relational database.

**Db2**

### Run Db2 locally

You can run IBM Db2 in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start IBM Db2, run the following command:

```console
docker compose up -d db2
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for Db2 in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For Db2
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:db2://db2-1:50000/sample
scalar.db.username=db2inst1
scalar.db.password=db2inst1
```

**MariaDB**

### Run MariaDB locally

You can run MariaDB in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start MariaDB, run the following command:

```console
docker compose up -d mariadb
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for MariaDB in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For MariaDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mariadb://mariadb-1:3306
scalar.db.username=root
scalar.db.password=mariadb
```

**MySQL**

### Run MySQL locally

You can run MySQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start MySQL, run the following command:

```console
docker compose up -d mysql
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for MySQL in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For MySQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://mysql-1:3306/
scalar.db.username=root
scalar.db.password=mysql
```

**Oracle Database**

### Run Oracle Database locally

You can run Oracle Database in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start Oracle Database, run the following command:

```console
docker compose up -d oracle
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for Oracle Database in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For Oracle
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:oracle:thin:@//oracle-1:1521/FREEPDB1
scalar.db.username=SYSTEM
scalar.db.password=Oracle
```

**PostgreSQL**

### Run PostgreSQL locally

You can run PostgreSQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start PostgreSQL, run the following command:

```console
docker compose up -d postgres
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for PostgreSQL in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For PostgreSQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://postgres-1:5432/
scalar.db.username=postgres
scalar.db.password=postgres
```

**SQL Server**

### Run SQL Server locally

You can run SQL Server in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start SQL Server, run the following command:

```console
docker compose up -d sqlserver
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for SQL Server in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For SQL Server
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:sqlserver://sqlserver-1:1433;encrypt=true;trustServerCertificate=true
scalar.db.username=sa
scalar.db.password=SqlServer22
```

**NewSQL databases**

Select your NewSQL database.

**YugabyteDB**

### Run YugabyteDB locally

You can run YugabyteDB in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start YugabyteDB, run the following command:

```console
docker compose up -d yugabyte
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for YugabyteDB in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For Yugabyte
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:yugabytedb://yugabyte-1:5433/postgres
scalar.db.username=yugabyte
scalar.db.password=yugabyte
```

**NoSQL databases**

Select your NoSQL database.

**Cassandra**

### Run Cassandra locally

You can run Apache Cassandra in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start Apache Cassandra, run the following command:

```console
docker compose up -d cassandra
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for Cassandra in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For Cassandra
scalar.db.storage=cassandra
scalar.db.contact_points=cassandra-1
scalar.db.username=cassandra
scalar.db.password=cassandra
```

**Cosmos DB for NoSQL**

To use Azure Cosmos DB for NoSQL, you must have an Azure account. If you don't have an Azure account, visit [Create an Azure Cosmos DB account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal#create-account).

### Configure Cosmos DB for NoSQL

Set the **default consistency level** to **Strong** according to the official document at [Configure the default consistency level](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-manage-consistency#configure-the-default-consistency-level).

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Be sure to change the values for `scalar.db.contact_points` and `scalar.db.password` as described.

```properties
# For Cosmos DB
scalar.db.storage=cosmos
scalar.db.contact_points=<COSMOS_DB_FOR_NOSQL_URI>
scalar.db.password=<COSMOS_DB_FOR_NOSQL_KEY>
```

You can use the primary key or the secondary key in your Azure Cosmos DB account as the value for `scalar.db.password`.

**DynamoDB**

### Run Amazon DynamoDB Local

You can run Amazon DynamoDB Local in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start Amazon DynamoDB Local, run the following command:

```console
docker compose up -d dynamodb
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for Amazon DynamoDB Local in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For DynamoDB Local
scalar.db.storage=dynamo
scalar.db.contact_points=sample
scalar.db.username=sample
scalar.db.password=sample
scalar.db.dynamo.endpoint_override=http://dynamodb-1:8000
```

For a comprehensive list of configurations for ScalarDB, see [ScalarDB Configurations](../configurations.md).

## Set up ScalarDB Cluster in standalone mode

To set up ScalarDB Cluster in standalone mode, you'll need to configure ScalarDB Cluster to run non-transactional storage operations, set a license key, and then start ScalarDB Cluster.

### Configure ScalarDB Cluster to run non-transactional storage operations

To run non-transactional storage operations, you need to configure the `scalar.db.transaction_manager` property to `single-crud-operation` in the configuration file `scalardb-cluster-node.properties`:

```properties
scalar.db.transaction_manager=single-crud-operation
```

### Set the license key

Set the license key (trial license or commercial license) for the ScalarDB Clusters in the properties file. For details, see [How to Configure a Product License Key](../scalar-licensing/section-home.md).

### Start ScalarDB Cluster in standalone mode

To start ScalarDB Cluster in standalone mode, run the following command:

:::note

If you want to change other configurations for ScalarDB Cluster, update the `scalardb-cluster-node.properties` file before running the command below.

:::

```console
docker compose up -d scalardb-cluster-node
```

## Create or import a schema

ScalarDB has its own data model and schema that maps to the implementation-specific data model and schema.

- **Need to create a database schema?** See [SQL CLI](./developer-guide-for-scalardb-cluster-with-java-api.md#sql-cli).
- **Need to import an existing database?** See [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](../schema-loader-import.md).

Also, for a list of supported DDLs, see [ScalarDB SQL Grammar](../scalardb-sql/grammar.md).

## Load initial data as necessary

ScalarDB Data Loader is a utility for importing and exporting data with ScalarDB.

:::note

Data Loader is currently built upon ScalarDB Core, so it can only import and export data directly to and from the backend databases. Therefore, it cannot import and export data through ScalarDB Cluster.

:::

- **Need to import data into your database?** See [Importing data](../data-loader.md#importing-data).
- **Need to export data from your database?** See [Exporting data](../data-loader.md#exporting-data).

## Create your application

**JDBC**

### Configure your JDBC application

This section describes how to add the ScalarDB JDBC driver to your project and how to configure it to run non-transactional storage operations by using Java.

### Add the ScalarDB JDBC driver to your project

You can add the ScalarDB JDBC driver as a build dependency to your application by using Gradle or Maven.

Select your build tool, and follow the instructions to add the build dependency for the ScalarDB JDBC driver to your application.

**Gradle**

To add the build dependency for the ScalarDB JDBC driver by using Gradle, add the following to `build.gradle` in your application:

```gradle
dependencies {
    implementation 'com.scalar-labs:scalardb-sql-jdbc:3.16.6'
    implementation 'com.scalar-labs:scalardb-cluster-java-client-sdk:3.16.6'
}
```

**Maven**

To add the build dependency for the ScalarDB SQL API by using Maven, add the following to `pom.xml` in your application:

```xml
<dependencies>
    <dependency>
        <groupId>com.scalar-labs</groupId>
        <artifactId>scalardb-sql-jdbc</artifactId>
        <version>3.16.6</version>
    </dependency>
    <dependency>
        <groupId>com.scalar-labs</groupId>
        <artifactId>scalardb-cluster-java-client-sdk</artifactId>
        <version>3.16.6</version>
    </dependency>
</dependencies>
```

### Configure the ScalarDB Cluster Java SDK for the SQL interface

For details about configuring the ScalarDB Cluster Java SDK for the SQL interface, see [ScalarDB Cluster SQL client configurations](./developer-guide-for-scalardb-cluster-with-java-api.md#scalardb-cluster-sql-client-configurations).

### Use the JDBC API

For details about the JDBC API, see [ScalarDB JDBC Guide](../scalardb-sql/jdbc-guide.md).

:::note

The following limitations apply to non-transactional storage operations:

- Beginning a transaction is not supported.
- Executing multiple mutations in a single SQL statement is not supported.
- The isolation level is always `READ_COMMITTED`.

:::

### Learn more

- [Developer Guide for ScalarDB Cluster with the Java API](./developer-guide-for-scalardb-cluster-with-java-api.md)
- [Java JDBC API](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/)

**Java**

### Configure your Java application

This section describes how to add the ScalarDB SQL API to your project and how to configure it to run non-transactional storage operations by using Java.

### Add ScalarDB SQL API to your project

You can add the ScalarDB SQL API as a build dependency to your application by using Gradle or Maven.

Select your build tool, and follow the instructions to add the build dependency for the ScalarDB SQL API to your application.

**Gradle**

To add the build dependency for the ScalarDB SQL API by using Gradle, add the following to `build.gradle` in your application:

```gradle
dependencies {
    implementation 'com.scalar-labs:scalardb-sql:3.16.6'
    implementation 'com.scalar-labs:scalardb-cluster-java-client-sdk:3.16.6'
}
```

**Maven**

To add the build dependency for the ScalarDB SQL API by using Maven, add the following to `pom.xml` in your application:

```xml
<dependencies>
    <dependency>
        <groupId>com.scalar-labs</groupId>
        <artifactId>scalardb-sql</artifactId>
        <version>3.16.6</version>
    </dependency>
    <dependency>
        <groupId>com.scalar-labs</groupId>
        <artifactId>scalardb-cluster-java-client-sdk</artifactId>
        <version>3.16.6</version>
    </dependency>
</dependencies>
```

### Configure the ScalarDB Cluster Java SDK for the SQL interface

For details about configuring the ScalarDB Cluster Java SDK for the SQL interface, see [ScalarDB Cluster SQL client configurations](./developer-guide-for-scalardb-cluster-with-java-api.md#scalardb-cluster-sql-client-configurations).

### Use the Java API

For details about the SQL API, see [ScalarDB SQL API Guide](../scalardb-sql/sql-api-guide.md).

:::note

The following limitations apply to non-transactional storage operations:

- Beginning a transaction is not supported.
- Executing multiple mutations in a single SQL statement is not supported.
- The isolation level is always `READ_COMMITTED`.

:::

### Learn more

- [Javadoc](https://javadoc.io/doc/com.scalar-labs/scalardb-sql/3.16.6/index.html)
