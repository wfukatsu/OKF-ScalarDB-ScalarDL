---
type: Operations Guide
title: Monitor Overview
description: 'Scalar Manager is a centralized management and monitoring solution for ScalarDL within Kubernetes cluster environments that allows you to:'
resource: https://scalardl.scalar-labs.com/docs/latest/manage-monitor-overview/
tags:
- scalardl
- v3.13
- phase:operate
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: manage-monitor-overview
lifecycle_phase: operate
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/manage-monitor-overview.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
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
