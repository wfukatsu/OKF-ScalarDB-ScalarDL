---
type: Release Notes
title: ScalarDL 3.13 Release Notes
description: This page includes a list of release notes for ScalarDL 3.13.
resource: https://scalardl.scalar-labs.com/docs/latest/releases/release-notes/
tags:
- scalardl
- v3.13
- phase:operate
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: releases/release-notes
lifecycle_phase: operate
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:59Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/docs/releases/release-notes.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# ScalarDL 3.13 Release Notes

This page includes a list of release notes for ScalarDL 3.13.

## v3.13.0

**Release date:** March 25, 2026

### Summary

This release introduces several enhancements related to the namespace feature and includes several improvements and bug fixes. For detailed changes, see the following.

### Community and Enterprise editions

#### Enhancements

- Added support for namespace management functionalities. ([#322](https://github.com/scalar-labs/scalardl/pull/322), [#345](https://github.com/scalar-labs/scalardl/pull/345), [#387](https://github.com/scalar-labs/scalardl/pull/387), [#392](https://github.com/scalar-labs/scalardl/pull/392))
- Added support for namespace-aware contract execution. ([#357](https://github.com/scalar-labs/scalardl/pull/357))
- Added support for isolated namespaces. ([#430](https://github.com/scalar-labs/scalardl/pull/430))

#### Improvements

- Upgraded server-side Java versions to Java 21. ([#395](https://github.com/scalar-labs/scalardl/pull/395))

#### Bug fixes

- Fixed the JSON Schema Validator repository and version. ([#277](https://github.com/scalar-labs/scalardl/pull/277))
- Fixed bugs to handle FLOAT and BLOB data types in the PutToMutable function. ([#297](https://github.com/scalar-labs/scalardl/pull/297))
- Fixed NullPointerException when a client is misconfigured with a digital signature. ([#302](https://github.com/scalar-labs/scalardl/pull/302))
- Fixed status code handling. ([#323](https://github.com/scalar-labs/scalardl/pull/323))
- Fixed the parameter name for the client entity ID. ([#376](https://github.com/scalar-labs/scalardl/pull/376))
- Fixed a bug where users cannot register a custom ValidateLedger contract after bootstrapping. ([#404](https://github.com/scalar-labs/scalardl/pull/404))
- Fixed [CVE-2025-47907](https://github.com/advisories/GHSA-j5pm-7495-qmr3 "CVE-2025-47907") and [CVE-2025-58183](https://github.com/advisories/GHSA-9gcr-gp5f-jw27 "CVE-2025-58183"). ([#364](https://github.com/scalar-labs/scalardl/pull/364))
- Fixed [CVE-2025-61726](https://github.com/advisories/GHSA-gm9r-q53w-2gh4 "CVE-2025-61726"), [CVE-2025-61728](https://github.com/advisories/GHSA-g9q4-qjx4-2v7q "CVE-2025-61728"), [CVE-2025-61729](https://github.com/advisories/GHSA-7c64-f9jr-v9h2 "CVE-2025-61729") and [CVE-2025-68121](https://github.com/advisories/GHSA-h355-32pf-p2xm "CVE-2025-68121"). ([#472](https://github.com/scalar-labs/scalardl/pull/472))

### Enterprise edition

#### Bug fixes

- Fixed duplicated read lock.
- Fixed Gateway exception handling.
- Fixed an SLF4J version conflict in BYOL Docker images.
