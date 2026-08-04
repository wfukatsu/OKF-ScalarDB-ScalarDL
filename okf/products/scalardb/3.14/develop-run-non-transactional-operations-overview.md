---
type: Development Guide
title: Run Non-Transactional Storage Operations Overview
description: ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use...
resource: https://scalardb.scalar-labs.com/docs/3.14/develop-run-non-transactional-operations-overview/
tags:
- scalardb
- v3.14
- phase:implement
- section:develop
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: develop-run-non-transactional-operations-overview
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Non-Transactional Storage Operations
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/develop-run-non-transactional-operations-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Run Non-Transactional Storage Operations Overview

ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use multiple, possibly diverse, databases.

ScalarDB can be configured to provide only the unified abstraction, without transaction capabilities, so that it only runs non-transactional operations on the underlying database and storage. Since ScalarDB in this configuration doesn't guarantee ACID across multiple operations, you can perform operations with better performance.

In this sub-category, you can learn how to run such non-transactional storage operations.

- Run Through the CRUD Interface
  - [Use the ScalarDB Core Library](./run-non-transactional-storage-operations-through-library.md)
  - [Use ScalarDB Cluster](./scalardb-cluster/run-non-transactional-storage-operations-through-scalardb-cluster.md)
- [Run Through the SQL Interface](./scalardb-cluster/run-non-transactional-storage-operations-through-sql-interface.md)
- [Run Through the Primitive CRUD Interface](./run-non-transactional-storage-operations-through-primitive-crud-interface.md)
