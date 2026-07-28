---
type: Deployment Guide
title: Collecting logs from Scalar products on a Kubernetes cluster
description: This document explains how to deploy Grafana Loki and Promtail on Kubernetes with Helm. After following this document, you can collect logs of Scalar products on your Kubernetes environment.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalar-kubernetes/K8sLogCollectionGuide/
tags:
- scalardb
- v3.16
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: scalar-kubernetes/K8sLogCollectionGuide
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/scalar-kubernetes/K8sLogCollectionGuide.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Collecting logs from Scalar products on a Kubernetes cluster

This document explains how to deploy Grafana Loki and Promtail on Kubernetes with Helm. After following this document, you can collect logs of Scalar products on your Kubernetes environment.

If you use a managed Kubernetes cluster and you want to use the cloud service features for monitoring and logging, please refer to the following document.

* [Logging and monitoring on Amazon EKS](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/amazon-eks-logging-monitoring.html)
* [Monitoring Azure Kubernetes Service (AKS) with Azure Monitor](https://learn.microsoft.com/en-us/azure/aks/monitor-aks)

## Prerequisites

* Create a Kubernetes cluster.
* [Create an EKS cluster for Scalar products](./CreateEKSClusterForScalarProducts.md)
* [Create an AKS cluster for Scalar products](./CreateAKSClusterForScalarProducts.md)
* Create a Bastion server and set `kubeconfig`.
* [Create a bastion server](./CreateBastionServer.md)
* Deploy Prometheus Operator (we use Grafana to explore collected logs)
* [Monitoring Scalar products on the Kubernetes cluster](./K8sMonitorGuide.md)

## Add the grafana helm repository

This document uses Helm for the deployment of Prometheus Operator.

```console
helm repo add grafana https://grafana.github.io/helm-charts
```
```console
helm repo update
```

## Prepare a custom values file

Please get the sample file [scalar-loki-stack-custom-values.yaml](https://github.com/scalar-labs/scalar-kubernetes/blob/master/conf/scalar-loki-stack-custom-values.yaml) for loki-stack. For the logging of Scalar products, this sample file's configuration is recommended.

### Set nodeSelector in the custom values file (Optional)

You might need to set nodeSelector in the custom values file (scalar-loki-stack-custom-values.yaml) as follows if you add labels to your Kubernetes worker node. See the following examples based on the product you're using.

**ScalarDB**

Select the ScalarDB product you're using.

**ScalarDB Cluster**

```yaml
promtail:
  nodeSelector:
    scalar-labs.com/dedicated-node: scalardb-cluster
```

**ScalarDB Server (deprecated)**

```yaml
promtail:
  nodeSelector:
    scalar-labs.com/dedicated-node: scalardb
```

**ScalarDL**

Select the ScalarDL product you're using.

**ScalarDL Ledger**

```yaml
promtail:
  nodeSelector:
    scalar-labs.com/dedicated-node: scalardl-ledger
```

**ScalarDL Auditor**

```yaml
promtail:
  nodeSelector:
    scalar-labs.com/dedicated-node: scalardl-auditor
```

### Set tolerations in the custom values file (Optional)

You might need to set tolerations in the custom values file (scalar-loki-stack-custom-values.yaml) as follows if you add taints to your Kubernetes worker node. See the following examples based on the product you're using.

**ScalarDB**

Select the ScalarDB product you're using.

**ScalarDB Cluster**

```yaml
promtail:
  tolerations:
    - effect: NoSchedule
      key: scalar-labs.com/dedicated-node
      operator: Equal
      value: scalardb-cluster
```

**ScalarDB Server (deprecated)**

```yaml
promtail:
  tolerations:
    - effect: NoSchedule
      key: scalar-labs.com/dedicated-node
      operator: Equal
      value: scalardb
```

**ScalarDL**

Select the ScalarDL product you're using.

**ScalarDL Ledger**

```yaml
promtail:
  tolerations:
    - effect: NoSchedule
      key: scalar-labs.com/dedicated-node
      operator: Equal
      value: scalardl-ledger
```

**ScalarDL Auditor**

```yaml
promtail:
  tolerations:
    - effect: NoSchedule
      key: scalar-labs.com/dedicated-node
      operator: Equal
      value: scalardl-auditor
```

## Deploy Loki and Promtail

It is recommended to deploy Loki and Promtail on the same namespace `monitoring` as Prometheus and Grafana. You have already created the `monitoring` namespace in the document [Monitoring Scalar products on the Kubernetes cluster](./K8sMonitorGuide.md).

```console
helm install scalar-logging-loki grafana/loki-stack -n monitoring -f scalar-loki-stack-custom-values.yaml
```

## Check if Loki and Promtail are deployed

If the Loki and Promtail pods are deployed properly, you can see the `STATUS` is `Running` using the `kubectl get pod -n monitoring` command. Since promtail pods are deployed as DaemonSet, the number of promtail pods depends on the number of Kubernetes nodes. In the following example, there are three worker nodes for Scalar products in the Kubernetes cluster.

```console
kubectl get pod -n monitoring
```

You should see the following output:

```console
NAME                                 READY   STATUS    RESTARTS   AGE
scalar-logging-loki-0                1/1     Running   0          35m
scalar-logging-loki-promtail-2fnzn   1/1     Running   0          32m
scalar-logging-loki-promtail-2pwkx   1/1     Running   0          30m
scalar-logging-loki-promtail-gfx44   1/1     Running   0          32m
```

## View log in Grafana dashboard

You can see the collected logs in the Grafana dashboard as follows.

1. Access the Grafana dashboard
1. Go to the `Explore` page
1. Select `Loki` from the top left pull-down
1. Set conditions to query logs
1. Select the `Run query` button at the top right

Please refer to the [Monitoring Scalar products on the Kubernetes cluster](./K8sMonitorGuide.md) for more details on how to access the Grafana dashboard.
