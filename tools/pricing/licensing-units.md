---
type: Licensing Reference
title: ライセンス数量の数え方（1 Pod の定義・契約期間）
description: 課金単位「1 Pod = 2vCPU / 4GB Memory」の換算式と、契約期間ごとのライセンス Pod 数のカウント方法。
tags: [pricing, licensing, pod, contract-term, scalardb, scalardl]
status: stable
currency: JPY
tax: excluded
price_basis: list-price
price_list_version: '2024-07-01'
resource: https://docs.google.com/spreadsheets/d/11JYhx_cz8TbTopHbcoRvEHDhgEnvVYkud--qFnw9G7A/edit
sources:
- id: scalar-price-list-2024-07-01
  resource: https://docs.google.com/spreadsheets/d/11JYhx_cz8TbTopHbcoRvEHDhgEnvVYkud--qFnw9G7A/edit
  title: Scalar 製品価格表 — シート「注釈・前提条件」
  author: org:scalar-labs
  last_modified: '2026-08-06T14:55:57Z'
---

# ライセンス数量の数え方（1 Pod の定義・契約期間）

Pod 単位サブスクリプション（ScalarDB Enterprise Edition、ScalarDL Ledger / Auditor）に共通するルールです。
ScalarDB Analytics は Pod 単位ではないので、[ScalarDB Analytics 価格表](./scalardb-analytics-pricing.md) を参照してください。

## 1 Pod の定義

| 項目 | 値 |
|---|---|
| 1 ライセンス Pod あたりの vCPU | **2 vCPU** |
| 1 ライセンス Pod あたりのメモリ | **4 GB** |
| 端数処理 | 常に**切り上げ** |

Pod のサイズがこれを超える場合は、vCPU 基準とメモリ基準のうち**大きい方**でライセンス Pod 数を計算します。

```
ライセンス Pod 数 = MAX( ceil(実 vCPU 数 ÷ 2) , ceil(実メモリ GB ÷ 4) )
```

### 換算例

上の式から導かれる計算例です（価格表の換算ルールに基づく算出値）。

| 実 Pod の vCPU | 実 Pod のメモリ | vCPU 基準 (÷2 切上) | メモリ基準 (÷4 切上) | ライセンス Pod 数 |
|---|---|---|---|---|
| 2 vCPU | 4 GB | 1 | 1 | **1** |
| 2 vCPU | 8 GB | 1 | 2 | **2** |
| 4 vCPU | 8 GB | 2 | 2 | **2** |
| 4 vCPU | 16 GB | 2 | 4 | **4** |
| 3 vCPU | 6 GB | 2 | 2 | **2** |
| 8 vCPU | 16 GB | 4 | 4 | **4** |

**注意:** 実行時の Pod 数ではなく、**リソース量から換算したライセンス Pod 数**が課金対象です。
2vCPU / 4GB を超える Pod を 1 Pod として見積もるのは誤りです。

### vCPU の定義

vCPU とは仮想 CPU を指します。

- Kubernetes を利用する場合 — Kubernetes に設定する `cpu` に相当します。
  Kubernetes における 1 CPU は、クラウドプロバイダーの 1 vCPU / コア、
  およびベアメタルの Intel プロセッサーの 1 ハイパースレッドに相当します。
- AWS / Azure の場合 — vCPU に相当します。
  AWS では各 vCPU は CPU コアのスレッドです（T2 インスタンスおよび AWS Graviton2 プロセッサ搭載インスタンスを除く）。

参考:
- https://kubernetes.io/ja/docs/concepts/configuration/manage-resources-containers/
- https://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/instance-optimize-cpu.html

## 契約期間と Pod 数のカウント

契約期間によって「何を数えるか」が変わります。

| 契約期間 | カウント対象 |
|---|---|
| 月額契約 | 契約期間中の**最大ピーク時**の Pod 数 |
| 年額契約 | 契約期間を通じて**同時に起動できる最大 Pod 数** |

年額契約では、契約 Pod 数の範囲内であればいつでも自由に Pod を起動・停止できます。
特定の月だけ契約 Pod 数を超過する場合は、**超過分を月額契約で追加**します。

### 超過分の追加例

年契約 3 Pod で、月ごとの起動 Pod 数が次のようになる場合:

| 月 | 1月 | 2月 | 3月 | 4月 | 5月 | 6月 | 7月〜12月 |
|---|---|---|---|---|---|---|---|
| 起動 Pod 数 | 1 | 1 | 3 | 4 | 4 | 5 | 3 |
| 年契約超過分 | — | — | — | +1 | +1 | +2 | — |

3 Pod を超える 4月（+1 Pod）、5月（+1 Pod）、6月（+2 Pod）について、それぞれ月額契約を追加します
（合計 **4 Pod・月**ぶんの月額契約）。

## 契約期間と月額換算

| 契約期間 | 月額換算（Standard / Ledger / Auditor） | 月額換算（Premium） |
|---|---|---|
| 1ヶ月 | ¥100,000 | ¥200,000 |
| 1年 | ¥95,000 | ¥190,000 |

年額契約は月額契約に対して 5.0% 有利になります。Pod 単位サブスクリプションの 4 製品
（ScalarDB EE Standard / Premium、ScalarDL Ledger / Auditor）に共通です。

**3年契約も提供していますが、その定価は本バンドルの公開範囲外です。**
長期契約を前提とする見積が必要な場合は営業担当にお問い合わせください。

## その他の前提

- **ScalarDL Auditor は ScalarDL Ledger の導入が前提**です。また Auditor は Ledger と
  **別の管理ドメイン（別アカウント / 別クラスタ）に配置する必要があります**。
  Auditor だけを見積もることはできません。
- 本バンドルが収録するのは **Pay as you go / 月額 / 年額 の定価のみ**です。
  3年契約の定価、先払いクレジットの販売価格、値引き条件は含みません。
- 本価格表は**定価**です。実際のご提供価格はボリューム・契約条件により調整されます。
- 金額は**税抜**表示です。
- USD 換算は参考値です（換算レート 1 USD = 120 JPY）。
