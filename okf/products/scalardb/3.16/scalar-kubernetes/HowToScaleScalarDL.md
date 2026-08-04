---
type: Deployment Guide
title: How to Scale ScalarDL
description: This guide explains how to scale ScalarDL. The contents of this guide assume that you used Scalar Helm Chart to deploy ScalarDL, which is the recommended way.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalar-kubernetes/HowToScaleScalarDL/
tags:
- scalardb
- v3.16
- phase:operate
- edition:enterprise
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.6
doc_id: scalar-kubernetes/HowToScaleScalarDL
lifecycle_phase: operate
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:54Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.16/scalar-kubernetes/HowToScaleScalarDL.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# How to Scale ScalarDL

This guide explains how to scale ScalarDL. The contents of this guide assume that you used [Scalar Helm Chart](https://github.com/scalar-labs/helm-charts) to deploy ScalarDL, which is the recommended way.

:::note

You might be able to resolve some performance issues by scaling ScalarDL if a bottleneck exists on the ScalarDL side. However, sometimes a performance issue is caused by a bottleneck in the backend databases. In such cases, scaling ScalarDL will not resolve the performance issue.

Instead, please check where the bottleneck exists. If the bottleneck exists in the backend databases, consider scaling the backend databases.

:::

**ScalarDL Ledger**

1. Add the following to your custom values file, replacing `<NUMBER_OF_PODS>` with the number of pods you want to scale:

```yaml
ledger:
  replicaCount: <NUMBER_OF_PODS>
```

1. Upgrade your ScalarDL Ledger deployment by running the following `helm upgrade` command, which uses the updated custom values file. Be sure to replace the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardl -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDL_LEDGER> --version <CHART_VERSION>
```

**ScalarDL Auditor**

1. Add the following to your custom values file, replacing `<NUMBER_OF_PODS>` with the number of pods you want to scale:

```yaml
auditor:
  replicaCount: <NUMBER_OF_PODS>
```

1. Upgrade your ScalarDL Auditor deployment by running the following `helm upgrade` command, which uses the updated custom values file. Be sure to replace the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardl-audit -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDL_AUDITOR> --version <CHART_VERSION>
```
