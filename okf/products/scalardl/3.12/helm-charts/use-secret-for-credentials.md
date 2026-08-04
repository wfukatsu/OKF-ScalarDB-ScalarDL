---
type: Deployment Guide
title: How to use Secret resources to pass credentials as environment variables into the properties file
description: You can pass credentials like username or password as environment variables via a Secret resource in Kubernetes. The docker images for previous versions of Scalar products use the dockerize command for templating properties files. The...
resource: https://scalardl.scalar-labs.com/docs/3.12/helm-charts/use-secret-for-credentials/
tags:
- scalardl
- v3.12
- phase:operate
- section:deploy
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardl
product_title: ScalarDL
version: '3.12'
patch_version: 3.12.3
doc_id: helm-charts/use-secret-for-credentials
lifecycle_phase: operate
breadcrumb:
- Deploy
- Reference
- Configuration Guides
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:01Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.12/helm-charts/use-secret-for-credentials.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# How to use Secret resources to pass credentials as environment variables into the properties file

You can pass credentials like **username** or **password** as environment variables via a `Secret` resource in Kubernetes. The docker images for previous versions of Scalar products use the `dockerize` command for templating properties files. The docker images for the latest versions of Scalar products get values directly from environment variables.

Note: You cannot use the following environment variable names in your custom values file since these are used in the Scalar Helm Chart internal.

```console
HELM_SCALAR_DB_CONTACT_POINTS
HELM_SCALAR_DB_CONTACT_PORT
HELM_SCALAR_DB_USERNAME
HELM_SCALAR_DB_PASSWORD
HELM_SCALAR_DB_STORAGE
HELM_SCALAR_DL_LEDGER_PROOF_ENABLED
HELM_SCALAR_DL_LEDGER_AUDITOR_ENABLED
HELM_SCALAR_DL_LEDGER_PROOF_PRIVATE_KEY_PATH
HELM_SCALAR_DL_AUDITOR_SERVER_PORT
HELM_SCALAR_DL_AUDITOR_SERVER_PRIVILEGED_PORT
HELM_SCALAR_DL_AUDITOR_SERVER_ADMIN_PORT
HELM_SCALAR_DL_AUDITOR_LEDGER_HOST
HELM_SCALAR_DL_AUDITOR_CERT_HOLDER_ID
HELM_SCALAR_DL_AUDITOR_CERT_VERSION
HELM_SCALAR_DL_AUDITOR_CERT_PATH
HELM_SCALAR_DL_AUDITOR_PRIVATE_KEY_PATH
SCALAR_DB_LOG_LEVEL
SCALAR_DL_LEDGER_LOG_LEVEL
SCALAR_DL_AUDITOR_LOG_LEVEL
SCALAR_DB_CLUSTER_MEMBERSHIP_KUBERNETES_ENDPOINT_NAMESPACE_NAME
SCALAR_DB_CLUSTER_MEMBERSHIP_KUBERNETES_ENDPOINT_NAME
```

1. Set environment variable name to the properties configuration in the custom values file. See the following examples based on the product you're using.

**ScalarDB Cluster**

```yaml
scalardbCluster:
  scalardbClusterNodeProperties: |
    ...
    scalar.db.username=${env:SCALAR_DB_USERNAME}
    scalar.db.password=${env:SCALAR_DB_PASSWORD}
    ...
```

**ScalarDB Server (Deprecated)**

### ScalarDB Server 3.8 or later (Apache Commons Text syntax)

```yaml
scalardb:
  databaseProperties: |
    ...
    scalar.db.username=${env:SCALAR_DB_USERNAME}
    scalar.db.password=${env:SCALAR_DB_PASSWORD}
    ...
```

### ScalarDB Server 3.7 or earlier (Go template syntax)

```yaml
scalardb:
  databaseProperties: |
    ...
    scalar.db.username={{ default .Env.SCALAR_DB_USERNAME "" }}
    scalar.db.password={{ default .Env.SCALAR_DB_PASSWORD "" }}
    ...
```

**ScalarDL Ledger**

### ScalarDL Ledger 3.8 or later (Apache Commons Text syntax)

```yaml
ledger:
  ledgerProperties: |
    ...
    scalar.db.username=${env:SCALAR_DB_USERNAME}
    scalar.db.password=${env:SCALAR_DB_PASSWORD}
    ...
```

### ScalarDL Ledger 3.7 or earlier (Go template syntax)

```yaml
ledger:
  ledgerProperties: |
    ...
    scalar.db.username={{ default .Env.SCALAR_DB_USERNAME "" }}
    scalar.db.password={{ default .Env.SCALAR_DB_PASSWORD "" }}
    ...
```

**ScalarDL Auditor**

### ScalarDL Auditor 3.8 or later (Apache Commons Text syntax)

```yaml
auditor:
  auditorProperties: |
    ...
    scalar.db.username=${env:SCALAR_DB_USERNAME}
    scalar.db.password=${env:SCALAR_DB_PASSWORD}
    ...
```

### ScalarDL Auditor 3.7 or earlier (Go template syntax)

```yaml
auditor:
  auditorProperties: |
    ...
    scalar.db.username={{ default .Env.SCALAR_DB_USERNAME "" }}
    scalar.db.password={{ default .Env.SCALAR_DB_PASSWORD "" }}
    ...
```

**ScalarDL Schema Loader**

### ScalarDL Schema Loader 3.8 or later (Apache Commons Text syntax)

```yaml
schemaLoading:
  databaseProperties: |
    ...
    scalar.db.username=${env:SCALAR_DB_USERNAME}
    scalar.db.password=${env:SCALAR_DB_PASSWORD}
    ...
```

### ScalarDL Schema Loader 3.7 or earlier (Go template syntax)

```yaml
schemaLoading:
  databaseProperties: |
    ...
    scalar.db.username={{ default .Env.SCALAR_DB_USERNAME "" }}
    scalar.db.password={{ default .Env.SCALAR_DB_PASSWORD "" }}
    ...
```

1. Create a `Secret` resource that includes credentials.
   You need to specify the environment variable name as keys of the `Secret`.
   * Example

```console
kubectl create secret generic scalardb-credentials-secret \
  --from-literal=SCALAR_DB_USERNAME=postgres \
  --from-literal=SCALAR_DB_PASSWORD=postgres
```

1. Set the `Secret` name to the following keys in the custom values file. See the following examples based on the product you're using.

**ScalarDB Cluster**

**Key:** `scalardbCluster.secretName`

```yaml
scalardbCluster:
  secretName: "scalardb-cluster-credentials-secret"
```

**ScalarDB Server (Deprecated)**

**Key:** `scalardb.secretName`

```yaml
scalardb:
  secretName: "scalardb-credentials-secret"
```

**ScalarDL Ledger**

**Key:** `ledger.secretName`

```yaml
ledger:
  secretName: "ledger-credentials-secret"
```

**ScalarDL Auditor**

**Key:** `auditor.secretName`

```yaml
auditor:
  secretName: "auditor-credentials-secret"
```

**ScalarDL Schema Loader**

**Key:** `schemaLoading.secretName`

```yaml
schemaLoading:
  secretName: "schema-loader-ledger-credentials-secret"
```

1. Deploy Scalar products with the above custom values file.

   After deploying Scalar products, the Go template strings (environment variables) are replaced by the values of the `Secret`.

   * Example
* Custom values file

```yaml
scalardb:
  databaseProperties: |
    scalar.db.contact_points=jdbc:postgresql://postgresql-scalardb.default.svc.cluster.local:5432/postgres
    scalar.db.username={{ default .Env.SCALAR_DB_USERNAME "" }}
    scalar.db.password={{ default .Env.SCALAR_DB_PASSWORD "" }}
    scalar.db.storage=jdbc
```

* Properties file in containers

```properties
scalar.db.contact_points=jdbc:postgresql://postgresql-scalardb.default.svc.cluster.local:5432/postgres
scalar.db.username=postgres
scalar.db.password=postgres
scalar.db.storage=jdbc
```

   If you use Apache Commons Text syntax, Scalar products get values directly from environment variables.
