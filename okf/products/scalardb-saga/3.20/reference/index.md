---
type: Documentation Section
title: ScalarDB Saga 3.20 — Reference
description: Directory listing for the `reference` section of the ScalarDB Saga 3.20 documentation.
resource: https://github.com/scalar-labs/scalardb-saga/tree/5765e9e6b1d499dc92627b387a711d306bdc6ce7
tags:
- scalardb-saga
- v3.20
- index
status: stable
product: scalardb-saga
version: '3.20'
generated:
  by: process:okf-build/1.0.0
  at: '2026-10-31T09:31:26Z'
---

# Reference

ScalarDB Saga 3.20 reference material generated from the files that define the contract in the source repository.

## Concepts

- [Admin gRPC API](./grpc-admin-api.md) — The AdminService gRPC contract — listing, recovering, force-completing and resetting sagas that need operator intervention.
- [Saga definition examples](./saga-definitions.md) — Working saga definitions from the repository: declarative service steps in JSON, and code steps (stepClass) in YAML and JSON.
- [Saga gRPC API](./grpc-saga-api.md) — The SagaService gRPC contract — starting a saga, awaiting it, and reading its snapshot and event history — as defined in saga.proto.
- [Server configuration reference](./server-configuration.md) — Every scalar.db.saga.server.* property the saga server accepts, with its default and the reasoning behind it, as shipped in the image's configuration template.
