---
type: Concept
title: ScalarDB Features
description: This document briefly explains which features are available in which editions of ScalarDB.
resource: https://scalardb.scalar-labs.com/docs/latest/features/
tags:
- scalardb
- v3.19
- phase:design
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.1
doc_id: features
lifecycle_phase: design
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-09-14T03:42:14Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/45b362692765eeed47d41bf36b23f6e7c007a55f/docs/features.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-09-11T06:55:58Z'
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
| [Attribute-based access control](./scalardb-cluster/authorize-with-abac.md)                                                          | –                         | –                                      | ✅ (3.15+) (Enterprise Premium Option*, Public Preview) | –                               |
| [SQL interface (SQL API, JDBC, Spring Data JDBC, and LINQ)](./scalardb-sql/section-home.md)                                                 | –                         | –                                      | ✅                                                         | –                               |
| [GraphQL interface](./scalardb-graphql/section-home.md)                                                                                     | –                         | –                                      | ✅                                                         | –                               |
| [Vector search interface](./scalardb-cluster/getting-started-with-vector-search.md)                                                  | –                         | –                                      | ✅ (3.15+) (Public Preview)                             | –                               |
| [Analytical query processing across ScalarDB-managed data sources](./scalardb-analytics/quickstart.md)     | –                         | –                                      | –                                                          | ✅ (3.14+)                      |
| [Analytical query processing across non-ScalarDB-managed data sources](./scalardb-analytics/quickstart.md) | –                         | –                                      | –                                                          | ✅ (3.15+)                      |
| [Remote replication](./scalardb-cluster/remote-replication.md)                                                                       | –                         | –                                      | ✅ (3.16+) (Public Preview)                             | –                               |

\* This feature is not available in the Enterprise Premium edition. If you want to use this feature, please [contact us](https://www.scalar-labs.com/contact).
