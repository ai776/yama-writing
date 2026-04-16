# 山本さん書籍作成ワークスペース

このリポジトリは、`tldv/` に保存した文字起こしを情報源として、AI活用・外注化・営業導線に関する書籍原稿を制作するためのワークスペースです。

## 現在の成果物

制作済みの書籍は次の場所にあります。

- `output/ai-katsuyou-uriage-3bai/AIと外注で売上の規模をつくる.md`
- `output/ai-katsuyou-uriage-3bai/AIと外注で売上の規模をつくる.docx`

テーマは「AI活用で売上を3倍にする方法」です。本文は5万字級の原稿として作成されています。

## ディレクトリ構成

- `tldv/`: 書籍制作の情報源となる文字起こし。原則として編集しません。
- `output/`: 書籍原稿、構成案、制作仕様、QAレポートなどの出力先。
- `review/`: レビュー済み原稿や確認用ファイルの置き場。
- `rules/`: 旧ルール類。
- `.claude/skills/`: 書籍制作スキルの正本。
- `.agents/skills`: Codex から参照するローカル Skill 入口。
- `.cursor/skills/`: Cursor 側で利用する Skill 群。
- `plugins/`: Codex 用プラグイン関連ファイル。

## 書籍制作の基本方針

- `tldv/` は一次情報源として扱い、内容を直接編集しません。
- 事実、エピソード、数値、主張は情報源にあるものだけを使います。
- 本文中には出典ファイル名、ファイルパス、行番号を書きません。
- 文体・NG表現は `◆ AI生成文章の特徴と執筆のポイント.md` を優先します。
- 書籍制作を始める場合は、まず `book-factory` を使い、必要に応じて下位 Skill を使います。

## Skills の使い方

このリポジトリでは、書籍制作の作業単位を Skills として管理しています。正本は `.claude/skills/`、Codex から使う入口は `.agents/skills` です。

### まず使う Skill

新しい書籍を作るときは、基本的に `book-factory` から始めます。

```text
/book-factory AI活用で売上を3倍にする方法
```

ペルソナや条件を指定したい場合は、次のように追加します。

```text
/book-factory
テーマ: 不用品回収ビジネスの始め方
ペルソナ: 副業を探している30代サラリーマン
分量: 5万字級
進行: 全部自動
```

`book-factory` は、`tldv/` から関連ナレッジを探し、戦略設計、制作仕様、目次、章設計、本文、QA、エクスポートまでをまとめて進める入口です。

### よく使う指示例

```text
/book-factory 全部自動で AI活用で売上を3倍にする方法
```

```text
/book-factory 5万字級で AIと外注を使って売上を伸ばす本を作って
```

```text
既存原稿を book-review でレビューして
```

```text
review の指摘を book-rewrite で反映して
```

```text
完成原稿を book-export で docx にして
```

### 主要 Skill の役割

- `book-factory`: テーマ入力から書籍一式を自動制作する入口。
- `book-ingest`: 素材を整形し、後工程で使いやすいテキストにする。
- `book-knowledge`: 文字起こしから主張、理由、具体例、数値、体験談を抽出する。
- `book-strategy`: 読者、CTA、核心メッセージなどの戦略を設計する。
- `book-spec`: 文字数、章数、文体、禁止表現、引用方針などの制作条件を決める。
- `book-structure`: 目次と章ごとの文字数配分を作る。
- `book-chapter-blueprint`: 各章の狙い、壊す誤解、入れるべき要素を設計する。
- `book-heading`: 章タイトルと小見出しを整える。
- `book-draft`: 承認済みの構成に沿って本文を書く。
- `book-qa`: 誤字脱字、論理、文体、AIっぽさ、事実関係をチェックする。
- `book-review`: 完成原稿を編集者視点でレビューし、修正指示を作る。
- `book-rewrite`: レビュー指示に沿って原稿を修正する。
- `book-consistency`: 章間の定義、数値、主張、推奨内容の矛盾を確認する。
- `book-export`: Markdown 原稿を docx や PDF に変換する。

### 制作フロー

1. `book-factory` でテーマを指定する。
2. `tldv/` から関連する情報源を抽出する。
3. `StrategySpec.md`、`ProductionSpec.md`、`BookSpec.json` を作る。
4. `toc.md`、`chapter_blueprints.md`、`heading_spec.md` を作る。
5. 本文 Markdown を作成する。
6. `book-qa`、`book-consistency`、必要に応じて `book-review` と `book-rewrite` で整える。
7. `book-export` で `docx` などに変換する。

「全部自動で」と指定した場合は、途中確認を最小限にして、完成原稿の確認まで一気に進めます。

## 主な出力ファイル

`output/ai-katsuyou-uriage-3bai/` には、本文以外に次の制作過程ファイルがあります。

- `StrategySpec.md`: 書籍の戦略設計。
- `ProductionSpec.md`: 制作仕様。
- `BookSpec.json`: 戦略と制作条件の統合仕様。
- `toc.md`: 目次。
- `chapter_blueprints.md`: 各章の設計図。
- `heading_spec.md`: 見出し設計。
- `knowledge_base.md`: 文字起こしから抽出した構造化ナレッジ。
- `qa_report.md`: 品質確認レポート。
- `submission_report.md`: 納品用サマリー。

## 運用メモ

新しい Skill を追加・更新する場合は、まず `.claude/skills/` を更新し、Codex 側の入口である `.agents/skills` と整合させます。

リポジトリの作業ルールは `AGENTS.md` にまとめています。Codex や他のエージェントで作業する場合は、README とあわせて確認してください。
