---
type: Reference
title: Schema Importer
description: Schema Importer is a CLI tool for automatically configuring PostgreSQL. By using this tool, your PostgreSQL database can have identical database objects, such as namespaces and tables, as your ScalarDB instance.
resource: https://scalardb.scalar-labs.com/docs/3.15/scalardb-analytics-postgresql/schema-importer/
tags:
- scalardb
- v3.15
- phase:implement
- edition:community
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.15'
patch_version: 3.15.8
doc_id: scalardb-analytics-postgresql/schema-importer
lifecycle_phase: implement
editions:
- Community
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:02Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.15/scalardb-analytics-postgresql/schema-importer.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Schema Importer

Schema Importer is a CLI tool for automatically configuring PostgreSQL. By using this tool, your PostgreSQL database can have identical database objects, such as namespaces and tables, as your ScalarDB instance.

Schema Importer reads the ScalarDB configuration file, retrieves the schemas of the tables defined in ScalarDB, and creates the corresponding foreign data wrapper external tables and views in that order. For more information, refer to [Getting Started with ScalarDB Analytics with PostgreSQL](./getting-started.md).

## Build Schema Importer

You can build Schema Importer by using [Gradle](https://gradle.org/). To build Schema Importer, run the following command:

```console
./gradlew build
```

You may want to build a fat JAR file so that you can launch Schema Importer by using `java -jar`. To build the fat JAR, run the following command:

```console
./gradlew shadowJar
```

After you build the fat JAR, you can find the fat JAR file in the `app/build/libs/` directory.

## Run Schema Importer

To run Schema Importer by using the fat JAR file, run the following command:

```console
java -jar <PATH_TO_FAT_JAR_FILE>
```
Available options are as follows:

| Name                        | Required | Description                                                                                                                                 | Default                                    |
| --------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `--config`                  | **Yes**  | Path to the ScalarDB configuration file                                                                                                     |                                            |
| `--config-on-postgres-host` | No       | Path to the ScalarDB configuration file on the PostgreSQL-running host                                                                      | The same value as `--config` will be used. |
| `--namespace`, `-n`         | **Yes**  | Namespaces to import into the analytics instance. You can specify the `--namespace` option multiple times if you have two or more namespaces.    |                                            |
| `--host`                    | No       | PostgreSQL host                                                                                                                             | localhost                                  |
| `--port`                    | No       | PostgreSQL port                                                                                                                             | 5432                                       |
| `--database`                | No       | PostgreSQL port                                                                                                                             | postgres                                   |
| `--user`                    | No       | PostgreSQL user                                                                                                                             | postgres                                   |
| `--password`                | No       | PostgreSQL password                                                                                                                         |                                            |
| `--debug`                   | No       | Enable debug mode                                                                                                                           |                                            |

## Test Schema Importer

To test Schema Importer, run the following command:

```console
./gradlew test
```

## Build a Docker image of Schema Importer

To build a Docker image of Schema Importer, run the following command, replacing `<TAG>` with the tag version of Schema Importer that you want to use:

```console
docker build -t ghcr.io/scalar-labs/scalardb-analytics-postgresql-schema-importer:<TAG> -f ./app/Dockerfile .
```
