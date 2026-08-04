---
type: Documentation Page
title: Add ScalarDB to Your Build
description: The ScalarDB library is available on the Maven Central Repository. You can add the library as a build dependency to your application by using Gradle or Maven.
resource: https://scalardb.scalar-labs.com/docs/latest/add-scalardb-to-your-build/
tags:
- scalardb
- v3.19
- phase:implement
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.0
doc_id: add-scalardb-to-your-build
lifecycle_phase: implement
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:47Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/docs/add-scalardb-to-your-build.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Add ScalarDB to Your Build

The ScalarDB library is available on the [Maven Central Repository](https://mvnrepository.com/artifact/com.scalar-labs/scalardb). You can add the library as a build dependency to your application by using Gradle or Maven.

## Configure your application based on your build tool

Select your build tool, and follow the instructions to add the build dependency for ScalarDB to your application.

**Gradle**

To add the build dependency for ScalarDB by using Gradle, add the following to `build.gradle` in your application, replacing `<VERSION>` with the version of ScalarDB that you want to use:

```gradle
dependencies {
  implementation 'com.scalar-labs:scalardb:<VERSION>'
}
```

**Maven**

To add the build dependency for ScalarDB by using Maven, add the following to `pom.xml` in your application, replacing `<VERSION>` with the version of ScalarDB that you want to use:

```xml
<dependency>
  <groupId>com.scalar-labs</groupId>
  <artifactId>scalardb</artifactId>
  <version><VERSION></version>
</dependency>
```
