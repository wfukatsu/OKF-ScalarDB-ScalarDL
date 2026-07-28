---
type: Development Guide
title: Add ScalarDB to your build
description: The library is available on maven central repository. You can install it in your application using your build tool such as Gradle and Maven.
resource: https://scalardb-community.scalar-labs.com/docs/3.4/add-scalardb-to-your-build/
tags:
- scalardb-community
- v3.4
- phase:implement
- section:develop
- unmaintained
status: deprecated
product: scalardb-community
product_title: ScalarDB Community
version: '3.4'
doc_id: add-scalardb-to-your-build
lifecycle_phase: implement
breadcrumb:
- Develop
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:10Z'
sources:
- id: docs-scalardb-community
  resource: https://github.com/scalar-labs/docs-scalardb-community/blob/71d199cb0df1c638bd7e305b64fa09fc7236e5c4/versioned_docs/version-3.4/add-scalardb-to-your-build.mdx
  title: ScalarDB Community documentation source (MDX)
  author: process:scalar-labs/docs-scalardb-community
  last_modified: '2025-04-07T11:32:02Z'
---

# Add ScalarDB to your build

The library is available on [maven central repository](https://mvnrepository.com/artifact/com.scalar-labs/scalardb).
You can install it in your application using your build tool such as Gradle and Maven.

To add a dependency on ScalarDB using Gradle, use the following:
```gradle
dependencies {
    implementation 'com.scalar-labs:scalardb:3.4.9'
}
```

To add a dependency using Maven:
```xml
<dependency>
  <groupId>com.scalar-labs</groupId>
  <artifactId>scalardb</artifactId>
  <version>3.4.9</version>
</dependency>
```
