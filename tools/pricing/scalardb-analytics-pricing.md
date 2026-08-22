---
type: Pricing Reference
title: ScalarDB Analytics 価格表
description: ScalarDB Analytics の SDBU 時間単位の従量課金 (Pay as you go) の定価、稼働量の計算式とシステム要件。
tags: [pricing, scalardb, scalardb-analytics, sdbu, consumption-based]
status: stable
product: scalardb
currency: JPY
tax: excluded
price_basis: list-price
price_unit: SDBU・時間
price_list_version: '2024-09-10'
resource: https://docs.google.com/spreadsheets/d/11JYhx_cz8TbTopHbcoRvEHDhgEnvVYkud--qFnw9G7A/edit
sources:
- id: scalardb-analytics-pricing-2024-09-10
  resource: https://docs.google.com/spreadsheets/d/11JYhx_cz8TbTopHbcoRvEHDhgEnvVYkud--qFnw9G7A/edit
  title: ScalarDB Analytics — Product feature overview and pricing（2024年9月10日 株式会社Scalar）
  author: org:scalar-labs
  last_modified: '2026-08-06T14:55:57Z'
---

# ScalarDB Analytics 価格表

課金単位: **SDBU (ScalarDB Unit) 時間** ｜ 1 SDBU = Databricks 1 DBU 相当 ｜ 最小構成 **6 SDBU** ｜ 金額は**税抜の定価**（JPY）

ScalarDB Analytics は **Pod 単位ではありません**。ScalarDB Enterprise Edition や ScalarDL とは
別体系の従量課金なので、混同しないでください。

## ① 定価（Pay as you go / 従量）

| 項目 | 定価 (JPY) | 定価 (USD) | 単位 | 最小購入数 |
|---|---|---|---|---|
| ScalarDB Analytics | **¥33.5** | $0.2784 | SDBU / 時間 | **6 SDBU** |

6 SDBU を最小構成とします。Spark Platform（Databricks SQL Compute 6DBU 等）上で稼働します。

## ② 先払いクレジット (Prepaid Credit)

**販売価格は本バンドルの公開範囲外です。** 先払いクレジットという購入形態があること、
およびその前提だけを記載します。

| 項目 | 内容 |
|---|---|
| クレジット量のプラン | 5,000 / 10,000 / 20,000 SDBU・時間 の 3 プラン |
| 販売価格 | **非公開**（営業担当にお問い合わせください） |
| 有効期間 | 契約締結日から **3ヶ月** |
| 超過分の扱い | 超えたクレジットに対する**定価での精算** |

有効期間が 3ヶ月であるため、1 年分を先払いクレジットで賄う場合は
**年 4 回の購入**として見積もります。金額は上記のとおり公開範囲外です。

## ③ 稼働量の計算式

| 項目 | 値 | 説明 |
|---|---|---|
| 最小構成 | 6 SDBU | 1 SDBU は Databricks の 1 DBU に相当。標準構成は 8vCPU / 32GB memory の VM × 3 相当 |
| 最小構成 1ヶ月あたりの消費 | **4,464 SDBU・時間** | 6 SDBU/時間 × 24時間 × 31日 |
| 最小構成 1ヶ月あたりの定価 | ¥149,544 | 4,464 SDBU・時間 × ¥33.5 |

```
消費 SDBU・時間 = SDBU 数 × 稼働時間/日 × 稼働日数
定価 (Pay as you go) = 消費 SDBU・時間 × ¥33.5
```

常時稼働を前提にせず、**実際の稼働時間で見積もる**のが原則です（バッチ用途なら大きく下がります）。

従量課金での年間定価の例（最小構成 6 SDBU）:

| 稼働前提 | 年間消費 (SDBU・時間) | 年間定価（税抜） |
|---|---|---|
| 常時稼働（24h × 365日） | 52,560 | ¥1,760,760 |
| 平日日中のみ（10h × 250日） | 15,000 | ¥502,500 |
| バッチのみ（2h × 250日） | 3,000 | ¥100,500 |

## システム要件（見積時に確認）

| 項目 | 値 | 説明 |
|---|---|---|
| Spark Platform | Databricks SQL Compute（最小 6 DBU）/ AWS EMR | ScalarDB Analytics の実行基盤 |
| Catalog Store | ScalarDB がサポートする RDBMS | スキーマ情報を保持するカタログストア |
| Kubernetes Platform | 必要 | ScalarDB Analytics with Spark の Agent を稼働させる基盤 |
| Block Storage | 必要 | クレジット消費レポート (Consumption Report) の出力先 |
| ScalarDB Cluster | 任意 (Optional) | ScalarDB Cluster 経由でのデータアクセス時に必要 |

**ScalarDB Cluster を併用する場合は、別途 ScalarDB Enterprise Edition のライセンスが必要です。**
Analytics のクレジットには含まれません。

また、上表の Spark Platform（Databricks / EMR）、Kubernetes、ストレージは
**お客様側のクラウド費用**であり、Scalar のライセンス費用には含まれません。

## 対応する分析クエリの範囲

| 機能 | 提供開始 |
|---|---|
| ScalarDB 管理下のデータソースに対する分析クエリ処理 | 3.14〜 |
| ScalarDB 管理外のデータソースに対する分析クエリ処理 | 3.15〜 |

機能そのものの仕様は `../products/scalardb/3.19/` 配下の Analytics 関連概念を参照してください。

## 注記

- 本バンドルが収録するのは **Pay as you go（従量）の定価のみ**です。
  先払いクレジットの販売価格・割引条件は含みません。
- 本価格表は**定価**です。実際のご提供価格はボリューム・契約条件により調整されます。
- USD 換算は参考値です（換算レート 1 USD = 120 JPY）。
