---
type: Development Guide
title: Manage the Contract and Function Lifecycle
description: This document explains the lifecycle of contracts and functions in ScalarDL—from creating and registering them to updating them when bug fixes or feature additions are needed.
resource: https://scalardl.scalar-labs.com/docs/3.12/manage-contract-and-function-lifecycle/
tags:
- scalardl
- v3.12
- phase:implement
- section:develop
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.12'
patch_version: 3.12.3
doc_id: manage-contract-and-function-lifecycle
lifecycle_phase: implement
breadcrumb:
- Develop
- Write Business Logic
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:07Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/versioned_docs/version-3.12/manage-contract-and-function-lifecycle.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Manage the Contract and Function Lifecycle

This document explains the lifecycle of contracts and functions in ScalarDL—from creating and registering them to updating them when bug fixes or feature additions are needed.

## Create a contract or function

In ScalarDL, you implement business logic as two types of Java programs: contracts and functions. Contracts manage tamper-evident asset records in the Ledger, while functions work alongside contracts to manage mutable records in an external database through ScalarDB.

To create a contract or function, write a Java class that extends one of the predefined base classes, such as [`JacksonBasedContract`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.12.3/com/scalar/dl/ledger/contract/JacksonBasedContract.html) for contracts or [`JacksonBasedFunction`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.12.3/com/scalar/dl/ledger/function/JacksonBasedFunction.html) for functions.

For details on how to write contracts and functions, see the following:

- [A Guide on How to Write a Good Contract for ScalarDL](./how-to-write-contract.md)
- [A Guide on How to Write Function for ScalarDL](./how-to-write-function.md)

## Register a contract or function

After creating a contract or function, you need to register it with ScalarDL before you can use it.

To register a contract:

```console
scalardl register-contract --properties client.properties --contract-id StateUpdater --contract-binary-name com.org1.contract.StateUpdater --contract-class-file build/classes/java/main/com/org1/contract/StateUpdater.class
```

To register a function:

```console
scalardl register-function --properties client.properties --function-id test-function --function-binary-name com.example.function.TestFunction --function-class-file /path/to/TestFunction.class
```

For details on registration commands and options, see [ScalarDL Client Command Reference](./scalardl-command-reference.md).

### Contract registration constraints

When registering a contract, note the following constraints:

- **Unique contract ID:** Each contract must have a unique contract ID. If you try to register a contract with an ID that already exists, the registration will fail.
- **Consistent binary name and byte code:** If a binary name has already been registered with a certain byte code, you cannot register a different byte code under the same binary name. However, you can register the same binary name and byte code under a different client or a different contract ID.

### Function registration constraints

Unlike contracts, functions can be re-registered with the same function ID. The behavior depends on how you access ScalarDL:

- **Privileged port (default: 50052):** Functions can always be registered and overwritten without restrictions.
- **Non-privileged port (default: 50051):** Function registration and overwriting are controlled by administrator settings.

## Update a contract or function

Contracts and functions have fundamentally different update mechanisms because they serve different architectural roles in ScalarDL. Contracts manage tamper-evident asset records in the Ledger, and ScalarDL needs to be able to replay the full history of asset updates to validate consistency with past contract executions. For this reason, contracts are immutable (append-only). Functions, on the other hand, manage mutable records in an external database through ScalarDB, so there is no need to preserve the history of past function versions, and they can be overwritten.

### Update a contract

Since contracts are immutable, you cannot modify or overwrite an existing contract. Instead, you must register a new version of the contract with a **new contract ID** and a **new binary name**.

#### Versioning best practices

There are two common approaches for versioning contracts:

**Package-based versioning (recommended for production):** Include the version number in the Java package name. The [predefined contracts](https://github.com/scalar-labs/scalardl/tree/master/generic-contracts/src/main/java/com/scalar/dl/genericcontracts) used internally by ScalarDL abstractions such as HashStore and TableStore also follow this approach.

For example, if your original contract is in `com.example.contract.v1.StateUpdater`, the updated version would be in `com.example.contract.v2.StateUpdater`. Similarly, the contract ID should reflect the version, such as `v1.StateUpdater` and `v2.StateUpdater`.

```console
scalardl register-contract --properties client.properties --contract-id v2.StateUpdater --contract-binary-name com.example.contract.v2.StateUpdater --contract-class-file build/classes/java/main/com/example/contract/v2/StateUpdater.class
```

**Class-name-based versioning (suitable for smaller scale or testing):** Append the version number directly to the class name, such as `StateUpdaterV2`. This approach is simpler but can become less organized for large-scale projects.

```console
scalardl register-contract --properties client.properties --contract-id StateUpdaterV2 --contract-binary-name com.example.contract.StateUpdaterV2 --contract-class-file build/classes/java/main/com/example/contract/StateUpdaterV2.class
```

#### Update your application code

After registering the new contract version, update your application code to use the new contract ID. For example, if you use [`ClientService`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.12.3/com/scalar/dl/client/service/ClientService.html), update the contract ID passed to the `executeContract` method.

:::note

Old contract versions remain registered in ScalarDL. This is by design—ScalarDL needs them for asset validation and history replay. Do not attempt to remove old contract versions.

:::

### Update a function

Since functions are mutable, you can update a function by re-registering it with the same function ID. The new byte code will overwrite the old one.

```console
scalardl register-function --properties client.properties --function-id test-function --function-binary-name com.example.function.TestFunction --function-class-file /path/to/TestFunction.class
```

When overwriting a function, you can also change the binary name if needed. The function ID is the only identifier that must remain the same.

### Execute updated contracts and functions

After updating a contract, use the **new contract ID** when executing it. The old contract ID still references the old version.

```console
scalardl execute-contract --properties client.properties --contract-id v2.StateUpdater --contract-argument '{"asset_id":"some_asset", "state":3}'
```

After updating a function, you can use the **same function ID** as before, and the updated function will be executed automatically.

```console
scalardl execute-contract --properties client.properties --contract-id v2.StateUpdater --contract-argument '{"asset_id":"some_asset", "state":3}' --function-id test-function --function-argument '{...}'
```

For details on executing contracts and functions, see the following:

- [Write a ScalarDL Application in Java](./how-to-write-applications.md)
- [ScalarDL Client Command Reference](./scalardl-command-reference.md)

## See also

- [A Guide on How to Write a Good Contract for ScalarDL](./how-to-write-contract.md)
- [A Guide on How to Write Function for ScalarDL](./how-to-write-function.md)
- [ScalarDL Client Command Reference](./scalardl-command-reference.md)
- [Write a ScalarDL Application in Java](./how-to-write-applications.md)
