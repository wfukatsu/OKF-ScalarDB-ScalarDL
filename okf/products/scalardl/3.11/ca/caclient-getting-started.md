---
type: Development Guide
title: How to Get a Certificate
description: This document describes how to get a certificate to enroll in ScalarDL.
resource: https://scalardl.scalar-labs.com/docs/3.11/ca/caclient-getting-started/
tags:
- scalardl
- v3.11
- phase:implement
- section:develop
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.11'
patch_version: 3.11.3
doc_id: ca/caclient-getting-started
lifecycle_phase: implement
breadcrumb:
- Develop
- Reference
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:02Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/c1dbc91f4c36ec4ce63e7181302c89b7b6669e62/versioned_docs/version-3.11/ca/caclient-getting-started.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-08-04T15:05:14Z'
---

# How to Get a Certificate

This document describes how to get a certificate to enroll in ScalarDL.

ScalarDL has several kinds of authentication methods. If you use `digital-signature` as the authentication method, you must prepare private key and certificate files. For more details on authentication methods, see [ScalarDL Authentication Guide](../authentication.md).

## Private key and certificate requirements

If you use [`digital-signature`](../authentication.md#digital-signatures) as the authentication method, you must create a private key and certificate that satisfy the following requirements:

- `SEC1` or `PKCS#8` key
- `ECDSA` as the algorithm
- `P-256` as the curve parameter
- `SHA256` as the hash function

:::note

ScalarDL does not check the expiration date of certificates. So, you can set any expiration dates to certificates that ScalarDL uses.

:::

## Create a private key and certificate file

**Self-signed**

You can create a self-signed certificate as follows:

:::note

This example creates a `SEC1` key.

:::

**CFSSL**

### Prerequisites

You must install the [cfssl and cfssljson](https://github.com/cloudflare/cfssl) command-line tools for the following steps.

### Create a local CA

1. Create a working directory.

```console
mkdir -p ${HOME}/scalardl/digital-signature/certs/
```

1. Change the working directory to `${HOME}/scalardl/digital-signature/certs/`.

```console
cd ${HOME}/scalardl/digital-signature/certs/
```

1. Create a JSON file that includes CA information.

```console
cat << 'EOF' > ${HOME}/scalardl/digital-signature/certs/ca.json
{
    "CN": "scalardl-example-ca",
    "key": {
        "algo": "ecdsa",
        "size": 256
    },
    "names": [
        {
            "C": "JP",
            "ST": "Tokyo",
            "L": "Shinjuku",
            "O": "ScalarDL Example CA"
        }
    ]
}
EOF
```

1. Create the CA private key and certificate files.

```console
cfssl gencert -initca ca.json | cfssljson -bare ca
```

1. Create a JSON file that includes CA configurations.

```console
cat << 'EOF' > ${HOME}/scalardl/digital-signature/certs/ca-config.json
{
    "signing": {
        "default": {
            "expiry": "87600h"
        },
        "profiles": {
            "scalardl-example-ca": {
                "expiry": "87600h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "server auth"
                ]
            }
        }
    }
}
EOF
```

### Create a private key and certificate for each component

**ScalarDL Ledger**

1. Create a JSON file that includes ScalarDL Ledger information.

```console
cat << 'EOF' > ${HOME}/scalardl/digital-signature/certs/ledger.json
{
    "CN": "scalardl-ledger",
    "hosts": [
        "ledger.scalardl.example.com",
        "localhost"
    ],
    "key": {
        "algo": "ecdsa",
        "size": 256
    },
    "names": [
        {
            "C": "JP",
            "ST": "Tokyo",
            "L": "Shinjuku",
            "O": "ScalarDL Ledger Example"
        }
    ]
}
EOF
```

1. Create the private key and certificate files for ScalarDL Ledger.

```console
cfssl gencert -ca ca.pem -ca-key ca-key.pem -config ca-config.json -profile scalardl-example-ca ledger.json | cfssljson -bare ledger
```

1. Confirm that the private key and certificate files were created.

```console
ls -1
```

   You should see the following output:

```console
ca-config.json
ca-key.pem
ca.csr
ca.json
ca.pem
ledger-key.pem
ledger.csr
ledger.json
ledger.pem
```

   In this case:

   - `ledger-key.pem` is the private key file for ScalarDL Ledger.
   - `ledger.pem` is the certificate file for ScalarDL Ledger.
   - `ca.pem` is the root CA certificate file.

**ScalarDL Auditor**

1. Create a JSON file that includes ScalarDL Auditor information.

```console
cat << 'EOF' > ${HOME}/scalardl/digital-signature/certs/auditor.json
{
    "CN": "scalardl-auditor",
    "hosts": [
        "auditor.scalardl.example.com",
        "localhost"
    ],
    "key": {
        "algo": "ecdsa",
        "size": 256
    },
    "names": [
        {
            "C": "JP",
            "ST": "Tokyo",
            "L": "Shinjuku",
            "O": "ScalarDL Auditor Example"
        }
    ]
}
EOF
```

1. Create the private key and certificate files for ScalarDL Auditor.

```console
cfssl gencert -ca ca.pem -ca-key ca-key.pem -config ca-config.json -profile scalardl-example-ca auditor.json | cfssljson -bare auditor
```

1. Confirm that the private key and certificate files were created.

```console
ls -1
```

   You should see the following output:

```console
auditor-key.pem
auditor.csr
auditor.json
auditor.pem
ca-config.json
ca-key.pem
ca.csr
ca.json
ca.pem
```

   In this case:

   - `auditor-key.pem` is the private key file for ScalarDL Auditor.
   - `auditor.pem` is the certificate file for ScalarDL Auditor.
   - `ca.pem` is the root CA certificate file.

**Client**

1. Create a JSON file that includes client information.

```console
cat << 'EOF' > ${HOME}/scalardl/digital-signature/certs/client.json
{
    "CN": "scalardl-client",
    "hosts": [
        "client.scalardl.example.com",
        "localhost"
    ],
    "key": {
        "algo": "ecdsa",
        "size": 256
    },
    "names": [
        {
            "C": "JP",
            "ST": "Tokyo",
            "L": "Shinjuku",
            "O": "ScalarDL Client Example"
        }
    ]
}
EOF
```

1. Create the private key and certificate files for the client.

```console
cfssl gencert -ca ca.pem -ca-key ca-key.pem -config ca-config.json -profile scalardl-example-ca client.json | cfssljson -bare client
```

1. Confirm that the private key and certificate files were created.

```console
ls -1
```

   You should see the following output:

```console
ca-config.json
ca-key.pem
ca.csr
ca.json
ca.pem
client-key.pem
client.csr
client.json
client.pem
```

   In this case:

   - `client-key.pem` is the private key file for the client.
   - `client.pem` is the certificate file for the client.
   - `ca.pem` is the root CA certificate file.

**OpenSSL**

### Prerequisites

You must install the `openssl` command-line tool for the following steps.

### Create a working directory

1. Create a working directory.

```console
mkdir -p ${HOME}/scalardl/digital-signature/certs/
```

1. Change the working directory to `${HOME}/scalardl/digital-signature/certs/`.

```console
cd ${HOME}/scalardl/digital-signature/certs/
```

### Create a private key and certificate for each component

**ScalarDL Ledger**

1. Create an EC parameter.

```console
openssl ecparam -name prime256v1 -out prime256v1.pem
```

1. Create a private key and CSR.

```console
openssl req -new -newkey ec:prime256v1.pem -nodes -keyout ledger-key.pem -out ledger.csr
```

1. Convert the `PKCS#8` key to the `SEC1` key.

```console
openssl ec -in ledger-key.pem -out ledger-key.pem
```

1. Create a certificate for ScalarDL Ledger.

```console
openssl x509 -req -days 3650 -signkey ledger-key.pem -in ledger.csr -out ledger.pem
```

1. Confirm that the private key and certificate files were created.

```console
ls -1
```

   You should see the following output:

```console
ledger-key.pem
ledger.csr
ledger.pem
prime256v1.pem
```

   In this case:

   - `ledger-key.pem` is the private key file for ScalarDL Ledger.
   - `ledger.pem` is the certificate file for ScalarDL Ledger.

**ScalarDL Auditor**

1. Create an EC parameter.

```console
openssl ecparam -name prime256v1 -out prime256v1.pem
```

1. Create a private key and CSR.

```console
openssl req -new -newkey ec:prime256v1.pem -nodes -keyout auditor-key.pem -out auditor.csr
```

1. Convert the `PKCS#8` key to the `SEC1` key.

```console
openssl ec -in auditor-key.pem -out auditor-key.pem
```

1. Create a certificate for ScalarDL Auditor.

```console
openssl x509 -req -days 3650 -signkey auditor-key.pem -in auditor.csr -out auditor.pem
```

1. Confirm that the private key and certificate files were created.

```console
ls -1
```

   You should see the following output:

```console
auditor-key.pem
auditor.csr
auditor.pem
prime256v1.pem
```

   In this case:

   - `auditor-key.pem` is the private key file for ScalarDL Auditor.
   - `auditor.pem` is the certificate file for ScalarDL Auditor.

**Client**

1. Create an EC parameter.

```console
openssl ecparam -name prime256v1 -out prime256v1.pem
```

1. Create a private key and CSR.

```console
openssl req -new -newkey ec:prime256v1.pem -nodes -keyout client-key.pem -out client.csr
```

1. Convert the `PKCS#8` key to the `SEC1` key.

```console
openssl ec -in client-key.pem -out client-key.pem
```

1. Create a certificate for the client.

```console
openssl x509 -req -days 3650 -signkey client-key.pem -in client.csr -out client.pem
```

1. Confirm that the private key and certificate files were created.

```console
ls -1
```

   You should see the following output:

```console
client-key.pem
client.csr
client.pem
prime256v1.pem
```

   In this case:

   - `client-key.pem` is the private key file for the client.
   - `client.pem` is the certificate file for the client.

**CFSSL server**

You can ask your [CFSSL server](./caserver-getting-started.md) to create a certificate file.

### Prerequisites

You must install the [cfssl and cfssljson](https://github.com/cloudflare/cfssl) command-line tools for the following steps.

### Create a private key and certificate file

1. Create a private key and CSR based on the [requirements](#private-key-and-certificate-requirements) by using a tool such as CFSSL or OpenSSL. You can see an example of how to create a private key and CSR by using the `cfssl` command in the [CFSSL](https://scalardl.scalar-labs.com/docs/3.11/ca/?methods=self-signed&tools=cfssl) tab or the `openssl` command in the [OpenSSL](https://scalardl.scalar-labs.com/docs/3.11/ca/?methods=self-signed&tools=openssl) tab.

1. Request a certificate from your CFSSL server.

       :::note

- The `-remote` option is needed to specify the CFSSL server endpoint URI.
- The `-bare` option for cfssljson is needed to specify a prefix for the output key files.

       :::

**ScalarDL Ledger**

```console
cfssl sign -remote "<IP_ADDRESS_OF_CFSSL_SERVER>:<PORT_OF_CFSSL_SERVER>" -profile "ledger" ledger.csr | cfssljson -bare ledger -
```

You will get a certificate named `ledger.pem` from the CFSSL server. You can use that certificate for ScalarDL Ledger.

**ScalarDL Auditor**

```console
cfssl sign -remote "<IP_ADDRESS_OF_CFSSL_SERVER>:<PORT_OF_CFSSL_SERVER>" -profile "auditor" auditor.csr | cfssljson -bare auditor -
```

You will get a certificate named `auditor.pem` from the CFSSL server. You can use that certificate for ScalarDL Auditor.

**Client**

```console
cfssl sign -remote "<IP_ADDRESS_OF_CFSSL_SERVER>:<PORT_OF_CFSSL_SERVER>" -profile "client" client.csr | cfssljson -bare client -
```

You will get a certificate named `client.pem` from the CFSSL server. You can use that certificate for the clients.

**Third-party CA or Private CA**

You can use a third-party CA or your private CA to create a certificate file. For details on how to create a certificate file, please ask your preferred third-party CA or private CA.
