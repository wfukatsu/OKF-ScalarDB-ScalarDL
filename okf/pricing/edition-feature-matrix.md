---
type: Licensing Reference
title: エディション別 機能・提供物マトリクス
description: どのエディションを見積もるべきかを決めるための、ScalarDB v3.19 / ScalarDL v3.13 時点の機能可否とライブラリ・ツールの提供エディション。
tags: [pricing, licensing, editions, feature-matrix, scalardb, scalardl]
status: stable
currency: JPY
price_basis: list-price
matrix_snapshot: 'scalardb 3.19 / scalardl 3.13'
snapshot_date: '2026-08-06'
sources:
- id: scalar-price-list-2024-07-01
  access: internal (Google Drive / Scalar 社内)
  title: Scalar 製品価格表 — シート「機能比較」
  author: org:scalar-labs
  last_modified: '2026-08-06T14:55:57Z'
- id: okf-scalardb-scalardl
  resource: https://github.com/wfukatsu/OKF-ScalarDB-ScalarDL
  title: OKF-ScalarDB-ScalarDL（ScalarDB v3.19 / ScalarDL v3.13 の概念から作成）
  author: process:okf-build
  last_modified: '2026-08-06T00:00:00Z'
---

# エディション別 機能・提供物マトリクス

**このマトリクスは価格を決めるための判断材料です。** 機能そのものの仕様は
`../products/scalardb/<version>/` および `../products/scalardl/<version>/` を正典としてください。

凡例: ○ = 利用可能 / 提供対象　　— = 対象外　　`(3.14〜)` はその機能が利用可能になったバージョン

> **スナップショットであることに注意**
> 本マトリクスは **ScalarDB v3.19 / ScalarDL v3.13** 時点（取得日 2026年8月6日）の内容です。
> バンドルに収録されている ScalarDL の最新版がこれより新しい場合、
> `../products/scalardl/index.md` で差分を確認してください。

## ① ScalarDB エディション別 機能比較 (v3.19)

| 機能 | Core (Community) | Cluster (EE Standard) | Cluster (EE Premium) | Analytics (Enterprise) | 備考 |
|---|---|---|---|---|---|
| 複数データベースにまたがるトランザクション処理（プリミティブインターフェース） | ○ | ○ | ○ | — | |
| クラスタリング (ScalarDB Cluster) | — | ○ | ○ | — | |
| 非トランザクショナルなストレージ操作 | — | ○ (3.14〜) | ○ (3.14〜) | — | |
| 認証 / 認可 (Authentication / Authorization) | — | ○ | ○ | — | |
| 保存データの暗号化 (Encryption) | — | — | ○ (3.14〜) | — | |
| 属性ベースアクセス制御 (ABAC) | — | — | ○ (3.15〜) | — | Enterprise Premium **Option** (\*1) / Private Preview (\*2) |
| SQL インターフェース (SQL API / JDBC / Spring Data JDBC / LINQ) | — | — | ○ | — | |
| GraphQL インターフェース | — | — | ○ | — | |
| ベクトル検索インターフェース | — | — | ○ (3.15〜) | — | Private Preview (\*2) |
| リモートレプリケーション | — | — | ○ (3.16〜) | — | Private Preview (\*2) |
| ScalarDB 管理下のデータソースに対する分析クエリ処理 | — | — | — | ○ (3.14〜) | |
| ScalarDB 管理外のデータソースに対する分析クエリ処理 | — | — | — | ○ (3.15〜) | |

\*1 属性ベースアクセス制御 (ABAC) は **Enterprise Premium エディションには含まれません**。
利用を希望される場合は別途お問い合わせください。

\*2 **Private Preview 版**は、あらかじめ申し入れされたお客様のみを対象とする実験的な機能です。
将来のバージョンでの一般提供をお待ちいただくか、お問い合わせください。**本番前提で見積もらないでください。**

## ② ScalarDB ライブラリ / ツール / コンポーネントの提供エディション (v3.19)

| 種別 | 名称 | Community | Enterprise Standard | Enterprise Premium |
|---|---|---|---|---|
| ライブラリ | ScalarDB Core Java API library | ○ | ○ | ○ |
| ライブラリ | ScalarDB Cluster Java Client SDK | — | ○ | ○ |
| ライブラリ | ScalarDB SQL | — | ○ | ○ |
| ライブラリ | JDBC driver for ScalarDB SQL | — | ○ | ○ |
| ライブラリ | Spring Data JDBC for ScalarDB | — | ○ | ○ |
| ツール | ScalarDB Schema Loader | ○ | ○ | ○ |
| ツール | ScalarDB Cluster Schema Loader | — | ○ | ○ |
| ツール | ScalarDB Data Loader CLI | ○ | ○ | ○ |
| ツール | ScalarDB Cluster Data Loader CLI | — | ○ | ○ |
| ツール | ScalarDB Cluster SQL CLI | — | — | ○ |
| ツール | Replication CLI | — | — | ○ |
| ツール | ScalarDB MCP Server | ○ | ○ | ○ |
| ツール | Helm Charts | ○ | ○ | ○ |
| ツール | Scalar Admin for Kubernetes | — | ○ | ○ |
| コンポーネント | ScalarDB Cluster Node (BYOL) | — | ○ | ○ |

> **配布 ≠ 利用可否**
> ライブラリ / ツールの配布エディションと、機能としての利用可否（①）は一致しない場合があります。
> 例: **ScalarDB SQL ライブラリは Enterprise Standard にも配布されますが、
> SQL インターフェース機能の利用は Enterprise Premium が対象**です。
> 「ライブラリが手元にあるから使える」と判断しないでください。

## ③ ScalarDL コンポーネント / ライブラリ / ツール (v3.13)

| 種別 | 名称 | Community | Enterprise | 備考 |
|---|---|---|---|---|
| コンポーネント | ScalarDL Ledger | ○ | — | Community 版コンテナイメージ |
| コンポーネント | ScalarDL Ledger (BYOL) | — | ○ | 商用ライセンス（課金対象） |
| コンポーネント | ScalarDL Auditor (BYOL) | — | ○ | 商用ライセンス（課金対象）。Ledger の導入が前提 |
| ライブラリ | ScalarDL Java Client SDK | ○ | ○ | |
| ライブラリ | ScalarDL HashStore Java Client SDK | ○ | ○ | |
| ライブラリ | ScalarDL TableStore Java Client SDK | ○ | ○ | |
| ツール | ScalarDL Client Command | ○ | ○ | |
| ツール | ScalarDL Schema Loader | ○ | ○ | |
| ツール | Helm Charts | ○ | ○ | |
| ツール | Scalar Admin for Kubernetes | ○ | ○ | |

- ScalarDL には ScalarDB のようなエディション別の機能マトリクスはありません。
  **Ledger / Auditor のコンポーネント単位**でライセンスされます。
- ScalarDL Auditor は ScalarDL Ledger の導入が前提です。また Auditor は Ledger と
  別の管理ドメイン（別アカウント / 別クラスタ）に配置する必要があります。
- ScalarDB Analytics (Enterprise) は Pod 単位ではなく SDBU 時間単位の従量課金です
  （[ScalarDB Analytics 価格表](./scalardb-analytics-pricing.md)）。

## 関連

- [ScalarDB 価格表](./scalardb-pricing.md)
- [ScalarDL 価格表](./scalardl-pricing.md)
- [製品・エディション・バージョンの選び方](../guides/product-and-version-selection.md) — 概念 frontmatter の `editions` との対応
