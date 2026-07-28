---
type: Deployment Guide
title: Create a bastion server
description: This document explains how to create a bastion server and install some tools for the deployment of Scalar products.
resource: https://scalardb.scalar-labs.com/docs/latest/scalar-kubernetes/CreateBastionServer/
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
doc_id: scalar-kubernetes/CreateBastionServer
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:24Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/docs/scalar-kubernetes/CreateBastionServer.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Create a bastion server

This document explains how to create a bastion server and install some tools for the deployment of Scalar products.

## Create a server on the same private network as a Kubernetes cluster

It is recommended to create a Kubernetes cluster for Scalar products on a private network. If you create a Kubernetes cluster on a private network, you should create a bastion server on the same private network to access your Kubernetes cluster.

## Install tools

Please install the following tools on the bastion server according to their official documents.

* [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)
* [helm](https://helm.sh/docs/intro/install/)

## Configure kubeconfig

After you install the kubectl command, you must configure a **kubeconfig** to access your Kubernetes cluster. Please refer to the following official document for more details on how to configure kubeconfig in each managed Kubernetes.

If you use Amazon EKS (Amazon Elastic Kubernetes Service), you must install the **AWS CLI** according to the official document [Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). After that, you can see how to configure kubeconfig in [Creating or updating a kubeconfig file for an Amazon EKS cluster](https://docs.aws.amazon.com/eks/latest/userguide/create-kubeconfig.html).

If you use AKS (Azure Kubernetes Service), you must install the **Azure CLI** according to the official document [How to install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli). After that, you can see how to configure kubeconfig in [az aks get-credentials](https://learn.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest#az-aks-get-credentials).

## Check installation

You can check if the tools are installed as follows.

* kubectl
```console
kubectl version --client
```
* helm
```console
helm version
```

You can also check if your kubeconfig is properly configured as follows. If you see a URL response, kubectl is correctly configured to access your cluster.
```console
kubectl cluster-info
```
