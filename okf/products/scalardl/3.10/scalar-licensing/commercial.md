---
type: Reference
title: How to Configure a Commercial License Key
description: To run ScalarDL Enterprise, you must create a .properties file and add your commercial license key and a certificate to the file. In your .properties file, copy one of the following configurations, based on the product you're using, and...
resource: https://scalardl.scalar-labs.com/docs/3.10/scalar-licensing/commercial/
tags:
- scalardl
- v3.10
- phase:implement
- section:reference
- edition:enterprise
- unmaintained
status: deprecated
product: scalardl
product_title: ScalarDL
version: '3.10'
patch_version: 3.10.5
doc_id: scalar-licensing/commercial
lifecycle_phase: implement
breadcrumb:
- Reference
- Configure a License Key
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:03Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.10/scalar-licensing/commercial.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# How to Configure a Commercial License Key

To run ScalarDL Enterprise, you must create a `.properties` file and add your commercial license key and a certificate to the file. In your `.properties` file, copy one of the following configurations, based on the product you're using, and paste the contents in the `.properties` file, replacing `<YOUR_LICENSE_KEY>` with your license key.

:::note

- If you don't have a license key, please see [How to Configure a Trial License Key](./trial.md) for ready-to-use keys or [contact us](https://www.scalar-labs.com/contact) to obtain a commercial license.
- The licensing mechanism for ScalarDL verifies the signature, expiration date, and edition of your license key. However, it doesn't check deployment details such as the number of running Pods or contract-specific limits. Because of this, you may technically be able to deploy more Pods than your contract allows, so make sure you use the number you are allowed.

:::

## ScalarDL Ledger

```properties
scalar.dl.licensing.license_key=<YOUR_LICENSE_KEY>
scalar.dl.licensing.license_check_cert_pem=-----BEGIN CERTIFICATE-----\nMIICKzCCAdKgAwIBAgIIBXxj3s8NU+owCgYIKoZIzj0EAwIwbDELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMSMwIQYDVQQDExplbnRlcnByaXNlLnNjYWxhci1sYWJzLmNv\nbTAeFw0yMzExMTYwNzExNTdaFw0yNDAyMTUxMzE2NTdaMGwxCzAJBgNVBAYTAkpQ\nMQ4wDAYDVQQIEwVUb2t5bzERMA8GA1UEBxMIU2hpbmp1a3UxFTATBgNVBAoTDFNj\nYWxhciwgSW5jLjEjMCEGA1UEAxMaZW50ZXJwcmlzZS5zY2FsYXItbGFicy5jb20w\nWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATJx5gvAr+GZAHcBpUvDFDsUlFo4GNw\npRfsntzwStIP8ac3dew7HT4KbGBWei0BvIthleaqpv0AEP7JT6eYAkNvo14wXDAO\nBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwG\nA1UdEwEB/wQCMAAwHQYDVR0OBBYEFMIe+XuuZcnDX1c3TmUPlu3kNv/wMAoGCCqG\nSM49BAMCA0cAMEQCIGGlqKpgv+KW+Z1ZkjfMHjSGeUZKBLwfMtErVyc9aTdIAiAy\nvsZyZP6Or9o40x3l3pw/BT7wvy93Jm0T4vtVQH6Zuw==\n-----END CERTIFICATE-----
```

## ScalarDL Auditor

```properties
scalar.dl.licensing.license_key=<YOUR_LICENSE_KEY>
scalar.dl.licensing.license_check_cert_pem=-----BEGIN CERTIFICATE-----\nMIICKzCCAdKgAwIBAgIIBXxj3s8NU+owCgYIKoZIzj0EAwIwbDELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMSMwIQYDVQQDExplbnRlcnByaXNlLnNjYWxhci1sYWJzLmNv\nbTAeFw0yMzExMTYwNzExNTdaFw0yNDAyMTUxMzE2NTdaMGwxCzAJBgNVBAYTAkpQ\nMQ4wDAYDVQQIEwVUb2t5bzERMA8GA1UEBxMIU2hpbmp1a3UxFTATBgNVBAoTDFNj\nYWxhciwgSW5jLjEjMCEGA1UEAxMaZW50ZXJwcmlzZS5zY2FsYXItbGFicy5jb20w\nWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATJx5gvAr+GZAHcBpUvDFDsUlFo4GNw\npRfsntzwStIP8ac3dew7HT4KbGBWei0BvIthleaqpv0AEP7JT6eYAkNvo14wXDAO\nBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwG\nA1UdEwEB/wQCMAAwHQYDVR0OBBYEFMIe+XuuZcnDX1c3TmUPlu3kNv/wMAoGCCqG\nSM49BAMCA0cAMEQCIGGlqKpgv+KW+Z1ZkjfMHjSGeUZKBLwfMtErVyc9aTdIAiAy\nvsZyZP6Or9o40x3l3pw/BT7wvy93Jm0T4vtVQH6Zuw==\n-----END CERTIFICATE-----
```
