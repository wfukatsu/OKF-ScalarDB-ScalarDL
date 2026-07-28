---
type: Deployment Guide
title: How to deploy ScalarDB Cluster
description: This document explains how to deploy ScalarDB Cluster by using Scalar Helm Charts. For details on the custom values file for ScalarDB Cluster, see Configure a custom values file for ScalarDB Cluster.
resource: https://scalardb.scalar-labs.com/docs/3.17/helm-charts/how-to-deploy-scalardb-cluster/
tags:
- scalardb
- v3.17
- phase:operate
- section:deploy
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.3
doc_id: helm-charts/how-to-deploy-scalardb-cluster
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
- Deployment Guides
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:26Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.17/helm-charts/how-to-deploy-scalardb-cluster.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to deploy ScalarDB Cluster

This document explains how to deploy ScalarDB Cluster by using Scalar Helm Charts. For details on the custom values file for ScalarDB Cluster, see [Configure a custom values file for ScalarDB Cluster](./configure-custom-values-scalardb-cluster.md).

## Deploy ScalarDB Cluster

```console
helm install <RELEASE_NAME> scalar-labs/scalardb-cluster -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_CLUSTER> --version <CHART_VERSION>
```

## Upgrade a ScalarDB Cluster deployment

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardb-cluster -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_CLUSTER> --version <CHART_VERSION>
```

## Delete a ScalarDB Cluster deployment

```console
helm uninstall <RELEASE_NAME> -n <NAMESPACE>
```

## Deploy your client application on Kubernetes with `direct-kubernetes` mode

If you use ScalarDB Cluster with `direct-kubernetes` mode, you must:

1. Deploy your application pods on the same Kubernetes cluster as ScalarDB Cluster.
2. Create three Kubernetes resources (`Role`, `RoleBinding`, and `ServiceAccount`).
3. Mount the `ServiceAccount` on your application pods.

This method is necessary because the ScalarDB Cluster client library with `direct-kubernetes` mode runs the Kubernetes API from inside of your application pods to get information about the ScalarDB Cluster pods.

* Role
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: scalardb-cluster-client-role
  namespace: <your namespace>
rules:
  - apiGroups: [""]
    resources: ["endpoints"]
    verbs: ["get", "watch", "list"]
```
* RoleBinding
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: scalardb-cluster-client-rolebinding
  namespace: <your namespace>
subjects:
  - kind: ServiceAccount
    name: scalardb-cluster-client-sa
roleRef:
  kind: Role
  name: scalardb-cluster-client-role
  apiGroup: rbac.authorization.k8s.io
```
* ServiceAccount
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: scalardb-cluster-client-sa
  namespace: <your namespace>
```
