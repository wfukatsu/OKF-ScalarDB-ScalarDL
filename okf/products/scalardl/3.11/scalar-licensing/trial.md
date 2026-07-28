---
type: Reference
title: How to Configure a Trial License Key
description: You can use the following trial license keys for ScalarDL Enterprise. If you have a commercial license key, please refer to Configure a Commercial License Key to configure your license key.
resource: https://scalardl.scalar-labs.com/docs/3.11/scalar-licensing/trial/
tags:
- scalardl
- v3.11
- phase:implement
- section:reference
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.3
doc_id: scalar-licensing/trial
lifecycle_phase: implement
breadcrumb:
- Reference
- Configure a License Key
editions:
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:08Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/versioned_docs/version-3.11/scalar-licensing/trial.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# How to Configure a Trial License Key

You can use the following trial license keys for ScalarDL Enterprise. If you have a commercial license key, please refer to [Configure a Commercial License Key](./commercial.md) to configure your license key.

To run ScalarDL Enterprise, you must create a `.properties` file and add the trial license key and the certificate to the file. In your `.properties` file, copy one of the following configurations, based on the product you're using, and paste the contents in the `.properties` file.

:::warning

- These trial license keys are for non-production, evaluation purposes only.
- These trial licenses are provided "as-is" without any warranty, and Scalar shall not be liable for any damages arising from their use.
- When using a trial license, ScalarDL must be connected to the Internet to validate the license and check its expiration.
- Redistribution or reverse engineering of these license keys is strictly prohibited.
- These trial license keys are updated periodically. For production use, please [contact us](https://www.scalar-labs.com/contact) to obtain a commercial license.

:::

## ScalarDL Ledger

:::note

ScalarDL Ledger is also available as open-source software under the Apache 2.0 License on [GitHub](https://github.com/scalar-labs/scalardl).

:::

```properties
scalar.dl.licensing.license_key={"organization_name":"Trial","product_name":"ScalarDL Ledger","product_version":3,"license_type":"trial","signature":"MEQCICQJbp1Q7F5vTZQV5/7t3/zf7B3Iyv8wiVMpkuixAVLoAiAFirR94xIBQEO/SXGnw5ykZdU94tU6WduyW96Hb3UD7g==","expiration_date_time":"2026-08-30T10:44:26.677+09:00[Asia/Tokyo]"}
scalar.dl.licensing.license_check_cert_pem=-----BEGIN CERTIFICATE-----\nMIICIzCCAcigAwIBAgIIKT9LIGX1TJQwCgYIKoZIzj0EAwIwZzELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMR4wHAYDVQQDExV0cmlhbC5zY2FsYXItbGFicy5jb20wHhcN\nMjMxMTE2MDcxMDM5WhcNMjQwMjE1MTMxNTM5WjBnMQswCQYDVQQGEwJKUDEOMAwG\nA1UECBMFVG9reW8xETAPBgNVBAcTCFNoaW5qdWt1MRUwEwYDVQQKEwxTY2FsYXIs\nIEluYy4xHjAcBgNVBAMTFXRyaWFsLnNjYWxhci1sYWJzLmNvbTBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABBSkIYAk7r5FRDf5qRQ7dbD3ib5g3fb643h4hqCtK+lC\nwM4AUr+PPRoquAy+Ey2sWEvYrWtl2ZjiYyyiZw8slGCjXjBcMA4GA1UdDwEB/wQE\nAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIw\nADAdBgNVHQ4EFgQUbFyOWFrsjkkOvjw6vK3gGUADGOcwCgYIKoZIzj0EAwIDSQAw\nRgIhAKwigOb74z9BdX1+dUpeVG8WrzLTIqdIU0w+9jhAueXoAiEA6cniJ3qsP4j7\nsck62kHnFpH1fCUOc/b/B8ZtfeXI2Iw=\n-----END CERTIFICATE-----
```

## ScalarDL Auditor

```properties
scalar.dl.licensing.license_key={"organization_name":"Trial","product_name":"ScalarDL Auditor","product_version":3,"license_type":"trial","signature":"MEUCIQD/vPeTWq7Z/eJMDfmPV6B9XlDDJGvMnwwta+KRoGhE3wIgV6c+gyTZit1JB2u7XLaVm/JznYK3URjTQQ+6vP72lkc=","expiration_date_time":"2026-08-30T10:44:28.297+09:00[Asia/Tokyo]"}
scalar.dl.licensing.license_check_cert_pem=-----BEGIN CERTIFICATE-----\nMIICIzCCAcigAwIBAgIIKT9LIGX1TJQwCgYIKoZIzj0EAwIwZzELMAkGA1UEBhMC\nSlAxDjAMBgNVBAgTBVRva3lvMREwDwYDVQQHEwhTaGluanVrdTEVMBMGA1UEChMM\nU2NhbGFyLCBJbmMuMR4wHAYDVQQDExV0cmlhbC5zY2FsYXItbGFicy5jb20wHhcN\nMjMxMTE2MDcxMDM5WhcNMjQwMjE1MTMxNTM5WjBnMQswCQYDVQQGEwJKUDEOMAwG\nA1UECBMFVG9reW8xETAPBgNVBAcTCFNoaW5qdWt1MRUwEwYDVQQKEwxTY2FsYXIs\nIEluYy4xHjAcBgNVBAMTFXRyaWFsLnNjYWxhci1sYWJzLmNvbTBZMBMGByqGSM49\nAgEGCCqGSM49AwEHA0IABBSkIYAk7r5FRDf5qRQ7dbD3ib5g3fb643h4hqCtK+lC\nwM4AUr+PPRoquAy+Ey2sWEvYrWtl2ZjiYyyiZw8slGCjXjBcMA4GA1UdDwEB/wQE\nAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIw\nADAdBgNVHQ4EFgQUbFyOWFrsjkkOvjw6vK3gGUADGOcwCgYIKoZIzj0EAwIDSQAw\nRgIhAKwigOb74z9BdX1+dUpeVG8WrzLTIqdIU0w+9jhAueXoAiEA6cniJ3qsP4j7\nsck62kHnFpH1fCUOc/b/B8ZtfeXI2Iw=\n-----END CERTIFICATE-----
```
