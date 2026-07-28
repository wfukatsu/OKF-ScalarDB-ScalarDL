# OKF-ScalarDB-ScalarDL

ScalarDB / ScalarDL の公式ドキュメント（developers.scalar-labs.com）を、
**製品ごと・バージョンごと**に [OKF (Open Knowledge Format) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
のバンドルとしてまとめたものです。ScalarDB / ScalarDL を使う開発プロジェクトで、
AI に設計・実装・運用のコンテキストを与えるために使います。

## 現在の内容

| 製品 | 最新 | 収録バージョン | 概念数 |
|---|---|---|---|
| ScalarDB | 3.18 | 3.18, 3.17, 3.16, 3.15, 3.14 | 983 |
| ScalarDL | 3.13 | 3.13, 3.12, 3.11, 3.10 | 548 |
| ScalarDB Community | 3.13 | 3.13 〜 3.4 | 269 |

合計 **1,800 概念 / 19 バージョン**（`okf/` 配下、2,048 ファイル）。

## 構成

```
okf/                                      ← OKF バンドルルート
├── index.md                              バンドル索引（okf_version: 0.2 を宣言）
├── log.md                                更新履歴
├── guides/
│   ├── how-ai-agents-use-this-bundle.md  ★ AI が最初に読むファイル
│   ├── product-and-version-selection.md  どのバージョンを参照するかの判断基準
│   └── bundle-maintenance.md             保守手順
└── products/
    ├── scalardb/
    │   ├── index.md                      製品概念（バージョン一覧・サポート状況）
    │   └── 3.18/ 3.17/ 3.16/ 3.15/ 3.14/
    │       ├── index.md                  バージョン概念＋フェーズ別ナビゲーション
    │       ├── <page>.md                 1 ドキュメントページ = 1 概念
    │       └── <section>/index.md        セクションの目次
    ├── scalardl/
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

## 更新する

上流が新バージョンを切ったら、次を実行するだけで追加されます。

```bash
make update      # 未収録バージョンを追加し、最新版は毎回再生成
make build       # 全バージョンを作り直す
make offline     # ネットワークを使わず、キャッシュから作り直す
make validate    # OKF v0.2 適合性を検査
```

`okf/` 配下は生成物です。直接編集せず、`tools/` を編集してください。

## 生成元と変換について

| 製品 | 上流リポジトリ | 公開サイト |
|---|---|---|
| ScalarDB | `scalar-labs/docs-scalardb` | https://scalardb.scalar-labs.com/docs/ |
| ScalarDL | `scalar-labs/docs-scalardl` | https://scalardl.scalar-labs.com/docs/ |
| ScalarDB Community | `scalar-labs/docs-scalardb-community` | https://scalardb-community.scalar-labs.com/docs/ |

developers.scalar-labs.com はこれら 3 サイトへのハブで、実体はこの Docusaurus リポジトリ群です。
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

## ライセンス

[Apache License 2.0](./LICENSE)。`okf/products/` 配下のコンテンツは
[scalar-labs/docs-scalardb](https://github.com/scalar-labs/docs-scalardb) /
[scalar-labs/docs-scalardl](https://github.com/scalar-labs/docs-scalardl) /
[scalar-labs/docs-scalardb-community](https://github.com/scalar-labs/docs-scalardb-community)
（いずれも Apache-2.0）から機械変換した派生物です。各概念の `sources[]` に
生成元コミットへのパーマリンクを保持しています。

## 既知の制限

- **英語版のみ。** 上流には日本語訳（`i18n/versioned_docs/ja-jp/`）もありますが、
  訳は英語版に遅れる場合があるため、正典である英語版のみを取り込んでいます。
- **画像は取り込んでいません。** 画像リンクはドキュメントサイトの絶対 URL に書き換えてあります。
- `<VERSION>` `<NAMESPACE>` のようなプレースホルダは原文どおり残しています。
- 上流サイドバーに載っていない 54 概念（全体の 3%）は `type: Documentation Page` に
  フォールバックしています。内容は完全です。
