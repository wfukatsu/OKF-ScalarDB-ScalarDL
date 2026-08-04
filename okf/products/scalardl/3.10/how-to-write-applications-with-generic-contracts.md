---
type: Development Guide
title: Write a ScalarDL Application with Generic Contracts
description: Although generic contracts were introduced in ScalarDL 3.10, HashStore, released in ScalarDL 3.12, provides a higher-level abstraction that wraps generic contracts. For most use cases, using HashStore is simpler and more efficient than...
resource: https://scalardl.scalar-labs.com/docs/3.10/how-to-write-applications-with-generic-contracts/
tags:
- scalardl
- v3.10
- phase:implement
- section:develop
- edition:community
- edition:enterprise
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.10'
patch_version: 3.10.5
doc_id: how-to-write-applications-with-generic-contracts
lifecycle_phase: implement
breadcrumb:
- Develop
- Write an Application
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:03Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.10/how-to-write-applications-with-generic-contracts.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Write a ScalarDL Application with Generic Contracts

:::tip

Although generic contracts were introduced in ScalarDL 3.10, HashStore, released in ScalarDL 3.12, provides a higher-level abstraction that wraps generic contracts. For most use cases, using HashStore is simpler and more efficient than using generic contracts directly. For details, see [Write a ScalarDL Application with the HashStore Abstraction](https://scalardl.scalar-labs.com/docs/latest/how-to-write-applications-with-hashstore) in the latest version of ScalarDL.

:::

This document explains how to write ScalarDL applications with generic contracts. You will learn how to interact with ScalarDL in your applications, handle errors, and validate your data when using generic contracts in ScalarDL.

## Use the ScalarDL Client SDK for generic contracts

You have two options to interact with ScalarDL when using generic contracts:

- Using [commands](./scalardl-command-reference.md), as shown in [Use Generic Contracts and Functions](./use-generic-contracts.md)
- Using the [Java Client SDK](https://javadoc.io/doc/com.scalar-labs/scalardl-java-client-sdk/latest/index.html)

Using commands is convenient because you don't need to write applications. However, they invoke a process for each execution, which is slow, so they are mainly for quickly testing generic contracts. Instead, using the Client SDK is usually recommended when you write ScalarDL-based applications because it is more efficient.

The Client SDK is available on [Maven Central](https://search.maven.org/search?q=a:scalardl-java-client-sdk). You can install it in your application by using a build tool such as Gradle. For example, in Gradle, you can add the following dependency to `build.gradle`, replacing `VERSION` with the version of ScalarDL that you want to use.

```gradle
dependencies {
    implementation group: 'com.scalar-labs', name: 'scalardl-java-client-sdk', version: '<VERSION>'
}
```

The Client SDK APIs for generic contracts are provided by a service class called [`GenericContractClientService`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.10.5/com/scalar/dl/client/service/GenericContractClientService.html). The following is a code snippet that shows how to use `GenericContractClientService` to execute a contract.

```java
  // ClientServiceFactory should always be reused.
  ClientServiceFactory factory = new ClientServiceFactory();

  // ClientServiceFactory creates a new GenericContractClientService object in every create method call
  // but reuses the internal objects and connections as much as possible for better performance and resource usage.
  GenericContractClientService service = factory.createForGenericContracts(new ClientConfig(new File(properties));
  try {
    // create an application-specific argument that matches the generic contract specification
    JsonNode jsonArgument = ...;
    ContractExecutionResult result = service.executeContract(contractId, jsonArgument);
    result.getContractResult().ifPresent(System.out::println);
  } catch (ClientException e) {
    System.err.println(e.getStatusCode());
    System.err.println(e.getMessage());
  }

  factory.close();
```

You should always use `ClientServiceFactory` to create `GenericContractClientService` objects. `ClientServiceFactory` caches objects that are required to create `GenericContractClientService` and reuses them on the basis of the given configurations, so `ClientServiceFactory` object should always be reused.

`GenericContractClientService` is a thread-safe client that interacts with ScalarDL components, like Ledger and Auditor, to register certificates, register contracts, execute contracts, and validate data. When you execute a generic contract, you need to specify a `JsonNode` argument. For details about the specification of the input argument, see [Generic Contracts and Functions Reference Guide](./generic-contracts-reference.md).

:::warning

Do not register and execute your custom contracts through `GenericContractClientService`. Using the generic contracts and your custom contracts together is not supported because the proper asset management cannot be guaranteed.

:::

For more information about `ClientServiceFactory` and `GenericContractClientService`, see the [`scalardl-java-client-sdk` Javadoc](https://javadoc.io/doc/com.scalar-labs/scalardl-java-client-sdk/latest/index.html).

## Handle errors

If an error occurs in your application, the Client SDK will return an exception with a status code and an error message with an error code. You should check the status code and the error code to identify the cause of the error. For details about the status code and the error codes, see [Status codes](./how-to-write-applications.md#status-codes) and [Error codes](./how-to-write-applications.md#error-codes).

### Implement error handling

The SDK throws [`ClientException`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.10.5/com/scalar/dl/client/exception/ClientException.html) when an error occurs. You can handle errors by catching the exception as follows:

```java
GenericContractClientService clientService = ...;
try {
    // interact with ScalarDL through a ClientService object
} catch (ClientException) {
    // e.getStatusCode() returns the status of the error
}
```

## Validate your data

In ScalarDL, you occasionally need to validate your data to make sure all the data is in a valid state. Since you can learn the basics of how ScalarDL validates your data in [Write a ScalarDL Application in Java](./how-to-write-applications.md#validate-your-data), this section mainly describes differences between the `validateLedger` method in the regular `ClientService` and the `validateLedger` method in `GenericContractClientService`.

When validating assets created by generic contracts, you need to specify the type of the asset and a list of keys to identify the asset. Currently, generic contracts create two types of assets: an object (`AssetType.OBJECT`) and a collection (`AssetType.COLLECTION`). For keys, you can specify the object ID or collection ID.

An example code for validating an object is as follows:

```java
  GenericContractClientService service = ...
  try {
    LedgerValidationResult result = service.validateLedger(AssetType.OBJECT, ImmutableList.of("an_object_ID"));
    // You can also specify age range.
    // LedgerValidationResult result = service.validateLedger(AssetType.OBJECT, ImmutableList.of("an_object_ID"), startAge, endAge);
  } catch (ClientException e) {
  }
```

:::note

Generic contracts internally assign a dedicated asset ID to an [asset record](./data-modeling.md#asset-record) that represents an object or a collection. The asset ID consists of a prefix for the asset type and keys; for example, a prefix `o_` and an object ID for `AssetType.OBJECT`. Therefore, you will see such raw asset IDs in `AssetProof` in `LedgerValidationResult`.

:::

## Use other languages

To interact with ScalarDL in languages other than Java, you can use ScalarDL Gateway.

:::note

Documentation for ScalarDL Gateway is currently being created and will be ready in the near future.

:::
