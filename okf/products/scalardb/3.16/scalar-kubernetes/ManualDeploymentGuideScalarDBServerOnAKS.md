---
type: Deployment Guide
title: '[Deprecated] Deploy ScalarDB Server on Azure Kubernetes Service (AKS)'
description: This guide explains how to deploy ScalarDB Server on Azure Kubernetes Service (AKS).
resource: https://scalardb.scalar-labs.com/docs/3.16/scalar-kubernetes/ManualDeploymentGuideScalarDBServerOnAKS/
tags:
- scalardb
- v3.16
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
- feature-status:deprecated
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: scalar-kubernetes/ManualDeploymentGuideScalarDBServerOnAKS
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
feature_status:
- Deprecated
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/scalar-kubernetes/ManualDeploymentGuideScalarDBServerOnAKS.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# [Deprecated] Deploy ScalarDB Server on Azure Kubernetes Service (AKS)

This guide explains how to deploy ScalarDB Server on Azure Kubernetes Service (AKS).

In this guide, you will create one of the following two environments in your Azure environment. The difference between the two environments is how you plan to deploy the application:

* Deploy your application in the same AKS cluster as your ScalarDB Server deployment. In this case, you don't need to use the load balancers that Azure provides to access Scalar Envoy from your application.

  ![image](https://scalardb.scalar-labs.com/docs/3.16/scalar-kubernetes/images/png/AKS_ScalarDB_Server_App_In_Cluster.drawio.png)

* Deploy your application in an environment that is different from the AKS cluster that contains your ScalarDB Server deployment. In this case, you must use the load balancers that Azure provides to access Scalar Envoy from your application.

  ![image](https://scalardb.scalar-labs.com/docs/3.16/scalar-kubernetes/images/png/AKS_ScalarDB_Server_App_Out_Cluster.drawio.png)

## Step 1. Create an AKS cluster

You must create an AKS cluster for the ScalarDB Server deployment. For details, see [Guidelines for creating an AKS cluster for Scalar products](./CreateAKSClusterForScalarProducts.md).

## Step 2. Set up a database for ScalarDB Server

You must prepare a database before deploying ScalarDB Server. To see which types of databases ScalarDB supports, refer to [ScalarDB Supported Databases](https://scalardb.scalar-labs.com/docs/latest/requirements#databases).

For details on setting up a database, see [Set up a database for ScalarDB/ScalarDL deployment in Azure](./SetupDatabaseForAzure.md).

## Step 3. Create a bastion server

To execute some tools for deploying and managing ScalarDB Server on AKS, you must prepare a bastion server in the same Azure Virtual Network (VNet) of the AKS cluster that you created in **Step 1**.  For details, see [Create a Bastion Server](./CreateBastionServer.md).

## Step 4. Prepare a custom values file for the Scalar Helm Chart

To perform tasks, like accessing information in the database that you created in **Step 2**, you must configure a custom values file for the Scalar Helm Chart for ScalarDB Server based on your environment. For details, see [Configure a custom values file of Scalar Helm Chart](../helm-charts/configure-custom-values-file.md).

**Note:** If you deploy your application in an environment that is different from the AKS cluster that has your ScalarDB Server deployment, you must set the `envoy.service.type` parameter to `LoadBalancer` to access Scalar Envoy from your application.

## Step 5. Deploy ScalarDB Server by using the Scalar Helm Chart

Deploy ScalarDB Server on your AKS cluster by using the Helm Chart for ScalarDB Server. For details, see [Deploy Scalar Products using Scalar Helm Chart](../helm-charts/how-to-deploy-scalar-products.md).

**Note:** We recommend creating a dedicated namespace by using the `kubectl create ns scalardb` command and deploying ScalarDB Server in the namespace by using the `-n scalardb` option with the `helm install` command.

## Step 6. Check the status of your ScalarDB Server deployment

After deploying ScalarDB Server in your AKS cluster, you must check the status of each component. For details, see [Components to Regularly Check When Running in a Kubernetes Environment](./RegularCheck.md).

## Step 7. Monitor your ScalarDB Server deployment

After deploying ScalarDB Server in your AKS cluster, we recommend monitoring the deployed components and collecting their logs, especially in production. For details, see [Monitoring Scalar products on a Kubernetes cluster](./K8sMonitorGuide.md) and [Collecting logs from Scalar products on a Kubernetes cluster](./K8sLogCollectionGuide.md).

## Remove ScalarDB Server from AKS

If you want to remove the environment that you created, please remove all the resources in reverse order from which you created them in.
