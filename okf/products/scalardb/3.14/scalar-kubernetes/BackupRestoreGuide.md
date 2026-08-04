---
type: Deployment Guide
title: Back up and restore ScalarDB or ScalarDL data in a Kubernetes environment
description: This guide explains how to backup and restore ScalarDB or ScalarDL data in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services provider as the backend database for...
resource: https://scalardb.scalar-labs.com/docs/3.14/scalar-kubernetes/BackupRestoreGuide/
tags:
- scalardb
- v3.14
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: scalar-kubernetes/BackupRestoreGuide
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/scalar-kubernetes/BackupRestoreGuide.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Back up and restore ScalarDB or ScalarDL data in a Kubernetes environment

This guide explains how to backup and restore ScalarDB or ScalarDL data in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services provider as the backend database for ScalarDB or ScalarDL. The following is a list of the managed databases that this guide assumes you might be using:

* NoSQL: does not support transactions
   * Amazon DynamoDB
   * Azure Cosmos DB for NoSQL
* Relational database (RDB): supports transactions
   * Amazon RDS
* MySQL
* Oracle
* PostgreSQL
* SQL Server
   * Amazon Aurora
* MySQL
* PostgreSQL
   * Azure Database
* MySQL
* PostgreSQL

For details on how to back up and restore databases used with ScalarDB in a transactionally consistent way, see [A Guide on How to Backup and Restore Databases Used Through ScalarDB](https://scalardb.scalar-labs.com/docs/latest/backup-restore/).

## Perform a backup

### Confirm the type of database and number of databases you are using

How you perform backup and restore depends on the type of database (NoSQL or RDB) and the number of databases you are using.

#### NoSQL or multiple databases

If you are using a NoSQL database, or if you have two or more databases that the [Multi-storage Transactions](https://scalardb.scalar-labs.com/docs/latest/multi-storage-transactions/) or [Two-phase Commit Transactions](https://scalardb.scalar-labs.com/docs/latest/two-phase-commit-transactions/) feature uses, please see [Back up a NoSQL database in a Kubernetes environment](./BackupNoSQL.md) for details on how to perform a backup.

#### Single RDB

If you are using a single RDB, please see [Back up an RDB in a Kubernetes environment](./BackupRDB.md) for details on how to perform a backup.

If you have two or more RDBs that the [Multi-storage Transactions](https://scalardb.scalar-labs.com/docs/latest/multi-storage-transactions/) or [Two-phase Commit Transactions](https://scalardb.scalar-labs.com/docs/latest/two-phase-commit-transactions/) feature uses, you must follow the instructions in [Back up a NoSQL database in a Kubernetes environment](./BackupNoSQL.md) instead.

## Restore a database

For details on how to restore data from a managed database, please see [Restore databases in a Kubernetes environment](./RestoreDatabase.md).
