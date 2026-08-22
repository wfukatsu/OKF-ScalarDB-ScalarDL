---
type: Documentation Section
title: 価格・ライセンス
description: ScalarDB / ScalarDL / ScalarDB Analytics の課金モデル、定価、ライセンス数量の数え方をまとめたセクション。
tags: [pricing, licensing, commercial, index]
status: stable
currency: JPY
tax: excluded
price_basis: list-price
price_list_version: '2024-07-01'
sources:
- id: scalar-price-list-2024-07-01
  access: internal (Google Drive / Scalar 社内)
  title: Scalar 製品価格表（2024年7月1日版をシート化したもの）
  author: org:scalar-labs
  last_modified: '2026-08-06T14:55:57Z'
- id: scalardb-analytics-pricing-2024-09-10
  access: internal (Google Drive / Scalar 社内)
  title: ScalarDB Analytics — Product feature overview and pricing（2024年9月10日 株式会社Scalar）
  author: org:scalar-labs
  last_modified: '2026-08-06T14:55:57Z'
---

# 価格・ライセンス

このセクションは、`products/` 配下の**製品ドキュメント（上流の developers.scalar-labs.com 由来）とは出典が異なります**。
価格は株式会社 Scalar の社内価格表に由来し、ドキュメントサイトには公開されていません。

> **取り扱い注意**
> ここに記載する金額はすべて**定価（税抜・JPY）**です。実際のご提供価格はボリューム・契約条件により調整されます。
> AI エージェントはこの情報を**参考見積の材料**としてのみ使い、確定金額・提出可能な見積として提示してはいけません。
> 提出する見積は必ず営業担当のレビューを経てください。

## 公開範囲

本バンドルが収録するのは、次の 3 つの定価だけです。

| 公開する | 内容 |
|---|---|
| **Pay as you go**（従量） | ScalarDB Analytics の SDBU・時間単価 |
| **月額** | Pod 単位サブスクリプション 4 製品の 1ヶ月契約 定価 |
| **年額** | 同 4 製品の 1年契約 定価 |

次のものは**収録していません**。必要な場合は営業担当にお問い合わせください。

- 3年契約の定価
- 先払いクレジット (Prepaid Credit) の販売価格
- 期間割引・ボリューム割引を含む値引き条件、値引き後の実売価格
- 顧客固有の契約条件

## 3 つの課金モデル

| # | モデル | 対象製品 | 課金単位 | 定価（最小契約単位） |
|---|---|---|---|---|
| ① | Pod 単位サブスクリプション | ScalarDB Enterprise Edition (Standard) | Pod / 期間 | ¥100,000 / Pod / 月 |
| ① | Pod 単位サブスクリプション | ScalarDB Enterprise Edition (Premium) | Pod / 期間 | ¥200,000 / Pod / 月 |
| ① | Pod 単位サブスクリプション | ScalarDL Ledger | Pod / 期間 | ¥100,000 / Pod / 月 |
| ① | Pod 単位サブスクリプション | ScalarDL Auditor | Pod / 期間 | ¥100,000 / Pod / 月 |
| ② | SDBU 時間単位の従量課金 | ScalarDB Analytics | SDBU・時間 | ¥33.5 / SDBU・時間（最小 6 SDBU） |
| ③ | 無償（OSS） | ScalarDB Community Edition | — | 無償（Apache v2） |

- **① Pod 単位サブスクリプション** — 1 Pod = 2vCPU / 4GB Memory。収録している契約期間は 1ヶ月 / 1年（3年契約もありますが定価は非公開）。
- **② SDBU 時間単位の従量課金 (Pay as you go)** — 1 SDBU = Databricks 1 DBU 相当。最小構成 6 SDBU。先払いクレジットという購入形態もありますが、販売価格は非公開。
- **③ 無償（OSS）** — クライアント・ライブラリとしての提供。**ScalarDB Cluster / Server は含まれません。**

## 概念

- [ライセンス数量の数え方（1 Pod の定義・契約期間）](./licensing-units.md) — 課金単位「1 Pod」の換算式、契約期間ごとの Pod 数のカウント、月額換算
- [ScalarDB 価格表](./scalardb-pricing.md) — Enterprise Edition Standard / Premium の定価
- [ScalarDL 価格表](./scalardl-pricing.md) — Ledger / Auditor の定価
- [ScalarDB Analytics 価格表](./scalardb-analytics-pricing.md) — Pay as you go（SDBU・時間）の定価と稼働量の計算
- [エディション別 機能・提供物マトリクス](./edition-feature-matrix.md) — どのエディションを見積もるべきかの判断材料
- [サンプル見積（5 パターン）](./sample-quotations.md) — 開発 / テスト / ステージング環境を想定した構成別の試算例（月額・年額・従量ベース）

## 出典と有効性

| 項目 | 内容 |
|---|---|
| ScalarDB / ScalarDL 定価（月額・年額） | Scalar 製品価格表 **2024年7月1日版** |
| ScalarDB Analytics 定価（従量） | ScalarDB Analytics — Product feature overview and pricing（**2024年9月10日** 株式会社Scalar） |
| 機能・提供物マトリクス | 本バンドル（ScalarDB v3.19 / ScalarDL v3.13）から作成。取得日 2026年8月6日 |
| USD 換算 | 参考値。換算レート 1 USD = 120 JPY |
| 消費税 | 別途。サンプル見積では 10% で計算 |

価格表の版が更新された場合、このセクションは `products/` と違って**自動再生成されません**。
更新手順は [バンドルの保守手順](../guides/bundle-maintenance.md) を参照してください。
