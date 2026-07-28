---
type: Reference
title: How to Configure a Trial License Key
description: You can use the following trial license keys for ScalarDB Enterprise Standard/Premium and ScalarDB Analytics. If you have a commercial license key, please refer to How to Configure a Commercial License Key to configure your license key.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalar-licensing/trial/
tags:
- scalardb
- v3.16
- phase:implement
- section:reference
- edition:enterprise-standard
- edition:enterprise-premium
- edition:enterprise-option
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: scalar-licensing/trial
lifecycle_phase: implement
breadcrumb:
- Reference
- Configure a License Key
editions:
- Enterprise Standard
- Enterprise Premium
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/scalar-licensing/trial.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# How to Configure a Trial License Key

You can use the following trial license keys for ScalarDB Enterprise Standard/Premium and ScalarDB Analytics. If you have a commercial license key, please refer to [How to Configure a Commercial License Key](./commercial.md) to configure your license key.

To run ScalarDB Enterprise Standard/Premium or ScalarDB Analytics, you must create a `.properties` file and add the trial license key and the certificate to the file. In your `.properties` file, copy one of the following configurations, based on the product you're using, and paste the contents in the `.properties` file.

:::warning

- These trial license keys are for non-production, evaluation purposes only.
- These trial licenses are provided "as-is" without any warranty, and Scalar shall not be liable for any damages arising from their use.
- When using a trial license, ScalarDB Cluster and/or ScalarDB Analytics must be connected to the Internet to validate the license and check its expiration.
- Redistribution or reverse engineering of these license keys is strictly prohibited.
- These trial license keys are updated periodically. For production use, please [contact us](https://www.scalar-labs.com/contact) to obtain a commercial license.

:::

:::note

ScalarDB Core is available as open-source software under the Apache 2.0 License on [GitHub](https://github.com/scalar-labs/scalardb).

:::

## ScalarDB Enterprise Standard/Premium

```properties
scalar.db.cluster.node.licensing.license_key={"organization_name":"Trial","product_name":"ScalarDB Cluster","product_version":3,"license_type":"trial","signature":"MEUCIQDzRbDIaQR2yOBpl6GkB3AJWu9jHyUeGmGfOV6xxr2VlAIgJoDcCTN80m52m8JRbQcaJ+hgw7Os76lMHnn/wVdC/Oo=","expiration_date_time":"2026-08-30T10:44:23.496+09:00[Asia/Tokyo]"}
scalar.db.cluster.node.licensing.license_check_cert_pem=-----BEGIN CERTIFICATE-----\nMIICIzCCAcigAwIBAgIIKT9LIGX1TJQwCgYIKoZIzj0EAwIwZzELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMR4wHAYDVQQDExV0cmlhbC5zY2FsYXItbGFicy5jb20wHhcN\nMjMxMTE2MDcxMDM5WhcNMjQwMjE1MTMxNTM5WjBnMQswCQYDVQQGEwJKUDEOMAwG\nA1UECBMFVG9reW8xETAPBgNVBAcTCFNoaW5qdWt1MRUwEwYDVQQKEwxTY2FsYXIs\nIEluYy4xHjAcBgNVBAMTFXRyaWFsLnNjYWxhci1sYWJzLmNvbTBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABBSkIYAk7r5FRDf5qRQ7dbD3ib5g3fb643h4hqCtK+lC\nwM4AUr+PPRoquAy+Ey2sWEvYrWtl2ZjiYyyiZw8slGCjXjBcMA4GA1UdDwEB/wQE\nAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIw\nADAdBgNVHQ4EFgQUbFyOWFrsjkkOvjw6vK3gGUADGOcwCgYIKoZIzj0EAwIDSQAw\nRgIhAKwigOb74z9BdX1+dUpeVG8WrzLTIqdIU0w+9jhAueXoAiEA6cniJ3qsP4j7\nsck62kHnFpH1fCUOc/b/B8ZtfeXI2Iw=\n-----END CERTIFICATE-----
```

## ScalarDB Analytics

```apacheconf
spark.sql.catalog.scalardb_catalog.license.key {"organization_name":"Trial","product_name":"ScalarDB Analytics","product_version":3,"license_type":"trial","signature":"MEUCIFG1ecsXAbKafnfE2FSMjYDB8w15/HntGrC8RHXAUtc7AiEAr39FEbDIEr39kB+w7+rJETH25k3Ex/TnWNM9Wm1zYSc=","expiration_date_time":"2026-08-30T10:44:25.095+09:00[Asia/Tokyo]"}
spark.sql.catalog.scalardb_catalog.license.cert_pem -----BEGIN CERTIFICATE-----\nMIICIzCCAcigAwIBAgIIKT9LIGX1TJQwCgYIKoZIzj0EAwIwZzELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMR4wHAYDVQQDExV0cmlhbC5zY2FsYXItbGFicy5jb20wHhcN\nMjMxMTE2MDcxMDM5WhcNMjQwMjE1MTMxNTM5WjBnMQswCQYDVQQGEwJKUDEOMAwG\nA1UECBMFVG9reW8xETAPBgNVBAcTCFNoaW5qdWt1MRUwEwYDVQQKEwxTY2FsYXIs\nIEluYy4xHjAcBgNVBAMTFXRyaWFsLnNjYWxhci1sYWJzLmNvbTBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABBSkIYAk7r5FRDf5qRQ7dbD3ib5g3fb643h4hqCtK+lC\nwM4AUr+PPRoquAy+Ey2sWEvYrWtl2ZjiYyyiZw8slGCjXjBcMA4GA1UdDwEB/wQE\nAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIw\nADAdBgNVHQ4EFgQUbFyOWFrsjkkOvjw6vK3gGUADGOcwCgYIKoZIzj0EAwIDSQAw\nRgIhAKwigOb74z9BdX1+dUpeVG8WrzLTIqdIU0w+9jhAueXoAiEA6cniJ3qsP4j7\nsck62kHnFpH1fCUOc/b/B8ZtfeXI2Iw=\n-----END CERTIFICATE-----
```
