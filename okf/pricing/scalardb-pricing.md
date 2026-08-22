---
type: Pricing Reference
title: ScalarDB 価格表
description: ScalarDB Enterprise Edition (Standard / Premium) の Pod 単位の定価と、エディションに含まれる機能。
tags: [pricing, scalardb, enterprise-standard, enterprise-premium]
status: stable
product: scalardb
currency: JPY
tax: excluded
price_basis: list-price
price_unit: Pod / 期間
price_list_version: '2024-07-01'
resource: https://docs.google.com/spreadsheets/d/11JYhx_cz8TbTopHbcoRvEHDhgEnvVYkud--qFnw9G7A/edit
sources:
- id: scalar-price-list-2024-07-01
  resource: https://docs.google.com/spreadsheets/d/11JYhx_cz8TbTopHbcoRvEHDhgEnvVYkud--qFnw9G7A/edit
  title: Scalar 製品価格表 — シート「価格表」
  author: org:scalar-labs
  last_modified: '2026-08-06T14:55:57Z'
---

# ScalarDB 価格表

価格単位: **Pod / 期間** ｜ 1 Pod = 2vCPU / 4GB Memory ｜ 金額は**税抜の定価**（JPY）

Pod 数の数え方は [ライセンス数量の数え方](./licensing-units.md) を参照してください。

## ScalarDB Enterprise Edition (Standard)

| 契約期間 | 定価 (JPY) | 参考 (USD) | 月額換算 (JPY) | 定価比 割引率 |
|---|---|---|---|---|
| 1ヶ月 | ¥100,000 | $833.33 | ¥100,000 | — |
| 1年 | ¥1,140,000 | $9,500.00 | ¥95,000 | 5.0% OFF |
| 3年 | 非公開 | 非公開 | 非公開 | 非公開 |

**含まれるもの**

- ScalarDB Cluster（クラスタリング）
- 複数データベースにまたがるトランザクション処理
- 認証 / 認可（Authentication / Authorization）
- 非トランザクショナルなストレージ操作（3.14〜）
- Core Java API / Schema Loader / Data Loader

## ScalarDB Enterprise Edition (Premium)

| 契約期間 | 定価 (JPY) | 参考 (USD) | 月額換算 (JPY) | 定価比 割引率 |
|---|---|---|---|---|
| 1ヶ月 | ¥200,000 | $1,666.67 | ¥200,000 | — |
| 1年 | ¥2,280,000 | $19,000.00 | ¥190,000 | 5.0% OFF |
| 3年 | 非公開 | 非公開 | 非公開 | 非公開 |

**Standard の全機能に加えて**

- SQL インターフェース（SQL API / JDBC / Spring Data JDBC / LINQ）
- GraphQL インターフェース
- 保存データの暗号化（3.14〜）
- ベクトル検索 / リモートレプリケーション（**Private Preview**）

## エディション選択の目安

| 要件 | 選ぶエディション |
|---|---|
| プログラム API（CRUD / トランザクション）だけで足りる | Standard |
| SQL / JDBC / Spring Data JDBC / LINQ を使う | **Premium** |
| GraphQL エンドポイントを使う | **Premium** |
| 保存データの暗号化が要件 | **Premium** |
| 属性ベースアクセス制御 (ABAC) が要件 | Premium **ではなく** Enterprise Premium Option（別途要問い合わせ） |
| ScalarDB Cluster を使わずクライアント・ライブラリのみ | Community Edition（無償） |
| 分析クエリ処理が要件 | [ScalarDB Analytics](./scalardb-analytics-pricing.md)（別体系） |

機能の可否は [エディション別 機能・提供物マトリクス](./edition-feature-matrix.md) を、
機能そのものの仕様は `../products/scalardb/3.19/` 配下の概念を参照してください。

## 課金対象外

| 製品 | 扱い |
|---|---|
| ScalarDB Community Edition | 無償。Apache v2 ライセンス。クライアント・ライブラリでの提供（**ScalarDB Cluster / Server は含まれません**） |
| ScalarDB Analytics | 別体系。SDBU 時間単位の従量課金（[価格表](./scalardb-analytics-pricing.md)） |

## 注記

- 本バンドルが収録するのは **Pay as you go / 月額 / 年額 の定価のみ**です。
  3年契約の定価は非公開のため、営業担当にお問い合わせください。
- 本価格表は**定価**です。実際のご提供価格はボリューム・契約条件により調整されます。
- USD 換算は参考値です（換算レート 1 USD = 120 JPY）。
- **Private Preview 版**は、あらかじめ申し入れされたお客様のみを対象とする実験的な機能です。
  価格に含まれていても、そのまま本番前提で提案しないでください。
