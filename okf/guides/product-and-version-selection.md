---
type: Decision Guide
title: 製品・エディション・バージョンの選び方
description: どの products/<product>/<version>/ を参照すべきかを決めるための判断基準。
tags: [guides, version-selection]
status: stable
---

# 製品・エディション・バージョンの選び方

## 製品

| バンドル内キー | 製品 | 使う場面 |
|---|---|---|
| `scalardb` | ScalarDB | 現行の ScalarDB 全般。Core ライブラリ、Cluster、SQL/GraphQL、Analytics、Data Loader を含む。**新規プロジェクトは原則こちら。** |
| `scalardl` | ScalarDL | 改竄検知・実行証明が要件にある場合。Ledger / Auditor、Contract / Function。 |
| `scalardb-saga` | ScalarDB Saga | **サービス間**の結果整合トランザクションを補償（Saga / TCC）で調整する場合。saga 状態は ScalarDB 経由で永続化され、メッセージブローカは不要。**未 GA（アルファ）。** |
| `scalardb-community` | ScalarDB Community | 3.13 以前の Community 版のみを対象とした旧ドキュメント。既存システムの調査用。新規では使わない。 |

ScalarDB と ScalarDL を併用する構成では、両方の対応バージョンが噛み合うかを
それぞれの `requirements` / `compatibility` 概念で確認してください。

### ScalarDB の 2PC と ScalarDB Saga の使い分け

| | ScalarDB（2PC を含む） | ScalarDB Saga |
|---|---|---|
| 一貫性 | 強一貫（ACID） | 結果整合（補償でロールバック） |
| 適用範囲 | 複数データベース間、複数サービス間（2PC） | 複数サービス間 |
| ロールバック | トランザクションのアボート | 逆順の補償ステップ実行 |
| ステップへの要求 | — | **冪等であること**（記録前に中断したステップは再実行される） |
| 障害時 | 参加者を同期的に拘束する | 別レプリカが引き取り終端状態まで駆動する |

即時の一貫性が正しさの要件なら ScalarDB のトランザクション（必要なら 2PC）を、
補償付きの結果整合で足りるなら ScalarDB Saga を選びます。両者は排他ではなく、
1 つのサービス内は ScalarDB のトランザクション、サービスを跨ぐ調整は Saga、
という組み合わせが典型です。

## バージョンの決め方

1. **既存プロジェクト** — 実際に動いている ScalarDB / ScalarDL のバージョンに合わせる。
   `build.gradle` / `pom.xml` の `com.scalar-labs` 依存、または Helm chart の
   `image.tag` から特定できます。マイナーバージョン（例 `3.17`）が
   `products/<product>/<version>/` に対応します。
2. **新規プロジェクト** — `maintenance: supported` かつ最新のバージョンを選ぶ。
   各製品の `index.md` の表で確認できます。
3. **移行検討** — 移行元と移行先の両方の `releases/release-notes.md` を突き合わせる。

`status: deprecated` / `maintenance: unmaintained` のバージョンは、
既存システムの現状把握には使えますが、新規設計の根拠にはしないでください。

### ScalarDB Saga のバージョン

ScalarDB Saga はドキュメントサイトを持たず、**マイナーリリースライン = リポジトリの
ブランチ**です。バンドルの `products/scalardb-saga/3.19/` はブランチ `3.19` に対応します。
プロジェクト側では `com.scalar-labs:scalardb-saga-*` の依存バージョン、または
`ghcr.io/scalar-labs/scalardb-saga-server` のイメージタグで特定できます。

- `main` や次期マイナーブランチは `-SNAPSHOT` を積むだけの開発ラインなので、
  バンドルには入れていません。
- GA リリースが無いラインは `status: draft` / `prerelease: true` /
  `pre-release` タグが付きます。`patch_version`（例 `3.19.0-alpha.1`）が
  そのブランチがビルドするリリースです。**本番採用の根拠にする前に、
  現時点のリリース状況を必ず確認してください。**

## エディション

各概念は frontmatter の `editions` に、その内容が適用されるエディションを持ちます。

| エディション | 製品 | 位置づけ |
|---|---|---|
| `Community` | ScalarDB / ScalarDL | OSS。 |
| `Enterprise Standard` | ScalarDB | 商用。Cluster などを含む。 |
| `Enterprise Premium` | ScalarDB | 商用上位。Analytics、SQL インターフェースなどを含む。 |
| `Enterprise Premium Option` | ScalarDB | Premium への追加オプション機能。 |
| `Enterprise` / `Enterprise Option` | ScalarDL | ScalarDL の商用エディションとそのオプション。 |

ScalarDB Saga の概念には `editions` が付きません。ライセンス区分が
ドキュメント上で宣言されていないためで、「エディション制限が無い」という意味では
ありません。採用判断の前に確認してください。

タグ形式では `edition:community` / `edition:enterprise-standard` のように
`tags` にも入っています。

エディションとは別に、機能のリリース段階は `feature_status` に入ります
（`Private Preview` / `Public Preview` / `Deprecated`）。
`feature_status: [Deprecated]` の付いた機能は新規設計で使わないでください。
Preview 段階の機能は本番投入前に SLA 対象かを確認してください。

**判断の順序:** プロジェクトが契約しているエディションを先に確定し、
そのエディションで使えない機能は提案しない。エディションが不明な場合は、
機能を提案する前にその旨を明示して確認してください。

## よくある取り違え

- **ScalarDB Core ライブラリ と ScalarDB Cluster** — 設定も API も異なります。
  対象がどちらかを確定してから設定キーを引くこと。
- **`scalardb` と `scalardb-community`** — 3.13 以降の内容は `scalardb` 側にのみあります。
  `scalardb-community` を新しいバージョンの根拠に使わないこと。
- **ScalarDB Saga と ScalarDB の 2PC** — どちらも「サービスを跨ぐトランザクション」に
  見えますが、一貫性モデルが違います。上の使い分け表で先に確定すること。
- **ドキュメントバージョンとパッチバージョン** — ディレクトリ名は
  マイナーバージョン（`3.17`）ですが、frontmatter の `patch_version`
  （`3.17.3` など）がそのドキュメントが記述する最新パッチです。
  依存バージョンを書くときはこちらを使ってください。
