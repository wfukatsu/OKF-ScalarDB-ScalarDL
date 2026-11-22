---
type: Documentation Section
title: ScalarDB PostgreSQL Frontend 3.20 — Reference
description: Directory listing for the `reference` section of the ScalarDB PostgreSQL Frontend 3.20 documentation.
resource: https://github.com/scalar-labs/scalardb-postgres-frontend/tree/d28a3ad131f99cc7a8f8f92bdff9621671d1dee8
tags:
- scalardb-postgres-frontend
- v3.20
- index
status: stable
product: scalardb-postgres-frontend
version: '3.20'
generated:
  by: process:okf-build/1.0.0
  at: '2026-11-22T03:58:44Z'
---

# Reference

ScalarDB PostgreSQL Frontend 3.20 reference material generated from the files that define the contract in the source repository.

## Concepts

- [Declared types in the frontend's metadata table](./type-encoding.md) — ScalarDB has no decimal type, no type modifiers and no metadata a client can attach to a column. So when a PostgreSQL client declares a type ScalarDB cannot hold as is, the frontend stores the value in a form that keeps it exact, under the...
