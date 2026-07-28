---
type: Troubleshooting
title: ScalarDL HashStore Error Codes
description: This page provides a list of error codes in ScalarDL HashStore.
resource: https://scalardl.scalar-labs.com/docs/latest/scalardl-hashstore-status-codes/
tags:
- scalardl
- v3.13
- phase:operate
- edition:community
- edition:enterprise
status: stable
product: scalardl
product_title: ScalarDL
version: '3.13'
patch_version: 3.13.0
doc_id: scalardl-hashstore-status-codes
lifecycle_phase: operate
editions:
- Community
- Enterprise
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:30Z'
sources:
- id: docs-scalardl
  resource: https://github.com/scalar-labs/docs-scalardl/blob/eecc7f890d648a2f4ff33d60e5a96d57a1aa74d4/docs/scalardl-hashstore-status-codes.mdx
  title: ScalarDL documentation source (MDX)
  author: process:scalar-labs/docs-scalardl
  last_modified: '2026-07-24T17:50:50Z'
---

# ScalarDL HashStore Error Codes

This page provides a list of error codes in ScalarDL HashStore.

## Error code classes and descriptions

| Class                 | Description                        |
|:----------------------|:-----------------------------------|
| `DL-HASH-STORE-4xxxx` | Errors for the user error category |

## `DL-HASH-STORE-4xxxx` status codes

The following are status codes and messages for the user error category.

### `DL-HASH-STORE-414001`

**Message**

```markdown
The PUT operation for the mutable database must have a namespace and table.
```

**Solution**

```markdown
Provide both a namespace and table name for the PUT operation.
```

### `DL-HASH-STORE-414002`

**Message**

```markdown
An unsupported data type is specified in the PUT operation. Data type: %s
```

**Solution**

```markdown
Use a supported data type for the PUT operation. Check the documentation for valid data types.
```
