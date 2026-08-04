---
type: Operations Guide
title: Monitor Overview
description: 'Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:'
resource: https://scalardb.scalar-labs.com/docs/3.15/manage-monitor-overview/
tags:
- scalardb
- v3.15
- phase:operate
- section:manage
- edition:enterprise-option
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.15'
patch_version: 3.15.9
doc_id: manage-monitor-overview
lifecycle_phase: operate
breadcrumb:
- Manage
- Monitor
editions:
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:56Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.15/manage-monitor-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Monitor Overview

Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:

- Check the availability of ScalarDB.
- Schedule or execute pausing jobs that create transactionally consistent periods in the databases used by ScalarDB.
- Check the time-series metrics and logs of ScalarDB through Grafana dashboards.

:::note

If you haven't already deployed Scalar Manager, you can do so with a Helm Chart. For details, see [Deploy Scalar Manager](./helm-charts/getting-started-scalar-manager.md).

:::
