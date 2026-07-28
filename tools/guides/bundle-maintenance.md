---
type: Runbook
title: バンドルの保守手順
description: 新しい製品バージョンが出たときにこのバンドルへ追加する手順と、生成の仕組み。
tags: [guides, maintenance, runbook]
status: stable
---

# バンドルの保守手順

このバンドルは手書きではなく、上流ドキュメントリポジトリから**再生成**されます。
`okf/` 配下を直接編集しないでください（次回生成で上書きされます）。
編集すべきは `tools/` 配下です。

## 生成元

| 製品 | リポジトリ | 公開先 |
|---|---|---|
| ScalarDB | `scalar-labs/docs-scalardb` | https://scalardb.scalar-labs.com/docs/ |
| ScalarDL | `scalar-labs/docs-scalardl` | https://scalardl.scalar-labs.com/docs/ |
| ScalarDB Community | `scalar-labs/docs-scalardb-community` | https://scalardb-community.scalar-labs.com/docs/ |

これらは developers.scalar-labs.com から辿れる公式ドキュメントサイトの生成元です。
上流は Docusaurus の MDX なので、生成時に以下を平文 Markdown へ展開しています。

- `import` した partial の実体埋め込み（`{props.x}` の置換を含む）
- `<Tabs>` / `<TabItem>` → 太字ラベル付きの節
- `<JavadocLink>` → そのバージョンのパッチリリースに固定した Javadoc URL
- `<CodeBlock>` → コードフェンス
- 相対リンク `foo.mdx` → バンドル内の `./foo.md`、バンドル外はドキュメントサイトの絶対 URL

## 新しいバージョンが出たとき

上流がバージョンを切ると `versioned_docs/version-<新バージョン>/` と
`docusaurus.config.js` の `versions` エントリが増えます。次を実行するだけで取り込まれます。

```bash
make update      # = python3 tools/okf_build.py --only-new
```

`--only-new` は次の動作をします。

- 上流リポジトリを fetch して最新化する
- `.okf-state.json` に無いバージョンだけを新規生成する
- 併せて **最新版（`is_latest: true`）は常に再生成する**（開発中バージョンは内容が動くため）
- 既存の安定版バージョンはそのまま残す
- `okf/log.md` に実行履歴を追記し、`.okf-state.json` を更新する

全バージョンを作り直したい場合:

```bash
make build       # = python3 tools/okf_build.py
```

特定のものだけ:

```bash
python3 tools/okf_build.py --products scalardb --versions 3.18
```

ネットワークを使わず、キャッシュ済みクローンから作り直す場合:

```bash
python3 tools/okf_build.py --offline
```

## 生成後の確認

```bash
make validate    # = python3 tools/okf_validate.py
```

OKF v0.2 の適合性（全ての非予約 `.md` に frontmatter があり `type` が空でないこと、
予約ファイルの構造、バンドル内リンクの解決可否）を検査します。

## バージョンの廃止

上流が古いバージョンを削除した場合、そのディレクトリはバンドルに残り続けます。
不要になったら手動で削除し、`.okf-state.json` の該当エントリも消してください。
既存システムの調査用に残す場合は、`status: deprecated` が付いているのでそのままで問題ありません。

## 状態ファイル

`.okf-state.json` に、製品ごとの上流コミット SHA・コミット日時・
バージョンごとの概念数が記録されます。差分更新の判断材料であり、
「いつ時点のドキュメントか」の記録でもあります。

## 日本語版ドキュメントについて

上流には日本語訳（`i18n/versioned_docs/ja-jp/`）も存在しますが、
このバンドルは英語版（正典）のみを取り込んでいます。
訳は英語版に遅れる場合があるため、コード生成の根拠としては英語版を使ってください。
