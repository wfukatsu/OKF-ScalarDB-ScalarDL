---
type: Troubleshooting
title: ScalarDB GraphQL Error Codes
description: This page provides a list of error codes in ScalarDB GraphQL.
resource: https://scalardb.scalar-labs.com/docs/3.14/scalardb-graphql/scalardb-graphql-status-codes/
tags:
- scalardb
- v3.14
- phase:operate
- section:troubleshoot
- edition:enterprise-premium
- unmaintained
status: deprecated
product: scalardb
product_title: ScalarDB
version: '3.14'
patch_version: 3.14.6
doc_id: scalardb-graphql/scalardb-graphql-status-codes
lifecycle_phase: operate
breadcrumb:
- Troubleshoot
- Error Codes
editions:
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:57Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.14/scalardb-graphql/scalardb-graphql-status-codes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB GraphQL Error Codes

This page provides a list of error codes in ScalarDB GraphQL.

## Error code classes and descriptions

| Class           | Description                        |
|:----------------|:-----------------------------------|
| `GRAPHQL-1xxxx` | Errors for the user error category |

## `GRAPHQL-1xxxx` status codes

The following are status codes and messages for the user error category.

### `GRAPHQL-10000`

**Message**

```markdown
A long value was expected
```

### `GRAPHQL-10001`

**Message**

```markdown
The value is out of range for BigIntValue
```

### `GRAPHQL-10002`

**Message**

```markdown
A long, integer, or string value was expected
```

### `GRAPHQL-10003`

**Message**

```markdown
The AST type `IntValue` was expected
```

### `GRAPHQL-10004`

**Message**

```markdown
A float value was expected
```

### `GRAPHQL-10005`

**Message**

```markdown
An integer or float value was expected
```

### `GRAPHQL-10006`

**Message**

```markdown
The AST type `IntValue` or `FloatValue` was expected
```

### `GRAPHQL-10007`

**Message**

```markdown
The type is not supported. Type: %s
```

### `GRAPHQL-10008`

**Message**

```markdown
The field `%s` requires a `@transaction` or `@twoPhaseCommit` directive with proper arguments
```

### `GRAPHQL-10009`

**Message**

```markdown
The field `%s` cannot be used together with other fields
```

### `GRAPHQL-10010`

**Message**

```markdown
The `@twoPhaseCommit` directive with the `id` argument is required to `%s` the transaction
```

### `GRAPHQL-10011`

**Message**

```markdown
`%s` and `prepare` cannot be run simultaneously
```

### `GRAPHQL-10012`

**Message**

```markdown
`%s` and `join` cannot be run simultaneously
```

### `GRAPHQL-10013`

**Message**

```markdown
The `@transaction` directive with the `id` argument is required to `%s` the transaction
```

### `GRAPHQL-10014`

**Message**

```markdown
`%s` and `commit` cannot be run simultaneously
```

### `GRAPHQL-10015`

**Message**

```markdown
An object cannot be annotated with both `@transaction` and `@twoPhaseCommit` directives
```

### `GRAPHQL-10016`

**Message**

```markdown
The `join` argument of the `@twoPhaseCommit` directive requires a transaction `id` argument
```

### `GRAPHQL-10017`

**Message**

```markdown
`%s` requires the mutation object to be annotated with a `@twoPhaseCommit` directive
```

### `GRAPHQL-10018`

**Message**

```markdown
The `%s` clustering key must have only one of the following: %s
```

### `GRAPHQL-10019`

**Message**

```markdown
A string variable is expected but got %s
```

### `GRAPHQL-10020`

**Message**

```markdown
Unexpected value of id: %s
```

### `GRAPHQL-10021`

**Message**

```markdown
A Boolean variable is expected but got %s
```

### `GRAPHQL-10022`

**Message**

```markdown
Unexpected value of %s: %s
```

### `GRAPHQL-10023`

**Message**

```markdown
Invalid column. Column: %s; Type: %s
```

### `GRAPHQL-10024`

**Message**

```markdown
Unexpected value of type: %s
```

### `GRAPHQL-10025`

**Message**

```markdown
Only one of the following can be specified: %s
```

### `GRAPHQL-10026`

**Message**

```markdown
Unexpected mutation field: %s
```

### `GRAPHQL-10027`

**Message**

```markdown
Invalid type: %s
```
