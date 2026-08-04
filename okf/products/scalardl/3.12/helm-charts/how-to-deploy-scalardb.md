---
type: Deployment Guide
title: '[Deprecated] How to deploy ScalarDB Server'
description: ScalarDB Server is now deprecated. Please use ScalarDB Cluster instead.
resource: https://scalardl.scalar-labs.com/docs/3.12/helm-charts/how-to-deploy-scalardb/
tags:
- scalardl
- v3.12
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
- feature-status:deprecated
status: stable
product: scalardl
product_title: ScalarDL
version: '3.12'
patch_version: 3.12.3
doc_id: helm-charts/how-to-deploy-scalardb
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
feature_status:
- Deprecated
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:01Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.12/helm-charts/how-to-deploy-scalardb.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
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
