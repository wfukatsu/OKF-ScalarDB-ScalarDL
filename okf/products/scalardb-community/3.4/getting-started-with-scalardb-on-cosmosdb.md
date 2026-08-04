---
type: Tutorial
title: Getting Started with Scalar DB on Cosmos DB
description: This document briefly explains how you can get started with Scalar DB on Cosmos DB with a simple electronic money application.
resource: https://scalardb-community.scalar-labs.com/docs/3.4/getting-started-with-scalardb-on-cosmosdb/
tags:
- scalardb-community
- v3.4
- phase:implement
- unmaintained
status: deprecated
product: scalardb-community
product_title: ScalarDB Community
version: '3.4'
doc_id: getting-started-with-scalardb-on-cosmosdb
lifecycle_phase: implement
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:51:05Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/versioned_docs/version-3.4/getting-started-with-scalardb-on-cosmosdb.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# Getting Started with Scalar DB on Cosmos DB

## Overview
This document briefly explains how you can get started with Scalar DB on Cosmos DB with a simple electronic money application.

## Install prerequisites

Scalar DB is written in Java. So the following software is required to run it.

* [Oracle JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (OpenJDK 8) or higher
* Other libraries used from the above are automatically installed through gradle

## Cosmos DB setup
You also need to set up a Cosmos DB account to get started with Scalar DB on Cosmos DB.

This section explains how to set up [Azure Cosmos DB](https://docs.microsoft.com/en-us/azure/cosmos-db/introduction) with Azure portal.
1. Select **Azure Cosmos DB** service from the services on Azure portal.
2. Select **Add**
3. On the **Create Azure Cosmos DB Account** page, enter the basic settings for the new **Azure Cosmos DB** account.
* Create new or choose the existing **Resource Group**
* Enter the Cosmos DB **Account Name**
* Choose **API** as `Core (SQL)`
* Choose **Location**
* Select **Review + create**. You can skip the **Network** and **Tags** sections.
* Review the account settings, and then select **Create**.
*  Wait some time for **Azure Cosmos DB** account creation.
 4. Select **Go to resource** to go to the Azure Cosmos DB account page.
 5. Select **Default consistency** from the left navigation on your Azure Cosmos DB account page.
* Change `Consistency Level` from `SESSION` to `STRONG`.
* Select **Save**

From here, we assume Oracle JDK 8 is properly installed in your local environment and the Azure Cosmos DB account is properly configured in Azure.

## Configure Scalar DB

The **scalardb.properties** (getting-started/scalardb.properties) file holds the configuration for Scalar DB. You need to update `contact_points` and `password` with your Cosmos DB account URI and the account's password respectively, and `storage` with `cosmos`.

```
# Comma separated contact points
scalar.db.contact_points=<COSMOS_DB_ACCOUNT_URI>

# Port number for all the contact points. Default port number for each database is used if empty.
#scalar.db.contact_port=

# Credential information to access the database
scalar.db.username=
scalar.db.password=<COSMOS_DB_KEY>

# Storage implementation. Either cassandra or cosmos or dynamo or jdbc can be set. Default storage is cassandra.
scalar.db.storage=cosmos
```
Note that you can use a primary key or a secondary key for `<COSMOS_DB_KEY>`.

Please follow [Getting Started with Scalar DB](./getting-started-with-scalardb.md) to run the application.
