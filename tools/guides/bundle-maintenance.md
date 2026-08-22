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

例外は `okf/guides/` と `okf/pricing/` の 2 セクションで、これらは上流を持たない
手書きのドキュメントです。実体は `tools/guides/` と `tools/pricing/` にあり、
生成時にそのままコピーされます（`copy_guides()` / `copy_pricing()`）。

## 生成元

| 製品 | リポジトリ | 種別 | 公開先 |
|---|---|---|---|
| ScalarDB | `scalar-labs/docs-scalardb` | Docusaurus | https://scalardb.scalar-labs.com/docs/ |
| ScalarDL | `scalar-labs/docs-scalardl` | Docusaurus | https://scalardl.scalar-labs.com/docs/ |
| ScalarDB Community | `scalar-labs/docs-scalardb-community` | Docusaurus | https://scalardb-community.scalar-labs.com/docs/ |
| ScalarDB Saga | `scalar-labs/scalardb-saga` | ソースリポジトリ | （ドキュメントサイト無し） |

前者 3 つは developers.scalar-labs.com から辿れる公式ドキュメントサイトの生成元です。
上流は Docusaurus の MDX なので、生成時に以下を平文 Markdown へ展開しています。

- `import` した partial の実体埋め込み（`{props.x}` の置換を含む）
- `<Tabs>` / `<TabItem>` → 太字ラベル付きの節
- `<JavadocLink>` → そのバージョンのパッチリリースに固定した Javadoc URL
- `<CodeBlock>` → コードフェンス
- 相対リンク `foo.mdx` → バンドル内の `./foo.md`、バンドル外はドキュメントサイトの絶対 URL

## ソースリポジトリ由来の製品（ScalarDB Saga）

ScalarDB Saga はドキュメントサイトを持たないため、別経路（`tools/okf_repo.py`）で
生成しています。Docusaurus 側と違うのは次の点です。

- **バージョン = リリースブランチ。** `^\d+\.\d+$` に一致するブランチ（`3.19` など）だけを
  バージョンとして取り込みます。`main` や次期マイナーブランチは `-SNAPSHOT` を積む
  開発ラインなので除外します。`patch_version` はそのブランチの
  `gradle.properties` の `version` です。
- **概念の対象は宣言されている。** サイドバーが無いので、どのファイルが概念になるかは
  `tools/okf_repo.py` の `REPO_DOCS` に列挙してあります。上流にドキュメントが増えても、
  ここに追記するまで概念は増えません（設計ノートの追加でバンドルの形が勝手に変わるのを
  避けるため）。
- **契約ファイルも概念にする。** `.proto` / `server.properties` / saga 定義は
  コードフェンスに入れた Reference 概念として出力します（`render="code"`）。
- **`resource` は GitHub の blob URL。** ドキュメントサイトが無いため、生成元コミットに
  固定した GitHub URL が正典です。リポジトリ内リンクは、概念になっているファイルなら
  バンドル内の相対パスへ、そうでなければ同じコミットの GitHub URL へ書き換えます。
- **GA 前のラインは `status: draft`。** `-alpha` / `-beta` / `-rc` / `-SNAPSHOT` を含む
  リリースは `prerelease: true` と `pre-release` タグが付きます。

`--only-new` は、Docusaurus 側が「バンドルに無いバージョン」を基準にするのに対し、
こちらは **ブランチ HEAD の SHA が `.okf-state.json` の記録と変わったか** で判断します
（GA 前のブランチは中身が動き続けるため）。

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
- ソースリポジトリ由来の製品では、ブランチ HEAD が動いたバージョンを再生成する
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

## 価格・ライセンスセクション (`okf/pricing/`)

**このセクションだけは上流リポジトリを持たず、自動更新されません。**
出典は株式会社 Scalar の社内価格表（Google Drive）で、ドキュメントサイトには公開されていません。

| 概念 | 出典 |
|---|---|
| `index.md` / `licensing-units.md` / `scalardb-pricing.md` / `scalardl-pricing.md` | Scalar 製品価格表 **2024年7月1日版** |
| `scalardb-analytics-pricing.md` | ScalarDB Analytics — Product feature overview and pricing（**2024年9月10日**） |
| `edition-feature-matrix.md` | 上記価格表 + 本バンドル（ScalarDB v3.19 / ScalarDL v3.13、取得日 2026年8月6日） |
| `sample-quotations.md` | Scalar 製品 サンプル見積書 |

### 更新手順

1. 価格表の新しい版を確認する。
2. `tools/pricing/*.md` を手で更新する。金額を変えたら
   frontmatter の `price_list_version`（Analytics は `2024-09-10` 系）と
   `sources[].last_modified` も併せて更新する。
3. `edition-feature-matrix.md` は `matrix_snapshot` / `snapshot_date` を、
   参照した ScalarDB / ScalarDL のバージョンに合わせて更新する。
   バンドルの最新版が上がったら、機能マトリクスの再確認が必要かを判断すること。
4. `make build`（または `make offline`）でコピーし、`make validate` で確認する。

### 公開範囲（重要）

このバンドルに収録してよいのは、次の 3 つの定価**だけ**です。

- **Pay as you go** — ScalarDB Analytics の SDBU・時間単価
- **月額** — Pod 単位サブスクリプション 4 製品の 1ヶ月契約 定価
- **年額** — 同 4 製品の 1年契約 定価

次のものは**入れないでください**。価格表を更新するときも同じ基準で取捨してください。

- 3年契約の定価および期間割引率
- 先払いクレジット (Prepaid Credit) の販売価格・割引率
- ボリューム割引を含む値引き条件、値引き後の実売価格
- 特定顧客向けの契約条件

該当箇所は「非公開」と記載し、営業担当への問い合わせに誘導しています。
削除ではなく「非公開」と明示しているのは、AI が欠落を推定で埋めないようにするためです。

出典の記録も同じ方針です。`pricing/` の概念は `resource`（公開 URL）を持たず、
`sources[]` には**タイトルのみ**を記録し `access: internal (Google Drive / Scalar 社内)`
を付けています。**社内ドキュメントの URL やファイル ID をバンドルに入れないでください。**

### 注意

- 記載はすべて**定価（税抜・JPY）**です。
- 本リポジトリを公開する場合、このセクションを含めてよいかを必ず確認してください。
  含めない運用にする場合は `tools/pricing/` を除外し、`copy_pricing()` の呼び出しを外します。

## バージョンの廃止

上流が古いバージョンを削除した場合、そのディレクトリはバンドルに残り続けます。
不要になったら手動で削除し、`.okf-state.json` の該当エントリも消してください。
既存システムの調査用に残す場合は、`status: deprecated` が付いているのでそのままで問題ありません。

## 状態ファイル

`.okf-state.json` に、製品ごとの上流コミット SHA・コミット日時・
バージョンごとの概念数が記録されます。差分更新の判断材料であり、
「いつ時点のドキュメントか」の記録でもあります。
ソースリポジトリ由来の製品は `kind: "repo"` を持ち、バージョンごとに
そのブランチの `sha` も記録されます。

## 日本語版ドキュメントについて

上流には日本語訳（`i18n/versioned_docs/ja-jp/`）も存在しますが、
このバンドルは英語版（正典）のみを取り込んでいます。
訳は英語版に遅れる場合があるため、コード生成の根拠としては英語版を使ってください。
