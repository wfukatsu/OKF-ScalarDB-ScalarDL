---
type: Deployment Guide
title: Back up an RDB in a Kubernetes environment
description: This guide explains how to create a backup of a single relational database (RDB) that ScalarDB or ScalarDL uses in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services...
resource: https://scalardb.scalar-labs.com/docs/3.18/scalar-kubernetes/BackupRDB/
tags:
- scalardb
- v3.18
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.18'
patch_version: 3.18.1
doc_id: scalar-kubernetes/BackupRDB
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:49Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.18/scalar-kubernetes/BackupRDB.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Back up an RDB in a Kubernetes environment

This guide explains how to create a backup of a single relational database (RDB) that ScalarDB or ScalarDL uses in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services provider.

If you have two or more RDBs that the [Multi-storage Transactions](https://scalardb.scalar-labs.com/docs/latest/multi-storage-transactions/) or [Two-phase Commit Transactions](https://scalardb.scalar-labs.com/docs/latest/two-phase-commit-transactions/) feature uses, you must follow the instructions in [Back up a NoSQL database in a Kubernetes environment](./BackupNoSQL.md) instead.

## Perform a backup

To perform backups, you should enable the automated backup feature available in the managed databases. By enabling this feature, you do not need to perform any additional backup operations. For details on the backup configurations in each managed database, see the following guides:

* [Set up a database for ScalarDB/ScalarDL deployment on AWS](./SetupDatabaseForAWS.md)
* [Set up a database for ScalarDB/ScalarDL deployment on Azure](./SetupDatabaseForAzure.md)

Because the managed RDB keeps backup data consistent from a transactions perspective, you can restore backup data to any point in time by using the point-in-time recovery (PITR) feature in the managed RDB.
