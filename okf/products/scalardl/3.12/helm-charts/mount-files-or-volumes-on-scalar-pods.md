---
type: Deployment Guide
title: Mount any files or volumes on Scalar product pods
description: You can mount any files or volumes on Scalar product pods when you use ScalarDB Server, ScalarDB Cluster, or ScalarDL Helm Charts (ScalarDL Ledger and ScalarDL Auditor).
resource: https://scalardl.scalar-labs.com/docs/3.12/helm-charts/mount-files-or-volumes-on-scalar-pods/
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
doc_id: helm-charts/mount-files-or-volumes-on-scalar-pods
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
  at: '2026-07-28T00:57:07Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/versioned_docs/version-3.12/helm-charts/mount-files-or-volumes-on-scalar-pods.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Mount any files or volumes on Scalar product pods

You can mount any files or volumes on Scalar product pods when you use ScalarDB Server, ScalarDB Cluster, or ScalarDL Helm Charts (ScalarDL Ledger and ScalarDL Auditor).

## Mount a private key file on a pod in ScalarDL Helm Charts

You must mount the private key file to run ScalarDL Auditor.

* Configuration example
* ScalarDL Ledger
```yaml
ledger:
  ledgerProperties: |
    ...
    scalar.dl.ledger.proof.enabled=true
    scalar.dl.ledger.auditor.enabled=true
    scalar.dl.ledger.proof.private_key_path=/keys/private-key
```
* ScalarDL Auditor
```yaml
auditor:
  auditorProperties: |
    ...
    scalar.dl.auditor.private_key_path=/keys/private-key
```

In this example, you need to mount a **private-key** file under the `/keys` directory in the container. And, you need to mount a file named `private-key`. You can use `extraVolumes` and `extraVolumeMounts` to mount this file.

1. Set `extraVolumes` and `extraVolumeMounts` in the custom values file using the same syntax of Kubernetes manifest. You need to specify the directory name to the key `mountPath`.
   * Example
* ScalarDL Ledger
```yaml
ledger:
  extraVolumes:
    - name: ledger-keys
      secret:
        secretName: ledger-keys
  extraVolumeMounts:
    - name: ledger-keys
      mountPath: /keys
      readOnly: true
```
* ScalarDL Auditor
```yaml
auditor:
   extraVolumes:
     - name: auditor-keys
       secret:
         secretName: auditor-keys
   extraVolumeMounts:
     - name: auditor-keys
       mountPath: /keys
       readOnly: true
 ```

1. Create a `Secret` resource that includes a private key file.

   You need to specify the file name as keys of `Secret`.

   * Example
* ScalarDL Ledger
```console
kubectl create secret generic ledger-keys \
  --from-file=private-key=./ledger-key.pem
```
* ScalarDL Auditor
```console
kubectl create secret generic auditor-keys \
  --from-file=private-key=./auditor-key.pem
```

1. Deploy Scalar products with the above custom values file.

   After deploying Scalar products, the private key file is mounted under the `/keys` directory as follows.

   * Example
* ScalarDL Ledger
```console
ls -l /keys/
```

         You should see the following output:

```console
total 0
lrwxrwxrwx 1 root root 18 Jun 27 03:12 private-key -> ..data/private-key
```

* ScalarDL Auditor
```console
ls -l /keys/
```

         You should see the following output:

```console
total 0
lrwxrwxrwx 1 root root 18 Jun 27 03:16 private-key -> ..data/private-key
```

## Mount emptyDir to get a heap dump file

You can mount emptyDir to Scalar product pods by using the following keys in your custom values file. For example, you can use this volume to get a heap dump of Scalar products.

* Keys
  * `scalardb.extraVolumes` / `scalardb.extraVolumeMounts` (ScalarDB Server)
  * `scalardbCluster.extraVolumes` / `scalardbCluster.extraVolumeMounts` (ScalarDB Cluster)
  * `ledger.extraVolumes` / `ledger.extraVolumeMounts` (ScalarDL Ledger)
  * `auditor.extraVolumes` / `auditor.extraVolumeMounts` (ScalarDL Auditor)

* Example (ScalarDB Server)
```yaml
scalardb:
  extraVolumes:
    - name: heap-dump
      emptyDir: {}
  extraVolumeMounts:
    - name: heap-dump
      mountPath: /dump
```

In this example, you can see the mounted volume in the ScalarDB Server pod as follows.

```console
ls -ld /dump
```

You should see the following output:

```console
drwxrwxrwx 2 root root 4096 Feb  6 07:43 /dump
```
