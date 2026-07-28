---
type: Development Guide
title: ScalarDB Core Configurations
description: This page describes the available configurations for ScalarDB Core.
resource: https://scalardb.scalar-labs.com/docs/3.16/configurations/
tags:
- scalardb
- v3.16
- phase:implement
- section:develop
- edition:community
- edition:enterprise-standard
- edition:enterprise-premium
status: stable
product: scalardb
product_title: ScalarDB
version: '3.16'
patch_version: 3.16.5
doc_id: configurations
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Transactions
- Reference
- Configurations
editions:
- Community
- Enterprise Standard
- Enterprise Premium
generated:
  by: process:okf-build/1.0.0
  at: '2026-07-28T00:57:29Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/dc5c112650d1543275b5c9de1bf3d1dd6d2d777a/versioned_docs/version-3.16/configurations.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-07-27T12:09:14Z'
---

# ScalarDB Core Configurations

This page describes the available configurations for ScalarDB Core.

:::tip

If you are using ScalarDB Cluster, please refer to [ScalarDB Cluster Configurations](./scalardb-cluster/scalardb-cluster-configurations.md) instead.

:::

## General configurations

The following configurations are available for the Consensus Commit transaction manager.

### `transaction_manager`

- **Field:** `scalar.db.transaction_manager`
- **Description:** Transaction manager of ScalarDB. Specify `consensus-commit` to use [Consensus Commit](./consensus-commit.md) or `single-crud-operation` to [run non-transactional storage operations](./run-non-transactional-storage-operations-through-library.md). Note that the configurations under the `scalar.db.consensus_commit` prefix are ignored if you use `single-crud-operation`.
- **Default value:** `consensus-commit`

### `isolation_level`

- **Field:** `scalar.db.consensus_commit.isolation_level`
- **Description:** Isolation level used for Consensus Commit. Either `SNAPSHOT`, `SERIALIZABLE`, or `READ_COMMITTED` can be specified.
- **Default value:** `SNAPSHOT`

### `coordinator.namespace`

- **Field:** `scalar.db.consensus_commit.coordinator.namespace`
- **Description:** Namespace name of Coordinator tables used for Consensus Commit.
- **Default value:** `coordinator`

## Performance-related configurations

The following performance-related configurations are available for the Consensus Commit transaction manager.

### `parallel_executor_count`

- **Field:** `scalar.db.consensus_commit.parallel_executor_count`
- **Description:** Number of executors (threads) for parallel execution. This number refers to the total number of threads across transactions in a ScalarDB Cluster node or a ScalarDB Core process.
- **Default value:** `128`

### `parallel_preparation.enabled`

- **Field:** `scalar.db.consensus_commit.parallel_preparation.enabled`
- **Description:** Whether or not the preparation phase is executed in parallel.
- **Default value:** `true`

### `parallel_validation.enabled`

- **Field:** `scalar.db.consensus_commit.parallel_validation.enabled`
- **Description:** Whether or not the validation phase (in `EXTRA_READ`) is executed in parallel.
- **Default value:** The value of `scalar.db.consensus_commit.parallel_commit.enabled`

### `parallel_commit.enabled`

- **Field:** `scalar.db.consensus_commit.parallel_commit.enabled`
- **Description:** Whether or not the commit phase is executed in parallel.
- **Default value:** `true`

### `parallel_rollback.enabled`

- **Field:** `scalar.db.consensus_commit.parallel_rollback.enabled`
- **Description:** Whether or not the rollback phase is executed in parallel.
- **Default value:** The value of `scalar.db.consensus_commit.parallel_commit.enabled`

### `async_commit.enabled`

- **Field:** `scalar.db.consensus_commit.async_commit.enabled`
- **Description:** Whether or not the commit phase is executed asynchronously.
- **Default value:** `false`

### `async_rollback.enabled`

- **Field:** `scalar.db.consensus_commit.async_rollback.enabled`
- **Description:** Whether or not the rollback phase is executed asynchronously.
- **Default value:** The value of `scalar.db.consensus_commit.async_commit.enabled`

### `parallel_implicit_pre_read.enabled`

- **Field:** `scalar.db.consensus_commit.parallel_implicit_pre_read.enabled`
- **Description:** Whether or not implicit pre-read is executed in parallel.
- **Default value:** `true`

### `one_phase_commit.enabled`

- **Field:** `scalar.db.consensus_commit.one_phase_commit.enabled`
- **Description:** Whether or not the one-phase commit optimization is enabled.
- **Default value:** `false`

### `coordinator.write_omission_on_read_only.enabled`

- **Field:** `scalar.db.consensus_commit.coordinator.write_omission_on_read_only.enabled`
- **Description:** Whether or not the Coordinator write omission optimization is enabled for read-only transactions. This optimization is useful for read-only transactions that do not modify any data, as it avoids unnecessary writes to the Coordinator tables.
- **Default value:** `true`

### `coordinator.group_commit.enabled`

- **Field:** `scalar.db.consensus_commit.coordinator.group_commit.enabled`
- **Description:** Whether or not committing the transaction state is executed in batch mode. This feature can't be used with a two-phase commit interface.
- **Default value:** `false`

### `coordinator.group_commit.slot_capacity`

- **Field:** `scalar.db.consensus_commit.coordinator.group_commit.slot_capacity`
- **Description:** Maximum number of slots in a group for the group commit feature. A large value improves the efficiency of group commit, but may also increase latency and the likelihood of transaction conflicts.[^1]
- **Default value:** `20`

### `coordinator.group_commit.group_size_fix_timeout_millis`

- **Field:** `scalar.db.consensus_commit.coordinator.group_commit.group_size_fix_timeout_millis`
- **Description:** Timeout to fix the size of slots in a group. A large value improves the efficiency of group commit, but may also increase latency and the likelihood of transaction conflicts.[^1]
- **Default value:** `40`

### `coordinator.group_commit.delayed_slot_move_timeout_millis`

- **Field:** `scalar.db.consensus_commit.coordinator.group_commit.delayed_slot_move_timeout_millis`
- **Description:** Timeout to move delayed slots from a group to another isolated group to prevent the original group from being affected by delayed transactions. A large value improves the efficiency of group commit, but may also increase the latency and the likelihood of transaction conflicts.[^1]
- **Default value:** `1200`

### `coordinator.group_commit.old_group_abort_timeout_millis`

- **Field:** `scalar.db.consensus_commit.coordinator.group_commit.old_group_abort_timeout_millis`
- **Description:** Timeout to abort an old ongoing group. A small value reduces resource consumption through aggressive aborts, but may also increase the likelihood of unnecessary aborts for long-running transactions.
- **Default value:** `60000`

### `coordinator.group_commit.timeout_check_interval_millis`

- **Field:** `scalar.db.consensus_commit.coordinator.group_commit.timeout_check_interval_millis`
- **Description:** Interval for checking the group commit–related timeouts.
- **Default value:** `20`

### `coordinator.group_commit.metrics_monitor_log_enabled`

- **Field:** `scalar.db.consensus_commit.coordinator.group_commit.metrics_monitor_log_enabled`
- **Description:** Whether or not the metrics of the group commit are logged periodically.
- **Default value:** `false`

## Storage-related configurations

ScalarDB has a storage (database) abstraction layer that supports multiple storage implementations. You can specify the storage implementation by using the `scalar.db.storage` property.

:::note

For details about using multiple storages, see [Multi-storage configurations](#multi-storage-configurations).

:::

Select a database to see the configurations available for each storage.

**JDBC databases**

The following configurations are available for JDBC databases.

#### `storage`

- **Field:** `scalar.db.storage`
- **Description:** `jdbc` must be specified.

#### `contact_points`

- **Field:** `scalar.db.contact_points`
- **Description:** JDBC connection URL.
- **Default value:** empty

#### `username`

- **Field:** `scalar.db.username`
- **Description:** Username to access the database.
- **Default value:** empty

#### `password`

- **Field:** `scalar.db.password`
- **Description:** Password to access the database.
- **Default value:** empty

#### `jdbc.connection_pool.min_idle`

- **Field:** `scalar.db.jdbc.connection_pool.min_idle`
- **Description:** Minimum number of idle connections in the connection pool.
- **Default value:** `20`

#### `jdbc.connection_pool.max_idle`

- **Field:** `scalar.db.jdbc.connection_pool.max_idle`
- **Description:** Maximum number of connections that can remain idle in the connection pool.
- **Default value:** `50`

#### `jdbc.connection_pool.max_total`

- **Field:** `scalar.db.jdbc.connection_pool.max_total`
- **Description:** Maximum total number of idle and borrowed connections that can be active at the same time for the connection pool. Use a negative value for no limit.
- **Default value:** `200`

#### `jdbc.prepared_statements_pool.enabled`

- **Field:** `scalar.db.jdbc.prepared_statements_pool.enabled`
- **Description:** Setting this property to `true` enables prepared-statement pooling.
- **Default value:** `false`

#### `jdbc.prepared_statements_pool.max_open`

- **Field:** `scalar.db.jdbc.prepared_statements_pool.max_open`
- **Description:** Maximum number of open statements that can be allocated from the statement pool at the same time. Use a negative value for no limit.
- **Default value:** `-1`

#### `jdbc.isolation_level`

- **Field:** `scalar.db.jdbc.isolation_level`
- **Description:** Isolation level for JDBC. `READ_COMMITTED`, `REPEATABLE_READ`, or `SERIALIZABLE` can be specified.
- **Default value:** Underlying-database specific

#### `jdbc.table_metadata.connection_pool.min_idle`

- **Field:** `scalar.db.jdbc.table_metadata.connection_pool.min_idle`
- **Description:** Minimum number of idle connections in the connection pool for the table metadata.
- **Default value:** `5`

#### `jdbc.table_metadata.connection_pool.max_idle`

- **Field:** `scalar.db.jdbc.table_metadata.connection_pool.max_idle`
- **Description:** Maximum number of connections that can remain idle in the connection pool for the table metadata.
- **Default value:** `10`

#### `jdbc.table_metadata.connection_pool.max_total`

- **Field:** `scalar.db.jdbc.table_metadata.connection_pool.max_total`
- **Description:** Maximum total number of idle and borrowed connections that can be active at the same time for the connection pool for the table metadata. Use a negative value for no limit.
- **Default value:** `25`

#### `jdbc.admin.connection_pool.min_idle`

- **Field:** `scalar.db.jdbc.admin.connection_pool.min_idle`
- **Description:** Minimum number of idle connections in the connection pool for admin.
- **Default value:** `5`

#### `jdbc.admin.connection_pool.max_idle`

- **Field:** `scalar.db.jdbc.admin.connection_pool.max_idle`
- **Description:** Maximum number of connections that can remain idle in the connection pool for admin.
- **Default value:** `10`

#### `jdbc.admin.connection_pool.max_total`

- **Field:** `scalar.db.jdbc.admin.connection_pool.max_total`
- **Description:** Maximum total number of idle and borrowed connections that can be active at the same time for the connection pool for admin. Use a negative value for no limit.
- **Default value:** `25`

#### `jdbc.mysql.variable_key_column_size`

- **Field:** `scalar.db.jdbc.mysql.variable_key_column_size`
- **Description:** Column size for TEXT and BLOB columns in MySQL when they are used as a primary key or secondary key. Minimum 64 bytes.
- **Default value:** `128`

#### `jdbc.oracle.variable_key_column_size`

- **Field:** `scalar.db.jdbc.oracle.variable_key_column_size`
- **Description:** Column size for TEXT and BLOB columns in Oracle when they are used as a primary key or secondary key. Minimum 64 bytes.
- **Default value:** `128`

#### `jdbc.oracle.time_column.default_date_component`

- **Field:** `scalar.db.jdbc.oracle.time_column.default_date_component`
- **Description:** Value of the date component used for storing `TIME` data in Oracle. Since Oracle has no data type to only store a time without a date component, ScalarDB stores `TIME` data with the same date component value for ease of comparison and sorting.
- **Default value:** `1970-01-01`

#### `jdbc.db2.variable_key_column_size`

- **Field:** `scalar.db.jdbc.db2.variable_key_column_size`
- **Description:** Column size for TEXT and BLOB columns in IBM Db2 when they are used as a primary key or secondary key. Minimum 64 bytes.
- **Default value:** `128`

#### `jdbc.db2.time_column.default_date_component`

- **Field:** `scalar.db.jdbc.db2.time_column.default_date_component`
- **Description:** Value of the date component used for storing `TIME` data in IBM Db2. Since the IBM Db2 TIMESTAMP type is used to store ScalarDB `TIME` type data because it provides fractional-second precision, ScalarDB stores `TIME` data with the same date component value for ease of comparison and sorting.
- **Default value:** `1970-01-01`

:::note

**SQLite3**

If you're using SQLite3 as a JDBC database, you must set `scalar.db.contact_points` as follows:

```properties
scalar.db.contact_points=jdbc:sqlite:<SQLITE_DB_FILE_PATH>?busy_timeout=10000
```

Unlike other JDBC databases, [SQLite3 doesn't fully support concurrent access](https://www.sqlite.org/lang_transaction.html). To avoid frequent errors caused internally by [`SQLITE_BUSY`](https://www.sqlite.org/rescode.html#busy), setting a [`busy_timeout`](https://www.sqlite.org/c3ref/busy_timeout.html) parameter is recommended.

**YugabyteDB**

If you're using YugabyteDB as a JDBC database, you can specify multiple endpoints in `scalar.db.contact_points` as follows:

```properties
scalar.db.contact_points=jdbc:yugabytedb://127.0.0.1:5433\\,127.0.0.2:5433\\,127.0.0.3:5433/?load-balance=true
```

Multiple endpoints should be separated by escaped commas.

For information on YugabyteDB's smart driver and load balancing, see [YugabyteDB smart drivers for YSQL](https://docs.yugabyte.com/preview/drivers-orms/smart-drivers/).

:::

**DynamoDB**

The following configurations are available for DynamoDB.

#### `storage`

- **Field:** `scalar.db.storage`
- **Description:** `dynamo` must be specified.

#### `contact_points`

- **Field:** `scalar.db.contact_points`
- **Description:** AWS region with which ScalarDB should communicate (for example, `us-east-1`).
- **Default value:** empty

#### `username`

- **Field:** `scalar.db.username`
- **Description:** AWS access key used to identify the user interacting with AWS.
- **Default value:** empty

#### `password`

- **Field:** `scalar.db.password`
- **Description:** AWS secret access key used to authenticate the user interacting with AWS.
- **Default value:** empty

#### `dynamo.endpoint_override`

- **Field:** `scalar.db.dynamo.endpoint_override`
- **Description:** Amazon DynamoDB endpoint with which ScalarDB should communicate. This is primarily used for testing with a local instance instead of an AWS service.
- **Default value:** empty

#### `dynamo.namespace.prefix`

- **Field:** `scalar.db.dynamo.namespace.prefix`
- **Description:** Prefix for the user namespaces and metadata namespace names. Since AWS requires having unique tables names in a single AWS region, this is useful if you want to use multiple ScalarDB environments (development, production, etc.) in a single AWS region.
- **Default value:** empty

**Cosmos DB for NoSQL**

The following configurations are available for CosmosDB for NoSQL.

#### `storage`

- **Field:** `scalar.db.storage`
- **Description:** `cosmos` must be specified.

#### `contact_points`

- **Field:** `scalar.db.contact_points`
- **Description:** Azure Cosmos DB for NoSQL endpoint with which ScalarDB should communicate.
- **Default value:** empty

#### `password`

- **Field:** `scalar.db.password`
- **Description:** Either a master or read-only key used to perform authentication for accessing Azure Cosmos DB for NoSQL.
- **Default value:** empty

#### `cosmos.consistency_level`

- **Field:** `scalar.db.cosmos.consistency_level`
- **Description:** Consistency level used for Cosmos DB operations. `STRONG` or `BOUNDED_STALENESS` can be specified.
- **Default value:** `STRONG`

**Cassandra**

The following configurations are available for Cassandra.

#### `storage`

- **Field:** `scalar.db.storage`
- **Description:** `cassandra` must be specified.

#### `contact_points`

- **Field:** `scalar.db.contact_points`
- **Description:** Comma-separated contact points.
- **Default value:** empty

#### `contact_port`

- **Field:** `scalar.db.contact_port`
- **Description:** Port number for all the contact points.
- **Default value:** empty

#### `username`

- **Field:** `scalar.db.username`
- **Description:** Username to access the database.
- **Default value:** empty

#### `password`

- **Field:** `scalar.db.password`
- **Description:** Password to access the database.
- **Default value:** empty

### Multi-storage configurations

ScalarDB supports using multiple storage implementations simultaneously. For details about using multiple storages, see [Multi-Storage Transactions](./multi-storage-transactions.md).

#### `storage`

- **Field:** `scalar.db.storage`
- **Description:** `multi-storage` must be specified.

#### `multi_storage.storages`

- **Field:** `scalar.db.multi_storage.storages`
- **Description:** Comma-separated storage names (for example, `cassandra,mysql`). These storage names will be used in the `scalar.db.multi_storage.namespace_mapping` property to map namespaces to storages.
- **Default value:** empty

#### `multi_storage.default_storage`

- **Field:** `scalar.db.multi_storage.default_storage`
- **Description:** Default storage name. This storage will be used for any namespace that doesn't have mapping defined in the `scalar.db.multi_storage.namespace_mapping` property.
- **Default value:** empty

#### `multi_storage.namespace_mapping`

- **Field:** `scalar.db.multi_storage.namespace_mapping`
- **Description:** Mapping of namespaces to storages (for example, `user:my_cassandra,coordinator:my_mysql`).
- **Default value:** empty

:::tip

The storage names (`<STORAGE_NAME_FOR_NAMESPACE>`) are arbitrary values that you need to define. You can use any names that you like as long as they are consistent across the multi-storage configurations.

:::

#### `multi_storage.storages.<STORAGE_NAME_FOR_NAMESPACE>.<PROPERTY_NAME>`

For configuring specific storages, use `scalar.db.multi_storage.storages.<STORAGE_NAME_FOR_NAMESPACE>.<PROPERTY_NAME>`, with `<STORAGE_NAME_FOR_NAMESPACE>` being one of the storage names specified in the `scalar.db.multi_storage.storages` property and `<PROPERTY_NAME>` being the property name for the specific storage.

For example, if you've defined [namespace mapping](#multi_storagenamespace_mapping) as `scalar.db.multi_storage.namespace_mapping=user:my_cassandra,coordinator:my_mysql`, with `my_cassandra` and `my_mysql` being the storage names for the `user` and `coordinator` namespaces, respectively:

- You can specify the contact points for Cassandra by using `scalar.db.multi_storage.storages.my_cassandra.contact_points`.
- You can specify the max idle time for the connection pool settings for MySQL by using `scalar.db.multi_storage.storages.my_mysql.jdbc.connection_pool.max_idle`.

For details about the properties available for each storage, see [Storage-related configurations](#storage-related-configurations).

### Cross-partition scan configurations

By enabling the cross-partition scan option as described below, the `Scan` operation can retrieve all records across partitions. In addition, you can specify arbitrary conditions and orderings in the cross-partition `Scan` operation by enabling `cross_partition_scan.filtering` and `cross_partition_scan.ordering`, respectively. Currently, the cross-partition scan with ordering option is available only for JDBC databases. To enable filtering and ordering, `scalar.db.cross_partition_scan.enabled` must be set to `true`.

For details on how to use cross-partition scan, see [Scan operation](./api-guide.md#scan-operation).

:::warning

For non-JDBC databases, transactions could be executed at read-committed snapshot isolation (`SNAPSHOT`), which is a lower isolation level, even if you enable cross-partition scan with the `SERIALIZABLE` isolation level. When using non-JDBC databases, use cross-partition scan only if consistency does not matter for your transactions.

:::

#### `cross_partition_scan.enabled`

- **Field:** `scalar.db.cross_partition_scan.enabled`
- **Description:** Enable cross-partition scan.
- **Default value:** `true`

#### `cross_partition_scan.filtering.enabled`

- **Field:** `scalar.db.cross_partition_scan.filtering.enabled`
- **Description:** Enable filtering in cross-partition scan.
- **Default value:** `false`

#### `cross_partition_scan.ordering.enabled`

- **Field:** `scalar.db.cross_partition_scan.ordering.enabled`
- **Description:** Enable ordering in cross-partition scan.
- **Default value:** `false`

### Scan configurations

You can configure the fetch size for storage scan operations by using the following property.

#### `scan_fetch_size`

- **Field:** `scalar.db.scan_fetch_size`
- **Description:** Specifies the number of records to fetch in a single batch during a storage scan operation. A larger value can improve performance for a large result set by reducing round trips to the storage, but it also increases memory usage. A smaller value uses less memory but may increase latency.
- **Default value:** `10`

## Other ScalarDB configurations

The following are additional configurations available for ScalarDB.

### `metadata.cache_expiration_time_secs`

- **Field:** `scalar.db.metadata.cache_expiration_time_secs`
- **Description:** ScalarDB has a metadata cache to reduce the number of requests to the database. This setting specifies the expiration time of the cache in seconds. If you specify `-1`, the cache will never expire.
- **Default value:** `60`

### `active_transaction_management.expiration_time_millis`

- **Field:** `scalar.db.active_transaction_management.expiration_time_millis`
- **Description:** ScalarDB maintains in-progress transactions, which can be resumed by using a transaction ID. This process expires transactions that have been idle for an extended period to prevent resource leaks. This setting specifies the expiration time of this transaction management feature in milliseconds.
- **Default value:** `-1` (no expiration)

### `consensus_commit.include_metadata.enabled`

- **Field:** `scalar.db.consensus_commit.include_metadata.enabled`
- **Description:** When using Consensus Commit, if this is set to `true`, `Get` and `Scan` operations results will contain transaction metadata. To see the transaction metadata columns details for a given table, you can use the `DistributedTransactionAdmin.getTableMetadata()` method, which will return the table metadata augmented with the transaction metadata columns. Using this configuration can be useful to investigate transaction-related issues.
- **Default value:** `false`

### `consensus_commit.index.eventually_consistent_read.enabled`

- **Field:** `scalar.db.consensus_commit.index.eventually_consistent_read.enabled`
- **Description:** When using Consensus Commit, if this is set to `true`, the before-image index check will be skipped, and index-based reads may miss records whose indexed column is being concurrently updated.
- **Default value:** `false`

:::warning

This is a backward-compatibility option and is **not recommended for new workloads**. For details, see [Correctness of index-based reads](./consensus-commit.md#correctness-of-index-based-reads).

:::

### `default_namespace_name`

- **Field:** `scalar.db.default_namespace_name`
- **Description:** The given namespace name will be used by operations that do not already specify a namespace.
- **Default value:** empty

## Placeholder usage

You can use placeholders in the values, and they are replaced with environment variables (`${env:<ENVIRONMENT_VARIABLE_NAME>}`) or system properties (`${sys:<SYSTEM_PROPERTY_NAME>}`). You can also specify default values in placeholders like `${sys:<SYSTEM_PROPERTY_NAME>:-<DEFAULT_VALUE>}`.

The following is an example of a configuration that uses placeholders:

```properties
scalar.db.username=${env:SCALAR_DB_USERNAME:-admin}
scalar.db.password=${env:SCALAR_DB_PASSWORD}
```

In this example configuration, ScalarDB reads the username and password from environment variables. If the environment variable `SCALAR_DB_USERNAME` does not exist, ScalarDB uses the default value `admin`.

## Configuration example - App and database

```mermaid
flowchart LR
    app["<b>App</b><br />(ScalarDB library with<br />Consensus Commit)"]
    db[(Underlying storage or database)]
    app --> db
```

In this example configuration, the app (ScalarDB library with Consensus Commit) connects to an underlying storage or database (in this case, Cassandra) directly.

:::warning

This configuration exists only for development purposes and isn't suitable for a production environment. This is because the app needs to implement the [Scalar Admin](https://github.com/scalar-labs/scalar-admin) interface to take transactionally consistent backups for ScalarDB, which requires additional configurations.

:::

The following is an example of the configuration for connecting the app to the underlying database through ScalarDB:

```properties
# Transaction manager implementation.
scalar.db.transaction_manager=consensus-commit

# Storage implementation.
scalar.db.storage=cassandra

# Comma-separated contact points.
scalar.db.contact_points=<CASSANDRA_HOST>

# Credential information to access the database.
scalar.db.username=<USERNAME>
scalar.db.password=<PASSWORD>
```
