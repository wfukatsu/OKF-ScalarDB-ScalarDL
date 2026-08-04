---
type: Concept
title: ScalarDB Features
description: This document briefly explains which features are available in which editions of ScalarDB.
resource: https://scalardb.scalar-labs.com/docs/3.17/features/
tags:
- scalardb
- v3.17
- phase:design
- section:about-scalardb
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.4
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
  at: '2026-08-04T23:50:51Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.17/features.mdx
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
| [Attribute-based access control](./scalardb-cluster/authorize-with-abac.md)                                                          | –                         | –                                      | ✅ (3.15+) (Enterprise Premium Option*, Private Preview**) | –                               |
| [SQL interface (SQL API, JDBC, Spring Data JDBC, and LINQ)](./scalardb-sql/section-home.md)                                                 | –                         | –                                      | ✅                                                         | –                               |
| [GraphQL interface](./scalardb-graphql/section-home.md)                                                                                     | –                         | –                                      | ✅                                                         | –                               |
| [Vector search interface](./scalardb-cluster/getting-started-with-vector-search.md)                                                  | –                         | –                                      | ✅ (3.15+) (Private Preview**)                             | –                               |
| [Analytical query processing across ScalarDB-managed data sources](./scalardb-analytics/quickstart.md)     | –                         | –                                      | –                                                          | ✅ (3.14+)                      |
| [Analytical query processing across non-ScalarDB-managed data sources](./scalardb-analytics/quickstart.md) | –                         | –                                      | –                                                          | ✅ (3.15+)                      |
| [Remote replication](./scalardb-cluster/remote-replication.md)                                                                       | –                         | –                                      | ✅ (3.16+) (Private Preview**)                             | –                               |

\* This feature is not available in the Enterprise Premium edition. If you want to use this feature, please [contact us](https://www.scalar-labs.com/contact).

\*\* This feature is currently in Private Preview. For details, please [contact us](https://www.scalar-labs.com/contact) or wait for this feature to become publicly available in a future version.
