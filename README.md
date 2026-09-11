# OKF-ScalarDB-ScalarDL

[![release](https://img.shields.io/github/v/release/wfukatsu/OKF-ScalarDB-ScalarDL)](https://github.com/wfukatsu/OKF-ScalarDB-ScalarDL/releases/latest)
[![OKF](https://img.shields.io/badge/OKF-v0.2-blue)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

ScalarDB / ScalarDL の公式ドキュメント（developers.scalar-labs.com）を、
**製品ごと・バージョンごと**に [OKF (Open Knowledge Format) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
のバンドルとしてまとめたものです。ScalarDB / ScalarDL を使う開発プロジェクトで、
AI に設計・実装・運用のコンテキストを与えるために使います。

## 現在の内容

| 製品 | 最新 | 収録バージョン | 概念数 |
|---|---|---|---|
| ScalarDB | 3.19 | 3.19, 3.18, 3.17, 3.16, 3.15, 3.14※ | 1,190 |
| ScalarDL | 3.14 | 3.14, 3.13, 3.12, 3.11, 3.10 | 692 |
| ScalarDB Saga | 3.19 | 3.19（未 GA / `3.19.0-alpha.1`） | 9 |
| ScalarDB Community | 3.13 | 3.13 〜 3.4 | 269 |

合計 **2,160 概念 / 22 バージョン**。
※ ScalarDB 3.14 は上流がドキュメントサイトから削除したため `archived` 扱いです（下記「バージョンの廃止」）。

これに加えて、上流ドキュメントには公開されていない**価格・ライセンス条件**を
`okf/pricing/` に収録しています（下記「価格・ライセンス」を参照）。

## 構成

```
okf/                                      ← OKF バンドルルート
├── index.md                              バンドル索引（okf_version: 0.2 を宣言）
├── log.md                                更新履歴
├── guides/
│   ├── how-ai-agents-use-this-bundle.md  ★ AI が最初に読むファイル
│   ├── product-and-version-selection.md  どのバージョンを参照するかの判断基準
│   └── bundle-maintenance.md             保守手順
├── pricing/                              ★ 上流ドキュメント由来ではない（手書き・定価のみ）
│   ├── index.md                          3 つの課金モデルとセクション索引
│   ├── licensing-units.md                1 Pod の定義・契約期間ごとの数量カウント
│   ├── scalardb-pricing.md               ScalarDB EE Standard / Premium の定価
│   ├── scalardl-pricing.md               ScalarDL Ledger / Auditor の定価
│   ├── scalardb-analytics-pricing.md     SDBU 従量課金 (Pay as you go)
│   ├── edition-feature-matrix.md         エディション別 機能・提供物マトリクス
│   └── sample-quotations.md              構成別サンプル見積（5 パターン）
└── products/
    ├── scalardb/
    │   ├── index.md                      製品概念（バージョン一覧・サポート状況）
    │   └── 3.19/ 3.18/ 3.17/ 3.16/ 3.15/ 3.14/
    │       ├── index.md                  バージョン概念＋フェーズ別ナビゲーション
    │       ├── <page>.md                 1 ドキュメントページ = 1 概念
    │       └── <section>/index.md        セクションの目次
    ├── scalardl/
    ├── scalardb-saga/                    ソースリポジトリ由来（ドキュメントサイト無し）
    │   └── 3.19/                         リリースブランチ = バージョン
    │       ├── overview.md               リポジトリ内 Markdown
    │       └── reference/                proto・設定テンプレート・saga 定義
    └── scalardb-community/

tools/                                    ジェネレータ（okf/ はここから再生成される）
.cache/                                   上流リポジトリのクローン（gitignore 済み）
.okf-state.json                            上流コミット SHA とバージョンごとの状態
```

## AI に使わせる

`okf/guides/how-ai-agents-use-this-bundle.md` を最初に読ませてください。
そこに「バージョンを跨いで回答しない」「エディションを確認する」といった
運用ルールと、フェーズ別のエントリポイントが書かれています。

各概念の frontmatter で絞り込めます。

```yaml
type: Development Guide          # Concept / Tutorial / Reference / Deployment Guide ...
product: scalardb
version: '3.17'
patch_version: 3.17.3            # そのドキュメントが記述する最新パッチ
lifecycle_phase: implement       # design | implement | operate
editions: [Community, Enterprise Standard, Enterprise Premium]
feature_status: [Public Preview]   # Deprecated / Private Preview / Public Preview（該当時のみ）
status: stable                   # unmaintained なバージョンは deprecated
resource: https://scalardb.scalar-labs.com/docs/3.17/api-guide/   # 正規 URL
sources:                         # 生成元 upstream コミットへのパーマリンク
  - resource: https://github.com/scalar-labs/docs-scalardb/blob/<sha>/...
```

`lifecycle_phase` は上流サイドバーの大分類（About / Quickstart / Develop /
Deploy / Manage / Migrate / Troubleshoot / Reference）から導出しています。

## 価格・ライセンス

`okf/pricing/` は、このバンドルで唯一**上流リポジトリを持たない**セクションです。
価格は developers.scalar-labs.com に公開されておらず、株式会社 Scalar の社内価格表
（ScalarDB / ScalarDL: 2024年7月1日版、ScalarDB Analytics: 2024年9月10日版）に由来します。

| 課金モデル | 対象製品 | 課金単位 |
|---|---|---|
| Pod 単位サブスクリプション | ScalarDB EE (Standard / Premium)、ScalarDL Ledger / Auditor | Pod / 期間（1 Pod = 2vCPU / 4GB Memory） |
| SDBU 時間単位の従量課金 (Pay as you go) | ScalarDB Analytics | SDBU・時間（最小 6 SDBU） |
| 無償 (OSS) | ScalarDB Community Edition | — |

### 公開範囲

収録しているのは、次の 3 つの**定価**だけです。

| 公開する | 内容 |
|---|---|
| **Pay as you go**（従量） | ScalarDB Analytics の SDBU・時間単価（¥33.5 / SDBU・時間） |
| **月額** | Pod 単位サブスクリプション 4 製品の 1ヶ月契約 定価 |
| **年額** | 同 4 製品の 1年契約 定価 |

次のものは**収録していません**。該当箇所は「非公開」と明記し、営業担当への問い合わせに誘導しています
（削除ではなく明記するのは、AI が欠落を推定で埋めないようにするためです）。

- 3年契約の定価および期間割引率
- 先払いクレジット (Prepaid Credit) の販売価格・割引率
- ボリューム割引を含む値引き条件、値引き後の実売価格
- 特定顧客向けの契約条件

> **取り扱い注意**
> 記載はすべて**定価（税抜・JPY）**です。実際のご提供価格は契約条件により調整されます。
> AI エージェントには**参考見積の材料**としてのみ使わせ、確定金額として提示させないでください。
> 社外に提出する見積は必ず営業担当のレビューを経てください。

このセクションは自動更新されません。更新手順は
[`okf/guides/bundle-maintenance.md`](./okf/guides/bundle-maintenance.md) の
「価格・ライセンスセクション」節を参照してください。

## 更新する

上流が新バージョンを切ったら、次を実行するだけで追加されます。

```bash
make update      # 未収録バージョンを追加し、最新版は毎回再生成
make build       # 全バージョンを作り直す
make offline     # ネットワークを使わず、キャッシュから作り直す
make validate    # OKF v0.2 適合性を検査
```

`okf/` 配下は生成物です。直接編集せず、`tools/` を編集してください。

GitHub Actions（`.github/workflows/update.yml`）が毎週月曜 09:00 JST に `make update` と
`make validate` を実行し、タイムスタンプ以外の差分があればプルリクエストを作成します。
Actions タブから手動実行も可能です。詳細は
[`okf/guides/bundle-maintenance.md`](./okf/guides/bundle-maintenance.md) の「定期自動更新」節を参照してください。

### バージョンの廃止（アーカイブ）

上流がドキュメントサイトからバージョンを削除しても、バンドルのディレクトリは残ります。
残っているものは生成時に自動で **`archived`** として扱われ、製品索引に理由つきで載り、
バージョンの `index.md` に注記が入り、概念数も合計に含まれます。手作業は不要です。

アーカイブ済みバージョンは `resource` のリンクが 404 します（上流にページが無いため）。
検証可能な出典は `sources[]` のコミットパーマリンクだけです。既存システムの調査にのみ使い、
新規設計の根拠にはしないでください。本当に不要なら、ディレクトリを削除して `make build` を実行します。
`okf/guides/` と `okf/pricing/` は手書きですが、実体は `tools/guides/` と
`tools/pricing/` にあり、生成時にコピーされます。

## 生成元と変換について

| 製品 | 上流リポジトリ | 種別 | 公開サイト |
|---|---|---|---|
| ScalarDB | `scalar-labs/docs-scalardb` | Docusaurus | https://scalardb.scalar-labs.com/docs/ |
| ScalarDL | `scalar-labs/docs-scalardl` | Docusaurus | https://scalardl.scalar-labs.com/docs/ |
| ScalarDB Community | `scalar-labs/docs-scalardb-community` | Docusaurus | https://scalardb-community.scalar-labs.com/docs/ |
| ScalarDB Saga | `scalar-labs/scalardb-saga` | ソースリポジトリ | （無し） |

developers.scalar-labs.com は前者 3 サイトへのハブで、実体はこの Docusaurus リポジトリ群です。
HTML をスクレイピングするのではなく、サイトの生成元である MDX を直接取り込んでいます。

上流は MDX なので、以下を平文 Markdown に展開しています。

- `import` した partial の実体埋め込み（`{props.x}` の解決を含む）
- MDX ローカルの React コンポーネント・JS ヘルパーの展開（node で式を評価）
- `<Tabs>` / `<TabItem>` → 太字ラベル付きの節
- `<JavadocLink>` → そのバージョンのパッチに固定した javadoc.io の URL
- `<CodeBlock>` → コードフェンス
- 相対リンク `foo.mdx` → バンドル内 `./foo.md`、バンドル外はドキュメントサイトの絶対 URL
- JSX 由来のインデント除去（Markdown ではコードブロックになるため）

変換の忠実性は、上流 225 万語に対して出力 235 万語（比 1.04、partial 展開分の増加）で確認済みです。
差分は frontmatter・`import` 文・JSX 属性といった非本文のみです。

ナビゲーション用コンポーネントのみのページやリダイレクトスタブ（全体で 14 ページ）は、
空概念になるため取り込まず、生成した `index.md` の目次が代わりになっています。

### ScalarDB Saga（ソースリポジトリ由来）

ScalarDB Saga はドキュメントサイトを持たないため、別経路（`tools/okf_repo.py`）で生成しています。

- **バージョン = リリースブランチ。** `^\d+\.\d+$` に一致するブランチ（現在は `3.19`）のみを
  取り込みます。`main` / 次期マイナーブランチは `-SNAPSHOT` の開発ラインなので対象外です。
- **概念にするファイルは `REPO_DOCS` に宣言。** サイドバーが無いため、リポジトリ内 Markdown
  （README / getting-started / server イメージ）に加え、契約そのものであるファイル
  （`saga.proto`・`admin.proto`・`server.properties` テンプレート・saga 定義の実例）を
  Reference 概念として出力します。リリース手順（`RELEASING.md`）は成果物の座標・ブランチモデル・
  公開イメージの署名検証を含むため取り込んでいます。上流の `CLAUDE.md`（本体開発の規約）も
  収録していますが、利用者側の規約と取り違えられないよう `contributor` タグと
  本文冒頭の注記を付けています。
- **`resource` は生成元コミットに固定した GitHub blob URL。** リポジトリ内リンクは、
  概念になっているファイルならバンドル内相対パスへ、それ以外は同じコミットの GitHub URL へ
  書き換えます。
- **GA 前のラインは `status: draft` + `prerelease: true` + `pre-release` タグ。**

## ライセンス

[Apache License 2.0](./LICENSE)。`okf/products/` 配下のコンテンツは
[scalar-labs/docs-scalardb](https://github.com/scalar-labs/docs-scalardb) /
[scalar-labs/docs-scalardl](https://github.com/scalar-labs/docs-scalardl) /
[scalar-labs/docs-scalardb-community](https://github.com/scalar-labs/docs-scalardb-community) /
[scalar-labs/scalardb-saga](https://github.com/scalar-labs/scalardb-saga)
（いずれも Apache-2.0）から機械変換した派生物です。各概念の `sources[]` に
生成元コミットへのパーマリンクを保持しています。

`okf/pricing/` 配下は上流ドキュメントの派生物ではなく、株式会社 Scalar の社内価格表を
出典とする手書きのコンテンツです。Apache-2.0 の対象外として扱ってください。

## 既知の制限

- **英語版のみ。** 上流には日本語訳（`i18n/versioned_docs/ja-jp/`）もありますが、
  訳は英語版に遅れる場合があるため、正典である英語版のみを取り込んでいます。
- **画像は取り込んでいません。** 画像リンクはドキュメントサイトの絶対 URL に書き換えてあります。
- `<VERSION>` `<NAMESPACE>` のようなプレースホルダは原文どおり残しています。
- 上流サイドバーに載っていない 54 概念（全体の 3%）は `type: Documentation Page` に
  フォールバックしています。内容は完全です。
- **ScalarDB Saga は未 GA。** 収録しているのはアルファ（`3.19.0-alpha.1`）の内容であり、
  API・設定キー・ワイヤ契約は変わり得ます。また REST API に OpenAPI 定義が上流に無いため、
  REST の網羅的なリファレンスはありません（gRPC の proto と getting-started の
  `curl` 例が根拠になります）。ライセンス/エディション区分も上流で宣言されていないため
  `editions` は付いていません。
- **価格情報は自動更新されない。** `okf/pricing/` は社内価格表を手で書き起こしたもので、
  上流の再生成対象ではありません。価格表が改版されても `make update` では追随しないため、
  `price_list_version` を確認してから使ってください。
- **価格は Pay as you go / 月額 / 年額 の定価のみ。** 3年契約の定価、先払いクレジットの
  販売価格、値引き条件は収録していません（上記「公開範囲」）。バンドルに無い価格を
  推定・逆算で埋めないでください。
