---
type: Reference
title: ScalarDL Schema Loader
description: A Docker image that loads the database schemas of ScalarDL using Schema Tool for ScalarDB.
resource: https://scalardl.scalar-labs.com/docs/latest/schema-loader/
tags:
- scalardl
- v3.14
- phase:implement
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.14'
patch_version: 3.14.1
doc_id: schema-loader
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-10-05T04:25:29Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/5a0ce6d90acfadea3a0e493f961c676890e2cc1a/docs/schema-loader.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-10-05T02:43:25Z'
---

# ScalarDL Schema Loader

A Docker image that loads the database schemas of ScalarDL using [Schema Tool for ScalarDB](https://scalardb.scalar-labs.com/docs/latest/schema-loader).

## How to Run

### For Cosmos DB

Run the following command, replacing `<X.Y.Z>` with the version of ScalarDL Schema Loader that you want to use and the contents in the other angle brackets as described:

```console
docker run --rm [--env SCHEMA_TYPE=auditor] ghcr.io/scalar-labs/scalardl-schema-loader:<X.Y.Z> \
  --cosmos -h <YOUR_ACCOUNT_URI> -p <YOUR_ACCOUNT_PASSWORD> [-r BASE_RESOURCE_UNIT]
```

### For DynamoDB

Run the following command, replacing `<X.Y.Z>` with the version of ScalarDL Schema Loader that you want to use and the contents in the other angle brackets as described:

```console
docker run --rm [--env SCHEMA_TYPE=auditor] ghcr.io/scalar-labs/scalardl-schema-loader:<X.Y.Z> \
  --dynamo --region <REGION> -u <ACCESS_KEY_ID> -p <SECRET_ACCESS_KEY> [-r BASE_RESOURCE_UNIT]
```

### For Cassandra

Run the following command, replacing `<X.Y.Z>` with the version of ScalarDL Schema Loader that you want to use and the contents in the other angle brackets as described:

```console
docker run --rm [--env SCHEMA_TYPE=auditor] ghcr.io/scalar-labs/scalardl-schema-loader:<X.Y.Z> \
  --cassandra -h <CASSANDRA_IP> -u <CASSNDRA_USER> -p <CASSANDRA_PASSWORD> [-n <NETWORK_STRATEGY> -R <REPLICATION_FACTOR>]
```

### For using a config file

* For Ledger

  Run the following command, replacing `<X.Y.Z>` with the version of ScalarDL Schema Loader that you want to use and the contents in the other angle brackets as described:

```console
docker run --rm \
  -v <PROPERTIES_FILE_PATH>:/scalardl-schema-loader/database.properties \
  ghcr.io/scalar-labs/scalardl-schema-loader:<X.Y.Z> \
  --config database.properties --coordinator [<SOME_OPTIONS> [, ...]]
```

* For Auditor

  Run the following command, replacing `<X.Y.Z>` with the version of ScalarDL Schema Loader that you want to use and the contents in the other angle brackets as described:

```console
docker run --rm --env SCHEMA_TYPE=auditor \
  -v <PROPERTIES_FILE_PATH>:/scalardl-schema-loader/database.properties \
  ghcr.io/scalar-labs/scalardl-schema-loader:<X.Y.Z> \
  --config database.properties [<SOME_OPTIONS> [, ...]]
```
