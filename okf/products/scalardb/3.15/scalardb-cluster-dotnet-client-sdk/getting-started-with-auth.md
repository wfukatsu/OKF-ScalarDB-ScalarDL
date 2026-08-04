---
type: Development Guide
title: Getting Started with Authentication and Authorization by Using ScalarDB Cluster .NET Client SDK
description: The ScalarDB Cluster .NET Client SDK supports authentication and authorization, which allows you to authenticate and authorize your requests to ScalarDB Cluster.
resource: https://scalardb.scalar-labs.com/docs/3.15/scalardb-cluster-dotnet-client-sdk/getting-started-with-auth/
tags:
- scalardb
- v3.15
- phase:implement
- section:develop
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.15'
patch_version: 3.15.9
doc_id: scalardb-cluster-dotnet-client-sdk/getting-started-with-auth
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Reference
- .NET Interface Guides
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:56Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.15/scalardb-cluster-dotnet-client-sdk/getting-started-with-auth.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Getting Started with Authentication and Authorization by Using ScalarDB Cluster .NET Client SDK

The ScalarDB Cluster .NET Client SDK supports [authentication and authorization](../scalardb-cluster/scalardb-auth-with-sql.md), which allows you to authenticate and authorize your requests to ScalarDB Cluster.

## Install the SDK

Install the same major and minor version of the [SDK](https://www.nuget.org/packages/ScalarDB.Client) as ScalarDB Cluster into the .NET project. You can do this by using the built-in NuGet package manager, replacing `<MAJOR>.<MINOR>` with the version that you're using:

```console
dotnet add package ScalarDB.Client --version '<MAJOR>.<MINOR>.*'
```

## Set credentials in the settings file

You need to set credentials in the settings file as follows, replacing the contents in the angle brackets as described:

```json
{
  "ScalarDbOptions": {
    "Address": "http://<HOSTNAME_OR_IP_ADDRESS>:<PORT>",
    "HopLimit": 10,
    "AuthEnabled": true,
    "Username": "<USERNAME>",
    "Password": "<PASSWORD>"
  }
}
```

For details about settings files and other ways to configure the client, see [Client configuration](./common-reference.md#client-configuration).

## Get a transaction manager

You need to get a transaction manager or transaction admin object by using `TransactionFactory` as follows. Be sure to replace `<GET_TRANSACTION_MANAGER>` with `GetTransactionManager()`, `GetTwoPhaseCommitTransactionManager()`, `GetSqlTransactionManager()`, or `GetSqlTwoPhaseCommitTransactionManager()`.

```c#
// Pass the path to the settings file.
var factory = TransactionFactory.Create("scalardb-options.json");

// To get a transaction manager
using var manager = factory.<GET_TRANSACTION_MANAGER>();

// To get a transaction admin
using var admin = factory.GetTransactionAdmin();
```

A transaction manager or transaction admin object created from `TransactionFactory` with the provided credentials will automatically log in to ScalarDB Cluster and can communicate with it.

## Wire encryption

[Wire encryption](../scalardb-cluster/scalardb-auth-with-sql.md#wire-encryption) is also supported. It can be turned on by setting `Address` to the URL starting with `https` as follows:

```json
{
  "ScalarDbOptions": {
    "Address": "https://<HOSTNAME_OR_IP_ADDRESS>:<PORT>"
  }
}
```

For details about settings files and other ways to configure the client, see [Client configuration](./common-reference.md#client-configuration).
