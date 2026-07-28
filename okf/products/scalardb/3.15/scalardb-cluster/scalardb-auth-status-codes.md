---
type: Troubleshooting
title: Authentication and Authorization Error Codes
description: This page provides a list of error codes related to authentication and authorization.
resource: https://scalardb.scalar-labs.com/docs/3.15/scalardb-cluster/scalardb-auth-status-codes/
tags:
- scalardb
- v3.15
- phase:operate
- section:troubleshoot
- edition:enterprise-standard
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.15'
patch_version: 3.15.8
doc_id: scalardb-cluster/scalardb-auth-status-codes
lifecycle_phase: operate
breadcrumb:
- Troubleshoot
- Error Codes
editions:
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:02Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.15/scalardb-cluster/scalardb-auth-status-codes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# Authentication and Authorization Error Codes

This page provides a list of error codes related to authentication and authorization.

## Error code classes and descriptions

| Class           | Description                            |
|:----------------|:---------------------------------------|
| `DB-AUTH-1xxxx` | Errors for the user error category     |
| `DB-AUTH-3xxxx` | Errors for the internal error category |

## `DB-AUTH-1xxxx` status codes

The following are status codes and messages for the user error category.

### `DB-AUTH-10000`

**Message**

```markdown
The user already exists. Username: %s
```

### `DB-AUTH-10001`

**Message**

```markdown
The user does not exist. Username: %s
```

### `DB-AUTH-10003`

**Message**

```markdown
The namespace does not exist. Namespace: %s
```

### `DB-AUTH-10004`

**Message**

```markdown
The table does not exist. Table: %s
```

### `DB-AUTH-10005`

**Message**

```markdown
Invalid username or password
```

### `DB-AUTH-10006`

**Message**

```markdown
Access denied: Invalid auth token
```

### `DB-AUTH-10007`

**Message**

```markdown
Access denied: You need the %s privilege on the namespace %s to execute this operation
```

### `DB-AUTH-10008`

**Message**

```markdown
Access denied: You need the %s privilege on the table %s to execute this operation
```

### `DB-AUTH-10009`

**Message**

```markdown
Access denied: You must be a superuser to execute this operation
```

### `DB-AUTH-10010`

**Message**

```markdown
Access denied: You can't access information about the user %s
```

### `DB-AUTH-10011`

**Message**

```markdown
Access denied: You can't alter the user %s
```

### `DB-AUTH-10012`

**Message**

```markdown
Access denied: You must be a superuser to change the SUPERUSER attribute
```

### `DB-AUTH-10013`

**Message**

```markdown
You can't change the SUPERUSER attribute for the current user %s
```

### `DB-AUTH-10014`

**Message**

```markdown
You can't drop the current user %s
```

### `DB-AUTH-10015`

**Message**

```markdown
Access denied: You can't grant the %s privilege because you don't have the same privilege on the table %s
```

### `DB-AUTH-10016`

**Message**

```markdown
Access denied: You can't grant the %s privilege because you don't have the same privilege on the namespace %s
```

### `DB-AUTH-10017`

**Message**

```markdown
Access denied: You can't revoke the %s privilege because you don't have the same privilege on the table %s
```

### `DB-AUTH-10018`

**Message**

```markdown
Access denied: You can't revoke the %s privilege because you don't have the same privilege on the namespace %s
```

### `DB-AUTH-10019`

**Message**

```markdown
The operation does not have the target namespace or table name. Operation: %s
```

## `DB-AUTH-3xxxx` status codes

The following are status codes and messages for the internal error category.

### `DB-AUTH-30000`

**Message**

```markdown
Getting auth token information failed
```

### `DB-AUTH-30001`

**Message**

```markdown
Getting the user failed. Username: %s
```

### `DB-AUTH-30002`

**Message**

```markdown
Creating a user failed. Username: %s
```

### `DB-AUTH-30003`

**Message**

```markdown
Altering the user failed. Username: %s
```

### `DB-AUTH-30004`

**Message**

```markdown
Dropping the user failed. Username: %s
```

### `DB-AUTH-30005`

**Message**

```markdown
Granting privileges failed. Username: %s; Namespace: %s; Privileges: %s
```

### `DB-AUTH-30006`

**Message**

```markdown
Granting privileges failed. Username: %s; Table: %s; Privileges: %s
```

### `DB-AUTH-30007`

**Message**

```markdown
Revoking privileges failed. Username: %s; Namespace: %s; Privileges: %s
```

### `DB-AUTH-30008`

**Message**

```markdown
Revoking privileges failed. Username: %s; Table: %s; Privileges: %s
```

### `DB-AUTH-30009`

**Message**

```markdown
Getting users failed
```

### `DB-AUTH-30010`

**Message**

```markdown
Getting privileges failed. Username: %s; Namespace: %s
```

### `DB-AUTH-30011`

**Message**

```markdown
Getting privileges failed. Username: %s; Table: %s
```

### `DB-AUTH-30012`

**Message**

```markdown
Deleting privileges failed. Namespace: %s
```

### `DB-AUTH-30013`

**Message**

```markdown
Deleting privileges failed. Table: %s
```

### `DB-AUTH-30014`

**Message**

```markdown
Logging in failed. Username: %s
```

### `DB-AUTH-30015`

**Message**

```markdown
Logging out failed
```
