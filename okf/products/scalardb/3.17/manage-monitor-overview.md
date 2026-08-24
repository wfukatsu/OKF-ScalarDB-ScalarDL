---
type: Operations Guide
title: Monitor Overview
description: 'Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:'
resource: https://scalardb.scalar-labs.com/docs/3.17/manage-monitor-overview/
tags:
- scalardb
- v3.17
- phase:operate
- section:manage
- edition:enterprise-option
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.4
doc_id: manage-monitor-overview
lifecycle_phase: operate
breadcrumb:
- Manage
- Monitor
editions:
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-24T00:15:36Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/4fa644f40396f8d8f5d3d0d90c217b77ea0e70d1/versioned_docs/version-3.17/manage-monitor-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-20T18:31:06Z'
---

# Monitor Overview

Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:

- Check the availability of ScalarDB.
- Schedule or execute pausing jobs that create transactionally consistent periods in the databases used by ScalarDB.
- Check the time-series metrics and logs of ScalarDB through Grafana dashboards.

:::note

If you haven't already deployed Scalar Manager, you can do so with a Helm Chart. For details, see [Deploy Scalar Manager](./helm-charts/getting-started-scalar-manager.md).

:::
