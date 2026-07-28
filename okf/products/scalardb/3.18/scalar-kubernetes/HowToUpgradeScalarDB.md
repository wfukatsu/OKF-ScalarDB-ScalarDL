---
type: Deployment Guide
title: How to Upgrade ScalarDB
description: This guide explains how to upgrade to a newer version of ScalarDB.
resource: https://scalardb.scalar-labs.com/docs/latest/scalar-kubernetes/HowToUpgradeScalarDB/
tags:
- scalardb
- v3.18
- phase:operate
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.18'
patch_version: 3.18.0
doc_id: scalar-kubernetes/HowToUpgradeScalarDB
lifecycle_phase: operate
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:24Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/docs/scalar-kubernetes/HowToUpgradeScalarDB.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to Upgrade ScalarDB

This guide explains how to upgrade to a newer version of ScalarDB.

## Before you begin

Before you upgrade to a new version, please check the [ScalarDB Cluster Compatibility Matrix](https://scalardb.scalar-labs.com/docs/latest/scalardb-cluster/compatibility/) to ensure compatibility between ScalarDB Cluster and the client SDKs.

## Upgrade versions

To learn about upgrading your version of ScalarDB, select the type of upgrade you want to do.

**Upgrade to a major version**

Major versions do **not** keep backward compatibility. So, you might need to do special operations when you upgrade from one major version to another major version. For example:

- Update the database schema on the backend database side.
- Update the API in your application.

For details on what you need when you upgrade to a major version, please refer to the release notes for the major version that you want to upgrade to.

**Upgrade to a minor version**

Minor versions keep backward compatibility. So, you can upgrade ScalarDB from one minor version to another minor version in the same major version without doing any special operations. For example, you don't need to update the database schema on the backend database side or update the API in your application.

**ScalarDB Cluster (Enterprise Edition)**

If you use [Scalar Helm Chart](https://github.com/scalar-labs/helm-charts) to deploy ScalarDB Cluster, you can upgrade your ScalarDB Cluster deployment as follows:

1. Set the ScalarDB Cluster Helm Chart version as an environment variable. You can do this by running the following command to put the chart version into the environment variable `SCALAR_DB_CLUSTER_CHART_VERSION`:

```console
SCALAR_DB_CLUSTER_CHART_VERSION=1.5.0
```

   :::tip

   You can search for the chart version that corresponds to the ScalarDB Cluster version, run the following command:

```console
helm search repo scalar-labs/scalardb-cluster -l
```

   The following command might be helpful, but please make sure to replace the contents in the angle brackets with your version of ScalarDB Cluster:

```console
SCALAR_DB_CLUSTER_VERSION=<MAJOR>.<MINOR>.<PATCH>; SCALAR_DB_CLUSTER_CHART_VERSION=$(helm search repo scalar-labs/scalardb-cluster -l | grep -F "${SCALAR_DB_CLUSTER_VERSION}" | awk '{print $2}' | sort --version-sort -r | head -n 1)
```

   :::

1. Upgrade your ScalarDB Cluster deployment by replacing the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardb-cluster -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDB_CLUSTER> --version ${SCALAR_DB_CLUSTER_CHART_VERSION}
```

After you upgrade the ScalarDB Cluster deployment, you should consider upgrading the version of the [ScalarDB Cluster Java Client SDK](https://mvnrepository.com/artifact/com.scalar-labs/scalardb-cluster-java-client-sdk) or the [ScalarDB Cluster .NET Client SDK](https://www.nuget.org/packages/ScalarDB.Net.Client) on your application side.

**ScalarDB Core library (Community edition)**

ScalarDB Core is provided as a Java library. So, you can update the dependencies of your Java project and rebuild your application to upgrade ScalarDB versions.

**Upgrade to a patch version**

Patch versions keep backward compatibility. So, you can upgrade ScalarDB from one patch version to another patch version in the same major version and minor version without doing any special operations. For example, you don't need to update the database schema on the backend database side or update the API in your application.

The method for upgrading to a patch version is the same as for upgrading to a minor version. For details on how to upgrade, see the [Upgrade to a minor version](https://scalardb.scalar-labs.com/docs/latest/scalar-kubernetes/?versions=upgrade-minor-version) tab.

:::warning

ScalarDB does **not** support downgrading to a previous version (major, minor, or patch). You can only upgrade to a newer version.

:::
