---
name: book-draft
description: >
  承認済み目次に基づき書籍本文を章ごとに執筆する。
  情報源厳守・AI表現回避・承認ゲートを遵守。
tags:
  - book
  - draft
  - writing
---

# book-draft — ⑥ 本文専門

承認済み目次・見出し体系に従い、プロのブックライターとして章ごとに本文を執筆する。

## Inputs / Outputs

- **In:** `BookSpec.json`, `toc.md`, `chapter_budget.md`, `heading_spec.md`, `cleaned_transcript.md`
- **Out:** `{書籍タイトル}.md`（単一ファイルに追記）

## ワークフロー

1. **サンプル実演**（300〜600字）→ 3段階レビュー: book-qa(G6-Q) → book-producer(G6-P) → 著者承認(G6-H) で文体確定
2. **章ごと執筆** → 各章を3段階レビュー: book-qa(G6-Q) → book-producer(G6-P) → 著者承認(G6-H)
3. **あとがき** → 著者になりきって執筆 → 3段階レビュー: book-qa(G6-Q) → book-producer(G6-P) → 著者承認(G6-H)

絶対ルール:
- 単一ファイルに追記（分割禁止）
- 情報源にない事実・エピソード・AIの意見は **絶対禁止**
- **本文中に引用表記・出典表記を入れない**（`（出典: ～.md L.x）`、`ソース:`等は一切禁止。読者が読む原稿に情報源パスや行番号を残さないこと）
- 根拠箇所の参照は本文ではなく **章の提出レポートにのみ** 記載する

各章の提出時に添える: 要約（3〜5行）、根拠箇所の参照（提出レポート内のみ）、AI表現セルフチェック（3点）

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/writing_guidelines.md](references/writing_guidelines.md) | 文体・表現の詳細ルール（語尾、強調、口語調整等）を確認するとき |
| [templates/chapter_draft.md](templates/chapter_draft.md) | 章の出力フォーマットを確認するとき |
