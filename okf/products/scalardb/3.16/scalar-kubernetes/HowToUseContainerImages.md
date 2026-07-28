---
type: Deployment Guide
title: How to use the container images
description: You can pull the container images from the public container repository. You must configure the license key and the certificate in your .properties file if you use the container images.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalar-kubernetes/HowToUseContainerImages/
tags:
- scalardb
- v3.16
- phase:operate
- section:deploy
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: scalar-kubernetes/HowToUseContainerImages
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
- Installation Guides
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/scalar-kubernetes/HowToUseContainerImages.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to use the container images

You can pull the container images from the public container repository. You must configure the license key and the certificate in your `.properties` file if you use the container images.

## Prerequisites

The public container images are available for the following products and versions:

* ScalarDB Cluster v3.12 or later
* ScalarDL v3.9 or later

## Pull the container images from the public container repository

You can pull the container image of each product from the public container repository. To pull a container image, select your Scalar product to see the link to the container image.

**ScalarDB Cluster**

Select your edition of ScalarDB Enterprise.

**ScalarDB Enterprise Edition (Standard)**

https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-byol-standard

**ScalarDB Enterprise Edition (Premium)**

https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-byol-premium

**ScalarDL Ledger**

https://github.com/orgs/scalar-labs/packages/container/package/scalardl-ledger-byol

**ScalarDL Auditor**

https://github.com/orgs/scalar-labs/packages/container/package/scalardl-auditor-byol

If you're using Scalar Helm Charts, you must set `*.image.repository` in the custom values file for the product that you're using. Select your Scalar product to see how to set `*.image.repository`.

**ScalarDB Cluster**

Select your edition of ScalarDB Enterprise.

**ScalarDB Enterprise Edition (Standard)**

```yaml
scalardbCluster:
  image:
    repository: "ghcr.io/scalar-labs/scalardb-cluster-node-byol-standard"
```

**ScalarDB Enterprise Edition (Premium)**

```yaml
scalardbCluster:
  image:
    repository: "ghcr.io/scalar-labs/scalardb-cluster-node-byol-premium"
```

**ScalarDL Ledger**

```yaml
ledger:
  image:
    repository: "ghcr.io/scalar-labs/scalardl-ledger-byol"
```

**ScalarDL Auditor**

```yaml
auditor:
  image:
    repository: "ghcr.io/scalar-labs/scalardl-auditor-byol"
```

## Set the license key in the `.properties` file

To run the container images, you must set `license key` and `certificate` in your `.properties` file. Select your Scalar product to see how to set `license key` and `certificate`. If you don't have a license key, please [contact us](https://www.scalar-labs.com/contact).

**ScalarDB Cluster**

```properties
scalar.db.cluster.node.licensing.license_key=<YOUR_LICENSE_KEY>
scalar.db.cluster.node.licensing.license_check_cert_pem=<CERT_PEM_FOR_LICENSE_KEY>
```

**ScalarDL Ledger**

```properties
scalar.dl.licensing.license_key=<YOUR_LICENSE_KEY>
scalar.dl.licensing.license_check_cert_pem=<CERT_PEM_FOR_LICENSE_KEY>
```

**ScalarDL Auditor**

```properties
scalar.dl.licensing.license_key=<YOUR_LICENSE_KEY>
scalar.dl.licensing.license_check_cert_pem=<CERT_PEM_FOR_LICENSE_KEY>
```

If you're using Scalar Helm Charts, you must set the properties in the custom values file for the product that you're using. Select your Scalar product to see how to set the properties in the custom values file.

**ScalarDB Cluster**

```yaml
scalardbCluster:
  scalardbClusterNodeProperties: |
    scalar.db.cluster.node.licensing.license_key=<YOUR_LICENSE_KEY>
    scalar.db.cluster.node.licensing.license_check_cert_pem=<CERT_PEM_FOR_LICENSE_KEY>
```

**ScalarDL Ledger**

```yaml
ledger:
  ledgerProperties: |
    scalar.dl.licensing.license_key=<YOUR_LICENSE_KEY>
    scalar.dl.licensing.license_check_cert_pem=<CERT_PEM_FOR_LICENSE_KEY>
```

**ScalarDL Auditor**

```yaml
auditor:
  auditorProperties: |
    scalar.dl.licensing.license_key=<YOUR_LICENSE_KEY>
    scalar.dl.licensing.license_check_cert_pem=<CERT_PEM_FOR_LICENSE_KEY>
```
