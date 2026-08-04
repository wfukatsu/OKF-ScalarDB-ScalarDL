---
type: Concept
title: ScalarDL Roadmap
description: This roadmap provides a look into the proposed future of ScalarDL. The purpose of this roadmap is to provide visibility into what changes may be coming so that you can more closely follow progress, learn about key milestones, and give...
resource: https://scalardl.scalar-labs.com/docs/3.11/roadmap/
tags:
- scalardl
- v3.11
- phase:design
- section:about-scalardl
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.3
doc_id: roadmap
lifecycle_phase: design
breadcrumb:
- About ScalarDL
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:02Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.11/roadmap.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# ScalarDL Roadmap

This roadmap provides a look into the proposed future of ScalarDL. The purpose of this roadmap is to provide visibility into what changes may be coming so that you can more closely follow progress, learn about key milestones, and give feedback during development. This roadmap will be updated as new versions of ScalarDL are released.

:::warning

During the course of development, this roadmap is subject to change based on user needs and feedback. **Do not schedule your release plans according to the contents of this roadmap.**

If you have a feature request or want to prioritize feature development, please create an issue in [GitHub](https://github.com/scalar-labs/scalardl/issues).

:::

### CY2025 Q4

#### New capabilities

- **SQL interface for generic contracts for tables**
- Users will be able to use SQL-like queries to access generic contracts for tables so that they can simplify their application development.

### CY2026 Q1

#### New capabilities

- **Namespaces**
- Users will be able to use namespaces to group assets so that they can better manage their data.

#### Usability

- **Java upgrade to version 21**
- Users will be able to run ScalarDL (except for the client SDK) on Java 21 so that they can use the latest features and improvements in Java.
- **Enable read operations during a paused duration.**
- Users will be able to issue read operations even during a paused duration so that users can still read data while taking backups.

#### Cloud support

- **Google Cloud Platform (GCP) support**
- Users will be able to deploy ScalarDL by using the GCP marketplace offering, which enables users to use a pay-as-you-go subscription model.
- **Azure support**
- Users will be able to deploy ScalarDL by using the Azure marketplace offering, which enables users to use a pay-as-you-go subscription model.

### CY2026 Q2

#### New capabilities

- **Lifecycle management for assets**
- Users will be able to better manage the lifecycle of assets, ensuring they are preserved securely for an extended period.

#### Improvements

- **Encryption**
- Users will be able to encrypt their data so that they can manage their data in a more secure way.
- **Elimination of out-of-memory errors due to large scans**
- Users will be able to issue large scans without experiencing out-of-memory errors.

#### Cloud support

- **Red Hat OpenShift support**
- Users will be able to use Red Hat–certified Helm Charts for ScalarDL in OpenShift environments.
- **AWS support**
- Users will be able to deploy ScalarDL by using the AWS marketplace offering, which enables users to use a pay-as-you-go subscription model.

### CY2026 Q3

#### Improvements

- **Performance optimizations**
- Users will be able to execute requests faster so that they can create ScalarDL applications in a more cost-effective way.

### CY2026 Q4 -

- **Lazy validation**
- Users will be able to validate the authenticity of their data lazily so that they can manage their data in a cost-effective way if their data doesn't need to be validated in real time.
