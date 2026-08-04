---
type: Troubleshooting
title: Embedding Store Error Codes
description: This page provides a list of error codes related to embedding stores.
resource: https://scalardb.scalar-labs.com/docs/3.17/scalardb-cluster/scalardb-embedding-store-status-codes/
tags:
- scalardb
- v3.17
- phase:operate
- section:troubleshoot
- edition:enterprise-premium
- feature-status:private-preview
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.4
doc_id: scalardb-cluster/scalardb-embedding-store-status-codes
lifecycle_phase: operate
breadcrumb:
- Troubleshoot
- Error Codes
editions:
- Enterprise Premium
feature_status:
- Private Preview
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:52Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.17/scalardb-cluster/scalardb-embedding-store-status-codes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Embedding Store Error Codes

This page provides a list of error codes related to embedding stores.

## Error code classes and descriptions

| Class                | Description                        |
|:---------------------|:-----------------------------------|
| `DB-EMBEDDING-1xxxx` | Errors for the user error category |

## `DB-EMBEDDING-1xxxx` status codes

The following are status codes and messages for the user error category.

### `DB-EMBEDDING-10001`

**Message**

```markdown
The embedding store name "scalar.db.embedding.client.store" is not specified
```

### `DB-EMBEDDING-10002`

**Message**

```markdown
The embedding model name "scalar.db.embedding.client.model" is not specified
```

### `DB-EMBEDDING-10003`

**Message**

```markdown
The embedding store is not found. Store: %s
```

### `DB-EMBEDDING-10004`

**Message**

```markdown
The embedding model is not found. Model: %s
```

### `DB-EMBEDDING-10005`

**Message**

```markdown
The property 'scalar.db.embedding.client.contact_points' must not be empty
```

### `DB-EMBEDDING-10006`

**Message**

```markdown
The property 'scalar.db.embedding.client.contact_points' must be prefixed with 'indirect:' or 'direct-kubernetes:'
```

### `DB-EMBEDDING-10007`

**Message**

```markdown
The format of the property 'scalar.db.embedding.client.contact_points' for direct-kubernetes client mode is 'direct-kubernetes:<NAMESPACE_NAME>/<ENDPOINT_NAME>' or 'direct-kubernetes:<ENDPOINT_NAME>'
```

### `DB-EMBEDDING-10008`

**Message**

```markdown
The embeddings must be provided
```

### `DB-EMBEDDING-10009`

**Message**

```markdown
Only one embedding can be added with an embedding ID
```

### `DB-EMBEDDING-10010`

**Message**

```markdown
Text segments cannot be provided when adding an embedding with an embedding ID
```

### `DB-EMBEDDING-10011`

**Message**

```markdown
Both embedding IDs and a filter cannot be provided
```

### `DB-EMBEDDING-10012`

**Message**

```markdown
Unsupported embedding store type. Type: %s
```

### `DB-EMBEDDING-10013`

**Message**

```markdown
Unsupported embedding model type. Type: %s
```

### `DB-EMBEDDING-10014`

**Message**

```markdown
The filter is not set
```

### `DB-EMBEDDING-10015`

**Message**

```markdown
Unsupported metadata value type. Type: %s
```

### `DB-EMBEDDING-10016`

**Message**

```markdown
The metadata value is not set
```
