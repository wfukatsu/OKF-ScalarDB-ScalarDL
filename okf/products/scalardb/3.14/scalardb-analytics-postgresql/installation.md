---
type: Deployment Guide
title: How to Install ScalarDB Analytics with PostgreSQL in Your Local Environment by Using Docker
description: This document explains how to set up a local environment that runs ScalarDB Analytics with PostgreSQL using the multi-storage back-end of Cassandra, PostgreSQL, and DynamoDB local server using Docker Compose.
resource: https://scalardb.scalar-labs.com/docs/3.14/scalardb-analytics-postgresql/installation/
tags:
- scalardb
- v3.14
- phase:operate
- edition:community
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: scalardb-analytics-postgresql/installation
lifecycle_phase: operate
editions:
- Community
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:04Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.14/scalardb-analytics-postgresql/installation.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to Install ScalarDB Analytics with PostgreSQL in Your Local Environment by Using Docker

This document explains how to set up a local environment that runs ScalarDB Analytics with PostgreSQL using the multi-storage back-end of Cassandra, PostgreSQL, and DynamoDB local server using [Docker Compose](https://docs.docker.com/compose/).

## Prerequisites

- [Docker Engine](https://docs.docker.com/engine/) and [Docker Compose](https://docs.docker.com/compose/).

Follow the instructions on the Docker website according to your platform.

## Step 1. Clone the `scalardb-samples` repository

[scalardb-samples/scalardb-analytics-postgresql-sample](https://github.com/scalar-labs/scalardb-samples/tree/main/scalardb-analytics-postgresql-sample) repository is a project containing a sample configuration to set up ScalarDB Analytics with PostgreSQL.

Determine the location on your local machine where you want to run the scalardb-analytics-postgresql-sample app. Then, open Terminal, go to the location by using the `cd` command, and run the following commands:

```console
git clone https://github.com/scalar-labs/scalardb-samples.git
cd scalardb-samples/scalardb-analytics-postgresql-sample
```

## Step 2. Start up the ScalarDB Analytics with PostgreSQL services

The following command starts up the PostgreSQL instance that serves ScalarDB Analytics with PostgreSQL along with the back-end servers of Cassandra, PostgreSQL, and DynamoDB local in the Docker containers. When you first run the command, the required Docker images will be downloaded from the GitHub Container Registry.

```console
docker-compose up
```

If you want to run the containers in the background, add the `-d` (--detach) option:

```console
docker-compose up -d
```

If you already have your own ScalarDB database and want to use it as a back-end service, you can launch only the PostgreSQL instance without starting additional back-end servers in the container.

```console
docker-compose up analytics
```

## Step 3. Run your analytical queries

Now, you should have all the required services running. To run analytical queries, see [Getting Started with ScalarDB Analytics with PostgreSQL](./getting-started.md).

## Step 4. Shut down the ScalarDB Analytics with PostgreSQL services

To shut down the containers, do one of the following in Terminal, depending on how you:

- If you started the containers in the foreground, press Ctrl+C where `docker-compose` is running.
- If you started the containers in the background, run the following command.

```console
docker-compose down
```
