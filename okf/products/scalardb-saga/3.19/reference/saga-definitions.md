---
type: Reference
title: Saga definition examples
description: 'Working saga definitions from the repository: declarative service steps in JSON, and code steps (stepClass) in YAML and JSON.'
resource: https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/getting-started/conf/definitions/order-saga.json
tags:
- scalardb-saga
- v3.19
- phase:implement
- section:reference
- pre-release
status: draft
product: scalardb-saga
product_title: ScalarDB Saga
version: '3.19'
patch_version: 3.19.0-alpha.1
prerelease: true
doc_id: reference/saga-definitions
lifecycle_phase: implement
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-05T00:20:30Z'
sources:
- id: scalardb-saga
  resource: https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/getting-started/conf/definitions/order-saga.json
  title: ScalarDB Saga source repository — getting-started/conf/definitions/order-saga.json
  author: process:scalar-labs/scalardb-saga
  last_modified: '2026-08-03T21:49:02Z'
- id: scalardb-saga
  resource: https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/getting-started/conf/definitions/order-saga-failing.json
  title: ScalarDB Saga source repository — getting-started/conf/definitions/order-saga-failing.json
  author: process:scalar-labs/scalardb-saga
  last_modified: '2026-08-03T21:49:02Z'
- id: scalardb-saga
  resource: https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/core/src/test/resources/sagas/transfer.yaml
  title: ScalarDB Saga source repository — core/src/test/resources/sagas/transfer.yaml
  author: process:scalar-labs/scalardb-saga
  last_modified: '2026-08-03T21:49:02Z'
- id: scalardb-saga
  resource: https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/core/src/test/resources/sagas/minimal.json
  title: ScalarDB Saga source repository — core/src/test/resources/sagas/minimal.json
  author: process:scalar-labs/scalardb-saga
  last_modified: '2026-08-03T21:49:02Z'
---

# Saga definition examples

A saga definition names the steps, the call each one makes and the call that undoes it. Values flow between steps through the saga context: `${...}` reads from it, and `output` captures fields of a response back into it. JSON and YAML are equally valid.

Two kinds of step exist. A **declarative service step** names a `service` configured on the server and the HTTP call to make; it works in both server and embedded mode. A **code step** names a `stepClass` implemented in Java and therefore only works in embedded mode — the server rejects such a definition at startup, because an operator cannot add classes to its image.

These are the definitions the repository ships, reproduced verbatim.

## `getting-started/conf/definitions/order-saga.json`

[View on GitHub](https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/getting-started/conf/definitions/order-saga.json)

```json
{
  "name": "order-saga",
  "mode": "SAGA",
  "steps": [
    {
      "name": "charge",
      "service": "payment",
      "execution": {
        "method": "POST",
        "path": "/charge",
        "jsonBody": { "orderId": "${orderId}", "amount": "${amount}" },
        "output": { "paymentId": "$.payment_id" }
      },
      "compensation": {
        "method": "POST",
        "path": "/refund",
        "jsonBody": { "orderId": "${orderId}" }
      }
    },
    {
      "name": "reserve",
      "service": "inventory",
      "execution": {
        "method": "POST",
        "path": "/reserve",
        "jsonBody": { "orderId": "${orderId}", "item": "${item}", "quantity": "${quantity}" },
        "output": { "reservationId": "$.inventory_id" }
      },
      "compensation": {
        "method": "POST",
        "path": "/release",
        "jsonBody": { "orderId": "${orderId}" }
      }
    },
    {
      "name": "ship",
      "service": "shipping",
      "execution": {
        "method": "POST",
        "path": "/ship",
        "jsonBody": {
          "orderId": "${orderId}",
          "paymentId": "${paymentId}",
          "reservationId": "${reservationId}"
        },
        "output": { "trackingId": "$.shipping_id" }
      },
      "compensation": {
        "method": "POST",
        "path": "/cancel",
        "jsonBody": { "orderId": "${orderId}" }
      }
    }
  ]
}
```

## `getting-started/conf/definitions/order-saga-failing.json`

[View on GitHub](https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/getting-started/conf/definitions/order-saga-failing.json)

```json
{
  "name": "order-saga-failing",
  "mode": "SAGA",
  "steps": [
    {
      "name": "charge",
      "service": "payment",
      "execution": {
        "method": "POST",
        "path": "/charge",
        "jsonBody": { "orderId": "${orderId}", "amount": "${amount}" },
        "output": { "paymentId": "$.payment_id" }
      },
      "compensation": {
        "method": "POST",
        "path": "/refund",
        "jsonBody": { "orderId": "${orderId}" }
      }
    },
    {
      "name": "reserve",
      "service": "inventory",
      "execution": {
        "method": "POST",
        "path": "/reserve",
        "jsonBody": { "orderId": "${orderId}", "item": "${item}", "quantity": "${quantity}" },
        "output": { "reservationId": "$.inventory_id" }
      },
      "compensation": {
        "method": "POST",
        "path": "/release",
        "jsonBody": { "orderId": "${orderId}" }
      }
    },
    {
      "name": "ship",
      "service": "shipping",
      "execution": {
        "method": "POST",
        "path": "/ship-fail",
        "jsonBody": { "orderId": "${orderId}", "paymentId": "${paymentId}" }
      },
      "compensation": {
        "method": "POST",
        "path": "/cancel",
        "jsonBody": { "orderId": "${orderId}" }
      }
    }
  ]
}
```

## `core/src/test/resources/sagas/transfer.yaml`

[View on GitHub](https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/core/src/test/resources/sagas/transfer.yaml)

```yaml
# Transfer money saga definition
name: transferMoney
mode: SAGA
version: "2.0"
recoveryStrategy: BACKWARD
timeoutMillis: 30000
steps:
  - name: debit
    stepClass: com.example.DebitStep
    timeoutMillis: 5000
  - name: credit
    stepClass: com.example.CreditStep
```

## `core/src/test/resources/sagas/minimal.json`

[View on GitHub](https://github.com/scalar-labs/scalardb-saga/blob/ecbd61722adae47620b2032be6974c9af593ecda/core/src/test/resources/sagas/minimal.json)

```json
{
  "name": "minimal",
  "steps": [
    { "name": "s1", "stepClass": "com.example.Step1" }
  ]
}
```
