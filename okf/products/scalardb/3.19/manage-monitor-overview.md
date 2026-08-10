---
type: Operations Guide
title: Monitor Overview
description: 'Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:'
resource: https://scalardb.scalar-labs.com/docs/latest/manage-monitor-overview/
tags:
- scalardb
- v3.19
- phase:operate
- edition:enterprise-option
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.0
doc_id: manage-monitor-overview
lifecycle_phase: operate
editions:
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-10T20:39:58Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/8bb9295f8fbd8a042360ebb5a3e70f8c4e5dfa47/docs/manage-monitor-overview.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-07T16:37:01Z'
---

# Monitor Overview

Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:

- Check the availability of ScalarDB.
- Schedule or execute pausing jobs that create transactionally consistent periods in the databases used by ScalarDB.
- Check the time-series metrics and logs of ScalarDB through Grafana dashboards.

:::note

If you haven't already deployed Scalar Manager, you can do so with a Helm Chart. For details, see [Deploy Scalar Manager](./helm-charts/getting-started-scalar-manager.md).

:::
