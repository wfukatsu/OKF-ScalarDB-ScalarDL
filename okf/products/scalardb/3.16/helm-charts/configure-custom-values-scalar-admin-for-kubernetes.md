---
type: Deployment Guide
title: Configure a custom values file for Scalar Admin for Kubernetes
description: This document explains how to create your custom values file for the Scalar Admin for Kubernetes chart. For details on the parameters, see the README of the Scalar Admin for Kubernetes chart.
resource: https://scalardb.scalar-labs.com/docs/3.16/helm-charts/configure-custom-values-scalar-admin-for-kubernetes/
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
doc_id: helm-charts/configure-custom-values-scalar-admin-for-kubernetes
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
- Configuration Guides
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/helm-charts/configure-custom-values-scalar-admin-for-kubernetes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Configure a custom values file for Scalar Admin for Kubernetes

This document explains how to create your custom values file for the Scalar Admin for Kubernetes chart. For details on the parameters, see the [README](https://github.com/scalar-labs/helm-charts/blob/main/charts/scalar-admin-for-kubernetes/README.md) of the Scalar Admin for Kubernetes chart.

## Required configurations

This section explains the required configurations when setting up a custom values file for Scalar Admin for Kubernetes.

### Flag configurations

You must specify several flags to `scalarAdminForKubernetes.commandArgs` as an array to run Scalar Admin for Kubernetes. For more details on the flags, see [README](https://github.com/scalar-labs/scalar-admin-for-kubernetes/blob/main/README.md) of Scalar Admin for Kubernetes.

```yaml
scalarAdminForKubernetes:
  commandArgs:
    - -r
    - <HELM_RELEASE_NAME>
    - -n
    - <SCALAR_PRODUCT_NAMESPACE>
    - -d
    - <PAUSE_DURATION>
    - -z
    - <TIMEZONE>
```

## Optional configurations

This section explains the optional configurations when setting up a custom values file for Scalar Admin for Kubernetes.

### CronJob configurations (optional based on your environment)

By default, the Scalar Admin for Kubernetes chart creates a [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/) resource to run the Scalar Admin for Kubernetes CLI tool once. If you want to run the Scalar Admin for Kubernetes CLI tool periodically by using [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/), you can set `scalarAdminForKubernetes.jobType` to `cronjob`. Also, you can set some configurations for the CronJob resource.

```yaml
scalarAdminForKubernetes:
  cronJob:
    timeZone: "Etc/UTC"
    schedule: "0 0 * * *"
```

### Resource configurations (recommended in production environments)

To control pod resources by using requests and limits in Kubernetes, you can use `scalarAdminForKubernetes.resources`.

You can configure requests and limits by using the same syntax as requests and limits in Kubernetes. For more details on requests and limits in Kubernetes, see [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

```yaml
scalarAdminForKubernetes:
  resources:
    requests:
      cpu: 1000m
      memory: 2Gi
    limits:
      cpu: 2000m
      memory: 4Gi
```

### SecurityContext configurations (default value is recommended)

To set SecurityContext and PodSecurityContext for Scalar Admin for Kubernetes pods, you can use `scalarAdminForKubernetes.securityContext` and `scalarAdminForKubernetes.podSecurityContext`.

You can configure SecurityContext and PodSecurityContext by using the same syntax as SecurityContext and PodSecurityContext in Kubernetes. For more details on the SecurityContext and PodSecurityContext configurations in Kubernetes, see [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

```yaml
scalarAdminForKubernetes:
  podSecurityContext:
    seccompProfile:
      type: RuntimeDefault
  securityContext:
    capabilities:
      drop:
        - ALL
    runAsNonRoot: true
    allowPrivilegeEscalation: false
```

### Image configurations (default value is recommended)

If you want to change the image repository, you can use `scalarAdminForKubernetes.image.repository` to specify the container repository information of the Scalar Admin for Kubernetes image that you want to pull.

```yaml
scalarAdminForKubernetes:
  image:
    repository: <SCALAR_ADMIN_FOR_KUBERNETES_CONTAINER_IMAGE>
```

### Taint and toleration configurations (optional based on your environment)

If you want to control pod deployment by using taints and tolerations in Kubernetes, you can use `scalarAdminForKubernetes.tolerations`.

You can configure taints and tolerations by using the same syntax as the tolerations in Kubernetes. For details on configuring tolerations in Kubernetes, see the official Kubernetes documentation [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

```yaml
scalarAdminForKubernetes:
  tolerations:
    - effect: NoSchedule
      key: scalar-labs.com/dedicated-node
      operator: Equal
      value: scalardb-cluster
```

### TLS configurations (optional based on your environment)

You can enable TLS between Scalar Admin for Kubernetes and the pause targets (ScalarDB Cluster or ScalarDL) by using the following configurations:

```yaml
scalarAdminForKubernetes:
  commandArgs:
    - (omit other options)
    - --tls
    - --ca-root-cert-path
    - /tls/certs/ca.crt
    - --override-authority
    - cluster.scalardb.example.com
```

You can mount the `/tls/certs/ca.crt` file on a pod by using a secret resource. To mount the file, specify the name of the secret resource that includes the root CA certificate file to `scalarAdminForKubernetes.tls.caRootCertSecret` as follows:

```yaml
scalarAdminForKubernetes:
  tls:
    caRootCertSecret: "scalar-admin-tls-ca"
```

In this case, you have to create a secret resource that includes the root CA certificate file for the pause targets (ScalarDB Cluster or ScalarDL) as follows:

```console
kubectl create secret generic scalar-admin-tls-ca --from-file=ca.crt=/path/to/your/ca/certificate/file -n <NAMESPACE>
```
