---
type: Development Guide
title: Run Transactions Through ScalarDB Cluster
description: This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using ScalarDB Cluster.
resource: https://scalardb.scalar-labs.com/docs/3.17/scalardb-cluster/run-transactions-through-scalardb-cluster/
tags:
- scalardb
- v3.17
- phase:implement
- section:develop
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.4
doc_id: scalardb-cluster/run-transactions-through-scalardb-cluster
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Run Through the CRUD Interface
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:52Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.17/scalardb-cluster/run-transactions-through-scalardb-cluster.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Run Transactions Through ScalarDB Cluster

This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using ScalarDB Cluster.

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

**AlloyDB**

### Run AlloyDB locally

You can run AlloyDB Omni in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start AlloyDB Omni, run the following command:

```console
docker compose up -d alloydb
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for AlloyDB in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For AlloyDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://alloydb-1:5432/
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

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for TiDB in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For TiDB
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://host.docker.internal:4000/
scalar.db.username=root
scalar.db.password=
```

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

**Object storage**

Select your object storage.

**Blob Storage**

### Run Azurite

You can run Azurite, which is a local emulator for Blob Storage, in Docker Compose by using the `docker-compose.yml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start Blob Storage, run the following command:

```console
docker compose up -d blobstorage
```

Then, create a container named `test-container` by running the following command:

```console
docker compose up blobstorage-container-creator
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Please uncomment the properties for Blob Storage in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For Blob Storage
scalar.db.storage=blob-storage
scalar.db.contact_points=http://blobstorage-1:10000/test/test-container
scalar.db.username=test
scalar.db.password=test
```

**Cloud Storage**

To use Google Cloud Storage, you must have a Google Cloud account. If you don't have a Google Cloud account, visit [Get started with Google Cloud](https://cloud.google.com/docs/get-started).

### Configure Cloud Storage

Create a Cloud Storage bucket. For instructions on creating a bucket, see [Create buckets](https://cloud.google.com/storage/docs/creating-buckets). You also need a service account key for authentication. For details, see [Create a service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating).

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Be sure to change the values for `scalar.db.contact_points`, `scalar.db.username`, and `scalar.db.password` as described.

```properties
# For Cloud Storage
scalar.db.storage=cloud-storage
scalar.db.contact_points=<CLOUD_STORAGE_BUCKET_NAME>
scalar.db.username=<GCP_PROJECT_ID>
scalar.db.password=<GCP_SERVICE_ACCOUNT_KEY_JSON>
```

Set `scalar.db.password` to the full content of your Google Cloud service account key file as a single-line JSON.

**S3**

To use Amazon S3, you must have an AWS account. If you don't have an AWS account, visit [Create an AWS account](https://aws.amazon.com/free/).

### Configure Amazon S3

Create an S3 bucket. For instructions on creating a bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). You also need an access key for authentication. For details, see [Creating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations. Be sure to change the values for `scalar.db.contact_points`, `scalar.db.username`, and `scalar.db.password` as described.

```properties
# For S3
scalar.db.storage=s3
scalar.db.contact_points=<REGION>/<S3_BUCKET_NAME>
scalar.db.username=<AWS_ACCESS_KEY>
scalar.db.password=<AWS_SECRET_ACCESS_KEY>
```

The format of `scalar.db.contact_points` is `&lt;REGION&gt;/&lt;S3_BUCKET_NAME&gt;` (for example, `us-east-1/my-bucket`).

For a comprehensive list of configurations for ScalarDB Cluster, see [ScalarDB Cluster Configurations](./developer-guide-for-scalardb-cluster-with-java-api.md#client-configurations).

## Set up ScalarDB Cluster in standalone mode

To set up ScalarDB Cluster in standalone mode, you'll need to set a license key and then start ScalarDB Cluster.

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

- **Need to create a database schema?** See [ScalarDB Schema Loader](../schema-loader.md).
- **Need to import an existing database?** See [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](../schema-loader-import.md).

## Load initial data as necessary

ScalarDB Cluster Data Loader is a utility for importing and exporting data with ScalarDB Cluster.

- **Need to import data into your database?** See [Importing data](../data-loader.md#importing-data).
- **Need to export data from your database?** See [Exporting data](../data-loader.md#exporting-data).

## Run transactions

You can run transactions by using a one-phase or a two-phase commit interface. Select your method for running transactions.

:::note

If you are building a monolithic application, you should use the one-phase commit interface. However, if you are building a microservice application, see [ScalarDB Cluster Deployment Patterns for Microservices](./deployment-patterns-for-microservices.md) to decide which interface to use.

:::

**Java**

### One-phase commit interface

For details about how to run transactions by using a one-phase commit interface, see the [ScalarDB Java API Guide](../api-guide.md#transactional-api).

:::note

To try running transactions by using a one-phase commit interface, see the following sample tutorials:

- [Create a Sample Application That Supports Multi-Storage Transactions](../scalardb-samples/multi-storage-transaction-sample/README.md)
- [Sample application of Spring Data JDBC for ScalarDB with Multi-storage Transactions](../scalardb-samples/spring-data-multi-storage-transaction-sample/README.md)

:::

### Two-phase commit interface

For details about how to run transactions by using a two-phase commit interface, see [Transactions with a Two-Phase Commit Interface](../two-phase-commit-transactions.md).

:::note

To try running transactions by using a two-phase commit interface, see the following sample tutorials:

- [Create a Sample Application That Supports Microservice Transactions](../scalardb-samples/microservice-transaction-sample/README.md)
- [Sample application of Spring Data JDBC for ScalarDB with Microservice Transactions](../scalardb-samples/spring-data-microservice-transaction-sample/README.md)

:::

### Learn more

To learn more about running transactions by using ScalarDB Cluster, see the following:

- [ScalarDB Cluster gRPC API Guide](./scalardb-cluster-grpc-api-guide.md)

**.NET**

### One-phase commit interface

For details about how to run transactions by using a one-phase commit interface, see the [Getting Started with Distributed Transactions in the ScalarDB Cluster .NET Client SDK](../scalardb-cluster-dotnet-client-sdk/getting-started-with-distributed-transactions.md).

### Two-phase commit interface

For details about how to run transactions by using a two-phase commit interface, see [Getting Started with Distributed Transactions with a Two-Phase Commit Interface in the ScalarDB Cluster .NET Client SDK](../scalardb-cluster-dotnet-client-sdk/getting-started-with-two-phase-commit-transactions.md).
