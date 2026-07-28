---
type: Reference
title: ScalarDL Schema Loader
description: A Docker image that loads the database schemas of ScalarDL using Schema Tool for ScalarDB.
resource: https://scalardl.scalar-labs.com/docs/latest/schema-loader/
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
doc_id: schema-loader
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/schema-loader.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# ScalarDL Schema Loader

A Docker image that loads the database schemas of ScalarDL using [Schema Tool for ScalarDB](https://scalardb.scalar-labs.com/docs/latest/schema-loader).

## How to Run

### For Cosmos DB

```console
docker run --rm [--env SCHEMA_TYPE=auditor] ghcr.io/scalar-labs/scalardl-schema-loader:<version> \
  --cosmos -h <YOUR_ACCOUNT_URI> -p <YOUR_ACCOUNT_PASSWORD> [-r BASE_RESOURCE_UNIT]
```

### For DynamoDB

```console
docker run --rm [--env SCHEMA_TYPE=auditor] ghcr.io/scalar-labs/scalardl-schema-loader:<version> \
  --dynamo --region <REGION> -u <ACCESS_KEY_ID> -p <SECRET_ACCESS_KEY> [-r BASE_RESOURCE_UNIT]
```

### For Cassandra

```console
docker run --rm [--env SCHEMA_TYPE=auditor] ghcr.io/scalar-labs/scalardl-schema-loader:<version> \
  --cassandra -h <CASSANDRA_IP> -u <CASSNDRA_USER> -p <CASSANDRA_PASSWORD> [-n <NETWORK_STRATEGY> -R <REPLICATION_FACTOR>]
```

### For using a config file

* For Ledger
```console
docker run --rm \
  -v <PROPERTIES_FILE_PATH>:/scalardl-schema-loader/database.properties \
  ghcr.io/scalar-labs/scalardl-schema-loader:<version> \
  --config database.properties --coordinator [<SOME_OPTIONS> [, ...]]
```

* For Auditor
```console
docker run --rm --env SCHEMA_TYPE=auditor \
  -v <PROPERTIES_FILE_PATH>:/scalardl-schema-loader/database.properties \
  ghcr.io/scalar-labs/scalardl-schema-loader:<version> \
  --config database.properties [<SOME_OPTIONS> [, ...]]
```
