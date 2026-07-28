---
type: Deployment Guide
title: How to Scale ScalarDB Cluster
description: This guide explains how to scale ScalarDB Cluster. The contents of this guide assume that you used Scalar Helm Chart to deploy ScalarDB Cluster, which is the recommended way.
resource: https://scalardl.scalar-labs.com/docs/latest/scalar-kubernetes/HowToScaleScalarDB/
tags:
- scalardl
- v3.13
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: scalar-kubernetes/HowToScaleScalarDB
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/scalar-kubernetes/HowToScaleScalarDB.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# How to Scale ScalarDB Cluster

This guide explains how to scale ScalarDB Cluster. The contents of this guide assume that you used [Scalar Helm Chart](https://github.com/scalar-labs/helm-charts) to deploy ScalarDB Cluster, which is the recommended way.

:::note

You might be able to resolve some performance issues by scaling ScalarDB Cluster if a bottleneck exists on the ScalarDB Cluster side. However, sometimes a performance issue is caused by a bottleneck in the backend databases. In such cases, scaling ScalarDB Cluster will not resolve the performance issue.

Instead, please check where the bottleneck exists. If the bottleneck exists in the backend databases, consider scaling the backend databases.

:::

1. Add the following to your custom values file, replacing `<NUMBER_OF_PODS>` with the number of pods you want to scale:

```yaml
scalardbCluster:
  replicaCount: <NUMBER_OF_PODS>
```

1. Upgrade your ScalarDB Cluster deployment by running the following `helm upgrade` command, which uses the updated custom values file. Be sure to replace the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardb-cluster -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_CLUSTER> --version <CHART_VERSION>
```
