---
type: Documentation Section
title: ScalarDB 3.18 — Scalardb Cluster
description: Directory listing for the `scalardb-cluster` section of the ScalarDB 3.18 documentation.
resource: https://scalardb.scalar-labs.com/docs/3.18/scalardb-cluster/
tags:
- scalardb
- v3.18
- index
status: stable
product: scalardb
version: '3.18'
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:49Z'
---

# Scalardb Cluster

ScalarDB 3.18 documentation under `scalardb-cluster/`.

Section overview: [ScalarDB Cluster](./section-home.md)

## Concepts

- [Attribute-Based Access Control Error Codes](./scalardb-abac-status-codes.md) — This page provides a list of error codes related to attribute-based access control.
- [Authenticate and Authorize Users](./scalardb-auth-with-sql.md) — ScalarDB Cluster can authenticate and authorize users in a coarse-grained manner. You can create users and grant or revoke their privileges. Roles can also be created to group privileges and can be granted to users or other roles. This...
- [Authentication and Authorization Error Codes](./scalardb-auth-status-codes.md) — This page provides a list of error codes related to authentication and authorization.
- [Control User Access in a Fine-Grained Manner](./authorize-with-abac.md) — ScalarDB Cluster can authorize users in a fine-grained manner with a mechanism called attributed-based access control (ABAC). This page explains how to use ABAC in ScalarDB Cluster.
- [Control User Access via OIDC-Based JWT Access Tokens](./control-access-via-oidc-based-jwt-tokens.md) — ScalarDB Cluster can control user access based on JWT access tokens issued by an OpenID Connect (OIDC) provider (for example, Keycloak), as an alternative to password-based authentication, allowing client applications to authenticate...
- [Deploy ScalarDB Cluster Through Google Cloud Marketplace](./deploy-scalardb-cluster-google-cloud-marketplace.md) — This document explains how to deploy ScalarDB Cluster in your Google Cloud environment through Google Cloud Marketplace.
- [Developer Guide for ScalarDB Cluster with the Java API](./developer-guide-for-scalardb-cluster-with-java-api.md) — ScalarDB Cluster provides a Java API for developing applications. This document explains how to use the Java API.
- [Embedding Store Error Codes](./scalardb-embedding-store-status-codes.md) — This page provides a list of error codes related to embedding stores.
- [Encrypt Data at Rest](./encrypt-data-at-rest.md) — This document explains how to encrypt data at rest in ScalarDB.
- [Encrypt Wire Communications](./encrypt-wire-communications.md) — ScalarDB can encrypt wire communications by using Transport Layer Security (TLS). This document explains the configurations for wire encryption in ScalarDB.
- [Encryption Error Codes](./scalardb-encryption-status-codes.md) — This page provides a list of error codes related to encryption.
- [Getting Started with ScalarDB Cluster](./getting-started-with-scalardb-cluster.md) — This tutorial describes how to create a sample application that uses ScalarDB Cluster through the Java API.
- [Getting Started with ScalarDB Cluster for Vector Search](./getting-started-with-vector-search.md) — ScalarDB Cluster provides a vector store abstraction to help applications interact with vector stores (embedding stores) in a unified way. This getting-started tutorial explains how to run vector search in ScalarDB Cluster.
- [Getting Started with ScalarDB Cluster GraphQL](./getting-started-with-scalardb-cluster-graphql.md) — This tutorial describes how to use ScalarDB Cluster GraphQL.
- [Getting Started with ScalarDB Cluster SQL via .NET](./getting-started-with-scalardb-cluster-sql-dotnet.md) — This tutorial describes how to create a sample application that uses ScalarDB Cluster SQL through the .NET API.
- [Getting Started with ScalarDB Cluster SQL via .NET and LINQ](./getting-started-with-scalardb-cluster-sql-linq.md) — This tutorial describes how to create a sample application that uses ScalarDB Cluster SQL through LINQ.
- [Getting Started with ScalarDB Cluster SQL via JDBC](./getting-started-with-scalardb-cluster-sql-jdbc.md) — This tutorial describes how to create a sample application by using ScalarDB Cluster SQL via JDBC.
- [Getting Started with ScalarDB Cluster SQL via Spring Data JDBC for ScalarDB](./getting-started-with-scalardb-cluster-sql-spring-data-jdbc.md) — This tutorial describes how to create a sample application by using ScalarDB Cluster SQL via Spring Data JDBC for ScalarDB.
- [Getting Started with ScalarDB Cluster via .NET](./getting-started-with-scalardb-cluster-dotnet.md) — This tutorial describes how to create a sample application that uses ScalarDB Cluster through the .NET API.
- [Getting Started with Using Go for ScalarDB Cluster](./getting-started-with-using-go-for-scalardb-cluster.md) — This document explains how to write gRPC client code for ScalarDB Cluster by using Go.
- [Getting Started with Using Python for ScalarDB Cluster](./getting-started-with-using-python-for-scalardb-cluster.md) — This document explains how to write gRPC client code for ScalarDB Cluster by using Python.
- [How to Deploy ScalarDB Cluster Locally](./setup-scalardb-cluster-on-kubernetes-by-using-helm-chart.md) — This guide provides instructions on how to deploy ScalarDB Cluster by using a Helm Chart on a local Kubernetes cluster, specifically designed for a test environment.
- [Remote Replication Error Codes](./scalardb-remote-replication-status-codes.md) — This page provides a list of error codes related to remote replication.
- [Replicate Data for High Availability](./remote-replication.md) — ScalarDB Cluster can replicate its managed data to remote sites for high availability and workload distribution. The remote replication feature provides near-real-time replication of write operations from a primary site to one or more...
- [Run Non-Transactional Storage Operations Through ScalarDB Cluster](./run-non-transactional-storage-operations-through-scalardb-cluster.md) — This guide explains how to run non-transactional storage operations through ScalarDB Cluster.
- [Run Non-Transactional Storage Operations Through the SQL Interface](./run-non-transactional-storage-operations-through-sql-interface.md) — This guide explains how to run non-transactional storage operations through the SQL interface for ScalarDB Cluster.
- [Run Transactions Through ScalarDB Cluster](./run-transactions-through-scalardb-cluster.md) — This guide explains how to configure your ScalarDB properties file and create schemas to run transactions through a one-phase or a two-phase commit interface by using ScalarDB Cluster.
- [Run Transactions Through ScalarDB Cluster SQL](./run-transactions-through-scalardb-cluster-sql.md) — This guide explains how to configure your ScalarDB properties file and creating schemas to run transactions through a one-phase or a two-phase commit interface by using ScalarDB Cluster SQL.
- [ScalarDB Cluster Compatibility Matrix](./compatibility.md) — This document shows the compatibility of ScalarDB Cluster versions among client SDK versions.
- [ScalarDB Cluster Configurations](./scalardb-cluster-configurations.md) — This document describes the configurations for ScalarDB Cluster. ScalarDB Cluster consists of multiple cluster nodes, each of which needs to be configured. The configurations need to be specified in the properties file.
- [ScalarDB Cluster Deployment Patterns for Microservices](./deployment-patterns-for-microservices.md) — When building microservice applications that use ScalarDB Cluster, there are two patterns you can choose for how to deploy ScalarDB Cluster: shared-cluster pattern and separated-cluster pattern. This document first explains those patterns,...
- [ScalarDB Cluster Error Codes](./scalardb-cluster-status-codes.md) — This page provides a list of error codes in ScalarDB Cluster.
- [ScalarDB Cluster gRPC API Guide](./scalardb-cluster-grpc-api-guide.md) — This document describes the ScalarDB Cluster gRPC API.
- [ScalarDB Cluster SQL gRPC API Guide](./scalardb-cluster-sql-grpc-api-guide.md) — This document describes the ScalarDB Cluster SQL gRPC API.
- [ScalarDB Cluster Standalone Mode](./standalone-mode.md) — Instead of setting up a Kubernetes cluster and deploying ScalarDB Cluster on top of it by using a Helm Chart, you can run ScalarDB Cluster in standalone mode, which simplifies development and testing processes. A primary use case for this...
