---
type: Development Guide
title: Run Non-Transactional Storage Operations Overview
description: ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use...
resource: https://scalardb.scalar-labs.com/docs/3.17/develop-run-non-transactional-operations-overview/
tags:
- scalardb
- v3.17
- phase:implement
- section:develop
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.4
doc_id: develop-run-non-transactional-operations-overview
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Advanced Configurations and Operations
- Run Single-Operation Transactions
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:51Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.17/develop-run-non-transactional-operations-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Run Non-Transactional Storage Operations Overview

ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use multiple, possibly diverse, databases.

ScalarDB can be configured to provide only the unified abstraction, without transaction capabilities, so that it only runs non-transactional operations on the underlying database and storage. Since ScalarDB in this configuration doesn't guarantee ACID across multiple operations, you can perform operations with better performance.
