---
type: Sample Application
title: API endpoints
description: There is no way to do this.
resource: https://scalardl.scalar-labs.com/docs/latest/applications/simple-bank-account/docs/api_endpoints/
tags:
- scalardl
- v3.13
- phase:implement
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: applications/simple-bank-account/docs/api_endpoints
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:59Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/docs/applications/simple-bank-account/docs/api_endpoints.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
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
