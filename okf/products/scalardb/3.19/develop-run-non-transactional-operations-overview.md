---
type: Documentation Page
title: Run Non-Transactional Storage Operations Overview
description: ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use...
resource: https://scalardb.scalar-labs.com/docs/latest/develop-run-non-transactional-operations-overview/
tags:
- scalardb
- v3.19
- phase:implement
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.1
doc_id: develop-run-non-transactional-operations-overview
lifecycle_phase: implement
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-09-11T05:23:06Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/c882c4103fe6e0aedff74e7afa67c2587a78ec9b/docs/develop-run-non-transactional-operations-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-09-09T05:43:01Z'
---

# Run Non-Transactional Storage Operations Overview

ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use multiple, possibly diverse, databases.

ScalarDB can be configured to provide only the unified abstraction, without transaction capabilities, so that it only runs non-transactional operations on the underlying database and storage. Since ScalarDB in this configuration doesn't guarantee ACID across multiple operations, you can perform operations with better performance.
