---
type: Operations Guide
title: Back Up and Restore Databases
description: This guide explains how to back up and restore databases that are used by ScalarDB.
resource: https://scalardb.scalar-labs.com/docs/3.14/manage-backup-and-restore/
tags:
- scalardb
- v3.14
- phase:operate
- section:manage
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: manage-backup-and-restore
lifecycle_phase: operate
breadcrumb:
- Manage
- Back Up and Restore
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/manage-backup-and-restore.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Back Up and Restore Databases

This guide explains how to back up and restore databases that are used by ScalarDB.

## Basic guidelines to back up and restore databases

Before performing a backup, be sure to read [How to Back Up and Restore Databases Used Through ScalarDB](./backup-restore.md).

## Back up databases when using ScalarDB in a Kubernetes environment

For details on how to back up databases in a Kubernetes environment, see [Back up a NoSQL database in a Kubernetes environment](./scalar-kubernetes/BackupNoSQL.md).

## Restore databases when using ScalarDB in a Kubernetes environment

For details on how to restore databases in a Kubernetes environment, see [Restore databases in a Kubernetes environment](./scalar-kubernetes/RestoreDatabase.md).
