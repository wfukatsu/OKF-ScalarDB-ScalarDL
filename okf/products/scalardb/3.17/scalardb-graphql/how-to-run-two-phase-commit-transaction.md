---
type: Development Guide
title: How to run two-phase commit transaction
description: ScalarDB GraphQL supports two-phase commit style transactions called Two-phase Commit Transactions. With Two-phase Commit Transactions, you can execute a transaction that spans multiple processes/applications (e.g., Microservices). We name...
resource: https://scalardb.scalar-labs.com/docs/3.17/scalardb-graphql/how-to-run-two-phase-commit-transaction/
tags:
- scalardb
- v3.17
- phase:implement
- section:develop
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.3
doc_id: scalardb-graphql/how-to-run-two-phase-commit-transaction
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Reference
- Java Interface Guides
- GraphQL Interface Guides
editions:
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:26Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.17/scalardb-graphql/how-to-run-two-phase-commit-transaction.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to run two-phase commit transaction

ScalarDB GraphQL supports two-phase commit style transactions
called [Two-phase Commit Transactions](../two-phase-commit-transactions.md).
With Two-phase Commit Transactions, you can execute a transaction that spans multiple
processes/applications (e.g., Microservices).
We name the application that starts a transaction "coordinator" while the applications that
join the transaction are named "participants".
Every two-phase commit operation requires annotating the mutation or query operation with
a `@twoPhaseCommit` directive. Below is a description of such operations.

## Start a transaction

To start a transaction, add the `@twoPhaseCommit` directive without setting parameters.

```graphql
query some_query @twoPhaseCommit {
  # some query
}
```

The transaction ID of the started transaction will be returned in the extensions object that is part
of the result.

```json
{
  "data": {
    ...
  },
  "extensions": {
    "transaction": {
      "id": "the_transaction_id"
    }
  }
}
```

## Join a transaction (for participants)

In a participant application, to join the transaction started by a coordinator application, set the
transaction ID with the `id` parameter and set the `join` parameter to true.

```graphql
query some_query_from_participant @twoPhaseCommit(id:"the_transaction_id", join:true) {
  # some query
}
```

## Resume a transaction

To continue executing operations in the started or joined transaction, set the transaction ID value in
the `id` parameter of `@twoPhaseCommit` directive.

```graphql
mutation some_mutation @twoPhaseCommit(id:"the_transaction_id") {
  # some mutation
}
```

## Prepare, validate and commit a transaction

After finishing the query and mutation operations, you need to commit the transaction. Like a
well-known
two-phase commit protocol, there are two phases: prepare and commit.
You first need to prepare the transaction in all the coordinator/participant applications, and then
you
need to commit the transaction in all the coordinator/participant applications.

If the Consensus Commit transaction manager is configured with the `EXTRA_READ` serializable strategy
in `SERIALIZABLE` isolation level, an extra "validate" phase is required between prepare and
commit phases.
Similarly to prepare and commit, validate need to be executed in all the coordinator/participants
applications.

Prepare, validate and commit can be executed in parallel with all the coordinator/participants
applications.

### Prepare a transaction

Two options are possible to prepare a two-phase commit transaction.

#### Via the directive parameter

By using the `prepare` parameter of the directive, the transaction will be prepared after the
execution of the operation fields and only if they do not raise an error.

```graphql
mutation some_mutation_then_prepare_tx @twoPhaseCommit(id:"the_transaction_id", prepare:true) {
  mutation1 : ...
  mutation2 : ...
  # the transaction will be prepared after the execution of the mutation1 and mutation2 fields
}
```

#### Via the mutation field

Add a `prepare` field in a mutation operation. This field will trigger the transaction
preparation.

```graphql
mutation prepare_tx @twoPhaseCommit(id:"the_transaction_id") {
  prepare
}
```

### Validate a transaction

Add a `validate` field in a mutation operation. This field will trigger the transaction
validation.

```graphql
mutation validate_tx @twoPhaseCommit(id:"the_transaction_id") {
  validate
}
```

### Commit a transaction

Add a `commit` field in a mutation operation. This field will trigger the transaction commit.

```graphql
mutation commit_tx @twoPhaseCommit(id:"the_transaction_id") {
  commit
}
```

### Abort/Rollback a transaction

When you need to abort/rollback a transaction explicitly, you can use the `abort` or `rollback`
mutation fields interchangeably (both have the same effect and usage). Note that you cannot mix it
with any other operations, so you must specify it alone.

```graphql
mutation AbortTx @twoPhaseCommit(id: "the_transaction_id") {
  abort
}
```

or

```graphql
mutation RollbackTx @twoPhaseCommit(id: "the_transaction_id") {
  rollback
}
```

## Error handling

If an exception is thrown by a `@twoPhaseCommit` operation, ScalarDB GraphQL triggers a rollback procedure that recovers the transaction.
For more details about the exception handling in two-phase commit transaction, please refer to
the [exception handling guide for ScalarDB two-phase commit transaction](../two-phase-commit-transactions.md#handle-exceptions).
