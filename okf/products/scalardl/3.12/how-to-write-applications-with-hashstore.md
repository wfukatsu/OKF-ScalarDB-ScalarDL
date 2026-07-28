---
type: Development Guide
title: Write a ScalarDL Application with the HashStore Abstraction
description: This document explains how to write ScalarDL applications with the HashStore abstraction. You will learn how to use ScalarDL HashStore in your applications, handle errors, and validate your data.
resource: https://scalardl.scalar-labs.com/docs/3.12/how-to-write-applications-with-hashstore/
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
doc_id: how-to-write-applications-with-hashstore
lifecycle_phase: implement
breadcrumb:
- Develop
- Write an Application
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:07Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/versioned_docs/version-3.12/how-to-write-applications-with-hashstore.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Write a ScalarDL Application with the HashStore Abstraction

This document explains how to write ScalarDL applications with the HashStore abstraction. You will learn how to use ScalarDL HashStore in your applications, handle errors, and validate your data.

## Use the ScalarDL HashStore Client SDK

You have two options to use ScalarDL HashStore:

- Using [commands](./scalardl-hashstore-command-reference.md), as shown in [Get Started with ScalarDL HashStore](./getting-started-hashstore.md)
- Using the [HashStore Java Client SDK](https://javadoc.io/doc/com.scalar-labs/scalardl-hashstore-java-client-sdk/)

Using commands is a convenient way to try HashStore without writing an application. For building HashStore-based applications, however, the HashStore Client SDK is recommended, as it runs more efficiently without launching a separate process for each operation.

The HashStore Client SDK is available on [Maven Central](https://central.sonatype.com/artifact/com.scalar-labs/scalardl-hashstore-java-client-sdk). You can install it in your application by using a build tool such as Gradle. For example, in Gradle, you can add the following dependency to `build.gradle`, replacing `VERSION` with the version of ScalarDL that you want to use.

```gradle
dependencies {
    implementation group: 'com.scalar-labs', name: 'scalardl-hashstore-java-client-sdk', version: '<VERSION>'
}
```

The Client SDK APIs for HashStore are provided by a service class called [`HashStoreClientService`](https://javadoc.io/static/com.scalar-labs/scalardl-hashstore-java-client-sdk/3.12.3/com/scalar/dl/hashstore/client/service/HashStoreClientService.html). The following is a code snippet that shows how to use `HashStoreClientService` to manage objects and collections. `HashStoreClientService` provides the same functionalities as the HashStore client commands shown in [Get Started with ScalarDL HashStore](./getting-started-hashstore.md).

```java
  // HashStoreClientServiceFactory should always be reused.
  HashStoreClientServiceFactory factory = new HashStoreClientServiceFactory();

  // HashStoreClientServiceFactory creates a new HashStoreClientService object in every create
  // method call but reuses the internal objects and connections as much as possible for better
  // performance and resource usage.
  HashStoreClientService service = factory.create(new ClientConfig(new File(properties)));
  try {
    // put the hash value of an object with metadata.
    String objectId = ...;
    String hash = ...;
    JsonNode metadata = ...;
    ExecutionResult result = service.putObject(objectId, hash, metadata);
  } catch (ClientException e) {
    System.err.println(e.getStatusCode());
    System.err.println(e.getMessage());
  }

  factory.close();
```

:::note

You should always use `HashStoreClientServiceFactory` to create `HashStoreClientService` objects. `HashStoreClientServiceFactory` caches objects that are required to create `HashStoreClientService` and reuses them on the basis of the given configurations, so the `HashStoreClientServiceFactory` object should always be reused.

:::

For more information about `HashStoreClientServiceFactory` and `HashStoreClientService`, see the [`scalardl-hashstore-java-client-sdk` Javadoc](https://javadoc.io/doc/com.scalar-labs/scalardl-hashstore-java-client-sdk/latest/index.html).

## Handle errors

If an error occurs in your application, the Client SDK will return an exception with a status code and an error message with an error code. You should check the status code and the error code to identify the cause of the error. For details about the status code and the error codes, see [Status codes](./how-to-write-applications.md#status-codes) and [Error codes](./how-to-write-applications.md#error-codes).

### Implement error handling

The SDK throws [`ClientException`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.12.3/com/scalar/dl/client/exception/ClientException.html) when an error occurs. You can handle errors by catching the exception as follows:

```java
HashStoreClientService service = ...;
try {
    // interact with ScalarDL HashStore through a HashStoreClientService object
} catch (ClientException e) {
    // e.getStatusCode() returns the status of the error
}
```

## Validate your data

In ScalarDL, you occasionally need to validate your data to make sure all the data is in a valid state. Since you can learn the basics of how ScalarDL validates your data in [Write a ScalarDL Application in Java](./how-to-write-applications.md#validate-your-data), this section mainly describes how you can perform the validation in HashStore.

When validating [assets](./data-modeling.md#asset) (objects and collections here) in HashStore, you only need to specify an object ID or a collection ID. An example code for validating an object is as follows:

```java
  HashStoreClientService service = ...
  try {
    LedgerValidationResult result = service.validateObject("an_object_ID");
    // You can also specify age range.
    // LedgerValidationResult result = service.validateObject("an_object_ID", startAge, endAge);
  } catch (ClientException e) {
  }
```

An example code for validating a collection is as follows:

```java
  HashStoreClientService service = ...
  try {
    LedgerValidationResult result = service.validateCollection("a_collection_ID");
    // You can also specify age range.
    // LedgerValidationResult result = service.validateCollection("a_collection_ID", startAge, endAge);
  } catch (ClientException e) {
  }
```

:::note

- The error-handling behavior of the validation methods differs when using Ledger compared to when using both Ledger and Auditor. For details, see [Validate your data](./how-to-write-applications.md#validate-your-data).
- HashStore internally assigns a dedicated asset ID to an asset that represents an object or a collection. The asset ID consists of a prefix to show the asset type and a key; for example, a prefix `o_` and an object ID for objects, and a prefix `c_` and a collection ID for collections are used. You will see such raw asset IDs in `AssetProof` in `LedgerValidationResult`.

:::
