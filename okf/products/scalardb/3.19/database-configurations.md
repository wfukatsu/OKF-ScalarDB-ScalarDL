---
type: Development Guide
title: Configure Databases for ScalarDB
description: This document explains how to configure the underlying databases of ScalarDB to make applications that use ScalarDB work correctly and efficiently.
resource: https://scalardb.scalar-labs.com/docs/3.19/database-configurations/
tags:
- scalardb
- v3.19
- phase:implement
- section:develop
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.1
doc_id: database-configurations
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-10-31T09:32:46Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/e492bf010d9ca2699301d485735f6b13d0dec7fa/versioned_docs/version-3.19/database-configurations.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-10-30T13:58:08Z'
---

# Configure Databases for ScalarDB

This document explains how to configure the underlying databases of ScalarDB to make applications that use ScalarDB work correctly and efficiently.

## General requirements for the underlying databases

ScalarDB requires each underlying database to provide certain capabilities to run transactions on the databases. This document explains the general requirements and how to configure each database to achieve the requirements.

ScalarDB requires each underlying database to provide at least the following capabilities to run transactions on the databases:

- Linearizable read and conditional mutations (write and delete) on a single database record.
- Durability of written database records.
- Ability to store arbitrary data beside application data in each database record.

## Configure databases to achieve the general requirements

Select your database for details on how to configure it to achieve the general requirements.

**JDBC databases**

- Use a single primary server or synchronized multi-primary servers for all operations (no read operations on read replicas that are asynchronously replicated from a primary database).
- Use read-committed or stricter isolation levels.

**NoSQL databases**

Select your NoSQL database.

**Cassandra**

- Use a single primary cluster for all operations (no read or write operations in non-primary clusters).
- Use `batch` or `group` for `commitlog_sync`.
- If you're using Cassandra-compatible databases, those databases must properly support lightweight transactions (LWT).

**Cosmos DB for NoSQL**

- Use a single primary region for all operations with `Strong` or `Bounded Staleness` consistency.

**DynamoDB**

- Use a single primary region for all operations. (No read and write operations on global tables in non-primary regions.)
  - There is no concept for primary regions in DynamoDB, so you must designate a primary region by yourself.

**Object Storage**

- Use a single region for all operations. For Blob Storage, use a single primary region.
- Choose the following storage classes or access tiers for each storage:
- **S3**: [S3 Standard](https://aws.amazon.com/s3/storage-classes/)
- **Blob Storage**: [Standard general-purpose v2, Hot tier](https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview)
- **Cloud Storage**: [Standard storage](https://docs.cloud.google.com/storage/docs/storage-classes#standard)

:::note

Other storage classes or access tiers can be used, but the ones listed above are verified and supported.

:::

## Recommendations

Properly configuring each underlying database of ScalarDB for high performance and high availability is recommended. The following recommendations include some knobs and configurations to update.

:::note

ScalarDB can be seen as an application of underlying databases, so you may want to try updating other knobs and configurations that are commonly used to improve efficiency.

:::

**JDBC databases**

- Use read-committed isolation for better performance.
- Follow the performance optimization best practices for each database. For example, increasing the buffer size (for example, `shared_buffers` in PostgreSQL) and increasing the number of connections (for example, `max_connections` in PostgreSQL) are usually recommended for better performance.

**NoSQL databases**

Select your NoSQL database.

**Cassandra**

- Increase `concurrent_reads` and `concurrent_writes` for high throughput. For details, see the official Cassandra documentation about [`concurrent_writes`](https://cassandra.apache.org/doc/stable/cassandra/configuration/cass_yaml_file.html#concurrent_writes).

**Cosmos DB for NoSQL**

- Increase the number of Request Units (RUs) for high throughput.
- Enable point-in-time restore (PITR).
- Enable availability zones.

**DynamoDB**

- Increase the number of read capacity units (RCUs) and write capacity units (WCUs) for high throughput.
- Enable point-in-time recovery (PITR).

:::note

Since DynamoDB stores data in multiple availability zones by default, you don't need to adjust any configurations to improve availability.

:::

**Object Storage**

- Configure a lifecycle rule to delete incomplete multipart uploads as described in [Configuring a bucket lifecycle configuration to delete incomplete multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html) when using S3.
- For schema design recommendations specific to object storage, see [Key and index mapping for the object storage adapter](./database-adapters.md#key-and-index-mapping-4).
