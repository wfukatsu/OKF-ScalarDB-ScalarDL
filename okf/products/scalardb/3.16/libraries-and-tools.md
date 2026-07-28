---
type: Reference
title: Libraries and Tools for ScalarDB
description: ScalarDB provides various libraries and tools to help you build and operate scalable and reliable applications. Below are some key libraries and tools available.
resource: https://scalardb.scalar-labs.com/docs/3.16/libraries-and-tools/
tags:
- scalardb
- v3.16
- phase:implement
- section:reference
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
- edition:enterprise-option
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: libraries-and-tools
lifecycle_phase: implement
breadcrumb:
- Reference
editions:
- Community
- Enterprise Standard
- Enterprise Premium
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/libraries-and-tools.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Libraries and Tools for ScalarDB

ScalarDB provides various libraries and tools to help you build and operate scalable and reliable applications. Below are some key libraries and tools available.

## Core and Cluster

This section lists the libraries and tools available for ScalarDB Core and Cluster.

### Libraries

The following libraries are available for ScalarDB Core and Cluster.

| Library                          | Edition                                              | Maven Package                                                                                                      | Container Image | Reference                                                                                  |
|----------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------------------------------------------------------------------------|
| ScalarDB Core Java API library   | Community, Enterprise Standard, & Enterprise Premium | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardb)                         | N/A             | [Documentation](./api-guide.md)                                                           |
| ScalarDB Cluster Java Client SDK | Enterprise Standard & Enterprise Premium             | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardb-cluster-java-client-sdk) | N/A             | [Documentation](./scalardb-cluster/developer-guide-for-scalardb-cluster-with-java-api.md) |
| ScalarDB SQL                     | Enterprise Standard & Enterprise Premium             | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardb-sql)                     | N/A             | [Documentation](./scalardb-sql/sql-api-guide.md)                                          |
| JDBC driver for ScalarDB SQL     | Enterprise Standard & Enterprise Premium             | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardb-sql-jdbc)                | N/A             | [Documentation](./scalardb-sql/jdbc-guide.md)                                             |
| Spring Data JDBC for ScalarDB    | Enterprise Standard & Enterprise Premium             | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardb-sql-spring-data)         | N/A             | [Documentation](./scalardb-sql/spring-data-guide.md)                                      |

### Tools

The following tools are available for ScalarDB Core and Cluster.

| Tool                             | Edition                                              | Maven Package                                                                                                 | JAR File                                                            | Container Image                                                                                           | Reference                                                                                                            |
|----------------------------------|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ScalarDB Schema Loader           | Community, Enterprise Standard, & Enterprise Premium | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardb-schema-loader)      | [GitHub Releases](https://github.com/scalar-labs/scalardb/releases) | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-schema-loader)           | [Documentation](./schema-loader.md)                                                                                 |
| ScalarDB Cluster Schema Loader   | Enterprise Standard & Enterprise Premium             | N/A                                                                                                           | [GitHub Releases](https://github.com/scalar-labs/scalardb/releases) | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-schema-loader)   | [Documentation](./scalardb-cluster/developer-guide-for-scalardb-cluster-with-java-api.md#schema-loader-for-cluster) |
| ScalarDB Data Loader CLI         | Community, Enterprise Standard, & Enterprise Premium | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardb-data-loader-cli)    | [GitHub Releases](https://github.com/scalar-labs/scalardb/releases) | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-data-loader-cli)         | [Documentation](./data-loader.md)                                                                                   |
| ScalarDB Cluster SQL CLI         | Enterprise Premium                                   | N/A                                                                                                           | [GitHub Releases](https://github.com/scalar-labs/scalardb/releases) | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-sql-cli)         | [Documentation](./scalardb-cluster/developer-guide-for-scalardb-cluster-with-java-api.md#sql-cli)                   |
| Replication CLI                  | Enterprise Premium                                   | N/A                                                                                                           | [GitHub Releases](https://github.com/scalar-labs/scalardb/releases) | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-replication-cli) | [Documentation](./scalardb-cluster/remote-replication.md#replication-cli)                                           |
| ScalarDB MCP Server              | Community, Enterprise Standard, & Enterprise Premium | N/A                                                                                                           | N/A                                                                 | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-mcp-server)              | [Documentation](./scalardb-mcp-server/getting-started-with-scalardb-mcp-server.md)                                  |
| Helm Charts                      | Community, Enterprise Standard, & Enterprise Premium | N/A                                                                                                           | N/A                                                                 | N/A                                                                                                       | [Documentation](./helm-charts/getting-started-scalar-helm-charts.md)                                                |
| Scalar Admin for Kubernetes      | Enterprise Standard & Enterprise Premium             | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalar-admin-for-kubernetes) | N/A                                                                 | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalar-admin-for-kubernetes)      | [Documentation](./helm-charts/how-to-deploy-scalar-admin-for-kubernetes.md)                                         |

### Cluster components

The following components are available for ScalarDB Cluster.

| Component                        | Edition             | Container Image                                                                                                  | Reference                   |
|----------------------------------|---------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------|
| ScalarDB Cluster Node (BYOL)     | Enterprise Premium  | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-byol-premium)      | Documentation (coming soon) |
| ScalarDB Cluster Node (BYOL)     | Enterprise Standard | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-byol-standard)     | Documentation (coming soon) |
| ScalarDB Cluster Node (UBI BYOL) | Enterprise Premium  | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-ubi-byol-premium)  | Documentation (coming soon) |
| ScalarDB Cluster Node (UBI BYOL) | Enterprise Standard | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-ubi-byol-standard) | Documentation (coming soon) |

## Analytics

This section lists the libraries and tools available for ScalarDB Analytics.

### Libraries

The following libraries are available for ScalarDB Analytics.

| Library                   | Edition           | Maven Package                                                                                  | Container Image | Reference                                                                                                   |
|---------------------------|-------------------|------------------------------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------|
| ScalarDB Analytics        | Enterprise Option | [Maven Central Repository](https://central.sonatype.com/search?q=scalardb-analytics-spark-all) | N/A             | [Documentation](./scalardb-analytics/run-analytical-queries.md#build-configuration-for-spark-applications) |

### Tools

The following tools are available for ScalarDB Analytics.

| Tool                      | Edition                                              | Maven Package | JAR File                                                            | Container Image                                                                                         | Reference                                                                  |
|---------------------------|------------------------------------------------------|---------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| ScalarDB Analytics server | Enterprise Option                                    | N/A           | N/A                                                                 | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-analytics-server-byol) | [Documentation](./scalardb-analytics/deploy-scalardb-analytics-server.md) |
| ScalarDB Analytics CLI    | Enterprise Option                                    | N/A           | [GitHub Releases](https://github.com/scalar-labs/scalardb/releases) | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-analytics-cli)         | [Documentation](./scalardb-analytics/reference-cli-command.md)            |
| Helm Charts               | Community, Enterprise Standard, & Enterprise Premium | N/A           | N/A                                                                 | N/A                                                                                                     | [Documentation](./helm-charts/getting-started-scalar-helm-charts.md)      |
