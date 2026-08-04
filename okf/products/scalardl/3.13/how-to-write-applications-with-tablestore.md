---
type: Development Guide
title: Write a ScalarDL Application with the TableStore Abstraction
description: This document explains how to write ScalarDL applications with the TableStore abstraction. You will learn how to use ScalarDL TableStore in your applications, handle errors, and validate your data.
resource: https://scalardl.scalar-labs.com/docs/latest/how-to-write-applications-with-tablestore/
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
doc_id: how-to-write-applications-with-tablestore
lifecycle_phase: implement
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:59Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/docs/how-to-write-applications-with-tablestore.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# Write a ScalarDL Application with the TableStore Abstraction

This document explains how to write ScalarDL applications with the TableStore abstraction. You will learn how to use ScalarDL TableStore in your applications, handle errors, and validate your data.

## Use the ScalarDL TableStore Client SDK

You have two options to use ScalarDL TableStore:

- Using [commands](./scalardl-tablestore-command-reference.md), as shown in [Get Started with ScalarDL TableStore](./getting-started-tablestore.md)
- Using the [TableStore Java Client SDK](https://javadoc.io/doc/com.scalar-labs/scalardl-tablestore-java-client-sdk/)

Using commands is a convenient way to try TableStore without writing an application. For building TableStore-based applications, however, the TableStore Client SDK is recommended, as it runs more efficiently without launching a separate process for each operation.

The TableStore Client SDK is available on [Maven Central](https://central.sonatype.com/artifact/com.scalar-labs/scalardl-tablestore-java-client-sdk). You can install it in your application by using a build tool such as Gradle. For example, in Gradle, you can add the following dependency to `build.gradle`, replacing `VERSION` with the version of ScalarDL that you want to use.

```gradle
dependencies {
    implementation group: 'com.scalar-labs', name: 'scalardl-tablestore-java-client-sdk', version: '<VERSION>'
}
```

The Client SDK APIs for TableStore are provided by a service class called [`TableStoreClientService`](https://javadoc.io/static/com.scalar-labs/scalardl-tablestore-java-client-sdk/3.13.0/com/scalar/dl/tablestore/client/service/TableStoreClientService.html). The following is a code snippet that shows how to use `TableStoreClientService` to manage table authenticity. `TableStoreClientService` provides the same functionalities as the TableStore client commands shown in [Get Started with ScalarDL TableStore](./getting-started-tablestore.md).

```java
  // TableStoreClientServiceFactory should always be reused.
  TableStoreClientServiceFactory factory = new TableStoreClientServiceFactory();

  // TableStoreClientServiceFactory creates a new TableStoreClientService object in every create
  // method call but reuses the internal objects and connections as much as possible for better
  // performance and resource usage.
  TableStoreClientService service = factory.create(new ClientConfig(new File(properties)));
  try {
    // execute a SQL statement.
    String sql = "SELECT * FROM employee WHERE id = '1001'";
    ExecutionResult result = service.executeStatement(sql);
    result.getResult().ifPresent(System.out::println);
  } catch (ClientException e) {
    System.err.println(e.getStatusCode());
    System.err.println(e.getMessage());
  }

  factory.close();
```

:::note

You should always use `TableStoreClientServiceFactory` to create `TableStoreClientService` objects. `TableStoreClientServiceFactory` caches objects that are required to create `TableStoreClientService` and reuses them on the basis of the given configurations, so the `TableStoreClientServiceFactory` object should always be reused.

:::

For more information about `TableStoreClientServiceFactory` and `TableStoreClientService`, see the [`scalardl-tablestore-java-client-sdk` Javadoc](https://javadoc.io/doc/com.scalar-labs/scalardl-tablestore-java-client-sdk/latest/index.html).

## Handle errors

If an error occurs in your application, the Client SDK will return an exception with a status code and an error message with an error code. You should check the status code and the error code to identify the cause of the error. For details about the status code and the error codes, see [Status codes](./how-to-write-applications.md#status-codes) and [Error codes](./how-to-write-applications.md#error-codes).

### Implement error handling

The SDK throws [`ClientException`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.13.0/com/scalar/dl/client/exception/ClientException.html) when an error occurs. You can handle errors by catching the exception as follows:

```java
TableStoreClientService service = ...;
try {
    // interact with ScalarDL TableStore through a TableStoreClientService object
} catch (ClientException e) {
    // e.getStatusCode() returns the status of the error
}
```

## Validate your data

In ScalarDL, you occasionally need to validate your data to make sure all the data is in a valid state. Since you can learn the basics of how ScalarDL validates your data in [Write a ScalarDL Application in Java](./how-to-write-applications.md#validate-your-data), this section mainly describes how you can perform the validation in TableStore.

When validating [assets](./data-modeling.md#asset) (records, index records, and table schema here) in TableStore, you need to specify a table and a primary or index key if necessary. An example code for validating assets in TableStore is as follows:

```java
  TableStoreClientService service = ...
  String tableName = "employee";
  String primaryKeyColumn = "id";
  String indexKeyColumn = "department";
  TextNode primaryKeyValue = TextNode.valueOf("1001");
  TextNode indexKeyValue = TextNode.valueOf("sales");
  try {
    LedgerValidationResult result1 =
        service.validateRecord(tableName, primaryKeyColumn, primaryKeyValue);
    LedgerValidationResult result2 =
        service.validateIndexRecord(tableName, indexKeyColumn, indexKeyValue);
    LedgerValidationResult result3 = service.validateTableSchema(tableName);
    // You can also specify age range.
    // LedgerValidationResult result1 =
    //     service.validateRecord(tableName, primaryKeyColumn, primaryKeyValue, startAge, endAge);
    // LedgerValidationResult result2 =
    //     service.validateIndexRecord(tableName, indexKeyColumn, indexKeyValue, startAge, endAge);
    // LedgerValidationResult result3 = service.validateTableSchema(tableName, startAge, endAge);
  } catch (ClientException e) {
  }
```

:::note

- The error-handling behavior of the validation methods differs when using Ledger compared to when using both Ledger and Auditor. For details, see [Validate your data](./how-to-write-applications.md#validate-your-data).
- TableStore internally assigns a dedicated asset ID to an asset that represents a record, an index record, and a table schema. The asset ID consists of a prefix to show the asset type and a key; for example, a prefix `rec_`, a primary-key column name, and a primary-key value are used for asset IDs of records. You will see such raw asset IDs in `AssetProof` in `LedgerValidationResult`.

:::
