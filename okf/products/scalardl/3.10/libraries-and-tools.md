---
type: Reference
title: Libraries and Tools for ScalarDL
description: ScalarDL provides various libraries and tools to help you build and operate scalable and reliable applications. Below are some key libraries and tools available.
resource: https://scalardl.scalar-labs.com/docs/3.10/libraries-and-tools/
tags:
- scalardl
- v3.10
- phase:implement
- section:reference
- edition:community
- edition:enterprise
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.10'
patch_version: 3.10.5
doc_id: libraries-and-tools
lifecycle_phase: implement
breadcrumb:
- Reference
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:03Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.10/libraries-and-tools.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Libraries and Tools for ScalarDL

ScalarDL provides various libraries and tools to help you build and operate scalable and reliable applications. Below are some key libraries and tools available.

## Libraries

The following libraries are available for ScalarDL.

| Library                  | Edition                | Maven Package                                                                                              | Container Image | Reference                                                                    |
|--------------------------|------------------------|------------------------------------------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------|
| ScalarDL Java Client SDK | Community & Enterprise | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalardl-java-client-sdk) | N/A             | [Documentation](./how-to-write-applications.md#use-the-scalardl-client-sdk) |

## Tools

The following tools are available for ScalarDL.

| Tool                        | Edition                | Maven Package                                                                                                 | Container Image                                                                                      | Reference                                                                    |
|-----------------------------|------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| ScalarDL Client Command     | Community & Enterprise | N/A                                                                                                           | [GitHub](https://github.com/scalar-labs/scalardl/pkgs/container/scalardl-client)                     | [Documentation](./scalardl-command-reference.md)                            |
| ScalarDL Schema Loader      | Community & Enterprise | N/A                                                                                                           | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-schema-loader)      | [Documentation](./schema-loader.md)                                         |
| Helm Charts                 | Community & Enterprise | N/A                                                                                                           | N/A                                                                                                  | [Documentation](./helm-charts/getting-started-scalar-helm-charts.md)        |
| Scalar Admin for Kubernetes | Community & Enterprise | [Maven Central Repository](https://central.sonatype.com/artifact/com.scalar-labs/scalar-admin-for-kubernetes) | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalar-admin-for-kubernetes) | [Documentation](./helm-charts/how-to-deploy-scalar-admin-for-kubernetes.md) |

### Components

The following components are available for ScalarDL.

| Component               | Edition    | Container Image                                                                                | Reference                   |
|-------------------------|------------|------------------------------------------------------------------------------------------------|-----------------------------|
| ScalarDL Ledger         | Community  | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-ledger)       | Documentation (coming soon) |
| ScalarDL Ledger (BYOL)  | Enterprise | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-ledger-byol)  | Documentation (coming soon) |
| ScalarDL Auditor (BYOL) | Enterprise | [GitHub](https://github.com/orgs/scalar-labs/packages/container/package/scalardl-auditor-byol) | Documentation (coming soon) |
