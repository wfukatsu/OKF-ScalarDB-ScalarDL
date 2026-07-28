---
type: Development Guide
title: Control User Access in a Fine-Grained Manner
description: ScalarDB Cluster can authorize users in a fine-grained manner with a mechanism called attributed-based access control (ABAC). This page explains how to use ABAC in ScalarDB Cluster.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalardb-cluster/authorize-with-abac/
tags:
- scalardb
- v3.16
- phase:implement
- section:develop
- edition:enterprise-premium-option
- feature-status:private-preview
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: scalardb-cluster/authorize-with-abac
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Advanced Configurations and Operations
editions:
- Enterprise Premium Option
feature_status:
- Private Preview
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/scalardb-cluster/authorize-with-abac.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Control User Access in a Fine-Grained Manner

:::info

- This feature is currently available only to customers in Japan. If you're a customer in Japan, please see the Japanese version of this page.
- If you need more details about this feature in English, please [contact support](https://www.scalar-labs.com/support).

:::

ScalarDB Cluster can authorize users in a fine-grained manner with a mechanism called attributed-based access control (ABAC). This page explains how to use ABAC in ScalarDB Cluster.

## What is ABAC?

ABAC is a fine-grained access control mechanism in ScalarDB Cluster, allowing for record-level access control instead of just table-level access control, done through [simple authorization](./scalardb-auth-with-sql.md). With ABAC, a user can access a particular record only if the user's attributes and the record's attributes match. For example, you can restrict access to some highly confidential records to only users with the required privileges. This mechanism is also useful when multiple applications share the same table but need to access different segments based on their respective privileges.

## Why use ABAC?

Enterprise databases often provide row-level security or similar alternatives to allow for controlling access to rows in a database table. However, if a system comprises several databases, you need to configure each database one by one in the same way. If different kinds of databases are used, you have to configure each database by understanding the differences in the capabilities of each database. Such configuration causes too much burden and is error-prone. With ABAC, you can just configure it once, even though you manage several databases under ScalarDB.

Row-level security features in most databases often require you to implement matching logic through functions like stored procedures. This can sometimes lead to writing lots of code to achieve the desired logic, which can become burdensome. In contrast, ABAC allows you to configure matching logic by using attributes known as tags. With ABAC, you only need to define these tags and assign them to users and records, eliminating the need for coding. Tags consist of several components that enable you to specify matching logic in a flexible and straightforward manner.
