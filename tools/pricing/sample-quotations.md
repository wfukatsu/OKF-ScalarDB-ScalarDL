---
type: Pricing Reference
title: サンプル見積（5 パターン）
description: 開発 1 Pod / テスト 3 Pod / ステージング 3 Pod を前提とした、ScalarDB / ScalarDL / Analytics の構成別 試算例（月額・年額・従量の定価ベース）。
tags: [pricing, quotation, sample, scalardb, scalardl, scalardb-analytics]
status: stable
currency: JPY
tax: excluded
price_basis: list-price
price_list_version: '2024-07-01'
sources:
- id: scalar-sample-quotation
  access: internal (Google Drive / Scalar 社内)
  title: Scalar 製品 サンプル見積書
  author: org:scalar-labs
  last_modified: '2026-08-06T15:16:11Z'
- id: scalar-sample-quotation-slides
  access: internal (Google Drive / Scalar 社内)
  title: Scalar 製品 サンプル見積もり 解説（AWS 構成図つき）
  author: org:scalar-labs
  last_modified: '2026-08-06T15:17:10Z'
---

# サンプル見積（5 パターン）

**これはサンプルです。** 定価をベースに試算した例であり、そのまま提出できる見積ではありません。
実際のご提供価格は契約条件により調整されます。
本バンドルが収録するのは **Pay as you go / 月額 / 年額 の定価のみ**で、値引き条件は含みません。

## 共通の前提

| 環境 | Pod 数 | ライセンス数量 | 構成の考え方 |
|---|---|---|---|
| 開発環境 | 1 | 1 Pod | 単一 AZ・HA なし。開発者 1 名が利用 |
| テスト環境 | 3 | 3 Pod | 2 AZ 分散（AZ-a に 2 Pod / AZ-c に 1 Pod） |
| ステージング環境 | 3 | 3 Pod | 2 AZ 分散（AZ-a に 2 Pod / AZ-c に 1 Pod） |
| **合計（1 製品あたり）** | **7** | **7 Pod** | **本番環境は本見積の対象外** |

- 契約期間は **1 年契約**を既定としています（1ヶ月 / 1年 に切替可能）。
- 1 Pod = 2vCPU / 4GB Memory。金額は税抜の定価ベース、合計欄で**消費税 10%** を加算しています。
- 見積有効期限は発行日より 30 日。

## 比較サマリ（1 年契約・定価）

| | パターン | 対象製品 | 数量計 | 定価合計（税抜） | 合計（税込） |
|---|---|---|---|---|---|
| A | ScalarDB EE (Standard) のみ | ScalarDB EE Standard | 7 Pod | ¥7,980,000 | ¥8,778,000 |
| B | ScalarDB EE (Premium) のみ | ScalarDB EE Premium | 7 Pod | ¥15,960,000 | ¥17,556,000 |
| C | ScalarDL Ledger のみ | ScalarDL Ledger | 7 Pod | ¥7,980,000 | ¥8,778,000 |
| D | ScalarDL Ledger + Auditor | ScalarDL Ledger / Auditor | 13 Pod | ¥14,820,000 | ¥16,302,000 |
| E | ScalarDB Analytics | ScalarDB Analytics | 52,560 SDBU・時間 | ¥1,760,760 | ¥1,936,836 |

- パターン E の「数量計」は**年間の消費量（SDBU・時間）**です。他パターンは Pod 数です。
- パターン E は **Pay as you go（従量）の定価**で算出しています。先払いクレジットを使う場合の
  販売価格は本バンドルの公開範囲外です。

## パターン別の内訳

### A — ScalarDB Enterprise Edition (Standard) のみ

トランザクション機能中心の最小構成。SQL / GraphQL / 暗号化は使いません。

| 品名 | 環境 | 数量 (Pod) | 定価単価 (1年) | 定価金額 |
|---|---|---|---|---|
| ScalarDB EE (Standard) | 開発環境 | 1 | ¥1,140,000 | ¥1,140,000 |
| ScalarDB EE (Standard) | テスト環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| ScalarDB EE (Standard) | ステージング環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| | | | **小計（税抜）** | **¥7,980,000** |
| | | | 消費税 (10%) | ¥798,000 |
| | | | **合計（税込）** | **¥8,778,000** |

AWS 構成の要点: Amazon EKS 上で ScalarDB Cluster を稼働。テスト / ステージングは 2 AZ 分散の HA 構成。
バックエンド DB は Amazon RDS for PostgreSQL (Multi-AZ)。内部 NLB (gRPC :60053) 経由で接続。
ECR / Secrets Manager / CloudWatch / IAM を全環境で共用。

### B — ScalarDB Enterprise Edition (Premium) のみ

SQL インターフェース / GraphQL / 保存データの暗号化を利用。**インフラ構成と Pod 数は A と同一**で、
ライセンスのエディションのみが変わります。

| 品名 | 環境 | 数量 (Pod) | 定価単価 (1年) | 定価金額 |
|---|---|---|---|---|
| ScalarDB EE (Premium) | 開発環境 | 1 | ¥2,280,000 | ¥2,280,000 |
| ScalarDB EE (Premium) | テスト環境 | 3 | ¥2,280,000 | ¥6,840,000 |
| ScalarDB EE (Premium) | ステージング環境 | 3 | ¥2,280,000 | ¥6,840,000 |
| | | | **小計（税抜）** | **¥15,960,000** |
| | | | 消費税 (10%) | ¥1,596,000 |
| | | | **合計（税込）** | **¥17,556,000** |

### C — ScalarDL Ledger のみ

改ざん検知台帳を Ledger 単独で構成。単価は Standard と同額のため、金額はパターン A と同じです。

| 品名 | 環境 | 数量 (Pod) | 定価単価 (1年) | 定価金額 |
|---|---|---|---|---|
| ScalarDL Ledger | 開発環境 | 1 | ¥1,140,000 | ¥1,140,000 |
| ScalarDL Ledger | テスト環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| ScalarDL Ledger | ステージング環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| | | | **小計（税抜）** | **¥7,980,000** |
| | | | 消費税 (10%) | ¥798,000 |
| | | | **合計（税込）** | **¥8,778,000** |

### D — ScalarDL Ledger + Auditor

Ledger 7 Pod + Auditor 6 Pod = **13 Pod**。Auditor は**別管理ドメイン**に配置します。
このサンプルでは Auditor を**テスト / ステージング環境にのみ**配置しています（開発環境は Ledger 1 Pod のみ）。

| 品名 | 環境 | 数量 (Pod) | 定価単価 (1年) | 定価金額 |
|---|---|---|---|---|
| ScalarDL Ledger | 開発環境 | 1 | ¥1,140,000 | ¥1,140,000 |
| ScalarDL Ledger | テスト環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| ScalarDL Ledger | ステージング環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| ScalarDL Auditor | テスト環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| ScalarDL Auditor | ステージング環境 | 3 | ¥1,140,000 | ¥3,420,000 |
| | | | **小計（税抜）** | **¥14,820,000** |
| | | | 消費税 (10%) | ¥1,482,000 |
| | | | **合計（税込）** | **¥16,302,000** |

### E — ScalarDB Analytics

SDBU 従量課金（Pay as you go）。最小構成 6 SDBU を**常時稼働**させた場合の年間定価です。

| 品名 | 稼働前提 | 年間消費 (SDBU・時間) | 単価 | 定価金額 |
|---|---|---|---|---|
| ScalarDB Analytics | 6 SDBU × 24h × 365日 | 52,560 | ¥33.5 / SDBU・時間 | ¥1,760,760 |
| | | | **小計（税抜）** | **¥1,760,760** |
| | | | 消費税 (10%) | ¥176,076 |
| | | | **合計（税込）** | **¥1,936,836** |

稼働前提を変えた場合の年間定価:

| 稼働前提 | 年間消費 (SDBU・時間) | 年間定価（税抜） |
|---|---|---|
| 常時稼働（24h × 365日） | 52,560 | ¥1,760,760 |
| 平日日中のみ（10h × 250日） | 15,000 | ¥502,500 |
| バッチのみ（2h × 250日） | 3,000 | ¥100,500 |

前提:
- **常時稼働を既定にしないこと。** Analytics は従量課金なので、実際の稼働時間で見積もると大きく下がります。
- 先払いクレジット（5,000 / 10,000 / 20,000 SDBU・時間、有効期間 3ヶ月）を使う購入形態もありますが、
  その販売価格は本バンドルの公開範囲外です。営業担当にお問い合わせください。
- **ScalarDB Cluster を併用する場合は、別途 ScalarDB Enterprise Edition のライセンスが必要**です。

## 値引きについて

**本バンドルは定価のみを収録しています。** 値引き率・値引き後の実売価格・顧客固有の条件は
含みません。実際のご提供価格は営業担当が契約条件に応じて決定します。

## 単価マスタ（定価・税抜）

| 製品名 | 1ヶ月 | 1年 |
|---|---|---|
| ScalarDB Enterprise Edition (Standard) | ¥100,000 | ¥1,140,000 |
| ScalarDB Enterprise Edition (Premium) | ¥200,000 | ¥2,280,000 |
| ScalarDL Ledger | ¥100,000 | ¥1,140,000 |
| ScalarDL Auditor | ¥100,000 | ¥1,140,000 |
| ScalarDB Analytics | ¥33.5 / SDBU・時間（Pay as you go） | 同左（従量） |

共通パラメータ: 消費税率 10.0% / 見積有効期限 発行日より 30 日 /
契約期間の月数換算 1ヶ月 = 1、1年 = 12。

3年契約の定価は本バンドルの公開範囲外です。

## 見積を作るときのチェックリスト

1. **本番環境が対象かどうか** — 上のサンプルはすべて本番環境を対象外にしています。
2. **Pod のサイズ** — 2vCPU / 4GB を超える Pod は切り上げ換算（[ライセンス数量の数え方](./licensing-units.md)）。
3. **エディションの必要性** — SQL / GraphQL / 暗号化が要件でなければ Standard で足ります（[機能マトリクス](./edition-feature-matrix.md)）。
4. **ABAC / Private Preview 機能** — Premium にも含まれません。別途問い合わせが必要です。
5. **ScalarDL Auditor** — Ledger の導入と別管理ドメインへの配置が前提です。
6. **Analytics** — Pod ではなく SDBU。常時稼働を既定にせず実稼働時間で見積もる。Cluster 併用時は EE ライセンスが別途必要です。
7. **クラウド費用は含まない** — EKS / RDS / Databricks などお客様側のインフラ費用は別勘定です。
