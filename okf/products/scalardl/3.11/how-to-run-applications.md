---
type: Development Guide
title: Run a ScalarDL Application Through ScalarDL Ledger
description: This guide explains how to run a ScalarDL application through ScalarDL Ledger. This document assumes that you have already tried the Get Started with ScalarDL Ledger tutorial and created your application that integrates ScalarDL by using...
resource: https://scalardl.scalar-labs.com/docs/3.11/how-to-run-applications/
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
doc_id: how-to-run-applications
lifecycle_phase: implement
breadcrumb:
- Develop
- Run an Application
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:08Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/versioned_docs/version-3.11/how-to-run-applications.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# Run a ScalarDL Application Through ScalarDL Ledger

This guide explains how to run a ScalarDL application through ScalarDL Ledger. This document assumes that you have already tried the [Get Started with ScalarDL Ledger](./getting-started.md) tutorial and created your application that integrates ScalarDL by using the Client SDK by referring to the [Write a ScalarDL Application in Java](./how-to-write-applications.md) guide.

## Decide on configurations

Before running ScalarDL applications through Ledger, you first need to configure Ledger and the client that interacts with Ledger.

There are several important options that you must set and decisions to make as described below.

### Disable Auditor

You must disable Auditor since you'll be running your applications through only Ledger. Disabling Auditor has to be done in the client and Ledger configurations as follows.

- In the client configuration, set `scalar.dl.client.auditor.enabled` to `false`. (Since `false` is the default value, you can choose to omit this property.)
- In the Ledger configuration, set `scalar.dl.ledger.auditor.enabled` to `false`. (Since `false` is the default value, you can choose to omit this property.)

:::note

If you are using the `scalardl-samples` environment, see the `ledger.properties` file for the corresponding storage.

:::

For details about the configurations, see the following:

- [Client configurations](./configurations.md#client-configurations)
- [Ledger configurations](./configurations.md#ledger-configurations)

### Decide on which authentication method to use

You must decide which authentication method to use for clients: digital signature or HMAC. As a simple comparison, the digital-signature method provides non-repudiation in addition to authentication but is slow, whereas the HMAC method provides only authentication but is fast.

You can configure an authentication method as follows. The same method (`digital-signature` or `hmac`) must be configured in both the client and Ledger.

- In the client configuration, set `scalar.dl.client.authentication.method` to `digital-signature` or `hmac` (depending on which method you choose).
- In the Ledger configuration, set `scalar.dl.ledger.authentication.method` to `digital-signature` or `hmac` (depending on which method you choose).

You also need to prepare some secret information. If you're using the digital-signature method you need to prepare a certificate and a private key. If you're using the HMAC method, you need to prepare a secret key. For more details about the authentication in ScalarDL, check out the [ScalarDL Authentication Guide](./authentication.md).

For details about the configurations, see the following:

- [Client configurations](./configurations.md#client-configurations)
- [Ledger configurations](./configurations.md#ledger-configurations)

### Configure your database

Ledger uses ScalarDB to interact with databases, which enables you to run ScalarDL on top of various databases. So, you need to decide on a database that ScalarDB supports based on your applications' requirements and configure several ScalarDB parameters.

For details about the ScalarDB parameters, see also [ScalarDB Configurations](https://scalardb.scalar-labs.com/docs/latest/configurations/).

#### Underlying database

You can configure which database to use as follows:

- In the Ledger configuration, set `scalar.db.storage`, `scalar.db.contact_points`, `scalar.db.username`, and `scalar.db.password` to the appropriate values based on the database that you'll be using.

For databases and their versions supported by ScalarDL via ScalarDB, see [Requirements](./requirements.md#databases).

:::warning

If your applications read and write a table through the Function feature, and the table is also directly accessed from ScalarDB applications, you need to properly configure the database chosen here. Specifically, both ScalarDL and ScalarDB applications must refer to the same Coordinator table to guarantee consistency.

:::

#### Isolation level

Ledger relies on the [Consensus Commit](https://scalardb.scalar-labs.com/docs/latest/consensus-commit/) transaction manager of ScalarDB to manage transactions. The transaction manager is responsible for guaranteeing the isolation property of transactions, which is crucial for ensuring the consistency and correctness of transactions.

You can configure the isolation level of Ledger as follows. If you are unsure about which isolation level to use, use `SERIALIZABLE`.

- In the Ledger configuration, set `scalar.db.consensus_commit.isolation_level` to an isolation level of your choice. The default value is `SNAPSHOT`.

#### Limitations

While ScalarDL leverages ScalarDB, the following ScalarDB feature is not compatible with the consistency guarantee mechanism of ScalarDL:

- [Group commit for the Coordinator table](https://scalardb.scalar-labs.com/docs/latest/api-guide/#group-commit-for-the-coordinator-table) (`scalar.db.consensus_commit.coordinator.group_commit.enabled` must be `false`.)

### Decide which other configurations to use

You can also apply other configurations, such as TLS and gRPC configurations, for the client and Ledger. For details about the configurations, see the following:

- [Client configurations](./configurations.md#client-configurations)
- [Ledger configurations](./configurations.md#ledger-configurations)

## Start Ledger

After configuring Ledger and the client, you need to start up Ledger.

For details on how to locally start up Ledger by using Docker Compose, see [Start up ScalarDL with your preferred database](./getting-started.md#start-up-scalardl-with-your-preferred-database). For how to start up Ledger in local or cloud-based Kubernetes environments, see [Deploy ScalarDL in your local Kubernetes environment](./deploy-local-environment-overview.md) or [Deploy ScalarDL in a cloud-based Kubernetes environment](./deploy-managed-kubernetes-environment-overview.md), respectively.

## Download the Client SDK

If you need to run ScalarDL commands, you need to download the Client SDK. For instructions, see [Download the Client SDK](./getting-started.md#download-the-client-sdk).

## Register a certificate or a secret key from a client

For the digital-signature authentication method, you can register a certificate with Ledger by using the following command. For details about the command, see the [ScalarDL Client Command Reference](./scalardl-command-reference.md#register-cert).

```shell
scalardl register-cert --properties <CLIENT_PROPERTIES_FILE>
```

For the HMAC authentication method, you can register a secret key with Ledger by using the following command. For details about the command, see the [ScalarDL Client Command Reference](./scalardl-command-reference.md#register-secret).

```shell
scalardl register-secret --properties <CLIENT_PROPERTIES_FILE>
```

You can also register certificates and secrets by using [`ClientService`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.11.3/com/scalar/dl/client/service/ClientService.html) in the [ScalarDL Java Client SDK](./how-to-write-applications.md#use-the-scalardl-client-sdk).

## Register contracts and functions from a client

You can register contracts with Ledger by using the following command. For details about the command, see the [ScalarDL Client Command Reference](./scalardl-command-reference.md#register-contract).

```shell
scalardl register-contract --properties <CLIENT_PROPERTIES_FILE> --contract-id <CONTRACT_ID> --contract-binary-name <CONTRACT_BINARY_NAME> --contract-class-file <CONTRACT_CLASS_FILE>
```

You can register functions with Ledger by using the following command. For details about the command, see the [ScalarDL Client Command Reference](./scalardl-command-reference.md#register-function).

```shell
scalardl register-function --properties <CLIENT_PROPERTIES_FILE> --function-id <FUNCTION_ID> --function-binary-name <FUNCTION_BINARY_NAME> --function-class-file <FUNCTION_CLASS_FILE>
```

You can also register contracts and functions with Ledger by using [`ClientService`](https://javadoc.io/static/com.scalar-labs/scalardl-java-client-sdk/3.11.3/com/scalar/dl/client/service/ClientService.html) in the [ScalarDL Java Client SDK](./how-to-write-applications.md#use-the-scalardl-client-sdk).

## Run your application

Now that you have registered contracts and functions from a client, you can now run your application that integrates ScalarDL.
