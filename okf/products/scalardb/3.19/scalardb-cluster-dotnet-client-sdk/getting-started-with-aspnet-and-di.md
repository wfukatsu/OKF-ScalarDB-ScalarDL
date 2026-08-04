---
type: Tutorial
title: Getting Started with ASP.NET Core and Dependency Injection in the ScalarDB Cluster .NET Client SDK
description: The ScalarDB Cluster .NET Client SDK supports dependency injection (DI) in frameworks like ASP.NET Core.
resource: https://scalardb.scalar-labs.com/docs/latest/scalardb-cluster-dotnet-client-sdk/getting-started-with-aspnet-and-di/
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
patch_version: 3.19.0
doc_id: scalardb-cluster-dotnet-client-sdk/getting-started-with-aspnet-and-di
lifecycle_phase: implement
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:47Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/docs/scalardb-cluster-dotnet-client-sdk/getting-started-with-aspnet-and-di.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Getting Started with ASP.NET Core and Dependency Injection in the ScalarDB Cluster .NET Client SDK

The ScalarDB Cluster .NET Client SDK supports dependency injection (DI) in frameworks like ASP.NET Core.

## Install the SDK

Install the same major and minor version of the [SDK](https://www.nuget.org/packages/ScalarDB.Client) as ScalarDB Cluster into the .NET project. You can do this by using the built-in NuGet package manager, replacing `<MAJOR>.<MINOR>` with the version that you're using:

```console
dotnet add package ScalarDB.Client --version '<MAJOR>.<MINOR>.*'
```

## Add client settings

Add the `ScalarDbOptions` section to the `appsettings.json` file of your ASP.NET Core app, replacing `<HOSTNAME_OR_IP_ADDRESS>` with the FQDN or the IP address, and `<PORT>` with the port number (`60053` by default) of your cluster:

```json
{
  "ScalarDbOptions": {
    "Address": "http://<HOSTNAME_OR_IP_ADDRESS>:<PORT>",
    "HopLimit": 10
  }
}
```

For details about settings files and other ways to configure the client, see [Client configuration](./common-reference.md#client-configuration).

## Set up the transaction managers

You can register the ScalarDB transaction managers in the DI container as follows:

```c#
using ScalarDB.Client.Extensions;

//...

var builder = WebApplication.CreateBuilder(args);

//...

builder.Services.AddScalarDb();
```

:::note

The ScalarDB transaction managers will be registered as transient services. For details about service lifetimes, see [.NET dependency injection - Service lifetimes](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection#service-lifetimes).

:::

After registering the transaction managers, they can be injected into the controller's constructor as follows:

```c#
[ApiController]
public class OrderController: ControllerBase
{
    private readonly IDistributedTransactionManager _manager;
    private readonly ISqlTransactionManager _sqlManager;
    private readonly ITwoPhaseCommitTransactionManager _twoPhaseManager;
    private readonly ISqlTwoPhaseCommitTransactionManager _sqlTwoPhaseManager;
    private readonly IDistributedTransactionAdmin _admin;

    public OrderController(IDistributedTransactionManager manager,
                           ISqlTransactionManager sqlManager,
                           ITwoPhaseCommitTransactionManager twoPhaseManager,
                           ISqlTwoPhaseCommitTransactionManager sqlTwoPhaseManager,
                           IDistributedTransactionAdmin admin)
    {
        _manager = manager;
        _sqlManager = sqlManager;
        _twoPhaseManager = twoPhaseManager;
        _sqlTwoPhaseManager = sqlTwoPhaseManager;
        _admin = admin;
    }
}
```

Although these examples are for WebApi projects, the examples will work in a similar way in GrpcService projects.

## Use read-only transactions

ScalarDB Cluster supports read-only transactions for distributed and SQL transaction managers. After injecting `IDistributedTransactionManager` or `ISqlTransactionManager`, call `BeginReadOnlyAsync`/`BeginReadOnly` to hint to the server that only read operations will be performed:

```c#
var tran = await distributedTransactionManager.BeginReadOnlyAsync();
// Execute only read operations inside this transaction
await tran.GetAsync(get);
await tran.CommitAsync();
```

:::note

Read-only mode is *not* supported for two-phase commit transaction managers (`ITwoPhaseCommitTransactionManager`, `ISqlTwoPhaseCommitTransactionManager`). Calling `BeginReadOnly*` on those managers throws `NotSupportedException`.

:::
