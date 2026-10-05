---
type: Development Guide
title: ScalarDL Schema Loader
description: A Docker image that loads the database schemas of ScalarDL using Schema Tool for ScalarDB.
resource: https://scalardl.scalar-labs.com/docs/3.11/schema-loader/
tags:
- scalardl
- v3.11
- phase:implement
- section:develop
- edition:community
- edition:enterprise
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.4
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
  at: '2026-10-05T04:25:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/5a0ce6d90acfadea3a0e493f961c676890e2cc1a/versioned_docs/version-3.11/schema-loader.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-10-05T02:43:25Z'
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
