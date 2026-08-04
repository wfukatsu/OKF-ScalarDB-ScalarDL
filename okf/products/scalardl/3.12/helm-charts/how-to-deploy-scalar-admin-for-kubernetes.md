---
type: Operations Guide
title: How to deploy Scalar Admin for Kubernetes
description: This document explains how to deploy Scalar Admin for Kubernetes by using Scalar Helm Charts. For details on the custom values file for Scalar Admin for Kubernetes, see Configure a custom values file for Scalar Admin for Kubernetes.
resource: https://scalardl.scalar-labs.com/docs/3.12/helm-charts/how-to-deploy-scalar-admin-for-kubernetes/
tags:
- scalardl
- v3.12
- phase:operate
- section:manage
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardl
product_title: ScalarDL
version: '3.12'
patch_version: 3.12.3
doc_id: helm-charts/how-to-deploy-scalar-admin-for-kubernetes
lifecycle_phase: operate
breadcrumb:
- Manage
- Monitor
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:01Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.12/helm-charts/how-to-deploy-scalar-admin-for-kubernetes.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
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
