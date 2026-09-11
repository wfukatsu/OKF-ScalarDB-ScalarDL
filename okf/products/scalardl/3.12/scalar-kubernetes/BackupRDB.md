---
type: Deployment Guide
title: Back up an RDB in a Kubernetes environment
description: This guide explains how to create a backup of a single relational database (RDB) that ScalarDB or ScalarDL uses in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services...
resource: https://scalardl.scalar-labs.com/docs/3.12/scalar-kubernetes/BackupRDB/
tags:
- scalardl
- v3.12
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardl
product_title: ScalarDL
version: '3.12'
patch_version: 3.12.3
doc_id: scalar-kubernetes/BackupRDB
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-24T00:15:44Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/db1535c35d0f746c5b5d8d9772f54afa0c709a34/versioned_docs/version-3.12/scalar-kubernetes/BackupRDB.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-20T15:35:18Z'
---

# Back up an RDB in a Kubernetes environment

This guide explains how to create a backup of a single relational database (RDB) that ScalarDB or ScalarDL uses in a Kubernetes environment. Please note that this guide assumes that you are using a managed database from a cloud services provider.

If you have two or more RDBs that the [Multi-storage Transactions](https://scalardb.scalar-labs.com/docs/latest/multi-storage-transactions/) or [Two-phase Commit Transactions](https://scalardb.scalar-labs.com/docs/latest/two-phase-commit-transactions/) feature uses, you must follow the instructions in [Back up a NoSQL database in a Kubernetes environment](./BackupNoSQL.md) instead.

## Perform a backup

To perform backups, you should enable the automated backup feature available in the managed databases. By enabling this feature, you do not need to perform any additional backup operations. For details on the backup configurations in each managed database, see the following guides:

* [Set up a database for ScalarDB/ScalarDL deployment on AWS](./SetupDatabaseForAWS.md)
* [Set up a database for ScalarDB/ScalarDL deployment on Azure](./SetupDatabaseForAzure.md)

Because the managed RDB keeps backup data consistent from a transactions perspective, you can restore backup data to any point in time by using the point-in-time recovery (PITR) feature in the managed RDB.
