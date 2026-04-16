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
