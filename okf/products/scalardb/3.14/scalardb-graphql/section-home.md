---
type: Development Guide
title: ScalarDB GraphQL Overview
description: ScalarDB GraphQL is an interface layer that allows client applications to communicate with ScalarDB Cluster by using GraphQL. It enables you to take advantage the benefits of GraphQL, such as flexible data retrieval and type safety, while...
resource: https://scalardb.scalar-labs.com/docs/3.14/scalardb-graphql/
tags:
- scalardb
- v3.14
- phase:implement
- section:develop
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: scalardb-graphql/index
lifecycle_phase: implement
breadcrumb:
- Develop
- Reference
- GraphQL Interface
editions:
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/scalardb-graphql/index.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB GraphQL Overview

ScalarDB GraphQL is an interface layer that allows client applications to communicate with ScalarDB Cluster by using GraphQL. It enables you to take advantage the benefits of GraphQL, such as flexible data retrieval and type safety, while benefiting from the transaction management and data access features in ScalarDB.

By using ScalarDB GraphQL, you can create GraphQL schemas automatically based on the ScalarDB schemas, perform CRUD operations, and execute complex transactions across multiple databases. The interface simplifies backend development by providing a unified querying mechanism, making it particularly useful for modern applications expecting advanced and responsive data interactions.

## Getting started with GraphQL in ScalarDB Cluster

ScalarDB GraphQL is designed to be intuitive and user-friendly, enabling developers to easily create GraphQL schemas automatically based on the ScalarDB schemas and interact with the underlying databases.

For details on how to set up ScalarDB Cluster with GraphQL support, see [Getting Started with ScalarDB Cluster GraphQL](../scalardb-cluster/getting-started-with-scalardb-cluster-graphql.md).

## Transactions with a two-phase commit

ScalarDB GraphQL supports executing transactions with a two-phase commit interface. By using the two-phase commit interface, you can execute a transaction that spans multiple processes/applications (for example, microservices applications).

For details on how to execute transactions by using the two-phase commit interface in ScalarDB GraphQL, see [How to Run Two-Phase Commit Transactions](./how-to-run-two-phase-commit-transaction.md).
