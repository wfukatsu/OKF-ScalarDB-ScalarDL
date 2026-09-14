---
type: Tutorial
title: Getting Started with Authentication and Authorization by Using ScalarDB Cluster .NET Client SDK
description: The ScalarDB Cluster .NET Client SDK supports authentication and authorization, which allows you to authenticate and authorize your requests to ScalarDB Cluster.
resource: https://scalardb.scalar-labs.com/docs/latest/scalardb-cluster-dotnet-client-sdk/getting-started-with-auth/
tags:
- scalardb
- v3.19
- phase:implement
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.1
doc_id: scalardb-cluster-dotnet-client-sdk/getting-started-with-auth
lifecycle_phase: implement
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-09-14T03:42:15Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/45b362692765eeed47d41bf36b23f6e7c007a55f/docs/scalardb-cluster-dotnet-client-sdk/getting-started-with-auth.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-09-11T06:55:58Z'
---

# Getting Started with Authentication and Authorization by Using ScalarDB Cluster .NET Client SDK

The ScalarDB Cluster .NET Client SDK supports [authentication and authorization](../scalardb-cluster/scalardb-auth-with-sql.md), which allows you to authenticate and authorize your requests to ScalarDB Cluster.

## Install the SDK

Install the same major and minor version of the [SDK](https://www.nuget.org/packages/ScalarDB.Client) as ScalarDB Cluster into the .NET project. You can do this by using the built-in NuGet package manager, replacing `<MAJOR>.<MINOR>` with the version that you're using:

```console
dotnet add package ScalarDB.Client --version '<MAJOR>.<MINOR>.*'
```

## Set credentials in the settings file

You need to set credentials in the settings file, replacing the contents in the angle brackets as described. ScalarDB Cluster supports two authentication types: username and password authentication, and authentication that uses a JWT access token issued by an OpenID Connect (OIDC) provider. Select the tab for the authentication type that you want to use.

**Username and password**

To authenticate by using a username and password, set `Username` and `Password` as follows:

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

**OIDC JWT access token**

To authenticate by using an OIDC JWT access token instead of a username and password, set `AuthType` to `OidcJwt` and set `AuthOidcJwtAccessToken` to a valid access token issued by your OIDC provider as follows:

```json
{
  "ScalarDbOptions": {
    "Address": "http://<HOSTNAME_OR_IP_ADDRESS>:<PORT>",
    "HopLimit": 10,
    "AuthEnabled": true,
    "AuthType": "OidcJwt",
    "AuthOidcJwtAccessToken": "<OIDC_JWT_ACCESS_TOKEN>"
  }
}
```

When you use `OidcJwt`, `Username` and `Password` aren't required. For details about how to configure ScalarDB Cluster to accept OIDC JWT access tokens and how to obtain a token from an OIDC provider, see [Control User Access via OIDC-Based JWT Access Tokens](../scalardb-cluster/control-access-via-oidc-based-jwt-tokens.md).

:::note

The SDK doesn't refresh OIDC JWT access tokens. Because the token is set when `TransactionFactory` is created, it can't be refreshed afterward. When the token expires or becomes invalid, the authentication error is propagated to your application. To use a new token, obtain a valid token and create a new `TransactionFactory` and transaction manager with that token.

:::

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
