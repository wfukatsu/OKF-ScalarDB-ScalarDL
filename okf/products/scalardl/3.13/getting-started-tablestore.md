---
type: Tutorial
title: Get Started with ScalarDL TableStore
description: ScalarDL TableStore is a high-level abstraction on top of the low-level ledger abstraction. It offers an SQL interface instead of primitive CRUD interfaces like get and put, enabling you to build versatile, tamper-evident applications with...
resource: https://scalardl.scalar-labs.com/docs/latest/getting-started-tablestore/
tags:
- scalardl
- v3.13
- phase:implement
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: getting-started-tablestore
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:59Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/docs/getting-started-tablestore.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Get Started with ScalarDL TableStore

ScalarDL TableStore is a high-level abstraction on top of the low-level ledger abstraction. It offers an [SQL interface](./sql-grammar.md) instead of primitive CRUD interfaces like get and put, enabling you to build versatile, tamper-evident applications with the familiar data model and commands quickly and easily.

This getting started tutorial explains how to configure TableStore on your preferred database and manage tables and records in a tamper-evident manner.

## What is ScalarDL TableStore?

TableStore provides table-based data management through an [SQL interface](./sql-grammar.md). You can create tables in a flexible schemaless manner, perform SQL operations like SELECT, INSERT, and UPDATE, and maintain complete audit trails of all data modifications. It also provides an indexing capability, allowing you to select records not only by a primary key but also by an index key.

## Prerequisites

- One of the following Java Development Kits (JDKs):

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, 17, or 21 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, 17, or 21 (LTS versions)

- [Docker](https://www.docker.com/get-started/) 20.10 or later with [Docker Compose](https://docs.docker.com/compose/install/) v2.20.0 or later

## Clone the ScalarDL samples repository

Open **Terminal**, then clone the ScalarDL samples repository by running the following command:

```console
git clone https://github.com/scalar-labs/scalardl-samples
```

Then, go to the directory that contains the sample configuration by running the following command:

```console
cd scalardl-samples
```

## Start up ScalarDL with your preferred database

Select your database, and follow the instructions to deploy ScalarDL Ledger with it. For a list of databases that ScalarDL supports, see [Databases](https://scalardl.scalar-labs.com/docs/latest/requirements#databases).

**MySQL**

### Set up your license (Enterprise edition only)

If you're using the ScalarDL Enterprise edition, set up your license as follows. If you're using the Community edition, skip to the next section to start up ScalarDL.

<details>
<summary>See here to set up your license</summary>

1. Enable the container image for the Enterprise edition in the `mysql/docker-compose-ledger.yml` file as follows:

- Before changing the image (default configuration):

```yaml
services:
  scalardl-ledger:
    image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    # image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

- After changing the image:

```yaml
services:
  scalardl-ledger:
    # image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

2. Set your license key for ScalarDL Ledger. In the `mysql/ledger.properties` file, replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```properties
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
scalar.dl.licensing.license_key={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
```

3. To check the license, update the `mysql/docker-compose-ledger.yml` file as follows. If you're using a trial license, skip this step.

- Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

- After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      # - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

</details>

### Start up ScalarDL

You can start ScalarDL Ledger by following the steps below:

1. Run MySQL locally by running the following command:

```console
docker compose -f mysql/docker-compose-ledger.yml up -d mysql
```

2. Load the database schema for ScalarDL Ledger by running the following command:

```console
docker compose -f mysql/docker-compose-ledger.yml up -d scalardl-ledger-schema-loader
```

3. Run ScalarDL Ledger and its dependent components by running the following command:

```console
docker compose -f mysql/docker-compose-ledger.yml up -d
```

**PostgreSQL**

### Set up your license (Enterprise edition only)

If you're using the ScalarDL Enterprise edition, set up your license as follows. If you're using the Community edition, skip to the next section to start up ScalarDL.

<details>
<summary>See here to set up your license</summary>

1. Enable the container image for the Enterprise edition in the `postgres/docker-compose-ledger.yml` file as follows:

- Before changing the image (default configuration):

```yaml
services:
  scalardl-ledger:
    image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    # image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

- After changing the image:

```yaml
services:
  scalardl-ledger:
    # image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

2. Set your license key for ScalarDL Ledger. In the `postgres/ledger.properties` file, replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```properties
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
scalar.dl.licensing.license_key={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
```

3. To check the license, update the `postgres/docker-compose-ledger.yml` file as follows. If you're using a trial license, skip this step.

- Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

- After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      # - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

</details>

### Start up ScalarDL

You can start ScalarDL Ledger by following the steps below:

1. Run PostgreSQL locally by running the following command:

```console
docker compose -f postgres/docker-compose-ledger.yml up -d postgres
```

2. Load the database schema for ScalarDL Ledger by running the following command:

```console
docker compose -f postgres/docker-compose-ledger.yml up -d scalardl-ledger-schema-loader
```

3. Run ScalarDL Ledger and its dependent components by running the following command:

```console
docker compose -f postgres/docker-compose-ledger.yml up -d
```

**Oracle Database**

### Set up your license (Enterprise edition only)

If you're using the ScalarDL Enterprise edition, set up your license as follows. If you're using the Community edition, skip to the next section to start up ScalarDL.

<details>
<summary>See here to set up your license</summary>

1. Enable the container image for the Enterprise edition in the `oracle/docker-compose-ledger.yml` file as follows:

- Before changing the image (default configuration):

```yaml
services:
  scalardl-ledger:
    image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    # image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

- After changing the image:

```yaml
services:
  scalardl-ledger:
    # image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

2. Set your license key for ScalarDL Ledger. In the `oracle/ledger.properties` file, replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```properties
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
scalar.dl.licensing.license_key={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
```

3. To check the license, update the `oracle/docker-compose-ledger.yml` file as follows. If you're using a trial license, skip this step.

- Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

- After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      # - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

</details>

### Start up ScalarDL

You can start ScalarDL Ledger by following the steps below:

1. Run Oracle Database locally by running the following command:

```console
docker compose -f oracle/docker-compose-ledger.yml up -d oracle
```

2. Load the database schema for ScalarDL Ledger by running the following command:

```console
docker compose -f oracle/docker-compose-ledger.yml up -d scalardl-ledger-schema-loader
```

3. Run ScalarDL Ledger and its dependent components by running the following command:

```console
docker compose -f oracle/docker-compose-ledger.yml up -d
```

**SQL Server**

### Set up your license (Enterprise edition only)

If you're using the ScalarDL Enterprise edition, set up your license as follows. If you're using the Community edition, skip to the next section to start up ScalarDL.

<details>
<summary>See here to set up your license</summary>

1. Enable the container image for the Enterprise edition in the `sqlserver/docker-compose-ledger.yml` file as follows:

- Before changing the image (default configuration):

```yaml
services:
  scalardl-ledger:
    image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    # image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

- After changing the image:

```yaml
services:
  scalardl-ledger:
    # image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

2. Set your license key for ScalarDL Ledger. In the `sqlserver/ledger.properties` file, replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```properties
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
scalar.dl.licensing.license_key={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
```

3. To check the license, update the `sqlserver/docker-compose-ledger.yml` file as follows. If you're using a trial license, skip this step.

- Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

- After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      # - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

</details>

### Start up ScalarDL

You can start ScalarDL Ledger by following the steps below:

1. Run SQL Server locally by running the following command:

```console
docker compose -f sqlserver/docker-compose-ledger.yml up -d sqlserver
```

2. Load the database schema for ScalarDL Ledger by running the following command:

```console
docker compose -f sqlserver/docker-compose-ledger.yml up -d scalardl-ledger-schema-loader
```

3. Run ScalarDL Ledger and its dependent components by running the following command:

```console
docker compose -f sqlserver/docker-compose-ledger.yml up -d
```

**DynamoDB**

### Set up your license (Enterprise edition only)

If you're using the ScalarDL Enterprise edition, set up your license as follows. If you're using the Community edition, skip to the next section to start up ScalarDL.

<details>
<summary>See here to set up your license</summary>

1. Enable the container image for the Enterprise edition in the `dynamodb/docker-compose-ledger.yml` file as follows:

- Before changing the image (default configuration):

```yaml
services:
  scalardl-ledger:
    image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    # image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

- After changing the image:

```yaml
services:
  scalardl-ledger:
    # image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

2. Set your license key for ScalarDL Ledger. In the `dynamodb/ledger.properties` file, replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```properties
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
scalar.dl.licensing.license_key={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
```

3. To check the license, update the `dynamodb/docker-compose-ledger.yml` file as follows. If you're using a trial license, skip this step.

- Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

- After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      # - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

</details>

### Start up ScalarDL

You can start ScalarDL Ledger by following the steps below:

1. Run DynamoDB locally by running the following command:

```console
docker compose -f dynamodb/docker-compose-ledger.yml up -d dynamodb
```

2. Load the database schema for ScalarDL Ledger by running the following command:

```console
docker compose -f dynamodb/docker-compose-ledger.yml up -d scalardl-ledger-schema-loader
```

3. Run ScalarDL Ledger and its dependent components by running the following command:

```console
docker compose -f dynamodb/docker-compose-ledger.yml up -d
```

**Cosmos DB for NoSQL**

### Set up your license (Enterprise edition only)

If you're using the ScalarDL Enterprise edition, set up your license as follows. If you're using the Community edition, skip to the next section to start up ScalarDL.

<details>
<summary>See here to set up your license</summary>

1. Enable the Docker image for the Enterprise edition in the `cosmosdb/docker-compose-ledger.yml` file as follows:

   - Before changing the image (default configuration):

```yaml
services:
  scalardl-ledger:
    image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    # image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

   - After changing the image:

```yaml
services:
  scalardl-ledger:
    # image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

2. Set your license key for ScalarDL Ledger. In the `cosmosdb/ledger.properties` file, replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```properties
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
scalar.dl.licensing.license_key={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
```

3. To check the license, update the `cosmosdb/docker-compose-ledger.yml` file as follows. If you're using a trial license, skip this step.

   - Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

   - After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      # - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

</details>

### Start up ScalarDL

You can start ScalarDL Ledger by following the steps below:

1. Configure Cosmos DB for NoSQL.

   To use Azure Cosmos DB for NoSQL, you must have an Azure account. If you don't have an Azure account, visit [Create an Azure Cosmos DB account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal#create-account).

   After setting up Cosmos DB for NoSQL, modify the following items in `cosmodb/ledger.properties` based on your configuration of Cosmos DB for NoSQL.

```properties
scalar.db.contact_points=<COSMOS_DB_FOR_NOSQL_URI>
scalar.db.password=<COSMOS_DB_FOR_NOSQL_KEY>
```

2. Load the database schema for ScalarDL Ledger by running the following command:

```console
docker compose -f cosmosdb/docker-compose-ledger.yml up -d scalardl-ledger-schema-loader
```

3. Run ScalarDL Ledger by running the following command:

```console
docker compose -f cosmosdb/docker-compose-ledger.yml up -d
```

**Cassandra**

### Set up your license (Enterprise edition only)

If you're using the ScalarDL Enterprise edition, set up your license as follows. If you're using the Community edition, skip to the next section to start up ScalarDL.

<details>
<summary>See here to set up your license</summary>

1. Enable the container image for the Enterprise edition in the `cassandra/docker-compose-ledger.yml` file as follows:

- Before changing the image (default configuration):

```yaml
services:
  scalardl-ledger:
    image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    # image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

- After changing the image:

```yaml
services:
  scalardl-ledger:
    # image: ghcr.io/scalar-labs/scalardl-ledger:${SCALARDL_VERSION}
    image: ghcr.io/scalar-labs/scalardl-ledger-byol:${SCALARDL_VERSION}
```

2. Set your license key for ScalarDL Ledger. In the `cassandra/ledger.properties` file, replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```properties
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
scalar.dl.licensing.license_key={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
##### PLEASE REPLACE THIS VALUE WITH YOUR LICENSE KEY (ENTERPRISE EDITION ONLY) #####
```

3. To check the license, update the `cassandra/docker-compose-ledger.yml` file as follows. If you're using a trial license, skip this step.

- Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

- After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./ledger.properties:/scalar/ledger/ledger.properties.tmpl
      - ../fixture/ledger-key.pem:/scalar/ledger-key.pem
      # - ../fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ../fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

</details>

### Start up ScalarDL

You can start ScalarDL Ledger by following the steps below:

1. Run Cassandra locally by running the following command:

```console
docker compose -f cassandra/docker-compose-ledger.yml up -d cassandra
```

2. Load the database schema for ScalarDL Ledger by running the following command:

```console
docker compose -f cassandra/docker-compose-ledger.yml up -d scalardl-ledger-schema-loader
```

3. Run ScalarDL Ledger and its dependent components by running the following command:

```console
docker compose -f cassandra/docker-compose-ledger.yml up -d
```

## Download the Client SDK

Next, you'll use the TableStore client tools. Specify a version that is the same as the deployed ScalarDL version and is used for downloading the tools by running the following command:

```console
VERSION=$(grep SCALARDL_VERSION .env | awk -F= '{print $2}')
```

Then, download the tools by running the following command:

```console
curl -OL https://github.com/scalar-labs/scalardl/releases/download/v$VERSION/scalardl-tablestore-java-client-sdk-$VERSION.zip
unzip scalardl-tablestore-java-client-sdk-$VERSION.zip
mv scalardl-tablestore-java-client-sdk-$VERSION tablestore
```

## Configure the client properties

Before interacting with TableStore, you need to configure the client. To create a configuration file with the minimum required properties for the client, run the following command:

```console
cat << 'EOF' > client.properties
# A host name for ScalarDL Ledger.
scalar.dl.client.server.host=localhost

# An ID for the certificate holder. This must be configured for each private key and must be unique in the system.
scalar.dl.client.cert_holder_id=foo

# A path to the certificate file.
scalar.dl.client.cert_path=./fixture/client.pem

# A path to the private key file.
scalar.dl.client.private_key_path=./fixture/client-key.pem
EOF
```

You can use `localhost` for the ScalarDL Ledger host name in this tutorial. For the private key and certificate, you can use the ones provided in the [`fixture` directory of the `scalardl-samples` repository](https://github.com/scalar-labs/scalardl-samples/tree/master/fixture) (`client-key.pem` and `client.pem`, respectively). For the certificate holder, any unique ID can be specified.

:::warning

Do not use the sample private key and certificate in production environments. For details about getting your own certificate, see [How to Get a Certificate](./ca/caclient-getting-started.md).

:::

## Bootstrap

Next, you can bootstrap TableStore by running the following command:

```console
tablestore/bin/scalardl-tablestore bootstrap --properties client.properties
```

The bootstrap command internally registers identity information (a certificate or secret) and predefined contracts necessary to use TableStore.

## Interact with TableStore

Now you can execute SQL statements with TableStore. In this section, you'll try the following functionalities through two sample tables (`employee` and `department`) that can be joined through the department IDs of employees:

- [Create and show tables](#create-and-show-tables)
- [Insert records](#insert-records)
- [Select records](#select-records)
- [Update records](#update-records)
- [Get record histories](#get-record-histories)

### Create and show tables

You can create the sample table by running the following commands:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "CREATE TABLE employee (id STRING PRIMARY KEY, department STRING)"
```
```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "CREATE TABLE department (id STRING PRIMARY KEY)"
```

When creating a table, you need to specify the name and the primary key. You can create secondary indexes by specifying additional columns. Because ScalarDL TableStore treats a JSON object as a record in tables, you don't have to specify a strict schema when creating a table.

You can show the created tables by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "SELECT * FROM information_schema.tables"
```

You should get a result like the following:

```console
Result:
[ {
  "name" : "employee",
  "key" : "id",
  "type" : "string",
  "indexes" : [ {
    "key" : "department",
    "type" : "string"
  } ]
}, {
  "name" : "department",
  "key" : "id",
  "type" : "string",
  "indexes" : [ ]
} ]
```

### Insert records

Next, insert several `employee` records by running the following commands:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "INSERT INTO employee VALUES {'id': '1001', 'name': 'Alice', 'department': 'sales', 'salary': 654.3}"
```
```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "INSERT INTO employee VALUES {'id': '1002', 'name': 'Bob', 'department': 'sales', 'salary': 543.2}"
```
```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "INSERT INTO employee VALUES {'id': '1003', 'name': 'Carol', 'department': 'engineering', 'salary': 654.3}"
```

Insert the corresponding `department` records as well by running the following commands:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "INSERT INTO department VALUES {'id': 'sales', 'location': 'Shinjuku', 'phone': '000-1234'}"
```
```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "INSERT INTO department VALUES {'id': 'engineering', 'location': 'Shibuya', 'phone': '000-4321'}"
```

### Select records

Then, check the inserted records. You need to specify at least a primary key or index key to select records. For example, you can get an `employee` record by specifying the primary key by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "SELECT id, name, department FROM employee WHERE id = '1001'"
```

You can optionally project the columns by specifying top-level fields in the JSON record object. You should get a result like the following:

```console
Result:
[ {
  "id" : "1001",
  "name" : "Alice",
  "department" : "sales"
} ]
```

You can also specify an index key to select records by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "SELECT id, name, department FROM employee WHERE department = 'sales'"
```

You should get a result like the following:

```console
Result:
[ {
  "id" : "1001",
  "name" : "Alice",
  "department" : "sales"
}, {
  "id" : "1002",
  "name" : "Bob",
  "department" : "sales"
} ]
```

If you want to filter records, specify additional conditions by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "SELECT id, name, department FROM employee WHERE department = 'sales' AND salary < 600"
```

You should get a result like the following:

```console
Result:
[ {
  "id" : "1002",
  "name" : "Bob",
  "department" : "sales",
  "salary" : 543.2
} ]
```

You can also join the two tables by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "SELECT * FROM employee JOIN department ON employee.department = department.id WHERE employee.department = 'engineering'"
```

You should get a result like the following:

```console
Result:
[ {
  "employee.id" : "1003",
  "employee.name" : "Carol",
  "employee.department" : "engineering",
  "employee.salary" : 654.3,
  "department.id" : "engineering",
  "department.location" : "Shibuya",
  "department.phone" : "000-4321"
} ]
```

### Update records

You can update the `employee` records by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "UPDATE employee SET salary = 754.3 WHERE department = 'engineering'"
```

Make sure to specify at least a primary key or an index key to update the records, in the same way as using the `SELECT` statement.

### Get record histories

You can get the update history of a record by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "SELECT history() FROM employee WHERE id = '1003'"
```

You should get a result like the following:

```console
Result:
[ {
  "age" : 1,
  "values" : {
    "id" : "1003",
    "name" : "Carol",
    "department" : "engineering",
    "salary" : 754.3
  }
}, {
  "age" : 0,
  "values" : {
    "id" : "1003",
    "name" : "Carol",
    "department" : "engineering",
    "salary" : 654.3
  }
} ]
```

If you want to limit the number of versions (ages), specify the `LIMIT` clause by running the following command:

```console
tablestore/bin/scalardl-tablestore execute-statement --properties client.properties \
--statement "SELECT history() FROM employee WHERE id = '1003' LIMIT 1"
```

You should get the specified number of the **latest** records like the following:

```console
Result:
[ {
  "age" : 1,
  "values" : {
    "id" : "1003",
    "name" : "Carol",
    "department" : "engineering",
    "salary" : 754.3
  }
} ]
```

## Validate data managed by TableStore

In ScalarDL, you occasionally need to validate your data to make sure all the data is in a valid state. You can use the `validate-ledger` command to validate data managed by TableStore.

You can validate the table schema by running the following command:

```console
tablestore/bin/scalardl-tablestore validate-ledger --properties client.properties \
--table-name employee
```

You should get a result like the following:

```console
{
  "status_code" : "OK",
  "Ledger" : {
    "id" : "tbl_employee",
    "age" : 0,
    "nonce" : "26af1229-1c1f-4b89-86e2-ec011da3b313",
    "hash" : "ZA9yFzjIg1qeHAd7Sub8uFvt2JrTb6XSzGUktPEITr0=",
    "signature" : "MEUCIAh4Xj93J/jldqbQor7AVM4ii9+suxQrZlCFnKWWDIo0AiEAiM6Yi6GO4bQ2VZg2GnqKmOFPEANrTU4g7pjBMcaX6TQ="
  },
  "Auditor" : null
}
```

You can validate the record by running the following command:

```console
tablestore/bin/scalardl-tablestore validate-ledger --properties client.properties \
--table-name employee --primary-key-column-name id --column-value '"1001"'
```

:::note

The `--column-value` option expects a JSON value; thus, you need to put double quotes for a string value.

:::

You should get a result like the following:

```console
{
  "status_code" : "OK",
  "Ledger" : {
    "id" : "rec_employee_id_1001",
    "age" : 0,
    "nonce" : "41a18e7f-314f-4aec-8984-62bf6cd355d0",
    "hash" : "n7KJLuC/KOzFZLnGKEs6pOQvCbl4WSF+xplOUd9MrSo=",
    "signature" : "MEUCIEHafCsSXWWtZnDbSpAwFQk4qjW1B7cXjEgdwVF8uKQeAiEAsvzEMKyuNFozAbLC/E8FEviCMLCqo9DPRQe4tVBFwIk="
  },
  "Auditor" : null
}
```

You can validate the index record by running the following command:

```console
tablestore/bin/scalardl-tablestore validate-ledger --properties client.properties \
--table-name employee --index-key-column-name department --column-value '"sales"'
```

You should get a result like the following:

```console
{
  "status_code" : "OK",
  "Ledger" : {
    "id" : "idx_employee_department_sales",
    "age" : 0,
    "nonce" : "41a18e7f-314f-4aec-8984-62bf6cd355d0",
    "hash" : "n7KJLuC/KOzFZLnGKEs6pOQvCbl4WSF+xplOUd9MrSo=",
    "signature" : "MEUCIEHafCsSXWWtZnDbSpAwFQk4qjW1B7cXjEgdwVF8uKQeAiEAsvzEMKyuNFozAbLC/E8FEviCMLCqo9DPRQe4tVBFwIk="
  },
  "Auditor" : null
}
```

:::note

ScalarDL TableStore internally assigns a dedicated asset ID to an [asset record](./data-modeling.md#asset-record), which is an object in the primitive data model of ScalarDL. The asset ID consists of a prefix for the asset type and keys for identification; for example, a prefix `rec_`, table name, primary key column name, and column value are used for the asset ID of a record. You will see such raw asset IDs in the result of `validate-ledger`.

:::

## See also

To interact with ScalarDL TableStore in your Java applications, see the following:

* [Javadocs for the ScalarDL TableStore Java Client SDK](https://javadoc.io/doc/com.scalar-labs/scalardl-tablestore-java-client-sdk/latest/index.html)

## References

* [ScalarDL TableStore SQL Grammar](./sql-grammar.md)
