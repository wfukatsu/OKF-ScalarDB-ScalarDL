---
type: Tutorial
title: Get Started with ScalarDL HashStore
description: 'ScalarDL HashStore is a high-level abstraction on top of a low-level ledger abstraction. It is specially designed for digital evidence preservation and offers two functionalities: object authenticity management and collection authenticity...'
resource: https://scalardl.scalar-labs.com/docs/3.12/getting-started-hashstore/
tags:
- scalardl
- v3.12
- phase:implement
- section:quickstart
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.12'
patch_version: 3.12.3
doc_id: getting-started-hashstore
lifecycle_phase: implement
breadcrumb:
- Quickstart
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:07Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/versioned_docs/version-3.12/getting-started-hashstore.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Get Started with ScalarDL HashStore

ScalarDL HashStore is a high-level abstraction on top of a low-level ledger abstraction. It is specially designed for digital evidence preservation and offers two functionalities: object authenticity management and collection authenticity management. By using HashStore, you can manage hash values of objects and a collection of objects in an immutable manner without writing a [contract](./design.md#contract), enabling you to develop authenticity management applications quickly and easily.

This getting started tutorial explains how to configure ScalarDL HashStore on your preferred database and manage objects and collections in a tamper-evident manner.

## What is ScalarDL HashStore?

HashStore provides two functionalities: object authenticity management and collection authenticity management. The object authenticity management enables you to manage the authenticity of any kind of your objects, like files, audit logs, and even directories in your file or object storage. The collection authenticity management enables you to manage which objects exist in a collection. For example, you can create a collection of objects that need to be validated in an auditing process.

For how HashStore achieves these functionalities, see the examples in [Manage object authenticity](#manage-object-authenticity) and [Manage collection authenticity](#manage-collection-authenticity) below.

## Prerequisites

- One of the following Java Development Kits (JDKs):

- **[Oracle JDK](https://www.oracle.com/java/):** 8, 11, 17, or 21 (LTS versions)
- **OpenJDK distribution ([Eclipse Temurin](https://adoptium.net/temurin/), [Amazon Corretto](https://aws.amazon.com/corretto/), or [Microsoft Build of OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/)):** 8, 11, 17, or 21 (LTS versions)

- [Docker](https://www.docker.com/get-started/) 20.10 or later with [Docker Compose](https://docs.docker.com/compose/install/) v2.20.0 or later

:::warning

Since ScalarDL is built with JDK 8, contracts must be a JDK 8–compatible binary. If you use a version other than JDK 8, you must configure your build tool to build the JDK 8–compatible binary. There are several ways to specify binary compatibility, including using the `--release 8` option for javac or setting Gradle or Maven configurations to use the JDK 8 toolchain. The following shows the configuration for Gradle:

```gradle
java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(8))
    }
}
```

For more details about the Gradle and Maven configurations, see [Toolchains for JVM projects for Gradle](https://docs.gradle.org/current/userguide/toolchains.html) and [Guide to Using Toolchains for Maven](https://maven.apache.org/guides/mini/guide-using-toolchains.html).

:::

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

Select your database, and follow the instructions to deploy ScalarDL Ledger with it. For a list of databases that ScalarDL supports, see [Databases](https://scalardl.scalar-labs.com/docs/3.12/requirements#databases).

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

Next, you'll use the ScalarDL HashStore client tools. Specify a version that is the same as the deployed ScalarDL version and is used for downloading the tools by running the following command:

```console
VERSION=$(grep SCALARDL_VERSION .env | awk -F= '{print $2}')
```

Then, download the tools by running the following command:

```console
curl -OL https://github.com/scalar-labs/scalardl/releases/download/v$VERSION/scalardl-hashstore-java-client-sdk-$VERSION.zip
unzip scalardl-hashstore-java-client-sdk-$VERSION.zip
mv scalardl-hashstore-java-client-sdk-$VERSION hashstore
```

## Configure the client properties

Before interacting with ScalarDL HashStore, you need to configure the client. To create a configuration file with the minimum required properties for the client, run the following command:

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

Next, you can bootstrap HashStore by running the following command:

```console
hashstore/bin/scalardl-hashstore bootstrap --properties client.properties
```

The bootstrap command internally registers identity information (a certificate or secret) and predefined contracts necessary to use HashStore.

## Manage object authenticity

With the object authenticity management in HashStore, you can put the hash value of an object by using the `put-object` command. Specify the target object ID and the hash value of the object, like in the following example. The object ID must be a unique ID that identifies your objects or files, for example, a key of an object or a file path. You can also put any metadata associated with the object by using the `metadata` option.

First, get the hash value of a file and put it into the tamper-evident ledger.

:::note

The `sha256sum` command is for Linux environments only. `shasum` and `certutil` are available for macOS and Windows environments, respectively. For details on getting the same SHA256 hash values, see the usage of those commands.

:::

```console
echo "Alice created this file." > a.txt
sha256sum a.txt
```

You should get the following hash value:

```console
5c7440fb2273a247f78aadefbc511c680a84e7d44004abfaedef2b145151dab0  a.txt
```

You can put the hash value by running the following command:

```console
hashstore/bin/scalardl-hashstore put-object --properties client.properties \
--object-id a.txt \
--hash 5c7440fb2273a247f78aadefbc511c680a84e7d44004abfaedef2b145151dab0 \
--metadata '{"note": "created"}'
```

If the object is updated, you can put the new hash value in the same way. For example, the following assumes that the command below was executed:

```console
echo "Alice updated this file." >> a.txt
sha256sum a.txt
```

You should get the following result as the hash value:

```console
b97a42c87a46ffebe1439f8c1cd2f86e2f9b84dad89c8e9ebb257a19b6fdfe1c  a.txt
```

You can then update the hash value as follows:

```console
hashstore/bin/scalardl-hashstore put-object --properties client.properties \
--object-id a.txt \
--hash b97a42c87a46ffebe1439f8c1cd2f86e2f9b84dad89c8e9ebb257a19b6fdfe1c \
--metadata '{"note": "updated"}'
```

You can also get the latest status of the object by running the following command:

```console
hashstore/bin/scalardl-hashstore get-object --properties client.properties \
--object-id a.txt
```

You should get a result like the following:

```console
Result:
{
  "object_id" : "a.txt",
  "hash_value" : "b97a42c87a46ffebe1439f8c1cd2f86e2f9b84dad89c8e9ebb257a19b6fdfe1c",
  "metadata" : {
    "note" : "updated"
  }
}
```

If you want to validate the object's authenticity, first recalculate the hash value, for example, by using the `sha256sum` command, for each version of the object that you want to validate.

Then, execute the `compare-object-versions` command with the recalculated hash values with the version IDs in descending order. You can specify any number of versions. The version IDs are only used for showing which hash values are different from the original values in the output, so any string values can be used as long as the values are uniquely identifiable.

:::note

If you cannot get the hash value of the older version of the `a.txt` file in your environment, specify only the current version instead.

:::

```console
hashstore/bin/scalardl-hashstore compare-object-versions --properties client.properties \
--object-id a.txt \
--versions '[{"version_id": "v2", "hash_value": "b97a42c87a46ffebe1439f8c1cd2f86e2f9b84dad89c8e9ebb257a19b6fdfe1c"}, {"version_id": "v1", "hash_value": "5c7440fb2273a247f78aadefbc511c680a84e7d44004abfaedef2b145151dab0"}]}'
```

You should see the following result if the recalculated hash values of the object are the same as the ones in the tamper-evident ledger.

```console
Result:
{
  "status" : "correct",
  "details" : "The status is correct.",
  "faulty_versions" : [ ]
}
```

Suppose that someone tampered with the file `a.txt` as follows:

```txt
Bob created this file.
Alice updated this file
```

Now the hash value of the latest version is `1f75d715648a3b4b3a33ecd7428a3e7139d9357da7d38735c23bf38618ecf9c7`. You can execute validation by running the following command:

```console
hashstore/bin/scalardl-hashstore compare-object-versions --properties client.properties \
--object-id a.txt \
--versions '[{"version_id": "v2", "hash_value": "1f75d715648a3b4b3a33ecd7428a3e7139d9357da7d38735c23bf38618ecf9c7"}, {"version_id": "v1", "hash_value": "5c7440fb2273a247f78aadefbc511c680a84e7d44004abfaedef2b145151dab0"}]}'
```

You should get a result like the following:

```console
Result:
{
  "status" : "faulty",
  "details" : "A faulty version is found.",
  "faulty_versions" : [ "v2" ]
}
```

This validation process confirms if the data outside ScalarDL has not been changed by comparing the hash value of the data with the corresponding hash value stored in ScalarDL. To validate whether the data in ScalarDL (the hash values in this case) has not been tampered with, you can use the `validate-ledger` command. For details, see [Validate data managed by HashStore](#validate-data-managed-by-hashstore).

### Synchronize the object state between ScalarDL Ledger and a ScalarDB table

Since ScalarDL manages data (called "assets") in a tamper-evident and append-only manner, you are not able to update data in place, and you need to model your data in a somewhat inflexible manner. To mitigate these limitations, you can use ScalarDB in conjunction with ScalarDL. Specifically, you can issue operations to ScalarDL in parallel with issuing ScalarDB's mutation operations to ScalarDB-managed databases.

For example, in object authenticity management, the `put-object` command (and the corresponding API) provides the `--put-to-mutable` option, for putting an arbitrary record into a ScalarDB table when putting an object hash value. One primary use case for the option is managing object status (whether the hash value of the object is stored correctly in ScalarDL) on the ScalarDB side, allowing for identifying target objects flexibly and efficiently by using ScalarDB APIs. In such a case, you would:

1. Create a table (for example, `objects`) in ScalarDB to manage whether the hash value of an object version has already been registered.
1. List and put target objects in the `objects` table with a hash-value-not-registered status.
1. Update the state in the `objects` table after the hash value is successfully registered to ScalarDL.

The third step above must be done in an ACID manner by executing the following command with the `--put-to-mutable` option:

```console
hashstore/bin/scalardl-hashstore put-object --properties client.properties \
--object-id a.txt \
--hash 5c7440fb2273a247f78aadefbc511c680a84e7d44004abfaedef2b145151dab0 \
--put-to-mutable '{...}'
```

For the argument of the `--put-to-mutable` option, you need to specify a namespace name, a table name, a partition key, a clustering key (if any), and columns, depending on your ScalarDB table schema. An example is as follows.

```json
{
  "namespace": "myns",
  "table": "objects",
  "partition_key": [
    { "column_name": "object_id", "value": "a.txt", "data_type": "TEXT" }
  ],
  "clustering_key": [
    { "column_name": "version", "value": "1234aef", "data_type": "TEXT" }
  ],
  "columns": [
    { "column_name": "status", "value": 3, "data_type": "INT" },
    { "column_name": "size", "value": 10.000, "data_type": "DOUBLE" },
    { "column_name": "timestamp", "value": 123456789, "data_type": "BIGINT" },
    { "column_name": "comment", "value": "hash-registered", "data_type": "TEXT" }
  ]
}
```

## Manage collection authenticity

Collection authenticity management allows you to manage the authenticity of a set. For example, when you use a file storage and manage the authenticity of the files by using the `compare-object-versions` command, you may also want to do the same for folders or sets of objects that must be validated in an auditing process. Collection management covers these use cases and protects the audit sets.

If a system cannot guarantee that an audit set has not been changed unexpectedly, a malicious user may be able to change an object fraudulently and remove it from the audit set to avoid being revealed as a fraud. Therefore, managing the audit set is an important and major use case of collection authenticity management.

You can create a collection for an audit set by running the following command:

```console
hashstore/bin/scalardl-hashstore create-collection --properties client.properties \
--collection-id audit_set --object-ids a.txt --object-ids b.txt
```

The collection ID must be a unique ID that identifies the collection. You can specify a set of object IDs by using the `--object-ids` option. The object IDs are just string values, so you can specify any IDs for them. For example, you can put the collection IDs to represent the audit set in a hierarchical manner.

You can also add objects to the collection by running the following command:

```console
hashstore/bin/scalardl-hashstore add-to-collection --properties client.properties \
--collection-id audit_set --object-ids c.txt --object-ids d.txt
```

And you can remove objects from the collection by running the following command:

```console
hashstore/bin/scalardl-hashstore remove-from-collection --properties client.properties \
--collection-id audit_set --object-ids a.txt
```

You can get the latest status of the collection by running the following command:

```console
hashstore/bin/scalardl-hashstore get-collection --properties client.properties \
--collection-id audit_set
```

You should get a result like the following:

```console
Result:
{"object_ids": ["d.txt", "c.txt", "b.txt"]}
```

To confirm that the audit set has not been changed unexpectedly, you can check the update history of the audit set by running the following command:

```console
hashstore/bin/scalardl-hashstore get-collection-history --properties client.properties \
--collection-id audit_set
```

You should get a result like the following:

```console
Result:
{
  "collection_id" : "audit_set",
  "collection_events" : [ {
    "operation_type" : "remove",
    "age" : 2,
    "object_ids" : [ "a.txt" ]
  }, {
    "operation_type" : "add",
    "age" : 1,
    "object_ids" : [ "c.txt", "d.txt" ]
  }, {
    "operation_type" : "create",
    "age" : 0,
    "object_ids" : [ "a.txt", "b.txt" ]
  } ]
}
```

## Validate data managed by HashStore

In ScalarDL, you occasionally need to validate your data to make sure all the data is in a valid state. You can use the `validate-ledger` command to validate data managed by HashStore.

You can validate an object by running the following command:

```console
hashstore/bin/scalardl-hashstore validate-ledger --properties client.properties \
--object-id a.txt
```

You should get a result like the following:

```console
{
  "status_code" : "OK",
  "Ledger" : {
    "id" : "o_a.txt",
    "age" : 2,
    "nonce" : "8182ce3f-620d-4b8d-8718-19fc2666e060",
    "hash" : "8wLsztcUHRBSfdu4vCLfmWeAuS4T8UUoz+9QkqDl7Xc=",
    "signature" : "MEYCIQC83aBqEiBtyGW0UHa7AlJeLWho/wOnL1U5AzTbDMb7ngIhAOkgyVQtEYjtCD4FBZuuqAWuIOIW9Gnbd/djkxnet53a"
  },
  "Auditor" : null
}
```

You can validate a collection by running the following command:

```console
hashstore/bin/scalardl-hashstore validate-ledger --properties client.properties \
--collection-id audit_set
```

You should get a result like the following:

```console
{
  "status_code" : "OK",
  "Ledger" : {
    "id" : "c_audit_set",
    "age" : 2,
    "nonce" : "cd99fb75-1bde-4be3-af03-b43bd05f85eb",
    "hash" : "9Mw+Z4BQkDeLyd+su3WAi2Pes89AKU9kdZmy5Bgtj6c=",
    "signature" : "MEUCIAcG5di+Tn+VK35J2ZlzembZXxO4DV9cv/9zS1kMdimHAiEAnR3nqQ5I8UzQ+n99Uew6rZQ1DGZWIJzhcmJ9U3axXBs="
  },
  "Auditor" : null
}
```

:::note

ScalarDL HashStore internally assigns a dedicated asset ID to an [asset record](./data-modeling.md#asset-record), which is an object in the primitive data model of ScalarDL. The asset ID consists of a prefix for the asset type and keys for identification; for example, a prefix `c_` and collection ID are used for the asset ID of a collection. You will see such raw asset IDs in the result of `validate-ledger`.

:::

## See also

To interact with ScalarDL HashStore in your Java applications, see the following:

* [Javadocs for the ScalarDL HashStore Java Client SDK](https://javadoc.io/doc/com.scalar-labs/scalardl-hashstore-java-client-sdk/latest/index.html)
