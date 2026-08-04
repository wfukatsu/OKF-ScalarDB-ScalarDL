---
type: Product Version
title: ScalarDB 3.19
description: Documentation set for ScalarDB 3.19 (newest patch 3.19.0).
resource: https://scalardb.scalar-labs.com/docs/latest/
tags:
- scalardb
- v3.19
- product-version
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.0
url_path: latest
maintenance: supported
is_latest: true
concept_count: 206
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:47Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/tree/6126dfe2f56389351d88b134752618641f9771dd
  title: ScalarDB documentation repository
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB 3.19

Supported release.

| | |
|---|---|
| Product | ScalarDB |
| Documentation version | 3.19 |
| Newest patch release described | 3.19.0 |
| Docs site | https://scalardb.scalar-labs.com/docs/latest/ |
| Upstream source | https://github.com/scalar-labs/docs-scalardb @ `6126dfe2f563` |
| Concepts in this version | 206 |

## By lifecycle phase

Start here when you know which phase of the project you are in.

### 設計 / Design (11)

- [Consensus Commit Protocol](./consensus-commit.md)
- [Glossary](./glossary.md)
- [Model Your Data](./data-modeling.md)
- [Requirements](./requirements.md)
- [ScalarDB Design](./design.md)
- [ScalarDB Features](./features.md)
- [ScalarDB Learning Paths](./learning-paths.md)
- [ScalarDB Overview](./overview.md)
- [ScalarDB Roadmap](./roadmap.md)
- [ScalarDB Analytics Design and Implementation](./scalardb-analytics/design.md)
- [ScalarDB Cluster Compatibility Matrix](./scalardb-cluster/compatibility.md)

### 実装 / Implement (90)

- [Add ScalarDB to Your Build](./add-scalardb-to-your-build.md)
- [Configurations for the Underlying Databases of ScalarDB](./database-configurations.md)
- [Database Adapters](./database-adapters.md)
- [Develop Overview](./develop-overview.md)
- [Getting Started with Benchmarking ScalarDB](./getting-started-with-benchmarking-scalardb.md)
- [Getting Started with ScalarDB](./getting-started-with-scalardb.md)
- [Getting Started with ScalarDB by Using Kotlin](./getting-started-with-scalardb-by-using-kotlin.md)
- [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](./schema-loader-import.md)
- [Libraries and Tools for ScalarDB](./libraries-and-tools.md)
- [Migrate Overview](./migrate-overview.md)
- [Multi-Storage Transactions](./multi-storage-transactions.md)
- [Quickstart Overview](./quickstart-overview.md)
- [Run Analytical Queries Overview](./develop-run-analytical-queries-overview.md)
- [Run Non-Transactional Storage Operations Overview](./develop-run-non-transactional-operations-overview.md)
- [Run Non-Transactional Storage Operations Through the Core Library](./run-non-transactional-storage-operations-through-library.md)
- [Run Non-Transactional Storage Operations Through the Primitive CRUD Interface](./run-non-transactional-storage-operations-through-primitive-crud-interface.md)
- [Run Transactions Overview](./develop-run-transactions-overview.md)
- [Run Transactions Through the ScalarDB Core Library](./run-transactions-through-scalardb-core-library.md)
- [ScalarDB Analytics Quickstart Overview](./quickstart-scalardb-analytics-overview.md)
- [ScalarDB Cluster Quickstart Overview](./quickstart-scalardb-cluster-overview.md)
- [ScalarDB Core Configurations](./configurations.md)
- [ScalarDB Core Quickstart Overview](./quickstart-scalardb-core-overview.md)
- [ScalarDB Data Loader](./data-loader.md)
- [ScalarDB Java API Guide](./api-guide.md)
- [ScalarDB Schema Loader](./schema-loader.md)
- [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md)
- [Authenticate and Authorize Users in ScalarDB Analytics](./scalardb-analytics/authentication-and-authorization.md)
- [Create a ScalarDB Analytics Catalog](./scalardb-analytics/create-scalardb-analytics-catalog.md)
- [Data Source Reference](./scalardb-analytics/reference-data-source.md)
- [Getting Started with ScalarDB Analytics](./scalardb-analytics/quickstart.md)
- [Run Analytical Queries Through ScalarDB Analytics](./scalardb-analytics/run-analytical-queries.md)
- [ScalarDB Analytics CLI Command Reference](./scalardb-analytics/reference-cli-command.md)
- [ScalarDB Analytics Configurations](./scalardb-analytics/configurations.md)
- [Authenticate and Authorize Users](./scalardb-cluster/scalardb-auth-with-sql.md)
- [Control User Access in a Fine-Grained Manner](./scalardb-cluster/authorize-with-abac.md)
- [Control User Access via OIDC-Based JWT Access Tokens](./scalardb-cluster/control-access-via-oidc-based-jwt-tokens.md)
- [Developer Guide for ScalarDB Cluster with the Java API](./scalardb-cluster/developer-guide-for-scalardb-cluster-with-java-api.md)
- [Encrypt Data at Rest](./scalardb-cluster/encrypt-data-at-rest.md)
- [Encrypt Wire Communications](./scalardb-cluster/encrypt-wire-communications.md)
- [Getting Started with ScalarDB Cluster](./scalardb-cluster/getting-started-with-scalardb-cluster.md)
- [Getting Started with ScalarDB Cluster for Vector Search](./scalardb-cluster/getting-started-with-vector-search.md)
- [Getting Started with ScalarDB Cluster GraphQL](./scalardb-cluster/getting-started-with-scalardb-cluster-graphql.md)
- [Getting Started with ScalarDB Cluster SQL via .NET](./scalardb-cluster/getting-started-with-scalardb-cluster-sql-dotnet.md)
- [Getting Started with ScalarDB Cluster SQL via .NET and LINQ](./scalardb-cluster/getting-started-with-scalardb-cluster-sql-linq.md)
- [Getting Started with ScalarDB Cluster SQL via JDBC](./scalardb-cluster/getting-started-with-scalardb-cluster-sql-jdbc.md)
- [Getting Started with ScalarDB Cluster SQL via Spring Data JDBC for ScalarDB](./scalardb-cluster/getting-started-with-scalardb-cluster-sql-spring-data-jdbc.md)
- [Getting Started with ScalarDB Cluster via .NET](./scalardb-cluster/getting-started-with-scalardb-cluster-dotnet.md)
- [Getting Started with Using Go for ScalarDB Cluster](./scalardb-cluster/getting-started-with-using-go-for-scalardb-cluster.md)
- [Getting Started with Using Python for ScalarDB Cluster](./scalardb-cluster/getting-started-with-using-python-for-scalardb-cluster.md)
- [How to Deploy ScalarDB Cluster Locally](./scalardb-cluster/setup-scalardb-cluster-on-kubernetes-by-using-helm-chart.md)
- [Replicate Data for High Availability](./scalardb-cluster/remote-replication.md)
- [Run Non-Transactional Storage Operations Through ScalarDB Cluster](./scalardb-cluster/run-non-transactional-storage-operations-through-scalardb-cluster.md)
- [Run Non-Transactional Storage Operations Through the SQL Interface](./scalardb-cluster/run-non-transactional-storage-operations-through-sql-interface.md)
- [Run Transactions Through ScalarDB Cluster](./scalardb-cluster/run-transactions-through-scalardb-cluster.md)
- [Run Transactions Through ScalarDB Cluster SQL](./scalardb-cluster/run-transactions-through-scalardb-cluster-sql.md)
- [ScalarDB Cluster](./scalardb-cluster/section-home.md)
- [ScalarDB Cluster Configurations](./scalardb-cluster/scalardb-cluster-configurations.md)
- [ScalarDB Cluster gRPC API Guide](./scalardb-cluster/scalardb-cluster-grpc-api-guide.md)
- [ScalarDB Cluster SQL gRPC API Guide](./scalardb-cluster/scalardb-cluster-sql-grpc-api-guide.md)
- [ScalarDB Cluster Standalone Mode](./scalardb-cluster/standalone-mode.md)
- [Exception Handling in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/exception-handling.md)
- [Getting Started with ASP.NET Core and Dependency Injection in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-aspnet-and-di.md)
- [Getting Started with Authentication and Authorization by Using ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-auth.md)
- [Getting Started with Distributed SQL Transactions in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-distributed-sql-transactions.md)
- [Getting Started with Distributed Transactions in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-distributed-transactions.md)
- [Getting Started with Distributed Transactions with a Two-Phase Commit Interface in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-two-phase-commit-transactions.md)
- [Getting Started with LINQ in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-linq.md)
- [Getting Started with Tables as C# Classes in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-scalardb-tables-as-csharp-classes.md)
- [Getting Started with the Administrative API in the ScalarDB Cluster .NET Client SDK](./scalardb-cluster-dotnet-client-sdk/getting-started-with-admin-api.md)
- [ScalarDB Cluster .NET Client SDK Overview](./scalardb-cluster-dotnet-client-sdk/section-home.md)
- [ScalarDB Cluster .NET Client SDK Reference](./scalardb-cluster-dotnet-client-sdk/common-reference.md)
- [Getting started with Export](./scalardb-data-loader/getting-started-export.md)
- [Getting started with Import](./scalardb-data-loader/getting-started-import.md)
- [How to run two-phase commit transaction](./scalardb-graphql/how-to-run-two-phase-commit-transaction.md)
- [ScalarDB GraphQL Overview](./scalardb-graphql/section-home.md)
- [Getting Started with ScalarDB MCP Server](./scalardb-mcp-server/getting-started-with-scalardb-mcp-server.md)
- [ScalarDB MCP Server Tools Reference](./scalardb-mcp-server/tools-reference.md)
- [Run Sample Applications Overview](./scalardb-samples/README.md)
- [Create an Application That Supports Microservice Transactions in a Shared ScalarDB Cluster Environment by Using LINQ](./scalardb-samples/dotnet-microservice-transactions-sample-with-shared-cluster-with-linq/README.md)
- [Create a Sample Application That Supports Microservice Transactions](./scalardb-samples/microservice-transaction-sample/README.md)
- [Create an Application That Supports Microservice Transactions in a Shared ScalarDB Cluster Environment by Using ScalarDB JDBC](./scalardb-samples/microservice-transactions-sample-with-shared-cluster-with-jdbc/README.md)
- [Create a Sample Application That Supports Multi-Storage Transactions](./scalardb-samples/multi-storage-transaction-sample/README.md)
- [Sample application of Spring Data JDBC for ScalarDB with Microservice Transactions](./scalardb-samples/spring-data-microservice-transaction-sample/README.md)
- [Sample application of Spring Data JDBC for ScalarDB with Multi-storage Transactions](./scalardb-samples/spring-data-multi-storage-transaction-sample/README.md)
- [Guide of Spring Data JDBC for ScalarDB](./scalardb-sql/spring-data-guide.md)
- [How to Migrate Your Applications and Databases into a ScalarDB-Based Environment](./scalardb-sql/migration-guide.md)
- [ScalarDB JDBC Guide](./scalardb-sql/jdbc-guide.md)
- [ScalarDB SQL API Guide](./scalardb-sql/sql-api-guide.md)
- [ScalarDB SQL Grammar](./scalardb-sql/grammar.md)
- [ScalarDB SQL Overview](./scalardb-sql/section-home.md)

### 運用 / Operate (105)

- [Back Up and Restore Databases Overview](./manage-backup-and-restore.md)
- [Deploy Overview](./deploy-overview.md)
- [How to Back Up and Restore Databases Used Through ScalarDB](./backup-restore.md)
- [Manage Overview](./manage-overview.md)
- [Monitor Overview](./manage-monitor-overview.md)
- [ScalarDB Core Error Codes](./scalardb-core-status-codes.md)
- [ScalarDB Data Loader Error Codes](./scalardb-data-loader-status-codes.md)
- [ScalarDB Schema Loader Error Codes](./scalardb-schema-loader-status-codes.md)
- [[Deprecated] Configure a custom values file for ScalarDB GraphQL](./helm-charts/configure-custom-values-scalardb-graphql.md)
- [[Deprecated] Configure a custom values file for ScalarDB Server](./helm-charts/configure-custom-values-scalardb.md)
- [[Deprecated] Getting Started with Helm Charts (ScalarDB Server)](./helm-charts/getting-started-scalardb.md)
- [[Deprecated] How to deploy ScalarDB GraphQL](./helm-charts/how-to-deploy-scalardb-graphql.md)
- [[Deprecated] How to deploy ScalarDB Server](./helm-charts/how-to-deploy-scalardb.md)
- [Configure a custom values file for Scalar Admin for Kubernetes](./helm-charts/configure-custom-values-scalar-admin-for-kubernetes.md)
- [Configure a custom values file for Scalar Envoy](./helm-charts/configure-custom-values-envoy.md)
- [Configure a custom values file for Scalar Helm Charts](./helm-charts/configure-custom-values-file.md)
- [Configure a Custom Values File for Scalar Manager](./helm-charts/configure-custom-values-scalar-manager.md)
- [Configure a custom values file for ScalarDB Analytics server](./helm-charts/configure-custom-values-scalardb-analytics-server.md)
- [Configure a custom values file for ScalarDB Cluster](./helm-charts/configure-custom-values-scalardb-cluster.md)
- [Configure a custom values file for ScalarDL Auditor](./helm-charts/configure-custom-values-scalardl-auditor.md)
- [Configure a custom values file for ScalarDL Ledger](./helm-charts/configure-custom-values-scalardl-ledger.md)
- [Configure a custom values file for ScalarDL Schema Loader](./helm-charts/configure-custom-values-scalardl-schema-loader.md)
- [Deploy Scalar Manager](./helm-charts/getting-started-scalar-manager.md)
- [Deploy Scalar products using Scalar Helm Charts](./helm-charts/how-to-deploy-scalar-products.md)
- [Getting Started with Helm Charts (Logging using Loki Stack)](./helm-charts/getting-started-logging.md)
- [Getting Started with Helm Charts (Monitoring using Prometheus Operator)](./helm-charts/getting-started-monitoring.md)
- [Getting Started with Helm Charts (ScalarDB Cluster with TLS by Using cert-manager)](./helm-charts/getting-started-scalardb-cluster-tls-cert-manager.md)
- [Getting Started with Helm Charts (ScalarDB Cluster with TLS)](./helm-charts/getting-started-scalardb-cluster-tls.md)
- [Getting Started with Helm Charts (ScalarDL Ledger / Ledger only)](./helm-charts/getting-started-scalardl-ledger.md)
- [Getting Started with Helm Charts (ScalarDL Ledger and Auditor / Auditor mode)](./helm-charts/getting-started-scalardl-auditor.md)
- [Getting Started with Helm Charts (ScalarDL Ledger and Auditor with TLS / Auditor Mode)](./helm-charts/getting-started-scalardl-auditor-tls.md)
- [Getting Started with Helm Charts (ScalarDL Ledger and Auditor with TLS by Using cert-manager / Auditor Mode)](./helm-charts/getting-started-scalardl-auditor-tls-cert-manager.md)
- [Getting Started with Scalar Helm Charts](./helm-charts/getting-started-scalar-helm-charts.md)
- [How to deploy Scalar Admin for Kubernetes](./helm-charts/how-to-deploy-scalar-admin-for-kubernetes.md)
- [How to deploy ScalarDB Cluster](./helm-charts/how-to-deploy-scalardb-cluster.md)
- [How to deploy ScalarDL Auditor](./helm-charts/how-to-deploy-scalardl-auditor.md)
- [How to deploy ScalarDL Ledger](./helm-charts/how-to-deploy-scalardl-ledger.md)
- [How to use Secret resources to pass credentials as environment variables into the properties file](./helm-charts/use-secret-for-credentials.md)
- [Mount any files or volumes on Scalar product pods](./helm-charts/mount-files-or-volumes-on-scalar-pods.md)
- [Release Support Policy](./releases/release-support-policy.md)
- [ScalarDB 3.19 Release Notes](./releases/release-notes.md)
- [(Deprecated) Guidelines for creating an EKS cluster for ScalarDB Server](./scalar-kubernetes/CreateEKSClusterForScalarDB.md)
- [[Deprecated] Deploy ScalarDB Server on Azure Kubernetes Service (AKS)](./scalar-kubernetes/ManualDeploymentGuideScalarDBServerOnAKS.md)
- [Back up a NoSQL database in a Kubernetes environment](./scalar-kubernetes/BackupNoSQL.md)
- [Back up an RDB in a Kubernetes environment](./scalar-kubernetes/BackupRDB.md)
- [Back up and restore ScalarDB or ScalarDL data in a Kubernetes environment](./scalar-kubernetes/BackupRestoreGuide.md)
- [Collecting logs from Scalar products on a Kubernetes cluster](./scalar-kubernetes/K8sLogCollectionGuide.md)
- [Components to Regularly Check When Running in a Kubernetes Environment](./scalar-kubernetes/RegularCheck.md)
- [Configure Network Peering for ScalarDL Auditor Mode](./scalar-kubernetes/NetworkPeeringForScalarDLAuditor.md)
- [Create a bastion server](./scalar-kubernetes/CreateBastionServer.md)
- [Deploy ScalarDB Cluster on Amazon Elastic Kubernetes Service (EKS)](./scalar-kubernetes/ManualDeploymentGuideScalarDBClusterOnEKS.md)
- [Deploy ScalarDB Server on Amazon Elastic Kubernetes Service (EKS)](./scalar-kubernetes/ManualDeploymentGuideScalarDBServerOnEKS.md)
- [Deploy ScalarDL Ledger and ScalarDL Auditor on Amazon Elastic Kubernetes Service (EKS)](./scalar-kubernetes/ManualDeploymentGuideScalarDLAuditorOnEKS.md)
- [Deploy ScalarDL Ledger and ScalarDL Auditor on Azure Kubernetes Service (AKS)](./scalar-kubernetes/ManualDeploymentGuideScalarDLAuditorOnAKS.md)
- [Deploy ScalarDL Ledger on Amazon Elastic Kubernetes Service (EKS)](./scalar-kubernetes/ManualDeploymentGuideScalarDLOnEKS.md)
- [Deploy ScalarDL Ledger on Azure Kubernetes Service (AKS)](./scalar-kubernetes/ManualDeploymentGuideScalarDLOnAKS.md)
- [Guidelines for creating an AKS cluster for Scalar products](./scalar-kubernetes/CreateAKSClusterForScalarProducts.md)
- [Guidelines for creating an AKS cluster for ScalarDB Server](./scalar-kubernetes/CreateAKSClusterForScalarDB.md)
- [Guidelines for creating an AKS cluster for ScalarDL Ledger](./scalar-kubernetes/CreateAKSClusterForScalarDL.md)
- [Guidelines for creating an AKS cluster for ScalarDL Ledger and ScalarDL Auditor](./scalar-kubernetes/CreateAKSClusterForScalarDLAuditor.md)
- [Guidelines for creating an Amazon EKS cluster for Scalar products](./scalar-kubernetes/CreateEKSClusterForScalarProducts.md)
- [Guidelines for creating an EKS cluster for ScalarDB Cluster](./scalar-kubernetes/CreateEKSClusterForScalarDBCluster.md)
- [Guidelines for creating an EKS cluster for ScalarDL Ledger](./scalar-kubernetes/CreateEKSClusterForScalarDL.md)
- [Guidelines for creating an EKS cluster for ScalarDL Ledger and ScalarDL Auditor](./scalar-kubernetes/CreateEKSClusterForScalarDLAuditor.md)
- [How to Create Private Key and Certificate Files for TLS Connections in Scalar Products](./scalar-kubernetes/HowToCreateKeyAndCertificateFiles.md)
- [How to get the container images of Scalar products](./scalar-kubernetes/HowToGetContainerImages.md)
- [How to install Scalar products through AWS Marketplace](./scalar-kubernetes/AwsMarketplaceGuide.md)
- [How to Scale ScalarDB Cluster](./scalar-kubernetes/HowToScaleScalarDB.md)
- [How to Scale ScalarDL](./scalar-kubernetes/HowToScaleScalarDL.md)
- [How to Upgrade ScalarDB](./scalar-kubernetes/HowToUpgradeScalarDB.md)
- [How to Upgrade ScalarDL](./scalar-kubernetes/HowToUpgradeScalarDL.md)
- [How to use the container images](./scalar-kubernetes/HowToUseContainerImages.md)
- [Make ScalarDB or ScalarDL deployed in a Kubernetes cluster environment available from applications](./scalar-kubernetes/AccessScalarProducts.md)
- [Monitoring Scalar products on a Kubernetes cluster](./scalar-kubernetes/K8sMonitorGuide.md)
- [Production checklist for Scalar products](./scalar-kubernetes/ProductionChecklistForScalarProducts.md)
- [Production checklist for ScalarDB Cluster](./scalar-kubernetes/ProductionChecklistForScalarDBCluster.md)
- [Production checklist for ScalarDL Auditor](./scalar-kubernetes/ProductionChecklistForScalarDLAuditor.md)
- [Production checklist for ScalarDL Ledger](./scalar-kubernetes/ProductionChecklistForScalarDLLedger.md)
- [Restore databases in a Kubernetes environment](./scalar-kubernetes/RestoreDatabase.md)
- [Set up a database for ScalarDB/ScalarDL deployment](./scalar-kubernetes/SetupDatabase.md)
- [Set up a database for ScalarDB/ScalarDL deployment on AWS](./scalar-kubernetes/SetupDatabaseForAWS.md)
- [Set up a database for ScalarDB/ScalarDL deployment on Azure](./scalar-kubernetes/SetupDatabaseForAzure.md)
- [Envoy Alerts](./scalar-kubernetes/alerts/Envoy.md)
- [Ledger Alerts](./scalar-kubernetes/alerts/Ledger.md)
- [Scalar Alerts](./scalar-kubernetes/alerts/README.md)
- [How to Configure a Commercial License Key](./scalar-licensing/commercial.md)
- [How to Configure a Trial License Key](./scalar-licensing/trial.md)
- [License Key Configuration Overview](./scalar-licensing/section-home.md)
- [How to Use Scalar Manager](./scalar-manager/how-to-use-scalar-manager.md)
- [Scalar Manager Metrics Reference](./scalar-manager/metrics-reference.md)
- [Scalar Manager Overview](./scalar-manager/overview.md)
- [Deploy a ScalarDB Analytics server](./scalardb-analytics/deploy-scalardb-analytics-server.md)
- [Deploy ScalarDB Analytics in Public Cloud Environments](./scalardb-analytics/deployment.md)
- [Deploy ScalarDB Analytics Locally](./scalardb-analytics/deployment-local.md)
- [ScalarDB Benchmarking Tools](./scalardb-benchmarks/README.md)
- [Attribute-Based Access Control Error Codes](./scalardb-cluster/scalardb-abac-status-codes.md)
- [Authentication and Authorization Error Codes](./scalardb-cluster/scalardb-auth-status-codes.md)
- [Deploy ScalarDB Cluster Through Google Cloud Marketplace](./scalardb-cluster/deploy-scalardb-cluster-google-cloud-marketplace.md)
- [Embedding Store Error Codes](./scalardb-cluster/scalardb-embedding-store-status-codes.md)
- [Encryption Error Codes](./scalardb-cluster/scalardb-encryption-status-codes.md)
- [Remote Replication Error Codes](./scalardb-cluster/scalardb-remote-replication-status-codes.md)
- [ScalarDB Cluster Deployment Patterns for Microservices](./scalardb-cluster/deployment-patterns-for-microservices.md)
- [ScalarDB Cluster Error Codes](./scalardb-cluster/scalardb-cluster-status-codes.md)
- [ScalarDB GraphQL Error Codes](./scalardb-graphql/scalardb-graphql-status-codes.md)
- [ScalarDB SQL Error Codes](./scalardb-sql/scalardb-sql-status-codes.md)

## Sections

- [helm-charts](./helm-charts/index.md)
- [releases](./releases/index.md)
- [scalar-kubernetes](./scalar-kubernetes/index.md)
- [scalar-licensing](./scalar-licensing/index.md)
- [scalar-manager](./scalar-manager/index.md)
- [scalardb-analytics](./scalardb-analytics/index.md)
- [scalardb-benchmarks](./scalardb-benchmarks/index.md)
- [scalardb-cluster](./scalardb-cluster/index.md)
- [scalardb-cluster-dotnet-client-sdk](./scalardb-cluster-dotnet-client-sdk/index.md)
- [scalardb-data-loader](./scalardb-data-loader/index.md)
- [scalardb-graphql](./scalardb-graphql/index.md)
- [scalardb-mcp-server](./scalardb-mcp-server/index.md)
- [scalardb-samples](./scalardb-samples/index.md)
- [scalardb-sql](./scalardb-sql/index.md)

## Top-level concepts

- [Add ScalarDB to Your Build](./add-scalardb-to-your-build.md) — The ScalarDB library is available on the Maven Central Repository. You can add the library as a build dependency to your application by using Gradle or Maven.
- [Back Up and Restore Databases Overview](./manage-backup-and-restore.md) — In this category, you can learn how to back up and restore databases that are used by ScalarDB.
- [Configurations for the Underlying Databases of ScalarDB](./database-configurations.md) — This document explains how to configure the underlying databases of ScalarDB to make applications that use ScalarDB work correctly and efficiently.
- [Consensus Commit Protocol](./consensus-commit.md) — Consensus Commit is the transaction protocol used in ScalarDB and is designed for executing transactions spanning multiple diverse databases. Its uniqueness is that the protocol achieves ACID transactions without relying on the transaction...
- [Database Adapters](./database-adapters.md) — ScalarDB provides a database-agnostic abstraction layer that enables applications to perform ACID transactions across different databases without being tied to any specific database product. To achieve this, ScalarDB uses database adapters...
- [Deploy Overview](./deploy-overview.md) — In this category, you can follow guides to help you become more familiar with deploying ScalarDB, specifically ScalarDB Cluster and ScalarDB Analytics, in local and cloud-based Kubernetes environments.
- [Develop Overview](./develop-overview.md) — In this category, you can follow guides to help you become more familiar with ScalarDB, specifically with how to run transactions, analytical queries, and non-transactional storage operations.
- [Getting Started with Benchmarking ScalarDB](./getting-started-with-benchmarking-scalardb.md) — This guide walks you through planning, running, and analyzing benchmarks for ScalarDB. A structured benchmarking methodology produces reliable, meaningful performance measurements that you can use to make informed decisions about system...
- [Getting Started with ScalarDB](./getting-started-with-scalardb.md) — This getting started tutorial explains how to configure your preferred database in ScalarDB and illustrates the process of creating a sample e-commerce application, where items can be ordered and paid for with a credit card by using...
- [Getting Started with ScalarDB by Using Kotlin](./getting-started-with-scalardb-by-using-kotlin.md) — This getting started tutorial explains how to configure your preferred database in ScalarDB and set up a basic electronic money application by using Kotlin. Since Kotlin has Java interoperability, you can use ScalarDB directly from Kotlin.
- [Glossary](./glossary.md) — This glossary includes database and distributed-system terms that are often used when using ScalarDB.
- [How to Back Up and Restore Databases Used Through ScalarDB](./backup-restore.md) — Since ScalarDB provides transaction capabilities on top of non-transactional or transactional databases non-invasively, you need to take special care to back up and restore the databases in a transactionally consistent way.
- [Importing Existing Tables to ScalarDB by Using ScalarDB Schema Loader](./schema-loader-import.md) — You might want to use ScalarDB (e.g., for database-spanning transactions) with your existing databases. In that case, you can import those databases under the ScalarDB control using ScalarDB Schema Loader. ScalarDB Schema Loader...
- [Libraries and Tools for ScalarDB](./libraries-and-tools.md) — ScalarDB provides various libraries and tools to help you build and operate scalable and reliable applications. Below are some key libraries and tools available.
- [Manage Overview](./manage-overview.md) — In this category, you can follow guides to help you manage ScalarDB.
- [Migrate Overview](./migrate-overview.md) — For details on importing your tables or migrating your applications and databases to a ScalarDB-based environment, see the following guides.
- [Model Your Data](./data-modeling.md) — Data modeling (or in other words, designing your database schemas) is the process of conceptualizing and visualizing how data will be stored and used by identifying the patterns used to access data and the types of queries to be performed...
- [Monitor Overview](./manage-monitor-overview.md) — Scalar Manager is a centralized management and monitoring solution for ScalarDB within Kubernetes cluster environments that allows you to:
- [Multi-Storage Transactions](./multi-storage-transactions.md) — ScalarDB transactions can span multiple storages or databases while maintaining ACID compliance by using a feature called multi-storage transactions.
- [Quickstart Overview](./quickstart-overview.md) — In this category, you can follow quickstart tutorials for how to get started with running transactions and queries through ScalarDB.
- [Requirements](./requirements.md) — This page outlines the requirements for using each ScalarDB component, including the programming languages and their versions, supported databases and their versions, and the necessary configurations.
- [Run Analytical Queries Overview](./develop-run-analytical-queries-overview.md) — In this category, you can learn how to set up and configure ScalarDB Analytics, an analytics component of ScalarDB. After setting it up, you can run analytical queries over ScalarDB-managed databases, which are updated through ScalarDB...
- [Run Non-Transactional Storage Operations Overview](./develop-run-non-transactional-operations-overview.md) — ScalarDB was initially designed to provide a unified abstraction between diverse databases and transactions across such databases. However, there are cases where you only need the unified abstraction to simplify your applications that use...
- [Run Non-Transactional Storage Operations Through the Core Library](./run-non-transactional-storage-operations-through-library.md) — This guide explains how to run non-transactional storage operations through the ScalarDB Core library.
- [Run Non-Transactional Storage Operations Through the Primitive CRUD Interface](./run-non-transactional-storage-operations-through-primitive-crud-interface.md) — This page explains how to run non-transactional storage operations through the primitive CRUD interface, also known as the Storage API. This guide assumes that you have an advanced understanding of ScalarDB.
- [Run Transactions Overview](./develop-run-transactions-overview.md) — In this category, you can learn how to model your data based on the ScalarDB data model and create schemas. Then, you can learn how to run transactions through the ScalarDB Core library and ScalarDB Cluster, a gRPC server that wraps the...
- [Run Transactions Through the ScalarDB Core Library](./run-transactions-through-scalardb-core-library.md) — This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using the ScalarDB Core library.
- [ScalarDB Analytics Quickstart Overview](./quickstart-scalardb-analytics-overview.md) — In this category, you can see tutorials on how to run analytical queries over the databases that you write through ScalarDB by using a component called ScalarDB Analytics.
- [ScalarDB Cluster Quickstart Overview](./quickstart-scalardb-cluster-overview.md) — In this category, you can see tutorials on how to run ACID transactions through ScalarDB Cluster, which is a gRPC server that wraps the ScalarDB Core library.
- [ScalarDB Core Configurations](./configurations.md) — This page describes the available configurations for ScalarDB Core.
- [ScalarDB Core Error Codes](./scalardb-core-status-codes.md) — This page provides a list of error codes in ScalarDB Core.
- [ScalarDB Core Quickstart Overview](./quickstart-scalardb-core-overview.md) — In this category, you can follow tutorials on how to run ACID transactions through the ScalarDB Core library, which is publicly available under the Apache 2 license.
- [ScalarDB Data Loader](./data-loader.md) — ScalarDB Data Loader is a utility tool enabling you to import and export data with ScalarDB Core easily. If you're using ScalarDB Cluster, you can use ScalarDB Cluster Data Loader, which is a version of Data Loader that you can use to...
- [ScalarDB Data Loader Error Codes](./scalardb-data-loader-status-codes.md) — This page provides a list of error codes in ScalarDB Data Loader.
- [ScalarDB Design](./design.md) — This document briefly explains the design and implementation of ScalarDB. For what ScalarDB is and its use cases, see ScalarDB Overview.
- [ScalarDB Features](./features.md) — This document briefly explains which features are available in which editions of ScalarDB.
- [ScalarDB Java API Guide](./api-guide.md) — The ScalarDB Java API is mainly composed of the Administrative API and Transactional API. This guide briefly explains what kinds of APIs exist, how to use them, and related topics like how to handle exceptions.
- [ScalarDB Learning Paths](./learning-paths.md) — This guide provides learning paths for different roles. Depending on your role, follow the appropriate sequence of documents to gain a comprehensive understanding of ScalarDB.
- [ScalarDB Overview](./overview.md) — This page describes what ScalarDB is and its primary use cases.
- [ScalarDB Roadmap](./roadmap.md) — This roadmap provides a look into the proposed future of ScalarDB. The purpose of this roadmap is to provide visibility into what changes may be coming so that you can more closely follow progress, learn about key milestones, and give...
- [ScalarDB Schema Loader](./schema-loader.md) — ScalarDB has its own data model and schema that maps to the implementation-specific data model and schema. In addition, ScalarDB stores internal metadata, such as transaction IDs, record versions, and transaction statuses, to manage...
- [ScalarDB Schema Loader Error Codes](./scalardb-schema-loader-status-codes.md) — This page provides a list of error codes in ScalarDB Schema Loader.
- [Transactions with a Two-Phase Commit Interface](./two-phase-commit-transactions.md) — ScalarDB supports executing transactions with a two-phase commit interface. With the two-phase commit interface, you can execute a transaction that spans multiple processes or applications, like in a microservice architecture.
