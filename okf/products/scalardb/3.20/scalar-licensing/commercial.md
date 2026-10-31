---
type: Reference
title: How to Configure a Commercial License Key
description: To run ScalarDB Enterprise Standard/Premium or ScalarDB Analytics, you must create a configuration file and add your commercial license key and a certificate to the file. In your configuration file, copy one of the following...
resource: https://scalardb.scalar-labs.com/docs/latest/scalar-licensing/commercial/
tags:
- scalardb
- v3.20
- phase:operate
- edition:enterprise-standard
- edition:enterprise-premium
- edition:enterprise-option
status: stable
product: scalardb
product_title: ScalarDB
version: '3.20'
patch_version: 3.20.0
doc_id: scalar-licensing/commercial
lifecycle_phase: operate
editions:
- Enterprise Standard
- Enterprise Premium
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-10-31T09:32:43Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/e492bf010d9ca2699301d485735f6b13d0dec7fa/docs/scalar-licensing/commercial.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-10-30T13:58:08Z'
---

# How to Configure a Commercial License Key

To run ScalarDB Enterprise Standard/Premium or ScalarDB Analytics, you must create a configuration file and add your commercial license key and a certificate to the file. In your configuration file, copy one of the following configurations, based on the product you're using, and paste the contents in the configuration file, replacing `<YOUR_LICENSE_KEY>` with your license key.

:::note

- If you don't have a license key, please see [How to Configure a Trial License Key](./trial.md) for ready-to-use keys or [contact us](https://www.scalar-labs.com/contact) to obtain a commercial license.
- The licensing mechanism for ScalarDB verifies the signature, expiration date, and edition of your license key. However, it doesn't check deployment details such as the number of running Pods or contract-specific limits. Because of this, you may technically be able to deploy more Pods than your contract allows, so make sure you use the number you are allowed.

:::

## ScalarDB Enterprise Standard/Premium

```properties
scalar.db.cluster.node.licensing.license_key=<YOUR_LICENSE_KEY>
scalar.db.cluster.node.licensing.license_check_cert_pem=-----BEGIN CERTIFICATE-----\nMIICKzCCAdKgAwIBAgIIBXxj3s8NU+owCgYIKoZIzj0EAwIwbDELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMSMwIQYDVQQDExplbnRlcnByaXNlLnNjYWxhci1sYWJzLmNv\nbTAeFw0yMzExMTYwNzExNTdaFw0yNDAyMTUxMzE2NTdaMGwxCzAJBgNVBAYTAkpQ\nMQ4wDAYDVQQIEwVUb2t5bzERMA8GA1UEBxMIU2hpbmp1a3UxFTATBgNVBAoTDFNj\nYWxhciwgSW5jLjEjMCEGA1UEAxMaZW50ZXJwcmlzZS5zY2FsYXItbGFicy5jb20w\nWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATJx5gvAr+GZAHcBpUvDFDsUlFo4GNw\npRfsntzwStIP8ac3dew7HT4KbGBWei0BvIthleaqpv0AEP7JT6eYAkNvo14wXDAO\nBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwG\nA1UdEwEB/wQCMAAwHQYDVR0OBBYEFMIe+XuuZcnDX1c3TmUPlu3kNv/wMAoGCCqG\nSM49BAMCA0cAMEQCIGGlqKpgv+KW+Z1ZkjfMHjSGeUZKBLwfMtErVyc9aTdIAiAy\nvsZyZP6Or9o40x3l3pw/BT7wvy93Jm0T4vtVQH6Zuw==\n-----END CERTIFICATE-----
```

:::note

If you're deploying by using a Helm Chart, these configurations must be placed inside your custom values file. For details, see [Set Up ScalarDB Cluster on Kubernetes by Using a Helm Chart](../scalardb-cluster/setup-scalardb-cluster-on-kubernetes-by-using-helm-chart.md#step-2-deploy-scalardb-cluster-on-the-kubernetes-cluster-by-using-a-helm-chart).

:::

## ScalarDB Analytics (library for Spark)

```apacheconf
spark.sql.catalog.scalardb_catalog.license.key <YOUR_LICENSE_KEY>
spark.sql.catalog.scalardb_catalog.license.cert_pem -----BEGIN CERTIFICATE-----\nMIICKzCCAdKgAwIBAgIIBXxj3s8NU+owCgYIKoZIzj0EAwIwbDELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMSMwIQYDVQQDExplbnRlcnByaXNlLnNjYWxhci1sYWJzLmNv\nbTAeFw0yMzExMTYwNzExNTdaFw0yNDAyMTUxMzE2NTdaMGwxCzAJBgNVBAYTAkpQ\nMQ4wDAYDVQQIEwVUb2t5bzERMA8GA1UEBxMIU2hpbmp1a3UxFTATBgNVBAoTDFNj\nYWxhciwgSW5jLjEjMCEGA1UEAxMaZW50ZXJwcmlzZS5zY2FsYXItbGFicy5jb20w\nWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATJx5gvAr+GZAHcBpUvDFDsUlFo4GNw\npRfsntzwStIP8ac3dew7HT4KbGBWei0BvIthleaqpv0AEP7JT6eYAkNvo14wXDAO\nBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwG\nA1UdEwEB/wQCMAAwHQYDVR0OBBYEFMIe+XuuZcnDX1c3TmUPlu3kNv/wMAoGCCqG\nSM49BAMCA0cAMEQCIGGlqKpgv+KW+Z1ZkjfMHjSGeUZKBLwfMtErVyc9aTdIAiAy\nvsZyZP6Or9o40x3l3pw/BT7wvy93Jm0T4vtVQH6Zuw==\n-----END CERTIFICATE-----
```

## ScalarDB Analytics server

```properties
scalar.db.analytics.server.licensing.license_key=<YOUR_LICENSE_KEY>
scalar.db.analytics.server.licensing.license_check_cert_pem=-----BEGIN CERTIFICATE-----\nMIICKzCCAdKgAwIBAgIIBXxj3s8NU+owCgYIKoZIzj0EAwIwbDELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMSMwIQYDVQQDExplbnRlcnByaXNlLnNjYWxhci1sYWJzLmNv\nbTAeFw0yMzExMTYwNzExNTdaFw0yNDAyMTUxMzE2NTdaMGwxCzAJBgNVBAYTAkpQ\nMQ4wDAYDVQQIEwVUb2t5bzERMA8GA1UEBxMIU2hpbmp1a3UxFTATBgNVBAoTDFNj\nYWxhciwgSW5jLjEjMCEGA1UEAxMaZW50ZXJwcmlzZS5zY2FsYXItbGFicy5jb20w\nWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATJx5gvAr+GZAHcBpUvDFDsUlFo4GNw\npRfsntzwStIP8ac3dew7HT4KbGBWei0BvIthleaqpv0AEP7JT6eYAkNvo14wXDAO\nBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwG\nA1UdEwEB/wQCMAAwHQYDVR0OBBYEFMIe+XuuZcnDX1c3TmUPlu3kNv/wMAoGCCqG\nSM49BAMCA0cAMEQCIGGlqKpgv+KW+Z1ZkjfMHjSGeUZKBLwfMtErVyc9aTdIAiAy\nvsZyZP6Or9o40x3l3pw/BT7wvy93Jm0T4vtVQH6Zuw==\n-----END CERTIFICATE-----
```

:::note

If you're deploying by using a Helm Chart, these configurations must be placed inside your custom values file. For details, see [Deploy a ScalarDB Analytics Server](https://scalardb.scalar-labs.com/docs/latest/scalardb-analytics/deploy-scalardb-analytics-server.mdx?billing-plan=byol-container-offer#set-the-required-configurations).

:::
