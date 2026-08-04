---
type: Deployment Guide
title: ScalarDB Cluster Standalone Mode
description: Instead of setting up a Kubernetes cluster and deploying ScalarDB Cluster on top of it by using a Helm Chart, you can run ScalarDB Cluster in standalone mode, which simplifies development and testing processes. A primary use case for this...
resource: https://scalardb.scalar-labs.com/docs/3.14/scalardb-cluster/standalone-mode/
tags:
- scalardb
- v3.14
- phase:operate
- section:deploy
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: scalardb-cluster/standalone-mode
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/scalardb-cluster/standalone-mode.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB Cluster Standalone Mode

Instead of setting up a Kubernetes cluster and deploying ScalarDB Cluster on top of it by using a Helm Chart, you can run ScalarDB Cluster in standalone mode, which simplifies development and testing processes. A primary use case for this would be when you want to start ScalarDB Cluster in standalone mode via Docker on your local machine and use it for development and testing.

To run ScalarDB Cluster in standalone mode, you need to set the `scalar.db.cluster.node.standalone_mode.enabled` property to `true`:

```properties
scalar.db.cluster.node.standalone_mode.enabled=true
```

## Run ScalarDB Cluster in standalone mode on Docker Compose

This section explains how to start ScalarDB Cluster in standalone mode on Docker Compose.

:::warning

You need to have a license key (trial license or commercial license) to use ScalarDB Cluster. If you don't have a license key, please [contact us](https://www.scalar-labs.com/contact-us).

:::

### Clone the ScalarDB samples repository

Open **Terminal**, then clone the ScalarDB samples repository by running the following command:

```console
git clone https://github.com/scalar-labs/scalardb-samples
```

Then, go to the directory that contains the necessary files by running the following command:

```console
cd scalardb-samples/scalardb-cluster-standalone-mode/
```

### Set up your database for ScalarDB Cluster

Select your database, and follow the instructions to configure it for ScalarDB Cluster.

For a list of databases that ScalarDB supports, see [Databases](../requirements.md#databases).

**MySQL**

### Run MySQL locally

You can run MySQL in Docker Compose by using the `docker-compose.yaml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start MySQL, run the following command:

```console
docker compose up -d mysql
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations for ScalarDB Cluster. Please uncomment the properties for MySQL in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For MySQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:mysql://mysql-1:3306/
scalar.db.username=root
scalar.db.password=mysql
```

**PostgreSQL**

### Run PostgreSQL locally

You can run PostgreSQL in Docker Compose by using the `docker-compose.yaml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start PostgreSQL, run the following command:

```console
docker compose up -d postgres
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations for ScalarDB Cluster. Please uncomment the properties for PostgreSQL in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For PostgreSQL
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:postgresql://postgres-1:5432/
scalar.db.username=postgres
scalar.db.password=postgres
```

**Oracle Database**

### Run Oracle Database locally

You can run Oracle Database in Docker Compose by using the `docker-compose.yaml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start Oracle Database, run the following command:

```console
docker compose up -d oracle
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations for ScalarDB Cluster. Please uncomment the properties for Oracle Database in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For Oracle
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:oracle:thin:@//oracle-1:1521/FREEPDB1
scalar.db.username=SYSTEM
scalar.db.password=Oracle
```

**SQL Server**

### Run SQL Server locally

You can run SQL Server in Docker Compose by using the `docker-compose.yaml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start SQL Server, run the following command:

```console
docker compose up -d sqlserver
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations for ScalarDB Cluster. Please uncomment the properties for SQL Server in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For SQL Server
scalar.db.storage=jdbc
scalar.db.contact_points=jdbc:sqlserver://sqlserver-1:1433;encrypt=true;trustServerCertificate=true
scalar.db.username=sa
scalar.db.password=SqlServer22
```

**DynamoDB**

### Run Amazon DynamoDB Local

You can run Amazon DynamoDB Local in Docker Compose by using the `docker-compose.yaml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start Amazon DynamoDB Local, run the following command:

```console
docker compose up -d dynamodb
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations for ScalarDB Cluster. Please uncomment the properties for Amazon DynamoDB Local in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For DynamoDB Local
scalar.db.storage=dynamo
scalar.db.contact_points=sample
scalar.db.username=sample
scalar.db.password=sample
scalar.db.dynamo.endpoint_override=http://dynamodb-1:8000
```

**Cosmos DB for NoSQL**

To use Azure Cosmos DB for NoSQL, you must have an Azure account. If you don't have an Azure account, visit [Create an Azure Cosmos DB account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal#create-account).

### Configure Cosmos DB for NoSQL

Set the **default consistency level** to **Strong** according to the official document at [Configure the default consistency level](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/how-to-manage-consistency#configure-the-default-consistency-level).

### Configure ScalarDB Cluster

The following instructions assume that you have properly installed and configured the JDK in your local environment and properly configured your Cosmos DB for NoSQL account in Azure.

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations for ScalarDB Cluster. Be sure to change the values for `scalar.db.contact_points` and `scalar.db.password` as described.

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

You can run Apache Cassandra in Docker Compose by using the `docker-compose.yaml` file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory.

To start Apache Cassandra, run the following command:

```console
docker compose up -d cassandra
```

### Configure ScalarDB Cluster

The **scalardb-cluster-node.properties** file in the `scalardb-samples/scalardb-cluster-standalone-mode` directory contains database configurations for ScalarDB Cluster. Please uncomment the properties for Cassandra in the **scalardb-cluster-node.properties** file so that the configuration looks as follows:

```properties
# For Cassandra
scalar.db.storage=cassandra
scalar.db.contact_points=cassandra-1
scalar.db.username=cassandra
scalar.db.password=cassandra
```

### Set the license key

Set the license key (trial license or commercial license) for the ScalarDB Clusters in the configuration file `scalardb-cluster-node.properties`. For details, see [How to Configure a Product License Key](../scalar-licensing/section-home.md).

### Start ScalarDB Cluster in standalone mode

To start ScalarDB Cluster in standalone mode, run the following command:

:::note

If you want to change other configurations for ScalarDB Cluster, update the `scalardb-cluster-node.properties` file before running the command below.

:::

```console
docker compose up -d scalardb-cluster-node
```

## Client configurations for the ScalarDB Cluster Java API

You can use the `indirect` client mode to connect to ScalarDB Cluster in standalone mode. For details about client configurations for the ScalarDB Cluster Java API, see [Developer Guide for ScalarDB Cluster with the Java API](./developer-guide-for-scalardb-cluster-with-java-api.md).
