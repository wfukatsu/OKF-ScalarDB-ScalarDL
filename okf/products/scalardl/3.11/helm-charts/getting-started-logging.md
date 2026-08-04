---
type: Deployment Guide
title: Getting Started with Helm Charts (Logging using Loki Stack)
description: This document explains how to get started with log aggregation for Scalar products on Kubernetes using Grafana Loki (with Promtail).
resource: https://scalardl.scalar-labs.com/docs/3.11/helm-charts/getting-started-logging/
tags:
- scalardl
- v3.11
- phase:operate
- section:deploy
- edition:community
status: stable
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.3
doc_id: helm-charts/getting-started-logging
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
- Getting Started Guides
editions:
- Community
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:02Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.11/helm-charts/getting-started-logging.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Getting Started with Helm Charts (Logging using Loki Stack)

This document explains how to get started with log aggregation for Scalar products on Kubernetes using Grafana Loki (with Promtail).

We assume that you have already read the [getting-started with monitoring](./getting-started-monitoring.md) for Scalar products and installed kube-prometheus-stack.

## What we create

We will deploy the following components on a Kubernetes cluster as follows.

```
+--------------------------------------------------------------------------------------------------+
| +------------------------------------+                                                           |
| |             loki-stack             |                                                           |
| |                                    |                                       +-----------------+ |
| | +--------------+  +--------------+ | <-----------------(Log)-------------- | Scalar Products | |
| | |     Loki     |  |   Promtail   | |                                       |                 | |
| | +--------------+  +--------------+ |                                       |  +-----------+  | |
| +------------------------------------+                                       |  | ScalarDB  |  | |
|                                                                              |  +-----------+  | |
| +------------------------------------------------------+                     |                 | |
| |                kube-prometheus-stack                 |                     |  +-----------+  | |
| |                                                      |                     |  | ScalarDL  |  | |
| | +--------------+  +--------------+  +--------------+ | -----(Monitor)----> |  +-----------+  | |
| | |  Prometheus  |  | Alertmanager |  |   Grafana    | |                     +-----------------+ |
| | +-------+------+  +------+-------+  +------+-------+ |                                         |
| |         |                |                 |         |                                         |
| |         +----------------+-----------------+         |                                         |
| |                          |                           |                                         |
| +--------------------------+---------------------------+                                         |
|                            |                                                                     |
|                            |         Kubernetes                                                  |
+----------------------------+---------------------------------------------------------------------+
                             | <- expose to localhost (127.0.0.1) or use load balancer etc to access
                             |
              (Access Dashboard through HTTP)
                             |
                        +----+----+
                        | Browser |
                        +---------+
```

## Step 1. Prepare a custom values file

1. Get the sample file [scalar-loki-stack-custom-values.yaml](https://scalardl.scalar-labs.com/docs/3.11/helm-charts/conf/scalar-loki-stack-custom-values.yaml) for the `loki-stack` helm chart.

## Step 2. Deploy `loki-stack`

1. Add the `grafana` helm repository.
```console
helm repo add grafana https://grafana.github.io/helm-charts
```

1. Deploy the `loki-stack` helm chart.
```console
helm install scalar-logging-loki grafana/loki-stack -n monitoring -f scalar-loki-stack-custom-values.yaml
```

## Step 3. Add a Loki data source in the Grafana configuration

1. Add a configuration of the Loki data source in the `scalar-prometheus-custom-values.yaml` file.
```yaml
grafana:
  additionalDataSources:
  - name: Loki
    type: loki
    uid: loki
    url: http://scalar-logging-loki:3100/
    access: proxy
    editable: false
    isDefault: false
```

1. Apply the configuration (upgrade the deployment of `kube-prometheus-stack`).
```console
helm upgrade scalar-monitoring prometheus-community/kube-prometheus-stack -n monitoring -f scalar-prometheus-custom-values.yaml
```

## Step 4. Access the Grafana dashboard

1. Add Loki as a data source
   - Go to Grafana http://localhost:3000 (If you use minikube)
   - Go to `Explore` to find the added Loki
   - You can see the collected logs in the `Explore` page

## Step 5. Delete the `loki-stack` helm chart

1. Uninstall `loki-stack`.
```console
helm uninstall scalar-logging-loki -n monitoring
```
