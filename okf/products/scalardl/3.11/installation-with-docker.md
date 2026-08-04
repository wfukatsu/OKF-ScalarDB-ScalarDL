---
type: Deployment Guide
title: How to Install ScalarDL in Your Local Environment with Docker
description: This document shows how to set up a local environment that runs ScalarDL along with the back-end Cassandra server using Docker Compose.
resource: https://scalardl.scalar-labs.com/docs/3.11/installation-with-docker/
tags:
- scalardl
- v3.11
- phase:operate
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.3
doc_id: installation-with-docker
lifecycle_phase: operate
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:02Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.11/installation-with-docker.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# How to Install ScalarDL in Your Local Environment with Docker

This document shows how to set up a local environment that runs ScalarDL along with the back-end Cassandra server using [Docker Compose](https://docs.docker.com/compose/).

:::warning

You need to have a license key (trial license or commercial license) to use ScalarDL. If you don't have a license key, please [contact us](https://www.scalar-labs.com/contact-us).

:::

## Prerequisites

- [Docker](https://www.docker.com/get-started/) 20.10 or later with [Docker Compose](https://docs.docker.com/compose/install/) V2 or later

    Follow the instructions on the Docker website according to your platform.

## Clone the scalardl-samples repository

The [scalar-labs/scalardl-samples](https://github.com/scalar-labs/scalardl-samples) repository includes sample applications for you to start using ScalarDL instantly.

1. In Terminal, determine the location on your local machine where you want to run the `scalardl-samples` app. Then, clone the `scalardl-samples` repository.

```console
git clone https://github.com/scalar-labs/scalardl-samples.git
```

1. Go to the `scalardl-samples` directory.

```console
cd scalardl-samples
```

## Set your license key

**ScalarDL Ledger only**

### Set your license key for ScalarDL Ledger

   You must set your license key for ScalarDL Ledger. In the `docker-compose.yml` file, please replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```yaml
services:
  scalardl-ledger:
    environment:
      - SCALAR_DL_LICENSING_LICENSE_KEY={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
```

**ScalarDL Auditor mode**

### Set your license key for ScalarDL Ledger

   You must set your license key for ScalarDL Ledger. In the `docker-compose.yml` file, please replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```yaml
services:
  scalardl-ledger:
    environment:
      - SCALAR_DL_LICENSING_LICENSE_KEY={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Ledger","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
```

### Set your license key for ScalarDL Auditor

   You must set your license key for ScalarDL Auditor. In the `docker-compose-auditor.yml` file, please replace `<SET_YOUR_LICENSE_KEY>` with your license key. For example:

```yaml
services:
  scalardl-auditor:
    environment:
      - SCALAR_DL_LICENSING_LICENSE_KEY={"organization_name":"XXXXXXXX","expiration_date_time":"YYYY-MM-DDTHH:mm:SS+TIMEZONE","product_name":"ScalarDL Auditor","product_version":N,"license_type":"trial","signature":"XXXXXXXX"}
```

## Set the certificate file for checking the license key

:::note

If you have a trial license, you can skip this step and [start up ScalarDL](#start-up-scalardl).

:::

**ScalarDL Ledger only**

In this step, you must set the certificate file for ScalarDL Ledger.

### Set the certificate file for ScalarDL Ledger

If you have a commercial license, you must update the `docker-compose.yml` file as follows:

   - Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ./fixture/ledger.properties.tmpl:/scalar/ledger/ledger.properties.tmpl
      - ./fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ./fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

   - After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ./fixture/ledger.properties.tmpl:/scalar/ledger/ledger.properties.tmpl
      # - ./fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ./fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

**ScalarDL Auditor mode**

In this step, you must set the certificate file for ScalarDL Ledger and ScalarDL Auditor.

### Set the certificate file for ScalarDL Ledger

If you have a commercial license, you must update the `docker-compose.yml` file as follows:

   - Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ./fixture/ledger.properties.tmpl:/scalar/ledger/ledger.properties.tmpl
      - ./fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ./fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

   - After changing the certificate file path:

```yaml
services:
  scalardl-ledger:
    volumes:
      - ./fixture/ledger-key.pem:/scalar/ledger-key.pem
      - ./fixture/ledger.properties.tmpl:/scalar/ledger/ledger.properties.tmpl
      # - ./fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ./fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

### Set the certificate file for ScalarDL Auditor

If you have a commercial license, you must update the `docker-compose-auditor.yml` file as follows:

   - Before changing the certificate file path (default configuration):

```yaml
services:
  scalardl-auditor:
    volumes:
      - ./fixture/auditor.pem:/scalar/auditor.pem
      - ./fixture/auditor-key.pem:/scalar/auditor-key.pem
      - ./fixture/auditor.properties.tmpl:/scalar/auditor/auditor.properties.tmpl
      - ./fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      # - ./fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

   - After changing the certificate file path:

```yaml
services:
  scalardl-auditor:
    volumes:
      - ./fixture/auditor.pem:/scalar/auditor.pem
      - ./fixture/auditor-key.pem:/scalar/auditor-key.pem
      - ./fixture/auditor.properties.tmpl:/scalar/auditor/auditor.properties.tmpl
      # - ./fixture/trial-license-cert.pem:/scalar/license-cert.pem
      # If you have a commercial license key, you must use `commercial-license-cert.pem` instead of `trial-license-cert.pem`.
      - ./fixture/commercial-license-cert.pem:/scalar/license-cert.pem
```

## Start up ScalarDL

**ScalarDL Ledger only**

  The following command starts up ScalarDL Ledger, along with the backend Cassandra server in the Docker containers.

:::note

The first time you run this command, the required Docker images will be downloaded from GitHub Container Registry.

:::

```console
docker compose up -d
```

**ScalarDL Auditor mode**

  The following command starts up ScalarDL Ledger and ScalarDL Auditor, along with the backend Cassandra server in the Docker containers.

:::note

The first time you run this command, the required Docker images will be downloaded from GitHub Container Registry.

:::

```console
docker compose -f docker-compose.yml -f docker-compose-auditor.yml up -d
```

## Shut down ScalarDL

To shut down the containers, run the following command.

**ScalarDL Ledger only**

```console
docker compose down -v
```

**ScalarDL Auditor mode**

```console
docker compose -f docker-compose.yml -f docker-compose-auditor.yml down -v
```
