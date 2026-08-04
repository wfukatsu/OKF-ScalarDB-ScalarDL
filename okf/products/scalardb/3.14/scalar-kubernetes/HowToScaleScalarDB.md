---
type: Operations Guide
title: How to Scale ScalarDB
description: This guide explains how to scale ScalarDB. The contents of this guide assume that you used Scalar Helm Chart to deploy ScalarDB Cluster, which is the recommended way.
resource: https://scalardb.scalar-labs.com/docs/3.14/scalar-kubernetes/HowToScaleScalarDB/
tags:
- scalardb
- v3.14
- phase:operate
- section:manage
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: scalar-kubernetes/HowToScaleScalarDB
lifecycle_phase: operate
breadcrumb:
- Manage
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/scalar-kubernetes/HowToScaleScalarDB.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# How to Scale ScalarDB

This guide explains how to scale ScalarDB. The contents of this guide assume that you used [Scalar Helm Chart](https://github.com/scalar-labs/helm-charts) to deploy ScalarDB Cluster, which is the recommended way.

:::note

You might be able to resolve some performance issues by scaling ScalarDB Cluster if a bottleneck exists on the ScalarDB Cluster side. However, sometimes a performance issue is caused by a bottleneck in the backend databases. In such cases, scaling ScalarDB Cluster will not resolve the performance issue.

Instead, please check where the bottleneck exists. If the bottleneck exists in the backend databases, consider scaling the backend databases.

:::

**ScalarDB Cluster (Enterprise edition)**

1. Add the following to your custom values file, replacing `<NUMBER_OF_PODS>` with the number of pods you want to scale:

```yaml
scalardbCluster:
  replicaCount: <NUMBER_OF_PODS>
```

1. Upgrade your ScalarDB Cluster deployment by running the following `helm upgrade` command, which uses the updated custom values file. Be sure to replace the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardb-cluster -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_CLUSTER> --version <CHART_VERSION>
```

**ScalarDB Core library (Community edition)**

ScalarDB Core is provided as a Java library. So, when you scale your application, ScalarDB scales with your application.
