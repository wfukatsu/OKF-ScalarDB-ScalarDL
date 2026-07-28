---
type: Tutorial
title: Get Started with ScalarDL Ledger
description: This getting started tutorial explains how to configure ScalarDL on your preferred database and illustrates the process of creating a simple application where the historical states of data are traced.
resource: https://scalardl.scalar-labs.com/docs/latest/getting-started/
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
doc_id: getting-started
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/getting-started.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Get Started with ScalarDL Ledger

This getting started tutorial explains how to configure ScalarDL on your preferred database and illustrates the process of creating a simple application where the historical states of data are traced.

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

## Configure the client properties

Before you can run ScalarDL Ledger, you need to configure the ScalarDL client. To create a configuration file with the minimum required properties for the client to interact with ScalarDL Ledger, run the following command:

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

You can use `localhost` for the ScalarDL Ledger host name in this tutorial. For the private key and certificate, you can use the ones provided in the `fixture` directory of `scalardl-samples` (`client-key.pem` and `client.pem`, respectively). For the certificate holder, any unique ID can be specified.

:::warning

Do not use the sample private key and certificate in production environments. For details about getting your own certificate, see [How to Get a Certificate](./ca/caclient-getting-started.md).

:::

## Register the certificate

Next, you can register your certificate to ScalarDL Ledger by running the following command:

```console
client/bin/scalardl register-cert --properties client.properties
```

The registered certificate will allow you to register and execute contracts and will also be used for detecting Byzantine faults in databases.
Note that you can only add new certs and cannot update existing certs in place for security reasons. When you want to add a new cert, increment `scalar.dl.client.cert_version` before executing the registration tool.

## Create a contract

You can interact with ScalarDL through a contract, which is a Java program that implements single business logic. In this tutorial, you can see how a contract is written, built, and works by using a basic contract example, which creates an asset and associates some states with it.

Below, you can see a sample contract, [StateUpdater.java](https://github.com/scalar-labs/scalardl-samples/blob/master/src/main/java/com/org1/contract/StateUpdater.java). A contract is simply a Java class that extends the predefined base contract classes (such as [`JacksonBasedContract`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.13.0/com/scalar/dl/ledger/contract/JacksonBasedContract.html) class) and overrides the `invoke` method. The business logic is implemented in the `invoke` method.

Specifically, the `invoke` method will extract a client-defined asset ID (`asset_id`) and state (`state`) from the argument, and then associate the asset ID with the state in the ledger if the given state is different from the asset's current state.

```java
package com.org1.contract;

import com.fasterxml.jackson.databind.JsonNode;
import com.scalar.dl.ledger.contract.JacksonBasedContract;
import com.scalar.dl.ledger.exception.ContractContextException;
import com.scalar.dl.ledger.statemachine.Asset;
import com.scalar.dl.ledger.statemachine.Ledger;
import java.util.Optional;
import javax.annotation.Nullable;

public class StateUpdater extends JacksonBasedContract {

  @Nullable
  @Override
  public JsonNode invoke(Ledger<JsonNode> ledger, JsonNode argument, @Nullable JsonNode properties) {
    if (!argument.has("asset_id") || !argument.has("state")) {
      // ContractContextException is the only throwable exception in a contract and
      // it should be thrown when a contract faces some non-recoverable error
      throw new ContractContextException("please set asset_id and state in the argument");
    }

    String assetId = argument.get("asset_id").asText();
    int state = argument.get("state").asInt();

    Optional<Asset<JsonNode>> asset = ledger.get(assetId);

    if (!asset.isPresent() || asset.get().data().get("state").asInt() != state) {
      ledger.put(assetId, getObjectMapper().createObjectNode().put("state", state));
    }

    return null;
  }
}
```

You can compile the contract by running the following command:

```console
./gradlew assemble
```

This will generate `build/classes/java/main/com/org1/contract/StateUpdater.class`.

## Register the contract

Next, register your contract by running the following command:

```console
client/bin/scalardl register-contract --properties client.properties --contract-id StateUpdater --contract-binary-name com.org1.contract.StateUpdater --contract-class-file build/classes/java/main/com/org1/contract/StateUpdater.class
```

Please set a globally unique ID for the contract ID (e.g. `StateUpdater` in the above command).

:::tip

You can set different contract IDs on the same contract by using different certificates to clarify "who did what" in a tamper-evident way.

For example, think about a voting application. In the application, anyone can vote with the same voting logic and therefore can use the same contract, but A's vote and B's vote need to be properly and securely distinguished—A cannot vote for B, and vice versa. By using different contract IDs on the same contract, you can ensure that A's vote and B's vote are identified differently from one another.

:::

## Execute the contract

Now you are ready to execute the contract with the following command.

```console
client/bin/scalardl execute-contract --properties client.properties --contract-id StateUpdater --contract-argument '{"asset_id":"some_asset", "state":3}'
```

In the contract argument, the value specified with the key `asset_id` must be unique globally for each asset.

## Validate the states of Ledger

You can validate the states of Ledger by executing the following command.

```console
client/bin/scalardl validate-ledger --properties client.properties --asset-id="some_asset"
```

What the validation does is depending on how you set up and configure ScalarDL.
Briefly speaking, if only ScalarDL Ledger is used, the validation traverses assets to see if the assets can be recomputed and have a valid hash-chain structure.
With ScalarDL Ledger and Auditor, the validation checks discrepancies (i.e., Byzantine faults) between the states of Ledger and Auditor without centralized coordination.
For more details about the validation with Auditor, see [Validate your data](./how-to-write-applications.md#validate-your-data) and [Run a ScalarDL Application Through ScalarDL Ledger and Auditor](./how-to-run-applications-with-auditor.md).

## Create your own contracts or use predefined contracts

There are two options for preparing contracts: creating your own or using predefined ones.

As explained above, what you need to do to create your contracts is to extend the predefined base contract classes and override the `invoke` method as you like. For details, see [A Guide on How to Write a Good Contract](./how-to-write-contract.md).

Predefined contracts for common use cases are available through two abstracted data stores: HashStore and TableStore.

* HashStore provides interfaces for ensuring the authenticity of objects and collections, making it ideal for chain-of-custody and similar applications.
* TableStore offers an SQL-compatible interface for verifying table authenticity, enabling developers to build versatile, tamper-evident applications with familiar data models and interfaces.

For details, see [Get Started with ScalarDL HashStore](./getting-started-hashstore.md) and [Get Started with ScalarDL TableStore](./getting-started-tablestore.md).

## See also

To write your own contracts, see the following:

* [A Guide on How to Write a Good Contract](./how-to-write-contract.md)

To interact with ScalarDL components in your Java applications, see the following:

* [Write a ScalarDL Application in Java](./how-to-write-applications.md)

To use abstracted data stores for easy Ledger interaction without writing your own contracts, see the following:

* [Get Started with ScalarDL HashStore](./getting-started-hashstore.md)
* [Get Started with ScalarDL TableStore](./getting-started-tablestore.md)

To better understand the foundation of ScalarDL, see the following:

* [ScalarDL Design Document](./design.md)
* [ScalarDL Implementation](./implementation.md)
