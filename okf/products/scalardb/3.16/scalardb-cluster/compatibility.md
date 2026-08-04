---
type: Reference
title: ScalarDB Cluster Compatibility Matrix
description: This document shows the compatibility of ScalarDB Cluster versions among client SDK versions.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalardb-cluster/compatibility/
tags:
- scalardb
- v3.16
- phase:implement
- section:reference
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.6
doc_id: scalardb-cluster/compatibility
lifecycle_phase: implement
breadcrumb:
- Reference
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:54Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.16/scalardb-cluster/compatibility.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB Cluster Compatibility Matrix

This document shows the compatibility of ScalarDB Cluster versions among client SDK versions.

## ScalarDB Cluster compatibility with client SDKs

| ScalarDB Cluster version | ScalarDB Cluster Java Client SDK version | ScalarDB Cluster .NET Client SDK version |
|:-------------------------|:-----------------------------------------|:-----------------------------------------|
| 3.16                     | 3.14 - 3.16                              | 3.14* - 3.16                             |
| 3.15                     | 3.14 - 3.15                              | 3.14* - 3.15                             |
| 3.14                     | 3.14                                     | 3.14*                                    |

\* This version is in private preview, which means that future versions might have backward-incompatible updates.

:::note

- You can consider the client tools (for example, [ScalarDB Cluster SQL CLI](./developer-guide-for-scalardb-cluster-with-java-api.md#sql-cli) and [ScalarDB Cluster Schema Loader](./developer-guide-for-scalardb-cluster-with-java-api.md#schema-loader-for-cluster)) to be the same as the ScalarDB Cluster Java Client SDK. In other words, you can apply the same compatibility rules to client tools as the ScalarDB Cluster Java Client SDK.
- When you access backend databases by using ScalarDB Data Loader, you must use a version of ScalarDB Data Loader that is compatible with the version of ScalarDB Cluster that you're using. In this case, the supported version of ScalarDB Data Loader is the same as the version of the ScalarDB Cluster Java Client SDK shown in the matrix above. Note that ScalarDB Data Loader doesn't access ScalarDB Cluster directly.
- If you use a new feature that ScalarDB Cluster provides in a new minor version, you may need to use the same or a later version of the client tools or re-create (or update) existing schemas. For details, please refer to the relevant documentation about each feature.
- For Scalar Admin and Scalar Admin for Kubernetes, using the latest versions of these tools is recommended to ensure compatibility with the version of ScalarDB Cluster that you are using.

:::

## Version skew policy

:::note

Versions are expressed as `x.y.z`, where `x` represents the major version, `y` represents the minor version, and `z` represents the patch version. This format follows [Semantic Versioning](https://semver.org/).

:::

- If the **major** versions are different between ScalarDB Cluster and a client SDK, they are **not** compatible and are **not** supported.
- If the **major** versions are the same and the **minor** versions are different between ScalarDB Cluster and a client SDK, the version of ScalarDB Cluster must be greater than or equal to the client SDK version. For example:
  - **Supported:** Combination of ScalarDB Cluster 3.16 and client SDK 3.15
  - **Not supported:** Combination of ScalarDB Cluster 3.15 and client SDK 3.16
- If the **major** versions and the **minor** versions are the same, you can use different **patch** versions between ScalarDB Cluster and a client SDK. For example:
  - **Supported:** Combination of ScalarDB Cluster 3.16.6 and client SDK 3.13.0
  - **Supported:** Combination of ScalarDB Cluster 3.15.0 and client SDK 3.16.6
