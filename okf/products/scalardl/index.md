---
type: Product
title: ScalarDL
description: Byzantine-fault-detection middleware that makes database state tamper-evident.
resource: https://scalardl.scalar-labs.com/docs/
tags:
- scalardl
- product
status: stable
product: scalardl
versions:
- '3.13'
- '3.12'
- '3.11'
- '3.10'
latest_version: '3.13'
supported_versions:
- '3.13'
- '3.12'
- '3.11'
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/tree/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4
  title: ScalarDL documentation repository
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# ScalarDL

Byzantine-fault-detection middleware that makes database state tamper-evident. Covers contracts and functions, Ledger and Auditor deployment, certificate/HMAC authentication and operations.

## Versions

| Version | Newest patch | Maintenance | Concepts | Docs |
|---|---|---|---|---|
| [3.13 (latest)](./3.13/index.md) | 3.13.0 | supported | 143 | https://scalardl.scalar-labs.com/docs/latest/ |
| [3.12](./3.12/index.md) | 3.12.3 | supported | 141 | https://scalardl.scalar-labs.com/docs/3.12/ |
| [3.11](./3.11/index.md) | 3.11.3 | supported | 132 | https://scalardl.scalar-labs.com/docs/3.11/ |
| [3.10](./3.10/index.md) | 3.10.5 | unmaintained | 132 | https://scalardl.scalar-labs.com/docs/3.10/ |

## How to pick a version

1. Match the version to the ScalarDB/ScalarDL release the project actually runs.
2. If the project is greenfield, use the newest supported version.
3. Never mix guidance across versions — configuration keys, error codes and API signatures differ between minor releases.
