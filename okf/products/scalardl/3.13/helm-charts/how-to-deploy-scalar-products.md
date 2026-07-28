---
type: Deployment Guide
title: Deploy Scalar products using Scalar Helm Charts
description: This document explains how to deploy Scalar products using Scalar Helm Charts. If you want to test Scalar products on your local environment using a minikube cluster, please refer to the following getting started guide.
resource: https://scalardl.scalar-labs.com/docs/latest/helm-charts/how-to-deploy-scalar-products/
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
doc_id: helm-charts/how-to-deploy-scalar-products
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/helm-charts/how-to-deploy-scalar-products.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Deploy Scalar products using Scalar Helm Charts

This document explains how to deploy Scalar products using Scalar Helm Charts. If you want to test Scalar products on your local environment using a minikube cluster, please refer to the following getting started guide.

* [Getting Started with Scalar Helm Charts](./getting-started-scalar-helm-charts.md)

## Prerequisites

### Install the helm command

You must install the helm command to use Scalar Helm Charts. Please install the helm command according to the [Helm document](https://helm.sh/docs/intro/install/).

### Add the Scalar Helm Charts repository

```console
helm repo add scalar-labs https://scalar-labs.github.io/helm-charts
```
```console
helm repo update scalar-labs
```

### Prepare a Kubernetes cluster

You must prepare a Kubernetes cluster for the deployment of Scalar products. If you use EKS (Amazon Elastic Kubernetes Service) or AKS (Azure Kubernetes Service) in the production environment. Please refer to the following document for more details.

- [Guidelines for creating an Amazon EKS cluster for Scalar products](../scalar-kubernetes/CreateEKSClusterForScalarProducts.md)
- [Guidelines for creating an AKS cluster for Scalar products](../scalar-kubernetes/CreateAKSClusterForScalarProducts.md)

You must prepare a supported version of Kubernetes. For versions that Scalar Helm Charts supports, see [Kubernetes](https://scalardb.scalar-labs.com/docs/latest/requirements/#kubernetes).

### Prepare a database (ScalarDB, ScalarDL Ledger, ScalarDL Auditor)

You must prepare a database as a backend storage of ScalarDB/ScalarDL. You can see the supported databases by ScalarDB/ScalarDL in the following document.

* [ScalarDB Supported Databases](https://scalardb.scalar-labs.com/docs/latest/requirements#databases)

### Prepare a custom values file

You must prepare your custom values file based on your environment. Please refer to the following documents for more details on how to create a custom values file.

* [Configure a custom values file for Scalar Helm Charts](./configure-custom-values-file.md)

### Get the container images

If you're using commercially licensed Scalar products, you must get the container images of those products. For details, see [How to get the container images of Scalar products](../scalar-kubernetes/HowToGetContainerImages.md).

If you're using any of the following products from the public container repository, you can get the container images from the public container repository with the default configuration of Scalar Helm Chart:

* Scalar Envoy (deploy with ScalarDB Cluster, ScalarDL Ledger, or ScalarDL Auditor)
* ScalarDL Schema Loader
* Scalar Admin for Kubernetes

## Deploy Scalar products

Please refer to the following documents for more details on how to deploy each product.

* [ScalarDB Cluster](./how-to-deploy-scalardb-cluster.md)
* [ScalarDL Ledger](./how-to-deploy-scalardl-ledger.md)
* [ScalarDL Auditor](./how-to-deploy-scalardl-auditor.md)
* [Scalar Admin for Kubernetes](./how-to-deploy-scalar-admin-for-kubernetes.md)
* [Scalar Manager](./getting-started-scalar-manager.md)
* [[Deprecated] ScalarDB Server](./how-to-deploy-scalardb.md)
* [[Deprecated] ScalarDB GraphQL](./how-to-deploy-scalardb-graphql.md)
