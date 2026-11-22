---
type: Documentation Section
title: ScalarDB PostgreSQL Frontend 3.20 — User
description: Directory listing for the `user` section of the ScalarDB PostgreSQL Frontend 3.20 documentation.
resource: https://github.com/scalar-labs/scalardb-postgres-frontend/tree/d28a3ad131f99cc7a8f8f92bdff9621671d1dee8
tags:
- scalardb-postgres-frontend
- v3.20
- index
status: stable
product: scalardb-postgres-frontend
version: '3.20'
generated:
  by: process:okf-build/1.0.0
  at: '2026-11-22T03:58:44Z'
---

# User

ScalarDB PostgreSQL Frontend 3.20 reference material generated from the files that define the contract in the source repository.

## Concepts

- [Clients and tools](./clients.md) — The frontend speaks the PostgreSQL wire protocol, version 3, so PostgreSQL's drivers and tools connect to it as they connect to PostgreSQL. This page lists the clients that have been tested and what to know about each.
- [Configuration](./configuration.md) — This page lists the properties that configure the PostgreSQL frontend, the ScalarDB properties that change how it behaves, the settings that a client can change for its session, and the fixed limits that protect the frontend from a single...
- [Designing tables and queries](./schema-and-queries.md) — The frontend accepts PostgreSQL's SQL, but it stores and reads data through ScalarDB, which reads by key. A query that names a table's key reads only the records it needs. A query that does not name a key reads the whole table and filters...
- [Operations](./operations.md) — This page covers what is specific to running the PostgreSQL frontend in ScalarDB Cluster nodes: how client connections spread over the nodes, how to size the frontend's limits, how to see what sessions are doing, how to upgrade, and how to...
- [Quick start: ScalarDB Cluster through PostgreSQL clients](./quick-start.md) — ScalarDB Cluster nodes can speak the PostgreSQL wire protocol, so that psql, the PostgreSQL JDBC driver and other PostgreSQL clients can run SQL as ScalarDB transactions. This guide starts one ScalarDB Cluster node in Docker with the...
- [ScalarDB PostgreSQL Frontend user documentation](./overview.md) — Entry point of the user documentation: deployment choices and where to read about clients, SQL, transactions, security and operations.
- [Security](./security.md) — In a ScalarDB Cluster node with authentication enabled, PostgreSQL clients log in as ScalarDB Cluster users, and ScalarDB Cluster enforces those users' privileges on every statement. This page explains how clients log in, how to manage...
- [SQL reference](./sql-reference.md) — The frontend accepts PostgreSQL 16's SQL dialect and reports itself to clients as PostgreSQL 16.0. This page summarizes what it supports. What it refuses, and where its results can differ from PostgreSQL, is listed in LIMITATIONS.md.
- [Transactions](./transactions.md) — Every statement that the frontend runs is a ScalarDB transaction, or part of one. ScalarDB's transactions are ACID, and they can span several backing databases when ScalarDB is configured with more than one storage, which PostgreSQL alone...
