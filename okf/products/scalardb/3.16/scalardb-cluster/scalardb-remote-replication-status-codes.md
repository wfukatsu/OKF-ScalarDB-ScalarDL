---
type: Troubleshooting
title: Remote Replication Error Codes
description: This page provides a list of error codes related to remote replication.
resource: https://scalardb.scalar-labs.com/docs/3.16/scalardb-cluster/scalardb-remote-replication-status-codes/
tags:
- scalardb
- v3.16
- phase:operate
- section:troubleshoot
- edition:enterprise-premium
- feature-status:private-preview
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: scalardb-cluster/scalardb-remote-replication-status-codes
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
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/scalardb-cluster/scalardb-remote-replication-status-codes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Remote Replication Error Codes

This page provides a list of error codes related to remote replication.

## Error code classes and descriptions

| Class           | Description                        |
|:----------------|:-----------------------------------|
| `DB-REPL-1xxxx` | Errors for the user error category |

## `DB-REPL-1xxxx` status codes

The following are status codes and messages for the user error category.

### `DB-REPL-10057`

**Message**

```markdown
Replication tables already exist
```

### `DB-REPL-10058`

**Message**

```markdown
Replication tables do not exist
```

### `DB-REPL-10059`

**Message**

```markdown
The namespace %s is reserved for the replication feature. Any operations on this namespace are not allowed
```

### `DB-REPL-10060`

**Message**

```markdown
One-phase commit is not supported in the remote replication feature
```
