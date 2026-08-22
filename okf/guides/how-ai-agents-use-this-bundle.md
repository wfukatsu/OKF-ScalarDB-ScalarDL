---
type: Operating Instructions
title: AI エージェント向け利用ガイド
description: ScalarDB / ScalarDL を使う開発プロジェクトで、設計・実装・運用の各フェーズにこのバンドルをどう引くかの手順。
tags: [guides, ai-agent, entrypoint]
status: stable
---

# AI エージェント向け利用ガイド

このバンドルは **ScalarDB / ScalarDL を使う開発プロジェクトのコンテキスト供給源**です。
コードを書く前に、必ず「どの製品の、どのバージョンを対象にしているか」を確定させてから読み込んでください。

## 鉄則

1. **バージョンを跨いで回答しない。** 設定キー名、エラーコード、API シグネチャは
   マイナーバージョン間で変わります。`products/<product>/<version>/` を 1 つ選び、
   その配下だけを根拠にすること。
2. **エディションを確認する。** 各概念の frontmatter にある `editions` は、その機能が
   Community / Enterprise Standard / Enterprise Premium のどれで使えるかを示します。
   Enterprise 限定機能を Community 前提のプロジェクトに提案しないこと。
3. **推測しない。** バンドル内に根拠が無い場合は「ドキュメントに記載が無い」と述べ、
   `resource` の URL を提示して確認を促すこと。
4. **`status: deprecated` の概念は設計判断の根拠にしない。** 既存システムの調査目的でのみ使う。
5. **価格を確定金額として提示しない。** `pricing/` 配下は上流ドキュメントではなく
   社内価格表由来の**定価**です。参考見積の材料としてのみ使い、確定金額・提出可能な
   見積として出力しないこと。詳細は下の「価格・ライセンスを引くとき」を参照。
6. **`status: draft` の概念は未 GA。** `prerelease: true` / `pre-release` タグが付いた
   バージョン（現時点では ScalarDB Saga 3.19 = `3.19.0-alpha.1`）は、API・設定キー・
   ワイヤ契約が変わり得ます。提案する際は必ず「未 GA である」と明示すること。

## 読み込み手順

### Step 1 — 対象を確定する

```
okf/products/<product>/index.md
```

`scalardb` / `scalardl` / `scalardb-saga` / `scalardb-community` の 4 製品があります。
バージョン一覧・最新版・サポート状況が表になっています。
判断基準は [製品・エディション・バージョンの選び方](./product-and-version-selection.md) を参照。

`scalardb-saga` だけはドキュメントサイトを持たず、ソースリポジトリ内の
ドキュメントと契約ファイル（proto、設定テンプレート、saga 定義）から生成されています。
バージョンはリリースブランチ（`3.19`）に対応します。

### Step 2 — バージョンのハブを読む

```
okf/products/<product>/<version>/index.md
```

このファイルには全概念がライフサイクルフェーズ別（設計 / 実装 / 運用）に列挙されています。
まずここを読み、必要な概念だけを開いてください。全ページを読み込む必要はありません。

### Step 3 — フェーズに対応する概念を引く

frontmatter の `lifecycle_phase` と `type` で絞り込めます。

| フェーズ | `lifecycle_phase` | 主な `type` | 典型的な用途 |
|---|---|---|---|
| 設計 | `design` | `Concept` | データモデリング、トランザクション境界、Consensus Commit の性質、制約の確認 |
| 実装 | `implement` | `Tutorial`, `Development Guide`, `Reference`, `Sample Application` | API の正しい使い方、設定値、例外処理、サンプルコード |
| 運用 | `operate` | `Deployment Guide`, `Operations Guide`, `Migration Guide`, `Troubleshooting`, `Release Notes` | Kubernetes へのデプロイ、バックアップ/リストア、監視、エラーコード対応 |

### Step 4 — 概念間をたどる

各概念は通常の Markdown リンクで相互接続されています。リンク先が同じバンドル内なら
相対パス（`./api-guide.md`）、バンドル外ならドキュメントサイトの絶対 URL になっています。

## フェーズ別の推奨エントリポイント

以下は ScalarDB の例です。ScalarDL でも同名/類似の概念があります。

**設計フェーズ**
- `design.md` — アーキテクチャと構成要素
- `data-modeling.md` — データモデル設計
- `consensus-commit.md` — トランザクションプロトコルの正確な性質（分離レベル、制約）
- `requirements.md` — 対応データベースとバージョン要件
- `glossary.md` — 用語の統一

**実装フェーズ**
- `getting-started-with-scalardb.md` — 最小構成の動作確認
- `api-guide.md` — CRUD / トランザクション API と例外処理
- `configurations.md` — 設定キーの一覧
- `scalardb-samples/` — 動作するサンプルアプリケーション

**運用フェーズ**
- `scalar-kubernetes/`, `helm-charts/` — デプロイ
- `backup-restore.md` — バックアップとリストア
- `scalar-manager/` — 監視・運用ツール
- `*-error-codes.md` — エラーコードから原因への逆引き
- `releases/release-notes.md` — バージョン間の差分

ScalarDB Saga（`products/scalardb-saga/<version>/`）は構成が異なり、次の 9 概念だけです。

- `overview.md` — Saga / TCC、サーバモードと組み込みモード、成果物一覧（設計）
- `getting-started.md` — Docker Compose で動かすチュートリアル（実装）
- `reference/saga-definitions.md` — saga 定義の実例（宣言的サービスステップと `stepClass`）（実装）
- `reference/grpc-saga-api.md` — `SagaService` の gRPC 契約（実装）
- `server-deployment.md` — サーバイメージの実行、ヘルスチェック、graceful shutdown（運用）
- `reference/server-configuration.md` — `scalar.db.saga.server.*` 設定キーと既定値の全量（運用）
- `reference/grpc-admin-api.md` — 運用者向け `AdminService`（運用）
- `releasing.md` — リリース手順。公開される成果物の座標（Maven Central / GHCR）、
  ブランチモデル、公開イメージの署名検証方法（運用）
- `contributing-conventions.md` — **ScalarDB Saga 本体に手を入れる場合**の規約
  （Java/Gradle、コードスタイル、静的解析、パッケージ命名、テスト方針）。
  タグ `contributor` / `upstream-development` が付いています。
  **Saga を利用するアプリケーション側の実装規約として適用しないこと。**

## 価格・ライセンスを引くとき

```
okf/pricing/index.md
```

`products/` 配下（上流ドキュメント由来）とは**出典が異なる**セクションです。
価格は developers.scalar-labs.com には公開されておらず、株式会社 Scalar の社内価格表に由来します。

- **収録しているのは Pay as you go / 月額 / 年額 の定価のみ**です（税抜・JPY）。
  3年契約の定価、先払いクレジットの販売価格、値引き条件は**収録していません**。
  これらを問われたら「本バンドルの公開範囲外」と答え、営業担当への確認を促すこと。
  **推定・按分・逆算で埋めないこと**（例: 年額から 3年額を推測しない）。
- 実際のご提供価格はボリューム・契約条件により調整されます。
- 概算・比較・エディション選定の材料としては使えます。**確定金額として提示しないこと。**
  提出する見積は必ず営業担当のレビューを経てください。
- 価格表の版（`price_list_version`）を必ず添えて回答すること。
  `products/` と違い**自動再生成されません**ので、古い版を根拠にしている可能性があります。

引く順序:

1. [価格・ライセンス](../pricing/index.md) — 3 つの課金モデルのどれに当たるかを先に確定する
2. [エディション別 機能・提供物マトリクス](../pricing/edition-feature-matrix.md) — 要件からエディションを決める
3. [ライセンス数量の数え方](../pricing/licensing-units.md) — Pod 数を換算する（2vCPU / 4GB を超える Pod は切り上げ）
4. 製品別の価格表 — [ScalarDB](../pricing/scalardb-pricing.md) / [ScalarDL](../pricing/scalardl-pricing.md) / [Analytics](../pricing/scalardb-analytics-pricing.md)
5. [サンプル見積（5 パターン）](../pricing/sample-quotations.md) — 試算の型として使う

よくある誤り:

- **2vCPU / 4GB を超える Pod を 1 Pod として数える。** 換算式は
  `MAX(ceil(vCPU÷2), ceil(memGB÷4))` です。
- **ScalarDB Analytics を Pod 単位で見積もる。** Analytics は SDBU 時間単位の従量課金です。
- **ライブラリが配布されている＝機能が使える、と判断する。** 例: ScalarDB SQL ライブラリは
  Enterprise Standard にも配布されますが、SQL インターフェース機能は Enterprise Premium が対象です。
- **ABAC を Premium に含める。** Enterprise Premium **Option** であり、Premium には含まれません。
- **ScalarDL Auditor を単独で見積もる。** Ledger の導入と別管理ドメインへの配置が前提です。
- **Private Preview 機能を本番前提で見積もる。**
- **公開範囲外の価格を推定して答える。** 3年契約・先払いクレジット・値引き条件は
  バンドルに存在しません。無い値を作らないこと。

## コード生成時の注意

- **例外処理を省略しない。** ScalarDB のトランザクション API は
  `UnknownTransactionStatusException` を含む複数の例外を投げ、
  それぞれリトライ可否が異なります。`api-guide.md` の該当節を必ず根拠にすること。
- **設定キーはリファレンスからそのまま引く。** 記憶で書かない。
- **Javadoc リンクはバージョン固定済み。** 本文中の Javadoc リンクは、その
  ドキュメントバージョンのパッチリリース（frontmatter の `patch_version`）に解決済みです。
- **2PC（`two-phase-commit-transactions.md`）はマイクロサービス跨ぎのみ。**
  単一サービス内で使わないこと。
- **ScalarDB の 2PC と ScalarDB Saga を取り違えない。** 2PC はサービスを跨いでも
  強一貫（ACID）を保つ代わりに参加者を同期的に拘束します。ScalarDB Saga は
  補償による結果整合であり、ステップは冪等である必要があります。
  「即時の一貫性が正しさの要件か」で先に選び分けること。
- **ScalarDB Saga のコードステップ（`stepClass`）は組み込みモード専用。**
  サーバモードの定義に書くと起動時に拒否されます。

## 引用の作法

回答に根拠を示すときは、概念の frontmatter にある `resource`（ドキュメントサイトの正規 URL）を
引用してください。`sources[].resource` は生成元の upstream コミットへのパーマリンクで、
「いつ時点の内容か」を検証する用途に使えます。
