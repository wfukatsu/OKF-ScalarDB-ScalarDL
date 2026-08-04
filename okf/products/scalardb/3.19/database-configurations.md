---
type: Reference
title: Configurations for the Underlying Databases of ScalarDB
description: This document explains how to configure the underlying databases of ScalarDB to make applications that use ScalarDB work correctly and efficiently.
resource: https://scalardb.scalar-labs.com/docs/latest/database-configurations/
tags:
- scalardb
- v3.19
- phase:implement
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.0
doc_id: database-configurations
lifecycle_phase: implement
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:47Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/docs/database-configurations.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Configurations for the Underlying Databases of ScalarDB

This document explains how to configure the underlying databases of ScalarDB to make applications that use ScalarDB work correctly and efficiently.

## General requirements for the underlying databases

ScalarDB requires each underlying database to provide certain capabilities to run transactions and analytics on the databases. This document explains the general requirements and how to configure each database to achieve the requirements.

### Transactions

ScalarDB requires each underlying database to provide at least the following capabilities to run transactions on the databases:

- Linearizable read and conditional mutations (write and delete) on a single database record.
- Durability of written database records.
- Ability to store arbitrary data beside application data in each database record.

### Analytics

ScalarDB requires each underlying database to provide the following capability to run analytics on the databases:

- Ability to return only committed records.

:::note

You need to have database accounts that have enough privileges to access the databases through ScalarDB since ScalarDB runs on the underlying databases not only for CRUD operations but also for performing operations like creating or altering schemas, tables, or indexes. ScalarDB basically requires a fully privileged account to access the underlying databases.

:::

## How to configure databases to achieve the general requirements

Select your database for details on how to configure it to achieve the general requirements.

**JDBC databases**

#### Transactions

- Use a single primary server or synchronized multi-primary servers for all operations (no read operations on read replicas that are asynchronously replicated from a primary database).
- Use read-committed or stricter isolation levels.

#### Analytics

- Use read-committed or stricter isolation levels.

**NoSQL databases**

Select your NoSQL database.

**Cassandra**

#### Transactions

- Use a single primary cluster for all operations (no read or write operations in non-primary clusters).
- Use `batch` or `group` for `commitlog_sync`.
- If you're using Cassandra-compatible databases, those databases must properly support lightweight transactions (LWT).

#### Analytics

- Not applicable. Cassandra always returns committed records, so there are no Cassandra-specific requirements.

**Cosmos DB for NoSQL**

#### Transactions

- Use a single primary region for all operations with `Strong` or `Bounded Staleness` consistency.

#### Analytics

- Not applicable. Cosmos DB always returns committed records, so there are no Cosmos DB–specific requirements.

**DynamoDB**

#### Transactions

- Use a single primary region for all operations. (No read and write operations on global tables in non-primary regions.)
  - There is no concept for primary regions in DynamoDB, so you must designate a primary region by yourself.

#### Analytics

- Not applicable. DynamoDB always returns committed records, so there are no DynamoDB-specific requirements.

**Object Storage**

#### Transactions

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
- For schema design recommendations specific to object storage, see [Database Adapters](./database-adapters.md#key-and-index-mapping-4).
