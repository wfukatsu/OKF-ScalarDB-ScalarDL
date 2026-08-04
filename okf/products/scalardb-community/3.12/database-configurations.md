---
type: Reference
title: Configurations for the Underlying Databases of ScalarDB
description: This document explains how to configure the underlying databases of ScalarDB to make applications that use ScalarDB work correctly and efficiently.
resource: https://scalardb-community.scalar-labs.com/docs/3.12/database-configurations/
tags:
- scalardb-community
- v3.12
- phase:implement
status: stable
product: scalardb-community
product_title: ScalarDB Community
version: '3.12'
doc_id: database-configurations
lifecycle_phase: implement
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:04Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/versioned_docs/version-3.12/database-configurations.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
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

**DynamoDB**

#### Transactions

- Use a single primary region for all operations. (No read and write operations on global tables in non-primary regions.)
  - There is no concept for primary regions in DynamoDB, so you must designate a primary region by yourself.

#### Analytics

- Not applicable. DynamoDB always returns committed records, so there are no DynamoDB-specific requirements.

**Cosmos DB for NoSQL**

#### Transactions

- Use a single primary region for all operations with `Strong` or `Bounded Staleness` consistency.

#### Analytics

- Not applicable. Cosmos DB always returns committed records, so there are no Cosmos DB–specific requirements.

**Cassandra**

#### Transactions

- Use a single primary cluster for all operations (no read or write operations in non-primary clusters).
- Use `batch` or `group` for `commitlog_sync`.
- If you're using Cassandra-compatible databases, those databases must properly support lightweight transactions (LWT).

#### Analytics

- Not applicable. Cassandra always returns committed records, so there are no Cassandra-specific requirements.

## Recommendations

Properly configuring each underlying database of ScalarDB for high performance and high availability is recommended. The following recommendations include some knobs and configurations to update.

:::note

ScalarDB can be seen as an application of underlying databases, so you may want to try updating other knobs and configurations that are commonly used to improve efficiency.

:::

**JDBC databases**

- Use read-committed isolation for better performance.
- Follow the performance optimization best practices for each database. For example, increasing the buffer size (for example, `shared_buffers` in PostgreSQL) and increasing the number of connections (for example, `max_connections` in PostgreSQL) are usually recommended for better performance.

**DynamoDB**

- Increase the number of read capacity units (RCUs) and write capacity units (WCUs) for high throughput.
- Enable point-in-time recovery (PITR).

:::note

Since DynamoDB stores data in multiple availability zones by default, you don’t need to adjust any configurations to improve availability.

:::

**Cosmos DB for NoSQL**

- Increase the number of Request Units (RUs) for high throughput.
- Enable point-in-time restore (PITR).
- Enable availability zones.

**Cassandra**

- Increase `concurrent_reads` and `concurrent_writes` for high throughput. For details, see the official Cassandra documentation about [`concurrent_writes`](https://cassandra.apache.org/doc/stable/cassandra/configuration/cass_yaml_file.html#concurrent_writes).
