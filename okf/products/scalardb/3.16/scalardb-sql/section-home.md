---
type: Development Guide
title: ScalarDB SQL Overview
description: ScalarDB SQL is an interface layer that allows client applications to communicate with ScalarDB Cluster by using SQL.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalardb-sql/
tags:
- scalardb
- v3.16
- phase:implement
- section:develop
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.6
doc_id: scalardb-sql/index
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Reference
- Java Interface Guides
- SQL Interface Guides
editions:
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:54Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.16/scalardb-sql/index.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB SQL Overview

ScalarDB SQL is an interface layer that allows client applications to communicate with ScalarDB Cluster by using SQL.

:::note

ScalarDB SQL is not fully compatible with standard SQL, but it offers a large subset of the SQL language.

:::

## Types of SQL interfaces

ScalarDB SQL has three types of SQL interfaces.

### JDBC

The JDBC interface lets you connect to ScalarDB Cluster by using the standard JDBC API. This is useful for applications that already use JDBC.

For details on how to set up and use the JDBC interface, see the [ScalarDB JDBC Guide](./jdbc-guide.md).

### SQL API

The SQL API lets you connect to ScalarDB Cluster by using the proprietary and modern Java SQL API. This is useful for applications that do not need to rely on the JDBC interface.

For details on how to set up and use the SQL API, see the [ScalarDB SQL API Guide](./sql-api-guide.md).

### Spring Data JDBC

The Spring Data JDBC interface lets you interact with ScalarDB Cluster via Spring Data JDBC repositories and entities. This is useful for applications that already use Spring Data or when you want to integrate ScalarDB Cluster into Spring applications.

For details on how to set up and use the Sprign Data JDBC interface, see the [Guide of Spring Data JDBC for ScalarDB](./spring-data-guide.md).
