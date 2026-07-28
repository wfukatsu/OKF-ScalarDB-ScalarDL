---
type: Tutorial
title: Quickstart Overview
description: In this category, you can follow quickstart tutorials for how to get started with running transactions and queries through ScalarDB.
resource: https://scalardb.scalar-labs.com/docs/3.14/quickstart-overview/
tags:
- scalardb
- v3.14
- phase:implement
- section:quickstart
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: quickstart-overview
lifecycle_phase: implement
breadcrumb:
- Quickstart
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:04Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.14/quickstart-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Quickstart Overview

In this category, you can follow quickstart tutorials for how to get started with running transactions and queries through ScalarDB.

## Try running transactions through the ScalarDB Core library

In this sub-category, you can follow tutorials on how to run ACID transactions through the ScalarDB Core library, which is publicly available under the Apache 2 License.

For an overview of this sub-category, see [ScalarDB Core Quickstart Overview](./quickstart-scalardb-core-overview.md).

## Try running transactions through ScalarDB Cluster

In this sub-category, you can see tutorials on how to run ACID transactions through ScalarDB Cluster, which is a [gRPC](https://grpc.io/) server that wraps the ScalarDB Core library.

For an overview of this sub-category, see [ScalarDB Cluster Quickstart Overview](./quickstart-scalardb-cluster-overview.md).

:::note

ScalarDB Cluster is available only in the Enterprise edition.

:::

## Try running analytical queries through ScalarDB Analytics

In this sub-category, you can see tutorials on how to run analytical queries over the databases that you write through ScalarDB by using a component called ScalarDB Analytics. ScalarDB Analytics targets both ScalarDB-managed databases, which are updated through ScalarDB transactions, and non-ScalarDB-managed databases.

For an overview of this sub-category, see [ScalarDB Analytics Quickstart Overview](./quickstart-scalardb-analytics-overview.md).

:::note

ScalarDB Analytics with Spark is in public preview.

:::
