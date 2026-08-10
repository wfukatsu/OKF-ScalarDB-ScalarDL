---
type: Operations Guide
title: Monitor Overview
description: 'Scalar Manager is a centralized management and monitoring solution for ScalarDL within Kubernetes cluster environments that allows you to:'
resource: https://scalardl.scalar-labs.com/docs/3.13/manage-monitor-overview/
tags:
- scalardl
- v3.13
- phase:operate
- section:manage
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: manage-monitor-overview
lifecycle_phase: operate
breadcrumb:
- Manage
- Monitor
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-10T20:40:03Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/03da04b21c1a7ce3eb94d9e29129a0ce194ecbeb/versioned_docs/version-3.13/manage-monitor-overview.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-07T17:27:19Z'
---

# Monitor Overview

Scalar Manager is a centralized management and monitoring solution for ScalarDL within Kubernetes cluster environments that allows you to:

- Check the availability of ScalarDL.
- Schedule or execute pausing jobs that create transactionally consistent periods in the databases used by ScalarDL.
- Check the time-series metrics and logs of ScalarDL through Grafana dashboards.

:::note

ScalarDL uses ScalarDB for its data management and the Function feature, so you may experience a case where you're using both ScalarDL and ScalarDB in your deployment. In such a case, you may also want to monitor ScalarDB in addition to ScalarDL.

:::

## Deploy Scalar Manager

You can deploy Scalar Manager by using a Helm Chart.

For details on how to deploy Scalar Manager, see [Deploy Scalar Manager](./helm-charts/getting-started-scalar-manager.md).
