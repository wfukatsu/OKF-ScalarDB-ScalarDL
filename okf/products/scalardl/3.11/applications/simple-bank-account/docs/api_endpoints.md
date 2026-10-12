---
type: Sample Application
title: API endpoints
description: There is no way to do this.
resource: https://scalardl.scalar-labs.com/docs/3.11/applications/simple-bank-account/docs/api_endpoints/
tags:
- scalardl
- v3.11
- phase:implement
- edition:community
- edition:enterprise
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.4
doc_id: applications/simple-bank-account/docs/api_endpoints
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-10-12T04:40:06Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/603f940d61f7886e62805f34643d0aa3a49db725/versioned_docs/version-3.11/applications/simple-bank-account/docs/api_endpoints.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-10-09T03:44:05Z'
---

# API endpoints

## `GET v1/accounts`

- **Not implemented yet**
- Return a list of accounts and their balances as a JSON array

```
[
    {
        "account": <id>,
        "balance": <balance>
    },
    ...
]
```

## `GET v1/accounts/{id}?start=<num>&end=<num>&order=<asc or desc>&limit=<num>`

- Return the given account history as a JSON array
- Return `200 OK` if success

```
[
    {
        "account": <id>,
        "balance": <balance>,
        "age": <age>
    },
    ...
]
```

## `PUT v1/accounts/{id}`

- Create the specified account with id=`{id}`
- Return `200 OK` if success
- Return `403 Bad Request` if the account already exists

## `POST v1/accounts/{id}/deposit?amount=<amount>`

- Deposit into a specified account
- Return `200 OK` if success

## `POST v1/accounts/{id}/withdraw?amount=<amount>`

- Withdraw from a specified account
- Return `200 OK` if success
- Return `403 Bad Request` if amount exceeds the balance in the account

## `POST v1/transfers?from=<id>&to=<id>&amount=<amount>`

- Transfer funds from one account to another
- Return `200 OK` if success
- Return `403 Bad Request` if amount exceeds the balance in the from account

## Delete an account

There is no way to do this.
