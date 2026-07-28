---
type: Operations Guide
title: How to Upgrade ScalarDL
description: This guide explains how to upgrade to a newer version of ScalarDL.
resource: https://scalardl.scalar-labs.com/docs/3.10/scalar-kubernetes/HowToUpgradeScalarDL/
tags:
- scalardl
- v3.10
- phase:operate
- section:manage
- edition:enterprise
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.10'
patch_version: 3.10.5
doc_id: scalar-kubernetes/HowToUpgradeScalarDL
lifecycle_phase: operate
breadcrumb:
- Manage
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:09Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/versioned_docs/version-3.10/scalar-kubernetes/HowToUpgradeScalarDL.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# How to Upgrade ScalarDL

This guide explains how to upgrade to a newer version of ScalarDL.

## Before you begin

Before you upgrade to a new version, please check the [ScalarDL Compatibility Matrix](https://scalardl.scalar-labs.com/docs/latest/compatibility/) to ensure compatibility between ScalarDL and the client SDKs.

## Upgrade versions

To learn about upgrading your version of ScalarDL, select the type of upgrade you want to do.

**Upgrade to a major version**

Major versions do **not** keep backward compatibility. So, you might need to do special operations when you upgrade from one major version to another major version. For example:

- Update the database schema on the backend database side.
- Update the API in your application.

For details on what you need when you upgrade to a major version, please refer to the release notes for the major version that you want to upgrade to.

**Upgrade to a minor version**

Minor versions keep backward compatibility. So, you can upgrade ScalarDL from one minor version to another minor version in the same major version without doing any special operations. For example, you don't need to update the database schema on the backend database side or update the API in your application.

**ScalarDL Ledger**

If you use [Scalar Helm Chart](https://github.com/scalar-labs/helm-charts) to deploy ScalarDL Ledger, you can upgrade your ScalarDL Ledger deployment as follows:

1. Set the ScalarDL Ledger Helm Chart version as an environment variable. You can do this by running the following command to put the chart version into the environment variable `SCALAR_DL_LEDGER_CHART_VERSION`:

```console
SCALAR_DL_LEDGER_CHART_VERSION=4.8.0
```

   :::tip

   You can search for the chart version that corresponds to the ScalarDL Ledger version as follows:

```console
helm search repo scalar-labs/scalardl -l
```

   The following command might be helpful, but please make sure to replace the contents in the angle brackets with your version of ScalarDL Ledger:

```console
SCALAR_DL_VERSION=<MAJOR>.<MINOR>.<PATCH>; SCALAR_DL_LEDGER_CHART_VERSION=$(helm search repo scalar-labs/scalardl -l | grep -v -e "scalar-labs/scalardl-audit" | grep -F "${SCALAR_DL_VERSION}" | awk '{print $2}' | sort --version-sort -r | head -n 1)
```

   :::

1. Upgrade your ScalarDL Ledger deployment by replacing the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardl -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDL_LEDGER> --version ${SCALAR_DL_LEDGER_CHART_VERSION}
```

After you upgrade the ScalarDL Ledger deployment (and the ScalarDL Auditor deployment if you use Auditor mode), you should consider upgrading the version of the [ScalarDL Java Client SDK](https://mvnrepository.com/artifact/com.scalar-labs/scalardl-java-client-sdk) on your application side.

**ScalarDL Auditor**

If you use [Scalar Helm Chart](https://github.com/scalar-labs/helm-charts) to deploy ScalarDL Auditor, you can upgrade your ScalarDL Auditor deployment as follows:

1. Set the ScalarDL Auditor Helm Chart version as an environment variable. You can do this by running the following command to put the chart version into the environment variable `SCALAR_DL_AUDITOR_CHART_VERSION`:

```console
SCALAR_DL_AUDITOR_CHART_VERSION=2.8.0
```

   :::tip

   You can search for the chart version that corresponds to the ScalarDL Auditor version as follows:

```console
helm search repo scalar-labs/scalardl-audit -l
```

   The following command might be helpful, but please make sure to replace the contents in the angle brackets with your version of ScalarDL Auditor:

```console
SCALAR_DL_VERSION=<MAJOR>.<MINOR>.<PATCH>; SCALAR_DL_AUDITOR_CHART_VERSION=$(helm search repo scalar-labs/scalardl-audit -l | grep -F "${SCALAR_DL_VERSION}" | awk '{print $2}' | sort --version-sort -r | head -n 1)
```

   :::

1. Upgrade your ScalarDL Auditor deployment by replacing the contents in the angle brackets as described:

```console
helm upgrade <RELEASE_NAME> scalar-labs/scalardl-audit -n <NAMESPACE> -f /<PATH_TO_YOUR_CUSTOM_VALUES_FILE_FOR_SCALARDL_AUDITOR> --version ${SCALAR_DL_AUDITOR_CHART_VERSION}
```

After you upgrade the ScalarDL Auditor deployment and the ScalarDL Ledger deployment, you should consider upgrading the version of the [ScalarDL Java Client SDK](https://mvnrepository.com/artifact/com.scalar-labs/scalardl-java-client-sdk) on your application side.

**Upgrade to a patch version**

Patch versions keep backward compatibility. So, you can upgrade ScalarDL from one patch version to another patch version in the same major version and minor version without doing any special operations. For example, you don't need to update the database schema on the backend database side or update the API in your application.

The method for upgrading to a patch version is the same as for upgrading to a minor version. For details on how to upgrade, see the [Upgrade to a minor version](https://scalardl.scalar-labs.com/docs/3.10/scalar-kubernetes/?versions=upgrade-minor-version) tab.

:::warning

ScalarDL does **not** support downgrading to a previous version (major, minor, or patch). You can only upgrade to a newer version.

:::
