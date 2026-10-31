---
type: Documentation Section
title: ScalarDB Saga 3.20 — Guides
description: Directory listing for the `guides` section of the ScalarDB Saga 3.20 documentation.
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

# Guides

ScalarDB Saga 3.20 reference material generated from the files that define the contract in the source repository.

## Concepts

- [Model Your Workflow](./model-your-workflow.md) — This page explains how to model a business workflow as a ScalarDB Saga definition: which steps to create, what each one calls, how to order them, and how they behave when something fails. It assumes you have run the getting started guide,...
- [Run Saga Transactions](./run-saga-transactions.md) — This page explains how an application runs sagas against a ScalarDB Saga server: starting them, learning their outcome, and handling failures. It uses the Java client SDK, which is the recommended interface for production applications, and...
- [ScalarDB Saga Configurations](./configurations.md) — This page describes the parameters you can set to configure the ScalarDB Saga server. For how the settings fit into a deployment, see server/docker/README.md.
- [ScalarDB Saga REST API](./rest-api.md) — This page lists every route of the ScalarDB Saga server's REST API, with its request, its response, and the status codes it answers with. The REST API lets applications in any language start and check sagas without an SDK. Java...
- [ScalarDB Saga Status Codes](./scalardb-saga-status-codes.md) — This page lists the status codes that ScalarDB Saga reports. A REST error response carries the code in the errorCode field of its body, and a gRPC error carries it as the reason of its google.rpc.ErrorInfo detail. The Java client SDK and...
