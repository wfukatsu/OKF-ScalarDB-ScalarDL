---
type: Troubleshooting
title: ScalarDB GraphQL Error Codes
description: This page provides a list of error codes in ScalarDB GraphQL.
resource: https://scalardb.scalar-labs.com/docs/3.17/scalardb-graphql/scalardb-graphql-status-codes/
tags:
- scalardb
- v3.17
- phase:operate
- section:troubleshoot
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.17'
patch_version: 3.17.4
doc_id: scalardb-graphql/scalardb-graphql-status-codes
lifecycle_phase: operate
breadcrumb:
- Troubleshoot
- Error Codes
editions:
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:52Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.17/scalardb-graphql/scalardb-graphql-status-codes.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# ScalarDB GraphQL Error Codes

This page provides a list of error codes in ScalarDB GraphQL.

## Error code classes and descriptions

| Class              | Description                        |
|:-------------------|:-----------------------------------|
| `DB-GRAPHQL-1xxxx` | Errors for the user error category |

## `DB-GRAPHQL-1xxxx` status codes

The following are status codes and messages for the user error category.

### `DB-GRAPHQL-10000`

**Message**

```markdown
A long value was expected
```

### `DB-GRAPHQL-10001`

**Message**

```markdown
The value is out of range for BigIntValue
```

### `DB-GRAPHQL-10002`

**Message**

```markdown
A long, integer, or string value was expected
```

### `DB-GRAPHQL-10003`

**Message**

```markdown
The AST type `IntValue` was expected
```

### `DB-GRAPHQL-10004`

**Message**

```markdown
A float value was expected
```

### `DB-GRAPHQL-10005`

**Message**

```markdown
An integer or float value was expected
```

### `DB-GRAPHQL-10006`

**Message**

```markdown
The AST type `IntValue` or `FloatValue` was expected
```

### `DB-GRAPHQL-10007`

**Message**

```markdown
The type is not supported. Type: %s
```

### `DB-GRAPHQL-10008`

**Message**

```markdown
The field `%s` requires a `@transaction` or `@twoPhaseCommit` directive with proper arguments
```

### `DB-GRAPHQL-10009`

**Message**

```markdown
The field `%s` cannot be used together with other fields
```

### `DB-GRAPHQL-10010`

**Message**

```markdown
The `@twoPhaseCommit` directive with the `id` argument is required to `%s` the transaction
```

### `DB-GRAPHQL-10011`

**Message**

```markdown
`%s` and `prepare` cannot be run simultaneously
```

### `DB-GRAPHQL-10012`

**Message**

```markdown
`%s` and `join` cannot be run simultaneously
```

### `DB-GRAPHQL-10013`

**Message**

```markdown
The `@transaction` directive with the `id` argument is required to `%s` the transaction
```

### `DB-GRAPHQL-10014`

**Message**

```markdown
`%s` and `commit` cannot be run simultaneously
```

### `DB-GRAPHQL-10015`

**Message**

```markdown
An object cannot be annotated with both `@transaction` and `@twoPhaseCommit` directives
```

### `DB-GRAPHQL-10016`

**Message**

```markdown
The `join` argument of the `@twoPhaseCommit` directive requires a transaction `id` argument
```

### `DB-GRAPHQL-10017`

**Message**

```markdown
`%s` requires the mutation object to be annotated with a `@twoPhaseCommit` directive
```

### `DB-GRAPHQL-10018`

**Message**

```markdown
The `%s` clustering key must have only one of the following: %s
```

### `DB-GRAPHQL-10019`

**Message**

```markdown
A string variable is expected but got %s
```

### `DB-GRAPHQL-10020`

**Message**

```markdown
Unexpected value of id: %s
```

### `DB-GRAPHQL-10021`

**Message**

```markdown
A Boolean variable is expected but got %s
```

### `DB-GRAPHQL-10022`

**Message**

```markdown
Unexpected value of %s: %s
```

### `DB-GRAPHQL-10023`

**Message**

```markdown
Invalid column. Column: %s; Type: %s
```

### `DB-GRAPHQL-10024`

**Message**

```markdown
Unexpected value of type: %s
```

### `DB-GRAPHQL-10025`

**Message**

```markdown
Only one of the following can be specified: %s
```

### `DB-GRAPHQL-10026`

**Message**

```markdown
Unexpected mutation field: %s
```

### `DB-GRAPHQL-10027`

**Message**

```markdown
Invalid type: %s
```
