---
type: Operations Guide
title: Monitor Overview
description: Monitoring is essential for maintaining the health and performance of your ScalarDL deployment. This section provides guidance on monitoring ScalarDL in Kubernetes cluster environments, including checking system availability, collecting...
resource: https://scalardl.scalar-labs.com/docs/latest/manage-monitor-overview/
tags:
- scalardl
- v3.14
- phase:operate
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.14'
patch_version: 3.14.1
doc_id: manage-monitor-overview
lifecycle_phase: operate
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-10-19T03:33:17Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/ab50260c7f47836bf097214504c93c86e6c2430d/docs/manage-monitor-overview.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-10-16T03:36:21Z'
---

# Monitor Overview

Monitoring is essential for maintaining the health and performance of your ScalarDL deployment. This section provides guidance on monitoring ScalarDL in Kubernetes cluster environments, including checking system availability, collecting time-series metrics, and viewing logs through monitoring dashboards.

:::note

ScalarDL uses ScalarDB for its data management and the Function feature, so you may experience a case where you're using both ScalarDL and ScalarDB in your deployment. In such a case, you may also want to monitor ScalarDB in addition to ScalarDL.

:::
