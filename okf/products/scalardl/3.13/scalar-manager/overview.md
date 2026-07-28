---
type: Operations Guide
title: Scalar Manager Overview
description: Scalar Manager is a centralized management and monitoring solution for ScalarDL within Kubernetes cluster environments. It simplifies the operational tasks associated with these products by aggregating essential functionalities into a...
resource: https://scalardl.scalar-labs.com/docs/latest/scalar-manager/overview/
tags:
- scalardl
- v3.13
- phase:operate
- edition:enterprise-option
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: scalar-manager/overview
lifecycle_phase: operate
editions:
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/scalar-manager/overview.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Scalar Manager Overview

Scalar Manager is a centralized management and monitoring solution for ScalarDL within Kubernetes cluster environments.
It simplifies the operational tasks associated with these products by aggregating essential functionalities into a graphical user interface (GUI).

## Why Scalar Manager?

Before Scalar Manager was released, you would need to use various command-line tools and third-party solutions individually to manage and monitor ScalarDL deployments.
For example, `kubectl` is often used to check deployment status, the Prometheus stack for monitoring metrics, the Loki stack for log analysis, and Scalar's proprietary CLI tool for pausing ScalarDL to ensure transactional consistency between multiple databases.
This constellation of tools presented a steep learning curve and lacked a unified interface, resulting in inefficient workflows for performing routine management tasks or troubleshooting issues.

Scalar Manager mitigates these pain points by aggregating essential functionalities into a single, user-friendly GUI.
With Scalar Manager, you can reduce the time and effort needed for management and monitoring, allowing you to focus on business development and operations.

## Key features

At its core, Scalar Manager provides the following features.

### Centralized cluster visualization

You can quickly gain real-time metrics about cluster health, pod logs, hardware usage, performance metrics like requests per second, and deep visibility into time-series data via the Grafana dashboards.

![dashboard-cluster](https://scalardl.scalar-labs.com/docs/latest/scalar-manager/images/dashboard-cluster.png)
![dashboard-pod-list](https://scalardl.scalar-labs.com/docs/latest/scalar-manager/images/dashboard-pod-list.png)

With the Grafana dashboards, you can also view pod logs and metrics in real-time or in time series.

![logs](https://scalardl.scalar-labs.com/docs/latest/scalar-manager/images/logs.png)
![metrics](https://scalardl.scalar-labs.com/docs/latest/scalar-manager/images/metrics2.png)

### Streamlined pausing job management

You can execute or schedule pausing jobs to ensure transactional consistency, review and manage scheduled jobs, and monitor paused states within an intuitive GUI.

![create-pauses](https://scalardl.scalar-labs.com/docs/latest/scalar-manager/images/backup-and-restore-create-pauses.png)
![check-pauses](https://scalardl.scalar-labs.com/docs/latest/scalar-manager/images/backup-and-restore-check-pauses.png)

### User management

Scalar Manager includes authentication capabilities, allowing for secure access control to your deployment. The system provides user management functionalities that enable administrators to create, modify, and remove user accounts through an intuitive interface.

### Authentication and authorization

By using the authorization feature, administrators can define and assign specific roles to users, controlling their access permissions within the Scalar Manager environment. This control ensures that users only have access to the functionalities relevant to their responsibilities.

### Integrated authentication with Grafana

Scalar Manager now offers seamless authentication integration between your Grafana instance and other components of the system. This single-sign-on capability eliminates the need for multiple authentication processes, streamlining the user experience and enhancing security by reducing credential management overhead.

## Required port

Scalar Manager requires port 13000 to be accessible.
