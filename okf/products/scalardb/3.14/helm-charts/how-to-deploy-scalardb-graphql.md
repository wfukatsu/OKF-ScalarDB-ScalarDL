---
type: Deployment Guide
title: '[Deprecated] How to deploy ScalarDB GraphQL'
description: ScalarDB GraphQL Server is now deprecated. Please use ScalarDB Cluster instead.
resource: https://scalardb.scalar-labs.com/docs/3.14/helm-charts/how-to-deploy-scalardb-graphql/
tags:
- scalardb
- v3.14
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: helm-charts/how-to-deploy-scalardb-graphql
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/helm-charts/how-to-deploy-scalardb-graphql.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# [Deprecated] How to deploy ScalarDB GraphQL

:::note

ScalarDB GraphQL Server is now deprecated. Please use [ScalarDB Cluster](./how-to-deploy-scalardb-cluster.md) instead.

:::

This document explains how to deploy ScalarDB GraphQL using Scalar Helm Charts. You must prepare your custom values file. Please refer to the following document for more details on the custom values file for ScalarDB GraphQL.

* [[Deprecated] Configure a custom values file for ScalarDB GraphQL](./configure-custom-values-scalardb-graphql.md)

## Deploy ScalarDB Server (recommended option)

When you deploy ScalarDB GraphQL, it is recommended to deploy ScalarDB Server between ScalarDB GraphQL and backend databases as follows.

```
[Client] ---> [ScalarDB GraphQL] ---> [ScalarDB Server] ---> [Backend databases]
```

Please deploy ScalarDB Server before you deploy ScalarDB GraphQL according to the document [How to deploy ScalarDB Server](./how-to-deploy-scalardb.md).

## Deploy ScalarDB GraphQL

```console
helm install <RELEASE_NAME> scalar-labs/scalardb-graphql -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_GRAPHQL> --version <CHART_VERSION>
```

## Upgrade the deployment of ScalarDB GraphQL

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardb-graphql -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_GRAPHQL> --version <CHART_VERSION>
```

## Delete the deployment of ScalarDB GraphQL

```console
helm uninstall <RELEASE_NAME> -n <NAMESPACE>
```
