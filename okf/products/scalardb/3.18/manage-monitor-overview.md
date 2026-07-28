---
type: Operations Guide
title: Monitor Overview
description: 'Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:'
resource: https://scalardb.scalar-labs.com/docs/latest/manage-monitor-overview/
tags:
- scalardb
- v3.18
- phase:operate
- edition:enterprise-option
status: stable
product: scalardb
product_title: ScalarDB
version: '3.18'
patch_version: 3.18.0
doc_id: manage-monitor-overview
lifecycle_phase: operate
editions:
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:24Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/docs/manage-monitor-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Monitor Overview

Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:

- Check the availability of ScalarDB.
- Schedule or execute pausing jobs that create transactionally consistent periods in the databases used by ScalarDB.
- Check the time-series metrics and logs of ScalarDB through Grafana dashboards.

## Deploy Scalar Manager

You can deploy Scalar Manager by using a Helm Chart.

For details on how to deploy Scalar Manager, see [Deploy Scalar Manager](./helm-charts/getting-started-scalar-manager.md).
