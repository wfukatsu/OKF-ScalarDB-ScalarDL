---
type: Deployment Guide
title: '[Deprecated] How to deploy ScalarDB Server'
description: ScalarDB Server is now deprecated. Please use ScalarDB Cluster instead.
resource: https://scalardb.scalar-labs.com/docs/latest/helm-charts/how-to-deploy-scalardb/
tags:
- scalardb
- v3.19
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
- feature-status:deprecated
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.1
doc_id: helm-charts/how-to-deploy-scalardb
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
feature_status:
- Deprecated
generated:
  by: process:okf-build/1.0.0
  at: '2026-09-11T05:23:06Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/c882c4103fe6e0aedff74e7afa67c2587a78ec9b/docs/helm-charts/how-to-deploy-scalardb.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-09-09T05:43:01Z'
---

# [Deprecated] How to deploy ScalarDB Server

:::note

ScalarDB Server is now deprecated. Please use [ScalarDB Cluster](./how-to-deploy-scalardb-cluster.md) instead.

:::

This document explains how to deploy ScalarDB Server using Scalar Helm Charts. You must prepare your custom values file. Please refer to the following document for more details on the custom values file for ScalarDB Server.

* [[Deprecated] Configure a custom values file for ScalarDB Server](./configure-custom-values-scalardb.md)

## Deploy ScalarDB Server

```console
helm install <RELEASE_NAME> scalar-labs/scalardb -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_SERVER> --version <CHART_VERSION>
```

## Upgrade the deployment of ScalarDB Server

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardb -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_SERVER> --version <CHART_VERSION>
```

## Delete the deployment of ScalarDB Server

```console
helm uninstall <RELEASE_NAME> -n <NAMESPACE>
```
