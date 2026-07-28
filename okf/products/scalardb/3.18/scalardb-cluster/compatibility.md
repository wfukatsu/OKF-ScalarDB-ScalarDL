---
type: Concept
title: ScalarDB Cluster Compatibility Matrix
description: This document shows the compatibility of ScalarDB Cluster versions among client SDK versions.
resource: https://scalardb.scalar-labs.com/docs/latest/scalardb-cluster/compatibility/
tags:
- scalardb
- v3.18
- phase:design
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.18'
patch_version: 3.18.0
doc_id: scalardb-cluster/compatibility
lifecycle_phase: design
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:24Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/docs/scalardb-cluster/compatibility.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# ScalarDB Cluster Compatibility Matrix

This document shows the compatibility of ScalarDB Cluster versions among client SDK versions.

## ScalarDB Cluster compatibility with client SDKs

| ScalarDB Cluster version | ScalarDB Cluster Java Client SDK version | ScalarDB Cluster .NET Client SDK version |
|:-------------------------|:-----------------------------------------|:-----------------------------------------|
| 3.18                     | 3.14 - 3.18                              | 3.14* - 3.18                             |
| 3.17                     | 3.14 - 3.17                              | 3.14* - 3.17                             |
| 3.16                     | 3.14 - 3.16                              | 3.14* - 3.16                             |
| 3.15                     | 3.14 - 3.15                              | 3.14* - 3.15                             |
| 3.14                     | 3.14                                     | 3.14*                                    |

\* This version is in private preview, which means that future versions might have backward-incompatible updates.

:::note

- You can consider the client tools (for example, [ScalarDB Cluster SQL CLI](./developer-guide-for-scalardb-cluster-with-java-api.md#sql-cli) and [ScalarDB Cluster Schema Loader](./developer-guide-for-scalardb-cluster-with-java-api.md#schema-loader-for-cluster)) to be the same as the ScalarDB Cluster Java Client SDK. In other words, you can apply the same compatibility rules to client tools as the ScalarDB Cluster Java Client SDK.
- When you access backend databases by using ScalarDB Cluster Data Loader, you must use a version of ScalarDB Cluster Data Loader that is compatible with the version of ScalarDB Cluster that you're using. In this case, the supported version of ScalarDB Cluster Data Loader is the same as the version of the ScalarDB Cluster Java Client SDK shown in the matrix above. Note that you can have ScalarDB Cluster Data Loader either access backend databases directly or connect to ScalarDB Cluster to access backend databases.
- If you use a new feature that ScalarDB Cluster provides in a new minor version, you may need to use the same or a later version of the client tools or re-create (or update) existing schemas. For details, please refer to the relevant documentation about each feature.
- For Scalar Admin and Scalar Admin for Kubernetes, using the latest versions of these tools is recommended to ensure compatibility with the version of ScalarDB Cluster that you are using.

:::

## Version skew policy

:::note

Versions are expressed as `x.y.z`, where `x` represents the major version, `y` represents the minor version, and `z` represents the patch version. This format follows [Semantic Versioning](https://semver.org/).

:::

- If the **major** versions are different between ScalarDB Cluster and a client SDK, they are **not** compatible and are **not** supported.
- If the **major** versions are the same and the **minor** versions are different between ScalarDB Cluster and a client SDK, the version of ScalarDB Cluster must be greater than or equal to the client SDK version. For example:
  - **Supported:** Combination of ScalarDB Cluster 3.17 and client SDK 3.14
  - **Not supported:** Combination of ScalarDB Cluster 3.14 and client SDK 3.17
- If the **major** versions and the **minor** versions are the same, you can use different **patch** versions between ScalarDB Cluster and a client SDK. For example:
  - **Supported:** Combination of ScalarDB Cluster 3.17.2 and client SDK 3.17.0
  - **Supported:** Combination of ScalarDB Cluster 3.17.0 and client SDK 3.17.2
