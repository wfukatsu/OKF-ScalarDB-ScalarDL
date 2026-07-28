---
type: Development Guide
title: Develop Overview
description: In this category, you can follow guides to help you become more familiar with ScalarDB, specifically with how to run transactions, analytical queries, and non-transactional storage operations.
resource: https://scalardb-community.scalar-labs.com/docs/3.12/develop-overview/
tags:
- scalardb-community
- v3.12
- phase:implement
- section:develop
status: stable
product: scalardb-community
product_title: ScalarDB Community
version: '3.12'
doc_id: develop-overview
lifecycle_phase: implement
breadcrumb:
- Develop
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:09Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/versioned_docs/version-3.12/develop-overview.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# Develop Overview

In this category, you can follow guides to help you become more familiar with ScalarDB, specifically with how to run transactions, analytical queries, and non-transactional storage operations.

## Run transactions

In this sub-category, you can learn how to model your data based on the ScalarDB data model and create schemas. Then, you can learn how to run transactions through the ScalarDB core library and ScalarDB Cluster, a gRPC server that wraps the core library.

You can also learn how to create correct, secure, and well-performing ScalarDB-based applications.

## Run analytical queries

In this section, you can learn how to set up and configure ScalarDB Analytics, an analytics component of ScalarDB. Then, you run analytical queries over the databases you write through ScalarDB transactions.

## Run non-transactional storage operations

ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use multiple, possibly diverse, databases.

ScalarDB can be configured to provide only the unified abstraction, without transaction capabilities, so that it only runs non-transactional operations on the underlying database and storage. Since ScalarDB doesn't guarantee ACID across multiple operations, you can perform operations with better performance.

In this sub-category, you can learn how to run such non-transactional storage operations.
