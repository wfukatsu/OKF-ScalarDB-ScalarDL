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
5. **`status: draft` の概念は未 GA。** `prerelease: true` / `pre-release` タグが付いた
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

ScalarDB Saga（`products/scalardb-saga/<version>/`）は構成が異なり、次の 7 概念だけです。

- `overview.md` — Saga / TCC、サーバモードと組み込みモード、成果物一覧（設計）
- `getting-started.md` — Docker Compose で動かすチュートリアル（実装）
- `reference/saga-definitions.md` — saga 定義の実例（宣言的サービスステップと `stepClass`）（実装）
- `reference/grpc-saga-api.md` — `SagaService` の gRPC 契約（実装）
- `server-deployment.md` — サーバイメージの実行、ヘルスチェック、graceful shutdown（運用）
- `reference/server-configuration.md` — `scalar.db.saga.server.*` 設定キーと既定値の全量（運用）
- `reference/grpc-admin-api.md` — 運用者向け `AdminService`（運用）

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
