---
type: Operations Guide
title: Back Up and Restore Databases
description: This guide explains how to back up and restore databases that are used by ScalarDL through ScalarDB.
resource: https://scalardl.scalar-labs.com/docs/3.10/manage-backup-and-restore-overview/
tags:
- scalardl
- v3.10
- phase:operate
- section:manage
- edition:community
- edition:enterprise
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.10'
patch_version: 3.10.5
doc_id: manage-backup-and-restore-overview
lifecycle_phase: operate
breadcrumb:
- Manage
- Back Up and Restore
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:03Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.10/manage-backup-and-restore-overview.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Back Up and Restore Databases

This guide explains how to back up and restore databases that are used by ScalarDL through ScalarDB.

:::note

ScalarDL uses ScalarDB in its internal to access backend databases. So, you must back up and restore databases that are managed by ScalarDB if you want to back up and restore ScalarDL.

:::

## Basic guidelines to back up and restore databases

Before performing a backup, be sure to read [A Guide on How to Backup and Restore Data in ScalarDL](./backup-restore.md).

## Back up databases when using ScalarDB in a Kubernetes environment

For details on how to back up databases in a Kubernetes environment, see [Back up a NoSQL database in a Kubernetes environment](./scalar-kubernetes/BackupNoSQL.md).

## Restore databases when using ScalarDB in a Kubernetes environment

For details on how to restore databases in a Kubernetes environment, see [Restore databases in a Kubernetes environment](./scalar-kubernetes/RestoreDatabase.md).
