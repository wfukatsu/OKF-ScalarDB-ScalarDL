---
type: Tutorial
title: Getting Started with Scalar DB on DynamoDB
description: This document briefly explains how you can get started with Scalar DB on DynamoDB with a simple electronic money application.
resource: https://scalardb-community.scalar-labs.com/docs/3.4/getting-started-with-scalardb-on-dynamodb/
tags:
- scalardb-community
- v3.4
- phase:implement
- unmaintained
status: deprecated
product: scalardb-community
product_title: ScalarDB Community
version: '3.4'
doc_id: getting-started-with-scalardb-on-dynamodb
lifecycle_phase: implement
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:10Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/versioned_docs/version-3.4/getting-started-with-scalardb-on-dynamodb.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# Getting Started with Scalar DB on DynamoDB

## Overview
This document briefly explains how you can get started with Scalar DB on DynamoDB with a simple electronic money application.

## Install prerequisites

Scalar DB is written in Java. So the following software is required to run it.

* [Oracle JDK 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (OpenJDK 8) or higher
* Other libraries used from the above are automatically installed through gradle

From here, we assume Oracle JDK 8 is properly installed in your local environment.

## Configure Scalar DB

The **scalardb.properties** (getting-started/scalardb.properties) file holds the configuration for Scalar DB. You need to update `contact_points` with AWS region, `username` with your AWS access key id, `password` with your AWS access secret key and `storage` with `dynamo`.
```
# Comma separated contact points
scalar.db.contact_points=<REGION>

# Port number for all the contact points. Default port number for each database is used if empty.
#scalar.db.contact_port=

# Credential information to access the database
scalar.db.username=<AWS_ACCESS_KEY_ID>
scalar.db.password=<AWS_ACCESS_SECRET_KEY>

# Storage implementation. Either cassandra or cosmos or dynamo or jdbc can be set. Default storage is cassandra.
scalar.db.storage=dynamo
```

Please follow [Getting Started with Scalar DB](./getting-started-with-scalardb.md) to run the application.
