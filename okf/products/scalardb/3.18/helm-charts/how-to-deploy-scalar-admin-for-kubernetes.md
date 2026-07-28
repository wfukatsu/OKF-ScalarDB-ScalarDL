---
type: Deployment Guide
title: How to deploy Scalar Admin for Kubernetes
description: This document explains how to deploy Scalar Admin for Kubernetes by using Scalar Helm Charts. For details on the custom values file for Scalar Admin for Kubernetes, see Configure a custom values file for Scalar Admin for Kubernetes.
resource: https://scalardb.scalar-labs.com/docs/latest/helm-charts/how-to-deploy-scalar-admin-for-kubernetes/
tags:
- scalardb
- v3.18
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.18'
patch_version: 3.18.0
doc_id: helm-charts/how-to-deploy-scalar-admin-for-kubernetes
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:24Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/docs/helm-charts/how-to-deploy-scalar-admin-for-kubernetes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to deploy Scalar Admin for Kubernetes

This document explains how to deploy Scalar Admin for Kubernetes by using Scalar Helm Charts. For details on the custom values file for Scalar Admin for Kubernetes, see [Configure a custom values file for Scalar Admin for Kubernetes](./configure-custom-values-scalar-admin-for-kubernetes.md).

## Deploy Scalar Admin for Kubernetes

To deploy Scalar Admin for Kubernetes, run the following command, replacing the contents in the angle brackets as described:

```console
helm install <RELEASE_NAME> scalar-labs/scalar-admin-for-kubernetes -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALAR_ADMIN_FOR_KUBERNETES> --version <CHART_VERSION>
```

## Upgrade a Scalar Admin for Kubernetes job

To upgrade a Scalar Admin for Kubernetes job, run the following command, replacing the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalar-admin-for-kubernetes -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALAR_ADMIN_FOR_KUBERNETES> --version <CHART_VERSION>
```

## Delete a Scalar Admin for Kubernetes job

To delete a Scalar Admin for Kubernetes job, run the following command, replacing the contents in the angle brackets as described:

```console
helm uninstall <RELEASE_NAME> -n <NAMESPACE>
```
