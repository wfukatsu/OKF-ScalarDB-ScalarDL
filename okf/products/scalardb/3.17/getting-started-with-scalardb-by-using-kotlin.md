---
type: Tutorial
title: Getting Started with ScalarDB by Using Kotlin
description: This getting started tutorial explains how to configure your preferred database in ScalarDB and set up a basic electronic money application by using Kotlin. Since Kotlin has Java interoperability, you can use ScalarDB directly from Kotlin.
resource: https://scalardb.scalar-labs.com/docs/3.17/getting-started-with-scalardb-by-using-kotlin/
tags:
- scalardb
- v3.17
- phase:implement
- section:quickstart
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.3
doc_id: getting-started-with-scalardb-by-using-kotlin
lifecycle_phase: implement
breadcrumb:
- Quickstart
- Try Using the ScalarDB Core Library to Run Transactions
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:26Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.17/getting-started-with-scalardb-by-using-kotlin.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Getting Started with ScalarDB by Using Kotlin

This getting started tutorial explains how to configure your preferred database in ScalarDB and set up a basic electronic money application by using Kotlin. Since Kotlin has Java interoperability, you can use ScalarDB directly from Kotlin.

:::warning

The electronic money application is simplified for this tutorial and isn't suitable for a production environment.

:::

## Prerequisites for this sample application

- One of the following Java Development Kits (JDKs):

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, 17, or 21 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, 17, or 21 (LTS versions)

- [Docker](https://www.docker.com/get-started/) 20.10 or later with [Docker Compose](https://docs.docker.com/compose/install/) V2 or later

## Clone the ScalarDB samples repository

Open **Terminal**, then clone the ScalarDB samples repository by running the following command:

```console
git clone https://github.com/scalar-labs/scalardb-samples
```

Then, go to the directory that contains the sample application by running the following command:

```console
cd scalardb-samples/scalardb-kotlin-sample
```

## Set up your database for ScalarDB

Follow the instructions below to configure your database for ScalarDB.

For a list of databases that ScalarDB supports, see [Databases](./requirements.md#databases).

**Relational databases**

Select your relational database.

**Db2**

### Run Db2 locally

You can run IBM Db2 in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start IBM Db2, run the following command:

```console
docker compose up -d db2
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for Db2 in the **database.properties** file so that the configuration looks as follows:

```properties
# For Db2
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:db2://localhost:50000/sample
scalar.db.username=db2inst1
scalar.db.password=db2inst1
```

**MariaDB**

### Run MariaDB locally

You can run MariaDB in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start MariaDB, run the following command:

```console
docker compose up -d mariadb
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for MariaDB in the **database.properties** file so that the configuration looks as follows:

```properties
# For MariaDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mariadb://localhost:3306
scalar.db.username=root
scalar.db.password=mariadb
```

**MySQL**

### Run MySQL locally

You can run MySQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start MySQL, run the following command:

```console
docker compose up -d mysql
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for MySQL in the **database.properties** file so that the configuration looks as follows:

```properties
# For MySQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://localhost:3306/
scalar.db.username=root
scalar.db.password=mysql
```

**Oracle Database**

### Run Oracle Database locally

You can run Oracle Database in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start Oracle Database, run the following command:

```console
docker compose up -d oracle
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for Oracle Database in the **database.properties** file so that the configuration looks as follows:

```properties
# For Oracle
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:oracle:thin:@//localhost:1521/FREEPDB1
scalar.db.username=SYSTEM
scalar.db.password=Oracle
```

**PostgreSQL**

### Run PostgreSQL locally

You can run PostgreSQL in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start PostgreSQL, run the following command:

```console
docker compose up -d postgres
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for PostgreSQL in the **database.properties** file so that the configuration looks as follows:

```properties
# For PostgreSQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://localhost:5432/
scalar.db.username=postgres
scalar.db.password=postgres
```

**SQL Server**

### Run SQL Server locally

You can run SQL Server in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start SQL Server, run the following command:

```console
docker compose up -d sqlserver
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for SQL Server in the **database.properties** file so that the configuration looks as follows:

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

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for SQLite in the **database.properties** file so that the configuration looks as follows:

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

You can run AlloyDB Omni in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start AlloyDB Omni, run the following command:

```console
docker compose up -d alloydb
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for AlloyDB in the **database.properties** file so that the configuration looks as follows:

```properties
# For AlloyDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://localhost:5432/
scalar.db.username=postgres
scalar.db.password=postgres
```

**TiDB**

### Run TiDB locally

You can run TiDB locally by using the TiUP tool. For installation instructions, see [Install TiUP](https://docs.pingcap.com/tidb/stable/tiup-overview/#install-tiup).

To start TiDB, run the following command:

```console
tiup playground v8.5 --without-monitor
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for TiDB in the **database.properties** file so that the configuration looks as follows:

```properties
# For TiDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://localhost:4000/
scalar.db.username=root
scalar.db.password=
```

**YugabyteDB**

### Run YugabyteDB locally

You can run YugabyteDB in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start YugabyteDB, run the following command:

```console
docker compose up -d yugabyte
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for YugabyteDB in the **database.properties** file so that the configuration looks as follows:

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

You can run Apache Cassandra in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start Apache Cassandra, run the following command:

```console
docker compose up -d cassandra
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for Cassandra in the **database.properties** file so that the configuration looks as follows:

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

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Be sure to change the values for `scalar.db.contact_points` and `scalar.db.password` as described.

```properties
# For Cosmos DB
scalar.db.storage=cosmos
scalar.db.contact_points=<COSMOS_DB_FOR_NOSQL_URI>
scalar.db.password=<COSMOS_DB_FOR_NOSQL_KEY>
```

You can use the primary key or the secondary key in your Azure Cosmos DB account as the value for `scalar.db.password`.

**DynamoDB**

### Run Amazon DynamoDB Local

You can run Amazon DynamoDB Local in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-kotlin-sample` directory.

To start Amazon DynamoDB Local, run the following command:

```console
docker compose up -d dynamodb
```

### Configure ScalarDB

The **database.properties** file in the `scalardb-samples/scalardb-kotlin-sample` directory contains database configurations. Please uncomment the properties for Amazon DynamoDB Local in the **database.properties** file so that the configuration looks as follows:

```properties
# For DynamoDB Local
scalar.db.storage=dynamo
scalar.db.contact_points=sample
scalar.db.username=sample
scalar.db.password=sample
scalar.db.dynamo.endpoint_override=http://localhost:8000
```

## Load the database schema

You need to define the database schema (the method in which the data will be organized) in the application. For details about the supported data types, see [Database Adapters](./database-adapters.md).

For this tutorial, a file named **schema.json** already exists in the `scalardb-samples/scalardb-kotlin-sample` directory. To apply the schema, go to the [`scalardb` Releases](https://github.com/scalar-labs/scalardb/releases) page and download the ScalarDB Schema Loader that matches the version of ScalarDB that you are using to the `scalardb-samples/scalardb-kotlin-sample` directory.

Then, based on your database, run the following command, replacing `<VERSION>` with the version of the ScalarDB Schema Loader that you downloaded:

**Relational databases**

Select your relational database.

**Db2**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**MariaDB**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**MySQL**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**Oracle Database**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**PostgreSQL**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**SQL Server**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**SQLite**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**NewSQL databases**

Select your NewSQL database.

**AlloyDB**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**TiDB**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**YugabyteDB**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**NoSQL databases**

Select your NoSQL database.

**Cassandra**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator --replication-factor=1
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

In addition, the `--replication-factor=1` option has an effect only when using Cassandra. The default replication factor is `3`, but to facilitate the setup in this tutorial, `1` is used so that you only need to prepare a cluster with one node instead of three nodes. However, keep in mind that a replication factor of `1` is not suited for production.

**Cosmos DB for NoSQL**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

**DynamoDB**

```console
java -jar scalardb-schema-loader-<VERSION>.jar --config database.properties --schema-file schema.json --coordinator --no-backup --no-scaling
```

  The `--coordinator` option is specified because a table with `transaction` set to `true` exists in the schema. For details about configuring and loading a schema, see [ScalarDB Schema Loader](./schema-loader.md).

Also, `--no-backup` and `--no-scaling` options are specified because Amazon DynamoDB Local does not support continuous backup and auto-scaling.

## Execute transactions and retrieve data in the basic electronic money application

After loading the schema, you can execute transactions and retrieve data in the basic electronic money application that is included in the repository that you cloned.

The application supports the following types of transactions:

- Create an account.
- Add funds to an account.
- Send funds between two accounts.
- Get an account balance.

:::note

When you first execute a Gradle command, Gradle will automatically install the necessary libraries.

:::

### Create an account with a balance

You need an account with a balance so that you can send funds between accounts.

To create an account for **customer1** that has a balance of **500**, run the following command:

```console
./gradlew run --args="-action charge -amount 500 -to customer1"
```

### Create an account without a balance

After setting up an account that has a balance, you need another account for sending funds to.

To create an account for **merchant1** that has a balance of **0**, run the following command:

```console
./gradlew run --args="-action charge -amount 0 -to merchant1"
```

### Add funds to an account

You can add funds to an account in the same way that you created and added funds to an account in [Create an account with a balance](#create-an-account-with-a-balance).

To add **500** to the account for **customer1**, run the following command:

```console
./gradlew run --args="-action charge -amount 500 -to customer1"
```

The account for **customer1** will now have a balance of **1000**.

### Send electronic money between two accounts

Now that you have created two accounts, with at least one of those accounts having a balance, you can send funds from one account to the other account.

To have **customer1** pay **100** to **merchant1**, run the following command:

```console
./gradlew run --args="-action pay -amount 100 -from customer1 -to merchant1"
```

### Get an account balance

After sending funds from one account to the other, you can check the balance of each account.

To get the balance of **customer1**, run the following command:

```console
./gradlew run --args="-action getBalance -id customer1"
```

You should see the following output:

```console
...
The balance for customer1 is 900
...
```

To get the balance of **merchant1**, run the following command:

```console
./gradlew run --args="-action getBalance -id merchant1"
```

You should see the following output:

```console
...
The balance for merchant1 is 100
...
```

## Stop the database

To stop the database, stop the Docker container by running the following command:

```console
docker compose down
```

## Reference

To see the source code for the electronic money application used in this tutorial, see [`ElectronicMoney.kt`](https://github.com/scalar-labs/scalardb-samples/blob/main/scalardb-kotlin-sample/src/main/kotlin/sample/ElectronicMoney.kt).
