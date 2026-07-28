---
type: Deployment Guide
title: How to deploy ScalarDL Auditor
description: This document explains how to deploy ScalarDL Auditor using Scalar Helm Charts. You must prepare your custom values file. Please refer to the following document for more details on the custom values file for ScalarDL Auditor and ScalarDL...
resource: https://scalardb.scalar-labs.com/docs/3.15/helm-charts/how-to-deploy-scalardl-auditor/
tags:
- scalardb
- v3.15
- phase:operate
- edition:enterprise
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.15'
patch_version: 3.15.8
doc_id: helm-charts/how-to-deploy-scalardl-auditor
lifecycle_phase: operate
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:02Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.15/helm-charts/how-to-deploy-scalardl-auditor.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to deploy ScalarDL Auditor

This document explains how to deploy ScalarDL Auditor using Scalar Helm Charts. You must prepare your custom values file. Please refer to the following document for more details on the custom values file for ScalarDL Auditor and ScalarDL Schema Loader.

* [Configure a custom values file for ScalarDL Auditor](./configure-custom-values-scalardl-auditor.md)
* [Configure a custom values file for ScalarDL Schema Loader](./configure-custom-values-scalardl-schema-loader.md)

## Prepare a private key file and a certificate file

When you deploy ScalarDL Auditor, you must create a Secrete resource to mount the private key file and the certificate file on the ScalarDL Auditor pods.

For more details on how to mount the key and certificate files on the ScalarDL pods, refer to [Mount key and certificate files on a pod in ScalarDL Helm Charts](./mount-files-or-volumes-on-scalar-pods.md#mount-key-and-certificate-files-on-a-pod-in-scalardl-helm-charts).

## Create schemas for ScalarDL Auditor (Deploy ScalarDL Schema Loader)

Before you deploy ScalarDL Auditor, you must create schemas for ScalarDL Auditor on the backend database.

```console
helm install <RELEASE_NAME> scalar-labs/schema-loading -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDL_SCHEMA_LOADER> --version <CHART_VERSION>
```

## Deploy ScalarDL Auditor

```console
helm install <RELEASE_NAME> scalar-labs/scalardl-audit -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDL_AUDITOR> --version <CHART_VERSION>
```

## Upgrade the deployment of ScalarDL Auditor

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardl-audit -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDL_AUDITOR> --version <CHART_VERSION>
```

## Delete the deployment of ScalarDL Auditor and ScalarDL Schema Loader

```console
helm uninstall <RELEASE_NAME> -n <NAMESPACE>
```
