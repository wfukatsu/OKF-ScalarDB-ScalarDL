---
type: Deployment Guide
title: Configure Network Peering for ScalarDL Auditor Mode
description: This document explains how to connect multiple private networks for ScalarDL Auditor mode to perform network peering. For ScalarDL Auditor mode to work properly, you must connect ScalarDL Ledger to ScalarDL Auditor.
resource: https://scalardl.scalar-labs.com/docs/3.11/scalar-kubernetes/NetworkPeeringForScalarDLAuditor/
tags:
- scalardl
- v3.11
- phase:operate
- section:deploy
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.3
doc_id: scalar-kubernetes/NetworkPeeringForScalarDLAuditor
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
- Configuration Guides
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:02Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.11/scalar-kubernetes/NetworkPeeringForScalarDLAuditor.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Configure Network Peering for ScalarDL Auditor Mode

This document explains how to connect multiple private networks for ScalarDL Auditor mode to perform network peering. For ScalarDL Auditor mode to work properly, you must connect ScalarDL Ledger to ScalarDL Auditor.

## What network you must connect

To make ScalarDL Auditor mode (Byzantine fault detection) work properly, you must connect three private networks.

* [ScalarDL Ledger network] ↔ [ScalarDL Auditor network]
* [ScalarDL Ledger network] ↔ [application (client) network]
* [ScalarDL Auditor network] ↔ [application (client) network]

## Network requirements

### IP address ranges

To avoid conflicting IP addresses between the private networks, you must have private networks with different IP address ranges. For example:

* **Private network for ScalarDL Ledger:** 10.1.0.0/16
* **Private network for ScalarDL Auditor:** 10.2.0.0/16
* **Private network for application (client):** 10.3.0.0/16

### Connections

The default network ports for connecting ScalarDL Ledger, ScalarDL Auditor, and the application (client) by default are as follows. You must allow these connections between each private network.

* **ScalarDL Ledger**
* **50051/TCP:** Accept requests from an application (client) and ScalarDL Auditor via Scalar Envoy.
* **50052/TCP:** Accept privileged requests from an application (client) and ScalarDL Auditor via Scalar Envoy.
* **ScalarDL Auditor**
* **40051/TCP:** Accept requests from an application (client) and ScalarDL Ledger via Scalar Envoy.
* **40052/TCP:** Accept privileged requests from an application (client) and ScalarDL Ledger via Scalar Envoy.
* **Scalar Envoy** (used with ScalarDL Ledger and ScalarDL Auditor)
* **50051/TCP:** Accept requests for ScalarDL Ledger from an application (client) and ScalarDL Auditor.
* **50052/TCP:** Accept privileged requests for ScalarDL Ledger from an application (client) and ScalarDL Auditor.
* **40051/TCP:** Accept requests for ScalarDL Auditor from an application (client) and ScalarDL Ledger.
* **40052/TCP:** Accept privileged requests for ScalarDL Auditor from an application (client) and ScalarDL Ledger.

Note that, if you change the listening port for ScalarDL in the configuration file (ledger.properties or auditor.properties) from the default, you must allow the connections by using the port that you configured.

## Private-network peering

For details on how to connect private networks in each cloud, see official documents.

### Amazon VPC peering

For details on how to peer virtual private clouds (VPCs) in an Amazon Web Services (AWS) environment, see the official documentation from Amazon at [Create a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html).

### Azure VNet peering

For details on how to peer virtual networks in an Azure environment, see the official documentation from Microsoft at [Virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview).
