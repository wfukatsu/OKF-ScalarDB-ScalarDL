---
type: Troubleshooting
title: Embedding Store Error Codes
description: This page provides a list of error codes related to embedding stores.
resource: https://scalardb.scalar-labs.com/docs/latest/scalardb-cluster/scalardb-embedding-store-status-codes/
tags:
- scalardb
- v3.19
- phase:operate
- edition:enterprise-premium
- feature-status:public-preview
status: stable
product: scalardb
product_title: ScalarDB
version: '3.19'
patch_version: 3.19.1
doc_id: scalardb-cluster/scalardb-embedding-store-status-codes
lifecycle_phase: operate
editions:
- Enterprise Premium
feature_status:
- Public Preview
generated:
  by: process:okf-build/1.0.0
  at: '2026-09-11T05:23:06Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/c882c4103fe6e0aedff74e7afa67c2587a78ec9b/docs/scalardb-cluster/scalardb-embedding-store-status-codes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-09-09T05:43:01Z'
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
