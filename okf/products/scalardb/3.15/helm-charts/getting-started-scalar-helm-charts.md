---
type: Deployment Guide
title: Getting Started with Scalar Helm Charts
description: This document explains how to get started with Scalar Helm Chart on a Kubernetes cluster as a test environment. Here, we assume that you already have a Mac or Linux environment for testing. We use Minikube in this document, but the steps...
resource: https://scalardb.scalar-labs.com/docs/3.15/helm-charts/getting-started-scalar-helm-charts/
tags:
- scalardb
- v3.15
- phase:operate
- section:deploy
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.15'
patch_version: 3.15.8
doc_id: helm-charts/getting-started-scalar-helm-charts
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
- Getting Started Guides
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:02Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.15/helm-charts/getting-started-scalar-helm-charts.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Getting Started with Scalar Helm Charts

This document explains how to get started with Scalar Helm Chart on a Kubernetes cluster as a test environment. Here, we assume that you already have a Mac or Linux environment for testing. We use **Minikube** in this document, but the steps we will show should work in any Kubernetes cluster.

## Tools

We will use the following tools for testing.

1. minikube (If you use other Kubernetes distributions, minikube is not necessary.)
1. kubectl
1. Helm
1. cfssl / cfssljson

## Step 1. Install tools

First, you need to install the following tools used in this guide.

1. Install the `minikube` command according to the [minikube documentation](https://minikube.sigs.k8s.io/docs/start/)

1. Install the `kubectl` command according to the [Kubernetes documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

1. Install the `helm` command according to the [Helm documentation](https://helm.sh/docs/intro/install/)

1. Install the `cfssl` and `cfssljson` according to the [CFSSL documentation](https://github.com/cloudflare/cfssl)

:::note

You need to install the `cfssl` and `cfssljson` command when following these getting started guides:

* [ScalarDB Cluster with TLS](./getting-started-scalardb-cluster-tls.md)
* [ScalarDL Ledger and Auditor with TLS (Auditor mode)](./getting-started-scalardl-auditor-tls.md)
* [ScalarDL Ledger (Ledger only)](./getting-started-scalardl-ledger.md)
* [ScalarDL Ledger and Auditor (Auditor mode)](./getting-started-scalardl-auditor.md)

:::

## Step 2. Start minikube with docker driver (Optional / If you use minikube)

1. Start minikube.
```console
minikube start
```

1. Check the status of the minikube and pods.
```console
kubectl get pod -A
```
   [Command execution result]
```console
NAMESPACE     NAME                               READY   STATUS    RESTARTS      AGE
kube-system   coredns-64897985d-lbsfr            1/1     Running   1 (20h ago)   21h
kube-system   etcd-minikube                      1/1     Running   1 (20h ago)   21h
kube-system   kube-apiserver-minikube            1/1     Running   1 (20h ago)   21h
kube-system   kube-controller-manager-minikube   1/1     Running   1 (20h ago)   21h
kube-system   kube-proxy-gsl6j                   1/1     Running   1 (20h ago)   21h
kube-system   kube-scheduler-minikube            1/1     Running   1 (20h ago)   21h
kube-system   storage-provisioner                1/1     Running   2 (19s ago)   21h
```
   If the minikube starts properly, you can see some pods are **Running** in the kube-system namespace.

## Step 3.

After the Kubernetes cluster starts, you can try each Scalar Helm Charts on it. Please refer to the following documents for more details.

* [ScalarDB Cluster with TLS](./getting-started-scalardb-cluster-tls.md)
* [ScalarDB Cluster with TLS by Using cert-manager](./getting-started-scalardb-cluster-tls-cert-manager.md)
* [ScalarDL Ledger and Auditor with TLS (Auditor mode)](./getting-started-scalardl-auditor-tls.md)
* [ScalarDL Ledger and Auditor with TLS by Using cert-manager (Auditor mode)](./getting-started-scalardl-auditor-tls-cert-manager.md)
* [ScalarDL Ledger (Ledger only)](./getting-started-scalardl-ledger.md)
* [ScalarDL Ledger and Auditor (Auditor mode)](./getting-started-scalardl-auditor.md)
* [Monitoring using Prometheus Operator](./getting-started-monitoring.md)
  * [Logging using Loki Stack](./getting-started-logging.md)
  * [Scalar Manager](./getting-started-scalar-manager.md)
* [[Deprecated] ScalarDB Server](./getting-started-scalardb.md)
