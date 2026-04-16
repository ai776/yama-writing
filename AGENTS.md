# このリポジトリでの作業指針

## 概要

- このリポジトリは、tldv文字起こしをナレッジベースに書籍を制作するワークスペース。
- Codex 用のローカル Skills は `.agents/skills/` 配下を参照する。
- Skill の正本は `.claude/skills/`。`.agents/skills` は Codex から使うための入口として扱う。

## 重要ルール

- `tldv/` は情報源。内容を編集しない。
- 事実・エピソードは情報源にあるものだけを使う。
- 本文中に出典やファイルパス、行番号を書かない。
- `◆ AI生成文章の特徴と執筆のポイント.md` の NG 表現方針を優先する。

## 主なディレクトリ

- `tldv/` : 情報源の文字起こし
- `output/` : 書籍出力
- `review/` : レビュー済み原稿
- `rules/` : 旧ルール類
- `.claude/skills/` : Skill の正本
- `.agents/skills/` : Codex 用ローカル Skill 入口

## 運用メモ

- 新しい Skill を追加・更新する場合は、まず `.claude/skills/` を更新し、Codex 側の入口も整合させる。
- 書籍制作を始めるときは `book-factory` を優先し、個別工程が必要な場合だけ下位 Skill を使う。
