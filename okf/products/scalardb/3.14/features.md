---
type: Concept
title: ScalarDB Features
description: This document briefly explains which features are available in which editions of ScalarDB.
resource: https://scalardb.scalar-labs.com/docs/3.14/features/
tags:
- scalardb
- v3.14
- phase:design
- section:about-scalardb
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: features
lifecycle_phase: design
breadcrumb:
- About ScalarDB
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/features.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB Features

This document briefly explains which features are available in which editions of ScalarDB.

|                                                                                                                                     | ScalarDB Core (Community) | ScalarDB Cluster (Enterprise Standard) | ScalarDB Cluster (Enterprise Premium)                      | ScalarDB Analytics (Enterprise) |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------|----------------------------------------|------------------------------------------------------------|---------------------------------|
| [Transaction processing across databases with primitive interfaces](./getting-started-with-scalardb.md)                              | ✅                        | ✅                                     | ✅                                                         | –                               |
| [Clustering](./scalardb-cluster/developer-guide-for-scalardb-cluster-with-java-api.md)                                               | -                         | ✅                                     | ✅                                                         | –                               |
| [Non-transactional storage operations](./develop-run-non-transactional-operations-overview.md)                                       | –                         | ✅ (3.14+)                             | ✅ (3.14+)                                                 | –                               |
| [Authentication/authorization](./scalardb-cluster/scalardb-auth-with-sql.md)                                                         | –                         | ✅                                     | ✅                                                         | –                               |
| [Encryption](./scalardb-cluster/encrypt-data-at-rest.md)                                                                             | –                         | –                                      | ✅ (3.14+)                                                 | –                               |
| [SQL interface (SQL API, JDBC, Spring Data JDBC, and LINQ)](./scalardb-sql/section-home.md)                                                 | –                         | –                                      | ✅                                                         | –                               |
| [GraphQL interface](./scalardb-graphql/section-home.md)                                                                                     | –                         | –                                      | ✅                                                         | –                               |
| [Analytical query processing across ScalarDB-managed data sources](./scalardb-samples/scalardb-analytics-spark-sample/README.md)     | –                         | –                                      | –                                                          | ✅ (3.14+)                      |
