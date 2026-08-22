---
type: Pricing Reference
title: ScalarDL 価格表
description: ScalarDL Ledger / Auditor の Pod 単位の定価と、Auditor を見積もる際の前提条件。
tags: [pricing, scalardl, ledger, auditor]
status: stable
product: scalardl
currency: JPY
tax: excluded
price_basis: list-price
price_unit: Pod / 期間
price_list_version: '2024-07-01'
sources:
- id: scalar-price-list-2024-07-01
  access: internal (Google Drive / Scalar 社内)
  title: Scalar 製品価格表 — シート「価格表」
  author: org:scalar-labs
  last_modified: '2026-08-06T14:55:57Z'
---

# ScalarDL 価格表

価格単位: **Pod / 期間** ｜ 1 Pod = 2vCPU / 4GB Memory ｜ 金額は**税抜の定価**（JPY）

Pod 数の数え方は [ライセンス数量の数え方](./licensing-units.md) を参照してください。

## ScalarDL Ledger

| 契約期間 | 定価 (JPY) | 参考 (USD) | 月額換算 (JPY) | 定価比 割引率 |
|---|---|---|---|---|
| 1ヶ月 | ¥100,000 | $833.33 | ¥100,000 | — |
| 1年 | ¥1,140,000 | $9,500.00 | ¥95,000 | 5.0% OFF |
| 3年 | 非公開 | 非公開 | 非公開 | 非公開 |

**含まれるもの**

- ScalarDL Ledger (BYOL) コンテナイメージ
- Java Client SDK（HashStore・TableStore クライアント SDK を含む）
- 改ざん検知機能を持つ台帳（Ledger）

## ScalarDL Auditor

| 契約期間 | 定価 (JPY) | 参考 (USD) | 月額換算 (JPY) | 定価比 割引率 |
|---|---|---|---|---|
| 1ヶ月 | ¥100,000 | $833.33 | ¥100,000 | — |
| 1年 | ¥1,140,000 | $9,500.00 | ¥95,000 | 5.0% OFF |
| 3年 | 非公開 | 非公開 | 非公開 | 非公開 |

**含まれるもの**

- ScalarDL Auditor (BYOL) コンテナイメージ

**前提条件（見積時に必ず確認）**

- **ScalarDL Ledger の導入が前提**です。Auditor 単独では成立しません。
- Auditor は Ledger と**別の管理ドメイン（別アカウント / 別クラスタ）に配置する必要があります**。
  同一クラスタに同居させる構成は Auditor の前提を満たしません。

## エディション区分

ScalarDL には ScalarDB のような**エディション別の機能マトリクスはありません**。
Ledger / Auditor の**コンポーネント単位**でライセンスされます。

| コンポーネント | Community | Enterprise | 備考 |
|---|---|---|---|
| ScalarDL Ledger | ○ | — | Community 版コンテナイメージ |
| ScalarDL Ledger (BYOL) | — | ○ | 商用ライセンス（**課金対象**） |
| ScalarDL Auditor (BYOL) | — | ○ | 商用ライセンス（**課金対象**）。Ledger の導入が前提 |

ライブラリ / ツール（Java Client SDK、HashStore / TableStore SDK、Client Command、
Schema Loader、Helm Charts、Scalar Admin for Kubernetes）は Community / Enterprise の
いずれでも提供されます。詳細は [エディション別 機能・提供物マトリクス](./edition-feature-matrix.md) を参照してください。

## 注記

- 本バンドルが収録するのは **Pay as you go / 月額 / 年額 の定価のみ**です。
  3年契約の定価は非公開のため、営業担当にお問い合わせください。
- 本価格表は**定価**です。実際のご提供価格はボリューム・契約条件により調整されます。
- USD 換算は参考値です（換算レート 1 USD = 120 JPY）。
