---
type: Development Guide
title: ScalarDB Analytics
description: The current version of ScalarDB Analytics leverages Apache Spark as its execution engine. It provides a unified view of ScalarDB-managed and non-ScalarDB-managed data sources by utilizing a Spark custom catalog. Using ScalarDB Analytics,...
resource: https://scalardb.scalar-labs.com/docs/3.14/scalardb-analytics/README/
tags:
- scalardb
- v3.14
- phase:implement
- section:develop
- edition:enterprise-option
- feature-status:public-preview
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: scalardb-analytics/README
lifecycle_phase: implement
breadcrumb:
- Develop
- Reference
- Analytics
editions:
- Enterprise Option
feature_status:
- Public Preview
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/scalardb-analytics/README.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB Analytics

**ScalarDB Analytics** is the analytical component of ScalarDB. Similar to ScalarDB, it unifies diverse data sources - ranging from RDBMSs like PostgreSQL and MySQL to NoSQL databases such as Cassandra and DynamoDB - into a single logical database. While ScalarDB focuses on operational workloads with strong transactional consistency across multiple databases, ScalarDB Analytics is optimized for analytical workloads. It supports a wide range of queries, including complex joins, aggregations, and window functions. ScalarDB Analytics operates seamlessly on both ScalarDB-managed data sources and non-ScalarDB-managed ones, enabling advanced analytical queries across various datasets.

The current version of ScalarDB Analytics leverages **Apache Spark** as its execution engine. It provides a unified view of ScalarDB-managed and non-ScalarDB-managed data sources by utilizing a Spark custom catalog. Using ScalarDB Analytics, you can treat tables from these data sources as native Spark tables. This allows you to execute arbitrary Spark SQL queries seamlessly. For example, you can join a table stored in Cassandra with a table in PostgreSQL to perform a cross-database analysis with ease.

:::warning

You need to have a license key (trial license or commercial license) to use ScalarDB Analytics with Spark. If you don't have a license key, please [contact us](https://www.scalar-labs.com/contact-us).

:::

## Further reading

* For tutorials on how to use ScalarDB Analytics by using a sample dataset and application, see [Getting Started with ScalarDB Analytics](../scalardb-samples/scalardb-analytics-spark-sample/README.md).
* For supported Spark and Scala versions, see [Version Compatibility of ScalarDB Analytics with Spark](./run-analytical-queries.md#version-compatibility)
