---
type: Reference
title: Requirements in the Underlining Databases of Scalar DB
description: This document explains the requirements in the underlining databases of Scalar DB to make Scalar DB applications work correctly.
resource: https://scalardb-community.scalar-labs.com/docs/3.4/requirements/
tags:
- scalardb-community
- v3.4
- phase:implement
- section:reference
- unmaintained
status: deprecated
product: scalardb-community
product_title: ScalarDB Community
version: '3.4'
doc_id: requirements
lifecycle_phase: implement
breadcrumb:
- Reference
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:10Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/versioned_docs/version-3.4/requirements.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# Requirements in the Underlining Databases of Scalar DB

This document explains the requirements in the underlining databases of Scalar DB to make Scalar DB applications work correctly.

## Cassandra (or Cassandra compatible databases)

Here are the requirements to make Scalar DB on Cassandra (or Cassandra compatible databases) work properly.

1. Durability is provided.
   1. In Cassandra, `commitlog_sync` in cassandra.yaml must be changed to `batch` or `group` from the default `periodic`.
2. (For Cassandra compatible databases) LWT is supported.

For the first, it is required since Scalar DB only provides Atomicity and Isolation properties of ACID and requests the underlining databases to provide Durability.
You can stil use `periodic`, but it is not recommended unless you know exactly what you are doing.

For the second, Scalar DB does not work on some Cassandra compatible databases such as [Amazon Keyspaces](https://aws.amazon.com/keyspaces/) that don't support LWT since `ConsensusCommit` transaction manager relies on linearizable operations of underlining databases to make transactions serializable.

If the above requirements are met, storage operations with `LINEARIZABLE` can provide linearizablity and transaction operations with `SERIALIZABLE` can provide strict serializability.

## JDBC databases

In Scalar DB on JDBC databases, you can't choose a consistency level (`LINEARIZABLE`, `SEQUENTIAL` or `EVENTUAL`) in your code with the `Operation.withConsistency()` method, and the consistency level depends on the setup of your JDBC database.
For example, when you have asynchronous read replicas in your setup and perform read operations against them, the consistency will be eventual because you can read stale data from the read replicas.
On the other hand, when you perform all operations against a single master instance, the consistency will be linearizable.
We recommend performing all operations/transactions against a single master instance (so that you can achieve linearizable) if you want to avoid caring consistency issues in your applications. Note that you can still use a read replica as a backup and standby even if you follow the recommendation.

If you strongly want to perform operations/transactions on read replicas, you can configure your application to perform read-write-mixed transactions against a master instance and read-only transactions against read replicas.
The resulting schedule would not be strict serializable (linearizable and serializable) but would be serializable.
