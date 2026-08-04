---
type: Development Guide
title: Data Source Reference
description: This reference guide provides detailed information about data source configuration formats, provider-specific settings, and data type mappings for ScalarDB Analytics.
resource: https://scalardb.scalar-labs.com/docs/3.18/scalardb-analytics/reference-data-source/
tags:
- scalardb
- v3.18
- phase:implement
- section:develop
- edition:enterprise-option
status: stable
product: scalardb
product_title: ScalarDB
version: '3.18'
patch_version: 3.18.1
doc_id: scalardb-analytics/reference-data-source
lifecycle_phase: implement
breadcrumb:
- Develop
- Run Analytical Queries
- Reference
editions:
- Enterprise Option
generated:
  by: process:okf-build/1.0.0
  at: '2026-08-04T23:50:49Z'
sources:
- id: docs-scalardb
  resource: https://github.com/scalar-labs/docs-scalardb/blob/6126dfe2f56389351d88b134752618641f9771dd/versioned_docs/version-3.18/scalardb-analytics/reference-data-source.mdx
  title: ScalarDB documentation source (MDX)
  author: process:scalar-labs/docs-scalardb
  last_modified: '2026-08-04T15:05:02Z'
---

# Data Source Reference

This reference guide provides detailed information about data source configuration formats, provider-specific settings, and data type mappings for ScalarDB Analytics.

:::warning

You need to have a license key (trial license or commercial license) to use ScalarDB Analytics. If you don't have a license key, please [contact us](https://www.scalar-labs.com/contact-us).

:::

## Data source registration file format

Data sources are registered to catalogs by using the CLI with provider configuration files. These files define the connection settings for each data source type. For CLI command details, see [CLI command reference](./reference-cli-command.md).

The provider configuration file has the following structure:

```json
{
  "type": "<database-type>", // Database type: postgresql, mysql, scalardb, sqlserver, oracle, dynamodb, databricks, snowflake
  // Type-specific connection configuration
  // Configuration varies by database type
}
```

The catalog name and data source name are specified as CLI options. (`--catalog` and `--data-source`)

:::tip File reference syntax

You can use the `${file:path}` syntax to load configuration values from an external file. This is useful for reusing existing configuration files or separating sensitive information.

**Supported file formats:**

- **`.properties` files**: Loaded and converted to a JSON object with string values
- **`.json` files**: Loaded as-is (any valid JSON structure)

For example:
```json
{
  "type": "scalardb",
  "configs": "${file:/path/to/scalardb.properties}"
}
```

:::

## Provider configuration by type

The following sections show the provider configuration for each supported database type:

**ScalarDB**

### Configurations

The following configuration is for ScalarDB.

#### `configs`

- **Field:** `configs`
- **Description:** A map of ScalarDB configuration properties. These are the same properties that would be specified in a ScalarDB configuration file. You can specify the configuration inline as a JSON object or use a file reference with the `${file:path}` syntax.

### Example

**Inline configuration:**

```json
{
  "type": "scalardb",
  "configs": {
    "scalar.db.contact_points": "localhost",
    "scalar.db.username": "admin",
    "scalar.db.password": "admin",
    "scalar.db.storage": "jdbc"
  }
}
```

**Using file reference with a properties file:**

```json
{
  "type": "scalardb",
  "configs": "${file:/path/to/scalardb.properties}"
}
```

### Data access method

ScalarDB Analytics reads data from ScalarDB by using the ScalarDB Core library directly, not through ScalarDB Cluster. As a result, features that are available only in ScalarDB Cluster (such as encryption) cannot be used with the ScalarDB data source.

### Scan behavior

Internally, the ScalarDB data source uses the [`Scan` operation with `all()`](../api-guide.md#scan-operation) to read data. This operation requires [cross-partition scan](../configurations.md#cross-partition-scan-configurations) to be enabled. Filtering and ordering are not applied at the ScalarDB level. The relevant settings are as follows:

- `scalar.db.cross_partition_scan.enabled` must be `true` (the default is `true`).
- `scalar.db.cross_partition_scan.filtering.enabled` has no effect.
- `scalar.db.cross_partition_scan.ordering.enabled` has no effect.

:::note

Filter push-down and other optimizations may be supported in future releases.

:::

### ScalarDB Core configuration overrides

[ScalarDB Core configuration properties](../configurations.md) are generally respected when used as a ScalarDB data source. However, the following properties are overridden by ScalarDB Analytics:

<ul>
  <li>**`scalar.db.scan_fetch_size`**: If not explicitly set by the user, defaults to `4096` instead of the ScalarDB Core default of `10`.</li>
  <li>**`scalar.db.consensus_commit.isolation_level`**: Always overridden to `READ_COMMITTED`, regardless of the user-specified value.</li>
</ul>

**PostgreSQL**

### Configuration

The following configurations are for PostgreSQL.

#### `host`

- **Field:** `host`
- **Description:** PostgreSQL server hostname.

#### `port`

- **Field:** `port`
- **Description:** Port number.

#### `username`

- **Field:** `username`
- **Description:** Database user.

#### `password`

- **Field:** `password`
- **Description:** Database password.

#### `database`

- **Field:** `database`
- **Description:** Database name to connect to.

### Example

```json
{
  "type": "postgresql",
  "host": "postgres.example.com",
  "port": 5432,
  "username": "analytics_user",
  "password": "secure_password",
  "database": "customers"
}
```

**MySQL**

### Configuration

The following configurations are for MySQL.

#### `host`

- **Field:** `host`
- **Description:** MySQL server hostname.

#### `port`

- **Field:** `port`
- **Description:** Port number.

#### `username`

- **Field:** `username`
- **Description:** Database user.

#### `password`

- **Field:** `password`
- **Description:** Database password.

#### `database`

- **Field:** `database`
- **Description:** Specific database to import. If omitted, all databases will be imported.
- **Default value:** None (imports all databases)

### Example

```json
{
  "type": "mysql",
  "host": "mysql.example.com",
  "port": 3306,
  "username": "analytics_user",
  "password": "secure_password",
  "database": "orders" // Optional - if omitted, all databases will be imported
}
```

**Oracle**

### Configuration

The following configurations are for Oracle.

#### `host`

- **Field:** `host`
- **Description:** Oracle server hostname.

#### `port`

- **Field:** `port`
- **Description:** Port number.

#### `username`

- **Field:** `username`
- **Description:** Database user.

#### `password`

- **Field:** `password`
- **Description:** Database password.

#### `serviceName`

- **Field:** `serviceName`
- **Description:** Oracle service name.

### Example

```json
{
  "type": "oracle",
  "host": "oracle.example.com",
  "port": 1521,
  "username": "analytics_user",
  "password": "secure_password",
  "serviceName": "ORCL"
}
```

**SQL Server**

### Configuration

The following configurations are for SQL Server.

#### `host`

- **Field:** `host`
- **Description:** SQL Server hostname.

#### `port`

- **Field:** `port`
- **Description:** Port number.

#### `username`

- **Field:** `username`
- **Description:** Database user.

#### `password`

- **Field:** `password`
- **Description:** Database password.

#### `database`

- **Field:** `database`
- **Description:** Specific database to connect to.
- **Default value:** None (connects to default database)

#### `secure`

- **Field:** `secure`
- **Description:** Enable encryption.
- **Default value:** `false`

### Example

```json
{
  "type": "sqlserver",
  "host": "sqlserver.example.com",
  "port": 1433,
  "username": "sa",
  "password": "secure_password",
  "database": "analytics", // Optional - if specified, only this database will be imported
  "secure": true // Optional - enable encryption
}
```

**Databricks**

### Configuration

The following configurations are for Databricks (Databricks SQL/JDBC).

#### `host`

- **Field:** `host`
- **Description:** Databricks workspace hostname (for example, `adb-1234567890123.4.azuredatabricks.net`).

#### `port`

- **Field:** `port`
- **Description:** Port number.
- **Default value:** Driver default. (Optional)

#### `httpPath`

- **Field:** `httpPath`
- **Description:** HTTP path of your SQL warehouse or cluster (for example, `/sql/1.0/warehouses/xxxxxxxxxxxxxx`).

#### `oAuthClientId`

- **Field:** `oAuthClientId`
- **Description:** OAuth machine-to-machine (M2M) service principal's UUID or Application ID for Databricks SQL/JDBC authentication.

#### `oAuthSecret`

- **Field:** `oAuthSecret`
- **Description:** OAuth M2M service principal's secret for Databricks SQL/JDBC authentication.

#### `catalog`

- **Field:** `catalog`
- **Description:** Default catalog to use. (Optional)

### Example

```json
{
  "type": "databricks",
  "host": "adb-1234567890123.4.azuredatabricks.net",
  "port": 443,
  "httpPath": "/sql/1.0/warehouses/xxxxxxxxxxxxxx",
  "oAuthClientId": "YOUR_CLIENT_ID",
  "oAuthSecret": "YOUR_CLIENT_SECRET",
  "catalog": "main"
}
```

**Snowflake**

### Configuration

The following configurations are for Snowflake.

#### `account`

- **Field:** `account`
- **Description:** Snowflake account identifier (for example, `xy12345.ap-northeast-1`).

#### `username`

- **Field:** `username`
- **Description:** A Snowflake user.

#### `password`

- **Field:** `password`
- **Description:** A Snowflake user's programmatic access token.

#### `database`

- **Field:** `database`
- **Description:** Default database to resolve/import. (Optional)

### Example

```json
{
  "type": "snowflake",
  "account": "YOUR-ACCOUNT",
  "username": "analytics_user",
  "password": "secure_password",
  "database": "ANALYTICS"
}
```

**DynamoDB**

### Configuration

The following configurations are for DynamoDB.

:::note AWS Credentials

DynamoDB authentication uses the standard AWS SDK credential provider chain. Credentials can be configured through:

- Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- AWS credentials file (`~/.aws/credentials`)
- IAM roles (when running on EC2, ECS, or Lambda)
- AWS SSO or other credential providers supported by the AWS SDK

For more information, see the [AWS SDK documentation on credential providers](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials.html).

:::

#### `region`

- **Field:** `region`
- **Description:** AWS region (for example, `us-east-1`). Either `region` or `endpoint` must be specified (not both).

#### `endpoint`

- **Field:** `endpoint`
- **Description:** Custom endpoint URL. Either `region` or `endpoint` must be specified (not both).

### Schema definition

Since DynamoDB is schema-less, you must provide a schema definition separately by using the `--schema-json` or `--schema-file` CLI option. The schema cannot be automatically resolved.

#### Schema structure

The schema file must contain the following structure:

##### `namespaces[]`

- **Field:** `namespaces[]`
- **Description:** Array of namespace definitions.

##### `namespaces[].names[]`

- **Field:** `namespaces[].names[]`
- **Description:** Array of namespace name components (strings). For single-level namespaces, use a single-element array.

##### `namespaces[].tables[]`

- **Field:** `namespaces[].tables[]`
- **Description:** Array of table definitions.

##### `namespaces[].tables[].name`

- **Field:** `namespaces[].tables[].name`
- **Description:** Table name. Must match the DynamoDB table name.

##### `namespaces[].tables[].columns[]`

- **Field:** `namespaces[].tables[].columns[]`
- **Description:** Array of column definitions.

##### `namespaces[].tables[].columns[].name`

- **Field:** `namespaces[].tables[].columns[].name`
- **Description:** Column name. Must match the DynamoDB attribute name.

##### `namespaces[].tables[].columns[].type`

- **Field:** `namespaces[].tables[].columns[].type`
- **Description:** Data type.

##### `namespaces[].tables[].columns[].nullable`

- **Field:** `namespaces[].tables[].columns[].nullable`
- **Description:** Whether the column can contain null values.
- **Default value:** `true`

### Example

**Provider configuration file (`provider.json`):**

```json
{
  "type": "dynamodb",
  "region": "us-east-1"
}
```

**Schema definition file (`schema.json`):**

```json
{
  "namespaces": [
    {
      "names": ["production"],
      "tables": [
        {
          "name": "user_events",
          "columns": [
            { "name": "user_id", "type": "TEXT", "nullable": false },
            { "name": "event_time", "type": "TIMESTAMP", "nullable": false },
            { "name": "event_type", "type": "TEXT" },
            { "name": "event_data", "type": "TEXT" }
          ]
        }
      ]
    }
  ]
}
```

**CLI command:**

```console
scalardb-analytics datasource register \
  --catalog production \
  --data-source dynamodb_events \
  --provider-file provider.json \
  --schema-file schema.json
```

## Catalog information reference

This section describes catalog structure mappings by data source and data type mappings.

### Catalog structure mappings by data source

When registering a data source to ScalarDB Analytics, the catalog structure of the data source, that is, namespaces, tables, and columns, are resolved and registered to the universal data catalog. To resolve the catalog structure of the data source, a particular object on the data sources side are mapped to the universal data catalog object.

#### Catalog-level mappings

The catalog-level mappings are the mappings of the namespace names, table names, and column names from the data sources to the universal data catalog. To see the catalog-level mappings in each data source, select a data source.

**ScalarDB**

The catalog structure of ScalarDB is automatically resolved by ScalarDB Analytics. The catalog-level objects are mapped as follows:

- The ScalarDB namespace is mapped to the namespace. Therefore, the namespace of the ScalarDB data source is always single level, consisting of only the namespace name.
- The ScalarDB table is mapped to the table.
- The ScalarDB column is mapped to the column.

**PostgreSQL**

The catalog structure of PostgreSQL is automatically resolved by ScalarDB Analytics. The catalog-level objects are mapped as follows:

- The PostgreSQL schema is mapped to the namespace. Therefore, the namespace of the PostgreSQL data source is always single level, consisting of only the schema name.
- Only user-defined schemas are mapped to namespaces. The following system schemas are ignored:
- `information_schema`
- `pg_catalog`
- The PostgreSQL table is mapped to the table.
- The PostgreSQL column is mapped to the column.

**MySQL**

The catalog structure of MySQL is automatically resolved by ScalarDB Analytics. The catalog-level objects are mapped as follows:

- The MySQL database is mapped to the namespace. Therefore, the namespace of the MySQL data source is always single level, consisting of only the database name.
- Only user-defined databases are mapped to namespaces. The following system databases are ignored:
- `mysql`
- `sys`
- `information_schema`
- `performance_schema`
- The MySQL table is mapped to the table.
- The MySQL column is mapped to the column.

**Oracle**

The catalog structure of Oracle is automatically resolved by ScalarDB Analytics. The catalog-level objects are mapped as follows:

- The Oracle schema is mapped to the namespace. Therefore, the namespace of the Oracle data source is always single level, consisting of only schema name.
- Only user-defined schemas are mapped to namespaces. The following system schemas are ignored:
- `ANONYMOUS`
- `APPQOSSYS`
- `AUDSYS`
- `CTXSYS`
- `DBSNMP`
- `DGPDB_INT`
- `DBSFWUSER`
- `DVF`
- `DVSYS`
- `GGSYS`
- `GSMADMIN_INTERNAL`
- `GSMCATUSER`
- `GSMROOTUSER`
- `GSMUSER`
- `LBACSYS`
- `MDSYS`
- `OJVMSYS`
- `ORDDATA`
- `ORDPLUGINS`
- `ORDSYS`
- `OUTLN`
- `REMOTE_SCHEDULER_AGENT`
- `SI_INFORMTN_SCHEMA`
- `SYS`
- `SYS$UMF`
- `SYSBACKUP`
- `SYSDG`
- `SYSKM`
- `SYSRAC`
- `SYSTEM`
- `WMSYS`
- `XDB`
- `DIP`
- `MDDATA`
- `ORACLE_OCM`
- `XS$NULL`

**SQL Server**

The catalog structure of SQL Server is automatically resolved by ScalarDB Analytics. The catalog-level objects are mapped as follows:

- Each SQL Server database-schema pair is mapped to a namespace in ScalarDB Analytics. Therefore, the namespace of the SQL Server data source is always two-level, consisting of the database name and the schema name.
- Only user-defined databases are mapped to namespaces. The following system databases are ignored:
- `master`
- `model`
- `msdb`
- `tempdb`
- Only user-defined schemas are mapped to namespaces. The following system schemas are ignored:
- `sys`
- `guest`
- `INFORMATION_SCHEMA`
- `db_accessadmin`
- `db_backupoperator`
- `db_datareader`
- `db_datawriter`
- `db_ddladmin`
- `db_denydatareader`
- `db_denydatawriter`
- `db_owner`
- `db_securityadmin`
- The SQL Server table is mapped to the table.
- The SQL Server column is mapped to the column.

**Databricks**

The catalog structure of Databricks is automatically resolved by ScalarDB Analytics. The catalog-level objects are mapped as follows:

- Each Databricks catalog-schema pair is mapped to a namespace in ScalarDB Analytics. Therefore, the namespace of the Databricks data source always has two levels, consisting of the catalog name and the schema name.
- The following system catalogs/schemas are ignored:
- **Catalogs:** `system`
- **Schemas:** `information_schema`, `global_temp`, `sys`, `routines`
- The Databricks table is mapped to the table.
- The Databricks column is mapped to the column.

**Snowflake**

The catalog structure of Snowflake is automatically resolved by ScalarDB Analytics. The catalog-level objects are mapped as follows:

- Each Snowflake database-schema pair is mapped to a namespace in ScalarDB Analytics. Therefore, the namespace of the Snowflake data source always has two levels, consisting of the database name and the schema name.
- The following system databases/schemas are ignored:
- **Databases:** `SNOWFLAKE`
- **Schemas:** `INFORMATION_SCHEMA`
- The Snowflake table is mapped to the table.
- The Snowflake column is mapped to the column.

**DynamoDB**

Since DynamoDB is schema-less, you need to specify the catalog structure explicitly when registering a DynamoDB data source by using the following format JSON:

```json
{
    "namespaces": [
        {
            "name": "<NAMESPACE_NAME>",
            "tables": [
                {
                    "name": "<TABLE_NAME>",
                    "columns": [
                        {
                            "name": "<COLUMN_NAME>",
                            "type": "<COLUMN_TYPE>"
                        },
                        ...
                    ]
                },
                ...
            ]
        },
        ...
    ]
}
```

In the specified JSON, you can use any arbitrary namespace names, but the table names must match the table names in DynamoDB and column name and type must match field names and types in DynamoDB.

### Data type mappings

The following sections show how native types from each data source are mapped to ScalarDB Analytics types:

:::warning

Columns with data types that are not included in the mapping tables below will be ignored during data source registration. These columns will not appear in the ScalarDB Analytics catalog and cannot be queried. Information about ignored columns is logged in the ScalarDB Analytics server logs.

:::

**ScalarDB**

| **ScalarDB Data Type** | **ScalarDB Analytics Data Type** |
| :--------------------- | :------------------------------- |
| `BOOLEAN`              | `BOOLEAN`                        |
| `INT`                  | `INT`                            |
| `BIGINT`               | `BIGINT`                         |
| `FLOAT`                | `FLOAT`                          |
| `DOUBLE`               | `DOUBLE`                         |
| `TEXT`                 | `TEXT`                           |
| `BLOB`                 | `BLOB`                           |
| `DATE`                 | `DATE`                           |
| `TIME`                 | `TIME`                           |
| `TIMESTAMP`            | `TIMESTAMP`                      |
| `TIMESTAMPTZ`          | `TIMESTAMPTZ`                    |

**PostgreSQL**

| **PostgreSQL Data Type**      | **ScalarDB Analytics Data Type** |
| :---------------------------- | :------------------------------- |
| `integer`                     | `INT`                            |
| `bigint`                      | `BIGINT`                         |
| `real`                        | `FLOAT`                          |
| `double precision`            | `DOUBLE`                         |
| `smallserial`                 | `SMALLINT`                       |
| `serial`                      | `INT`                            |
| `bigserial`                   | `BIGINT`                         |
| `char`                        | `TEXT`                           |
| `varchar`                     | `TEXT`                           |
| `text`                        | `TEXT`                           |
| `bpchar`                      | `TEXT`                           |
| `boolean`                     | `BOOLEAN`                        |
| `bytea`                       | `BLOB`                           |
| `date`                        | `DATE`                           |
| `time`                        | `TIME`                           |
| `time with time zone`         | `TIME`                           |
| `time without time zone`      | `TIME`                           |
| `timestamp`                   | `TIMESTAMP`                      |
| `timestamp with time zone`    | `TIMESTAMPTZ`                    |
| `timestamp without time zone` | `TIMESTAMP`                      |

**MySQL**

| **MySQL Data Type**  | **ScalarDB Analytics Data Type** |
| :------------------- | :------------------------------- |
| `bit`                | `BOOLEAN`                        |
| `bit(1)`             | `BOOLEAN`                        |
| `bit(x)` if _x >= 2_ | `BLOB`                           |
| `tinyint`            | `SMALLINT`                       |
| `tinyint(1)`         | `BOOLEAN`                        |
| `boolean`            | `BOOLEAN`                        |
| `smallint`           | `SMALLINT`                       |
| `smallint unsigned`  | `INT`                            |
| `mediumint`          | `INT`                            |
| `mediumint unsigned` | `INT`                            |
| `int`                | `INT`                            |
| `int unsigned`       | `BIGINT`                         |
| `bigint`             | `BIGINT`                         |
| `float`              | `FLOAT`                          |
| `double`             | `DOUBLE`                         |
| `real`               | `DOUBLE`                         |
| `char`               | `TEXT`                           |
| `varchar`            | `TEXT`                           |
| `text`               | `TEXT`                           |
| `binary`             | `BLOB`                           |
| `varbinary`          | `BLOB`                           |
| `blob`               | `BLOB`                           |
| `date`               | `DATE`                           |
| `time`               | `TIME`                           |
| `datetime`           | `TIMESTAMP`                      |
| `timestamp`          | `TIMESTAMPTZ`                    |

**Oracle**

| **Oracle Data Type**             | **ScalarDB Analytics Data Type** |
| :------------------------------- | :------------------------------- |
| `NUMBER` if _scale = 0_          | `BIGINT`                         |
| `NUMBER` if _scale > 0_          | `DOUBLE`                         |
| `FLOAT` if _precision ≤ 53_      | `DOUBLE`                         |
| `BINARY_FLOAT`                   | `FLOAT`                          |
| `BINARY_DOUBLE`                  | `DOUBLE`                         |
| `CHAR`                           | `TEXT`                           |
| `NCHAR`                          | `TEXT`                           |
| `VARCHAR2`                       | `TEXT`                           |
| `NVARCHAR2`                      | `TEXT`                           |
| `CLOB`                           | `TEXT`                           |
| `NCLOB`                          | `TEXT`                           |
| `BLOB`                           | `BLOB`                           |
| `BOOLEAN`                        | `BOOLEAN`                        |
| `DATE`                           | `DATE`                           |
| `TIMESTAMP`                      | `TIMESTAMPTZ`                    |
| `TIMESTAMP WITH TIME ZONE`       | `TIMESTAMPTZ`                    |
| `TIMESTAMP WITH LOCAL TIME ZONE` | `TIMESTAMP`                      |
| `RAW`                            | `BLOB`                           |

**SQL Server**

| **SQL Server Data Type** | **ScalarDB Analytics Data Type** |
| :----------------------- | :------------------------------- |
| `bit`                    | `BOOLEAN`                        |
| `tinyint`                | `SMALLINT`                       |
| `smallint`               | `SMALLINT`                       |
| `int`                    | `INT`                            |
| `bigint`                 | `BIGINT`                         |
| `real`                   | `FLOAT`                          |
| `float`                  | `DOUBLE`                         |
| `float(n)` if _n ≤ 24_   | `FLOAT`                          |
| `float(n)` if _n ≥ 25_   | `DOUBLE`                         |
| `binary`                 | `BLOB`                           |
| `varbinary`              | `BLOB`                           |
| `char`                   | `TEXT`                           |
| `varchar`                | `TEXT`                           |
| `nchar`                  | `TEXT`                           |
| `nvarchar`               | `TEXT`                           |
| `ntext`                  | `TEXT`                           |
| `text`                   | `TEXT`                           |
| `date`                   | `DATE`                           |
| `time`                   | `TIME`                           |
| `datetime`               | `TIMESTAMP`                      |
| `datetime2`              | `TIMESTAMP`                      |
| `smalldatetime`          | `TIMESTAMP`                      |
| `datetimeoffset`         | `TIMESTAMPTZ`                    |

**Databricks**

| **Databricks SQL Data Type** | **ScalarDB Analytics Data Type**                                                               |
| :--------------------------- | :--------------------------------------------------------------------------------------------- |
| `TINYINT`                    | `SMALLINT`                                                                                     |
| `SMALLINT`                   | `SMALLINT`                                                                                     |
| `INT` / `INTEGER`            | `INT`                                                                                          |
| `BIGINT`                     | `BIGINT`                                                                                       |
| `FLOAT`                      | `FLOAT`                                                                                        |
| `DOUBLE`                     | `DOUBLE`                                                                                       |
| `DECIMAL(p,s)` if _s = 0_    | `BYTE` (p ≤ 2), `SMALLINT` (p 3–4), `INT` (p 5–9), `BIGINT` (p 10–18), `DECIMAL(p,0)` (p > 18) |
| `DECIMAL(p,s)` if _s ≠ 0_    | `DECIMAL(p,s)`                                                                                 |
| `STRING` / `VARCHAR`         | `TEXT`                                                                                         |
| `BINARY`                     | `BLOB`                                                                                         |
| `BOOLEAN`                    | `BOOLEAN`                                                                                      |
| `DATE`                       | `DATE`                                                                                         |
| `TIMESTAMP`                  | `TIMESTAMPTZ`                                                                                  |
| `TIMESTAMP_NTZ`              | `TIMESTAMP`                                                                                    |

:::note

- For `DECIMAL` types, when precision and scale are not specified during table creation, the default values of precision = 38 and scale = 0 are applied.
- For `DECIMAL` types with scale = 0 and small precision, optimized integer types (`BYTE`, `SMALLINT`, `INT`, `BIGINT`) are used to improve storage and performance.

:::

**Snowflake**

| **Snowflake Data Type**                                                                                                      | **ScalarDB Analytics Data Type**                                                               |
| :--------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| `NUMBER(p,0)` / `INT` / `INTEGER` / `BIGINT` / `SMALLINT` / `TINYINT` / `BYTEINT`                                            | `BYTE` (p ≤ 2), `SMALLINT` (p 3–4), `INT` (p 5–9), `BIGINT` (p 10–18), `DECIMAL(p,0)` (p > 18) |
| `NUMBER(p,s)` / `NUMERIC` / `DECIMAL` if _s ≠ 0_                                                                             | `DECIMAL(p,s)`                                                                                 |
| `FLOAT` / `FLOAT4` / `FLOAT8` / `DOUBLE` / `DOUBLE PRECISION` / `REAL`                                                       | `DOUBLE`                                                                                       |
| `VARCHAR` / `STRING` / `TEXT` / `NVARCHAR` / `NVARCHAR2` / `CHAR VARYING` / `NCHAR VARYING` / `CHAR` / `CHARACTER` / `NCHAR` | `TEXT`                                                                                         |
| `BINARY` / `VARBINARY`                                                                                                       | `BLOB`                                                                                         |
| `BOOLEAN`                                                                                                                    | `BOOLEAN`                                                                                      |
| `DATE`                                                                                                                       | `DATE`                                                                                         |
| `TIME`                                                                                                                       | `TIME`                                                                                         |
| `TIMESTAMP_NTZ` / `DATETIME`                                                                                                 | `TIMESTAMP`                                                                                    |
| `TIMESTAMP_LTZ`                                                                                                              | `TIMESTAMPTZ`                                                                                  |
| `TIMESTAMP_TZ`                                                                                                               | `TIMESTAMPTZ`                                                                                  |

:::note

- For `NUMBER` and `DECIMAL` types, when precision and scale are not specified during table creation, the default values of precision = 38 and scale = 0 are applied.
- For `NUMBER` and `DECIMAL` types with scale = 0 and small precision, optimized integer types (`BYTE`, `SMALLINT`, `INT`, `BIGINT`) are used to improve storage and performance.

:::

**DynamoDB**

| **DynamoDB Data Type** | **ScalarDB Analytics Data Type** |
| :--------------------- | :------------------------------- |
| `String`               | `TEXT`                           |
| `Number`               | `DOUBLE`                         |
| `Binary`               | `BLOB`                           |
| `Boolean`              | `BOOLEAN`                        |
| `Null`                 | `NULL`                           |
| `String Set`           | `TEXT`                           |
| `Number Set`           | `TEXT`                           |
| `Binary Set`           | `TEXT`                           |
| `List`                 | `TEXT`                           |
| `Map`                  | `TEXT`                           |

:::note

DynamoDB complex data types (String Set, Number Set, Binary Set, List, Map) are mapped to `TEXT` for compatibility. The actual values are serialized as JSON strings in ScalarDB Analytics queries.

:::
