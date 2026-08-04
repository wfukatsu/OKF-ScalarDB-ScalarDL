---
type: Documentation Page
title: Access Namespaces in a Restricted Manner
description: The namespace feature is currently in Public Preview. The feature and related documentation are subject to change.
resource: https://scalardl.scalar-labs.com/docs/latest/access-namespaces-in-a-restricted-manner/
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
doc_id: access-namespaces-in-a-restricted-manner
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:59Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/docs/access-namespaces-in-a-restricted-manner.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Access Namespaces in a Restricted Manner

:::warning

The namespace feature is currently in Public Preview. The feature and related documentation are subject to change.

:::

This document explains how to set up namespaces and access them in a restricted manner in a multi-tenant deployment of ScalarDL.

## What is restricted access to namespaces?

Restricting access to namespaces allows you to host multiple tenants on a single ScalarDL cluster while ensuring strict data isolation between them. Each tenant operates within its own namespace and can only access assets within that namespace.

### Security model

Restricted access to namespaces relies on port-based access control:

- **Privileged port:** Used by administrators for namespace management and credential registration. Only administrators should have access to this port.
- **Non-privileged port:** Used by tenant clients for contract registration and execution. Tenants access this port with their credentials registered to their specific namespace.

Because tenant credentials are registered to a specific namespace, all operations performed with those credentials are automatically scoped to that namespace. Tenants cannot register contracts or execute operations outside their assigned namespace.

:::note

This tutorial uses default ports and runs all commands from the same client machine for simplicity, assuming both the privileged and non-privileged ports are accessible. In a production environment, you should restrict access to the privileged port so that only administrators can reach it, while tenants connect only through the non-privileged port.

:::

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

Next, you'll use the ScalarDL client tools and samples to interact with ScalarDL.

Specify a version that is the same as the deployed ScalarDL version and is used for downloading the tools by running the following command:

```console
VERSION=$(grep SCALARDL_VERSION .env | awk -F= '{print $2}')
```

Then, download the tools by running the following command:

```console
curl -OL https://github.com/scalar-labs/scalardl/releases/download/v$VERSION/scalardl-java-client-sdk-$VERSION.zip
unzip scalardl-java-client-sdk-$VERSION.zip
mv scalardl-java-client-sdk-$VERSION client
```

## Set up a tenant namespace

This section walks you through the steps to set up a new tenant namespace.

### Configure the administrator client

You need to configure client properties for administrators to manage tenant namespaces and credentials. To create a configuration file with the minimum required properties for the administrator client, run the following command:

```console
cat << 'EOF' > admin.properties
# A host name for ScalarDL Ledger.
scalar.dl.client.server.host=localhost

# An entity ID. This must be configured for each private key and must be unique in a namespace.
scalar.dl.client.entity.id=admin

# A path to the certificate file.
scalar.dl.client.entity.identity.digital_signature.cert_path=./fixture/client.pem

# A path to the private key file.
scalar.dl.client.entity.identity.digital_signature.private_key_path=./fixture/client-key.pem
EOF
```

You can use `localhost` for the ScalarDL Ledger host name in this tutorial. For the private key and certificate, you can use the ones provided in the `fixture` directory of `scalardl-samples` (`client-key.pem` and `client.pem`, respectively). For the certificate holder, any unique ID can be specified.

:::warning

Do not use the sample private key and certificate in production environments. For details about getting your own certificate, see [How to Get a Certificate](./ca/caclient-getting-started.md).

:::

### Create a tenant namespace

As an administrator, create a namespace for the tenant by running the following command. This operation requires access to the privileged port.

```console
client/bin/scalardl create-namespace --properties admin.properties --namespace tenant_a
```

### Register tenant credentials

Register the tenant's certificate to the newly created namespace by running the following commands. This associates the tenant's identity with their namespace.

```console
client/bin/scalardl register-cert --properties admin.properties --namespace tenant_a --entity-id foo --cert-path ./fixture/client.pem
```

:::note

This sample uses the same `client.pem` as the administrator client for simplicity. In an actual production environment with digital signature authentication, you should use a certificate issued by the tenant user.

:::

## Use a tenant namespace

This section explains how to set up the tenant client to interact with its assigned namespace.

### Configure the tenant client

You need to configure client properties for the tenant to register and execute contracts or validate assets on the assigned namespace. To create a configuration file with the minimum required properties for the tenant client, run the following command:

```console
cat << 'EOF' > tenant.properties
# A host name for ScalarDL Ledger.
scalar.dl.client.server.host=localhost

# An entity ID. This must match the entity ID registered to the namespace in the previous step.
scalar.dl.client.entity.id=foo

# A namespace where client requests are executed.
scalar.dl.client.context.namespace=tenant_a

# A path to the certificate file.
scalar.dl.client.entity.identity.digital_signature.cert_path=./fixture/client.pem

# A path to the private key file.
scalar.dl.client.entity.identity.digital_signature.private_key_path=./fixture/client-key.pem
EOF
```

### Register and execute contracts

The tenant can now register contracts and execute them within their namespace. You can use the same contracts introduced in [Get Started with ScalarDL Ledger](./getting-started.md#create-a-contract) without needing to be aware of namespaces because all operations are automatically scoped to the namespace configured in the client properties.

First, compile the contracts in `scalardl-samples` by running the following command:

```console
./gradlew assemble
```

This will generate `build/classes/java/main/com/org1/contract/StateUpdater.class`. Then, register the contract by running the following command:

```console
client/bin/scalardl register-contract --properties tenant.properties --contract-id StateUpdater --contract-binary-name com.org1.contract.StateUpdater --contract-class-file build/classes/java/main/com/org1/contract/StateUpdater.class
```

Execute the contract by running the following command:

```console
client/bin/scalardl execute-contract --properties tenant.properties --contract-id StateUpdater --contract-argument '{"asset_id":"some_asset", "state":3}'
```

### Register and execute functions

By default, tenants can register contracts through the non-privileged port but cannot register functions. To allow tenants to register functions, administrators must set the following Ledger configuration options:

- `scalar.dl.ledger.function.non_privileged_port_registration.enabled`: Set to `true` to allow tenants to register functions through the non-privileged port. The default is `false`.
- `scalar.dl.ledger.function.non_privileged_port_registration.overwrite.enabled`: Set to `true` to allow tenants to overwrite existing functions through the non-privileged port. The default is `false`.

Once function registration is enabled, tenants can register and execute functions within their namespace in the same way as in the default namespace.

:::note

A function can access only the ScalarDB namespace that has the same name as the tenant's context namespace (the namespace configured in `scalar.dl.client.context.namespace`) or a namespace whose name starts with the context namespace followed by an underscore. For example, with a context namespace of `tenant_a`, a function can access `tenant_a`, `tenant_a_logs`, and `tenant_a_2024` but not `tenant_ax` or any unrelated namespace. When a function issues a `Get`, `Scan`, `Put`, or `Delete` operation, the namespace specified in that operation must be one of these accessible namespaces. Operations that target any other namespace or that do not specify a namespace are rejected.

Make sure to create the ScalarDB namespaces that the function accesses with the tenant's namespace as the prefix. Because this access rule is prefix-based, it is hierarchical: a shorter context namespace can access longer namespaces that share its prefix (for example, `tenant_a` can access `tenant_a_logs`). Design your namespace names so that these prefixes reflect the intended access boundaries between tenants. Note that the tables that the function accesses can have any name within those namespaces.

:::

For example, to register a function, run the following command:

```console
client/bin/scalardl register-function --properties tenant.properties --function-id test-function --function-binary-name com.example.function.TestFunction --function-class-file /path/to/TestFunction.class
```

To execute a function along with a contract, run the following command:

```console
client/bin/scalardl execute-contract --properties tenant.properties --contract-id StateUpdater --contract-argument '{"asset_id":"some_asset", "state":3}' --function-id test-function --function-argument '{}'
```

For details on updating contracts and functions, see [Manage Contract and Function Lifecycle](./manage-contract-and-function-lifecycle.md).

### Validate assets

You can also validate assets as usual, like in the default namespace, by running the following command:

```console
client/bin/scalardl validate-ledger --properties tenant.properties --asset-id="some_asset"
```

## See also

To write your own contracts, see the following:

- [A Guide on How to Write a Good Contract](./how-to-write-contract.md)

To interact with ScalarDL components in your Java applications, see the following:

- [Write a ScalarDL Application in Java](./how-to-write-applications.md)

To learn more about namespaces and how to manage them, see the following:

- [Manage Namespaces](./manage-namespaces.md)
- [ScalarDL Client Command Reference](./scalardl-command-reference.md)
