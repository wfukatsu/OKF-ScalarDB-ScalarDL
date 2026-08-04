---
type: Deployment Guide
title: How to install Scalar products through AWS Marketplace
description: Scalar products (ScalarDB, ScalarDL, and their tools) are available in the AWS Marketplace as container images. This guide explains how to install Scalar products through the AWS Marketplace.
resource: https://scalardl.scalar-labs.com/docs/3.10/scalar-kubernetes/AwsMarketplaceGuide/
tags:
- scalardl
- v3.10
- phase:operate
- section:deploy
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.10'
patch_version: 3.10.5
doc_id: scalar-kubernetes/AwsMarketplaceGuide
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
  at: '2026-08-04T23:51:03Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.10/scalar-kubernetes/AwsMarketplaceGuide.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# How to install Scalar products through AWS Marketplace

Scalar products (ScalarDB, ScalarDL, and their tools) are available in the AWS Marketplace as container images. This guide explains how to install Scalar products through the AWS Marketplace.

:::note

- Some Scalar products are available under commercial licenses, and the AWS Marketplace provides those products as pay-as-you-go (PAYG) pricing. When you use pay-as-you-go pricing, AWS will charge you the Scalar product license fee based on your usage.
- Previously, a bring-your-own-license (BYOL) option was offered in the AWS Marketplace. However, that option has been deprecated and removed, so it is no longer supported in the AWS Marketplace.
- A BYOL option is provided in the following public container repositories outside of the AWS Marketplace. If you don't have a license key, please [contact us](https://www.scalar-labs.com/contact-us).
  - [ScalarDB Cluster Enterprise Standard](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-byol-standard)
  - [ScalarDB Cluster Enterprise Premium](https://github.com/orgs/scalar-labs/packages/container/package/scalardb-cluster-node-byol-premium)
  - [ScalarDB Analytics Server](https://github.com/scalar-labs/scalardb-analytics/pkgs/container/scalardb-analytics-server-byol)
  - [ScalarDL Ledger](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-ledger-byol)
  - [ScalarDL Auditor](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-auditor-byol)

:::

## Subscribe to Scalar products from AWS Marketplace

1. Select your Scalar product to see the links to the AWS Marketplace.

**ScalarDB Cluster**

Select your edition of ScalarDB Enterprise.

**ScalarDB Enterprise Edition (Standard)**

| PAYG                                                                             | BYOL (Deprecated)                                                                |
|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [ScalarDB Cluster](https://aws.amazon.com/marketplace/pp/prodview-jx6qxatkxuwm4) | [ScalarDB Cluster](https://aws.amazon.com/marketplace/pp/prodview-alcwrmw6v4cfy) |

**ScalarDB Enterprise Edition (Premium)**

| PAYG                                                                             | BYOL (Deprecated)                                                                            |
|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [ScalarDB Cluster](https://aws.amazon.com/marketplace/pp/prodview-djqw3zk6dwyk6) | [ScalarDB Cluster](https://aws.amazon.com/marketplace/pp/prodview-alcwrmw6v4cfy)             |

**ScalarDB Analytics server**

| PAYG                                                                                       |
|:-------------------------------------------------------------------------------------------|
| [ScalarDB Analytics Server](https://aws.amazon.com/marketplace/pp/prodview-53ik57autkmci)  |

**ScalarDL Ledger**

| PAYG                                                                             | BYOL (Deprecated)                                                                |
|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [ScalarDL Ledger](https://aws.amazon.com/marketplace/pp/prodview-wttioaezp5j6e)  | [ScalarDL Ledger](https://aws.amazon.com/marketplace/pp/prodview-3jdwfmqonx7a2)  |

**ScalarDL Auditor**

| PAYG                                                                             | BYOL (Deprecated)                                                                |
|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [ScalarDL Auditor](https://aws.amazon.com/marketplace/pp/prodview-ke3yiw4mhriuu) | [ScalarDL Auditor](https://aws.amazon.com/marketplace/pp/prodview-tj7svy75gu7m6) |

1. Select **Continue to Subscribe**.

1. Sign in to AWS Marketplace using your IAM user.
   If you have already signed in, this step will be skipped automatically.

1. Read the **Terms and Conditions** and select **Accept Terms**.
   It takes some time. When it's done, you can see the current date in the **Effective date** column.
   Also, you can see our products on the [Manage subscriptions](https://us-east-1.console.aws.amazon.com/marketplace/home#/subscriptions) page of AWS Console.

## **[Pay-As-You-Go]** Deploy containers on EKS (Amazon Elastic Kubernetes Service) from AWS Marketplace using Scalar Helm Charts

By subscribing to Scalar products in the AWS Marketplace, you can pull the container images of Scalar products from the private container registry ([ECR](https://aws.amazon.com/ecr/)) of the AWS Marketplace. This section explains how to deploy Scalar products with pay-as-you-go pricing in your [EKS](https://aws.amazon.com/eks/) cluster from the private container registry.

1. Create an OIDC provider.

   You must create an identity and access management (IAM) OpenID Connect (OIDC) provider to run the AWS Marketplace Metering Service from ScalarDL pods.

```console
eksctl utils associate-iam-oidc-provider --region <REGION> --cluster <EKS_CLUSTER_NAME> --approve
```

   For details, see [Creating an IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

1. Create a service account.

   To allow your pods to run the AWS Marketplace Metering Service, you can use [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

```console
eksctl create iamserviceaccount \
    --name <SERVICE_ACCOUNT_NAME> \
    --namespace <NAMESPACE> \
    --region <REGION> \
    --cluster <EKS_CLUSTER_NAME> \
    --attach-policy-arn arn:aws:iam::aws:policy/AWSMarketplaceMeteringFullAccess \
    --approve \
    --override-existing-serviceaccounts
```

1. Update the custom values file of the Helm Chart for the Scalar product that you want to install.
   You need to specify the private container registry (ECR) of the AWS Marketplace as the value for `[].image.repository` in the custom values file. You also need to specify the service account name that you created in the previous step as the value for `[].serviceAccount.serviceAccountName` and set `[].serviceAccount.automountServiceAccountToken` to `true`. See the following examples based on the product you're using.

**ScalarDB Cluster**

Select your edition of ScalarDB Enterprise.

**ScalarDB Enterprise Edition (Standard)**

In the `scalardb-cluster-standard-custom-values.yaml` file:

```yaml
scalardbCluster:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalardb-cluster-node-aws-payg-standard"
  serviceAccount:
    serviceAccountName: "<SERVICE_ACCOUNT_NAME>"
    automountServiceAccountToken: true
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDB Cluster](../helm-charts/configure-custom-values-scalardb-cluster.md).

:::

**ScalarDB Enterprise Edition (Premium)**

In the `scalardb-cluster-premium-custom-values.yaml` file:

```yaml
scalardbCluster:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalardb-cluster-node-aws-payg-premium"
  serviceAccount:
    serviceAccountName: "<SERVICE_ACCOUNT_NAME>"
    automountServiceAccountToken: true
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDB Cluster](../helm-charts/configure-custom-values-scalardb-cluster.md).

:::

**ScalarDB Analytics server**

### ScalarDB Analytics server

  In the `scalardb-analytics-server-custom-values.yaml` file:

```yaml
scalarDbAnalyticsServer:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalardb-analytics-server-aws-payg"
  serviceAccount:
    serviceAccountName: "<SERVICE_ACCOUNT_NAME>"
    automountServiceAccountToken: true
```

:::note

For more details on the configurations, see [Configure a Custom Values File for ScalarDB Analytics Server](../helm-charts/configure-custom-values-scalardb-analytics-server.md).

:::

**ScalarDL Ledger**

### ScalarDL Ledger

  In the `scalardl-ledger-custom-values.yaml` file:

```yaml
ledger:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalardl-ledger-aws-payg"
  serviceAccount:
    serviceAccountName: "<SERVICE_ACCOUNT_NAME>"
    automountServiceAccountToken: true
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Ledger](../helm-charts/configure-custom-values-scalardl-ledger.md).

:::

### ScalarDL Schema Loader for Ledger

  You don't need to update the `[].image.repository` configuration in your `schema-loader-ledger-custom-values.yaml` file. The container image of ScalarDL Schema Loader is provided in the [public container repository](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-schema-loader).

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Schema Loader](../helm-charts/configure-custom-values-scalardl-schema-loader.md).

:::

**ScalarDL Auditor**

### ScalarDL Auditor

  In the `scalardl-auditor-custom-values.yaml` file:

```yaml
auditor:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalardl-auditor-aws-payg"
  serviceAccount:
    serviceAccountName: "<SERVICE_ACCOUNT_NAME>"
    automountServiceAccountToken: true
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Auditor](../helm-charts/configure-custom-values-scalardl-auditor.md).

:::

### ScalarDL Schema Loader for Auditor

  You don't need to update the `[].image.repository` configuration in your `schema-loader-auditor-custom-values.yaml` file. The container image of ScalarDL Schema Loader is provided in the [public container repository](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-schema-loader).

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Schema Loader](../helm-charts/configure-custom-values-scalardl-schema-loader.md).

:::

1. Deploy Scalar products by using Helm Charts in conjunction with the above custom values files. See the following examples based on the product you're using.

**ScalarDB Cluster**

Select your edition of ScalarDB Enterprise.

**ScalarDB Enterprise Edition (Standard)**

```console
helm install scalardb-cluster-standard scalar-labs/scalardb-cluster -f scalardb-cluster-standard-custom-values.yaml
```

**ScalarDB Enterprise Edition (Premium)**

```console
helm install scalardb-cluster-premium scalar-labs/scalardb-cluster -f scalardb-cluster-premium-custom-values.yaml
```

**ScalarDB Analytics server**

### ScalarDB Analytics server

```console
helm install scalardb-analytics-server scalar-labs/scalardb-analytics-server -f scalardb-analytics-server-custom-values.yaml
```

**ScalarDL Ledger**

### ScalarDL Ledger

```console
helm install scalardl-ledger scalar-labs/scalardl -f scalardl-ledger-custom-values.yaml
```

### ScalarDL Schema Loader for Ledger

```console
helm install schema-loader scalar-labs/schema-loading -f schema-loader-ledger-custom-values.yaml
```

**ScalarDL Auditor**

### ScalarDL Auditor

```console
helm install scalardl-auditor scalar-labs/scalardl-audit -f scalardl-auditor-custom-values.yaml
```

### ScalarDL Schema Loader for Auditor

```console
helm install schema-loader scalar-labs/schema-loading -f schema-loader-auditor-custom-values.yaml
```

## **[Deprecated] [BYOL]** Deploy containers on EKS (Amazon Elastic Kubernetes Service) from AWS Marketplace using Scalar Helm Charts

By subscribing to Scalar products in the AWS Marketplace, you can pull the container images of Scalar products from the private container registry ([ECR](https://aws.amazon.com/ecr/)) of the AWS Marketplace. This section explains how to deploy Scalar products with the BYOL option in your [EKS](https://aws.amazon.com/eks/) cluster from the private container registry.

1. Update the custom values file of the Helm Chart for the Scalar product that you want to install.
   You need to specify the private container registry (ECR) of AWS Marketplace as the value of `[].image.repository` in the custom values file. See the following examples based on the product you're using.

**ScalarDB Cluster**

```yaml
scalardbCluster:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalardb-cluster-node-aws-byol"
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDB Cluster](../helm-charts/configure-custom-values-scalardb-cluster.md).

:::

**ScalarDL Ledger**

### ScalarDL Ledger

  In the `scalardl-ledger-custom-values.yaml` file:

```yaml
ledger:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalar-ledger"
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Ledger](../helm-charts/configure-custom-values-scalardl-ledger.md).

:::

### ScalarDL Schema Loader for Ledger

  You don't need to update the `[].image.repository` configuration in your `schema-loader-ledger-custom-values.yaml` file. The container image of ScalarDL Schema Loader is provided in the [public container repository](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-schema-loader).

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Schema Loader](../helm-charts/configure-custom-values-scalardl-schema-loader.md).

:::

**ScalarDL Auditor**

### ScalarDL Auditor

  In the `scalardl-auditor-custom-values.yaml` file:

```yaml
auditor:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalar-auditor"
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Auditor](../helm-charts/configure-custom-values-scalardl-auditor.md).

:::

### ScalarDL Schema Loader for Auditor

  You don't need to update the `[].image.repository` configuration in your `schema-loader-auditor-custom-values.yaml` file. The container image of ScalarDL Schema Loader is provided in the [public container repository](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-schema-loader).

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Schema Loader](../helm-charts/configure-custom-values-scalardl-schema-loader.md).

:::

1. Deploy the Scalar products using the Helm Chart with the above custom values files. See the following examples based on the product you're using. See the following examples based on the product you're using.

**ScalarDB Cluster**

```console
helm install scalardb-cluster scalar-labs/scalardb-cluster -f scalardb-cluster-custom-values.yaml
```

**ScalarDL Ledger**

### ScalarDL Ledger

```console
helm install scalardl-ledger scalar-labs/scalardl -f scalardl-ledger-custom-values.yaml
```

### ScalarDL Schema Loader for Ledger

```console
helm install schema-loader scalar-labs/schema-loading -f schema-loader-ledger-custom-values.yaml
```

**ScalarDL Auditor**

### ScalarDL Auditor

```console
helm install scalardl-auditor scalar-labs/scalardl-audit -f scalardl-auditor-custom-values.yaml
```

### ScalarDL Schema Loader for Auditor

```console
helm install schema-loader scalar-labs/schema-loading -f schema-loader-auditor-custom-values.yaml
```

## **[Deprecated] [BYOL]** Deploy containers on Kubernetes other than EKS from AWS Marketplace using Scalar Helm Charts

1. Install the `aws` command according to the [AWS Official Document (Installing or updating the latest version of the AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. Configure the AWS CLI with your credentials according to the [AWS Official Document (Configuration basics)](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).

1. Create a `reg-ecr-mp-secrets` secret resource for pulling the container images from the ECR of AWS Marketplace.
```console
kubectl create secret docker-registry reg-ecr-mp-secrets \
  --docker-server=709825985650.dkr.ecr.us-east-1.amazonaws.com \
  --docker-username=AWS \
  --docker-password=$(aws ecr get-login-password --region us-east-1)
```

1. Update the custom values file of the Helm Chart for the Scalar product that you want to install.
   You need to specify the private container registry (ECR) of AWS Marketplace as the value of `[].image.repository` in the custom values file.
   Also, you need to specify the `reg-ecr-mp-secrets` as the value of `[].imagePullSecrets`. See the following examples based on the product you're using.

**ScalarDB Cluster**

```yaml
scalardbCluster:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalardb-cluster-node-aws-byol"
  imagePullSecrets:
    - name: "reg-ecr-mp-secrets"
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDB Cluster](../helm-charts/configure-custom-values-scalardb-cluster.md).

:::

**ScalarDL Ledger**

### ScalarDL Ledger

  In the `scalardl-ledger-custom-values.yaml` file:

```yaml
ledger:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalar-ledger"
  imagePullSecrets:
    - name: "reg-ecr-mp-secrets"
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Ledger](../helm-charts/configure-custom-values-scalardl-ledger.md).

:::

### ScalarDL Schema Loader for Ledger

  You don't need to update the `[].image.repository` configuration in your `schema-loader-ledger-custom-values.yaml` file. The container image of ScalarDL Schema Loader is provided in the [public container repository](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-schema-loader).

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Schema Loader](../helm-charts/configure-custom-values-scalardl-schema-loader.md).

:::

**ScalarDL Auditor**

### ScalarDL Auditor

  In the `scalardl-auditor-custom-values.yaml` file:

```yaml
auditor:
  image:
    repository: "709825985650.dkr.ecr.us-east-1.amazonaws.com/scalar/scalar-auditor"
  imagePullSecrets:
    - name: "reg-ecr-mp-secrets"
```

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Auditor](../helm-charts/configure-custom-values-scalardl-auditor.md).

:::

### ScalarDL Schema Loader for Auditor

  You don't need to update the `[].image.repository` configuration in your `schema-loader-auditor-custom-values.yaml` file. The container image of ScalarDL Schema Loader is provided in the [public container repository](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-schema-loader).

:::note

For more details on the configurations, see [Configure a custom values file for ScalarDL Schema Loader](../helm-charts/configure-custom-values-scalardl-schema-loader.md).

:::

1. Deploy the Scalar products using the Helm Chart with the above custom values files.
   * Examples
     Please refer to the **[Deprecated] [BYOL] Deploy containers on EKS (Amazon Elastic Kubernetes Service) from AWS Marketplace using Scalar Helm Charts** section of this document.
