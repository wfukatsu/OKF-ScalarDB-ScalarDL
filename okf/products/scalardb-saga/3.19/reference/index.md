---
type: Documentation Section
title: ScalarDB Saga 3.19 — Reference
description: Directory listing for the `reference` section of the ScalarDB Saga 3.19 documentation.
resource: https://github.com/scalar-labs/scalardb-saga/tree/ecbd61722adae47620b2032be6974c9af593ecda
tags:
- scalardb-saga
- v3.19
- index
status: draft
product: scalardb-saga
version: '3.19'
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-05T00:09:17Z'
---

# Reference

ScalarDB Saga 3.19 reference material generated from the files that define the contract in the source repository.

## Concepts

- [Admin gRPC API](./grpc-admin-api.md) — The AdminService gRPC contract — listing, recovering, force-completing and resetting sagas that need operator intervention.
- [Saga definition examples](./saga-definitions.md) — Working saga definitions from the repository: declarative service steps in JSON, and code steps (stepClass) in YAML and JSON.
- [Saga gRPC API](./grpc-saga-api.md) — The SagaService gRPC contract — starting a saga, awaiting it, and reading its snapshot and event history — as defined in saga.proto.
- [Server configuration reference](./server-configuration.md) — Every scalar.db.saga.server.* property the saga server accepts, with its default and the reasoning behind it, as shipped in the image's configuration template.
