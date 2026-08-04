---
type: Development Guide
title: ScalarDL Schema Loader
description: A Docker image that loads the database schemas of ScalarDL using Schema Tool for ScalarDB.
resource: https://scalardl.scalar-labs.com/docs/3.12/schema-loader/
tags:
- scalardl
- v3.12
- phase:implement
- section:develop
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.12'
patch_version: 3.12.3
doc_id: schema-loader
lifecycle_phase: implement
breadcrumb:
- Develop
- Reference
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:01Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.12/schema-loader.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
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
