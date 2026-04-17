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

# book-draft — ⑨ 本文専門

承認済み目次・見出し体系・Blueprint（章設計図）に従い、プロのブックライターとして章ごとに本文を執筆する。
Blueprint（`chapter_blueprints.md`）の「章の核心」「禁止事項」「優先順位ルール」「ストーリー構造」を必ず参照し、
見出しの文言に引きずられない、章の意図通りの本文を執筆する。
knowledge_base.md がある場合は、タグ付きナレッジを情報源として活用する。

## Inputs / Outputs

- **In:** `BookSpec.json`, `toc.md`, `chapter_budget.md`, `chapter_blueprints.md`（⑦の出力）, `heading_spec.md`, `knowledge_base.md`（あれば）, `cleaned_transcript.md`
- **Out:** `{書籍タイトル}.md`（単一ファイルに追記）

## ワークフロー

1. **サンプル実演**（300〜600字）→ 3段階レビュー: book-qa(G9-Q) → book-producer(G9-P) → 著者承認(G9-H) で文体確定
2. **章ごと執筆** → 各章を3段階レビュー: book-qa(G9-Q) → book-producer(G9-P) → 著者承認(G9-H)
3. **あとがき** → 著者になりきって執筆 → 3段階レビュー: book-qa(G9-Q) → book-producer(G9-P) → 著者承認(G9-H)

絶対ルール:
- 単一ファイルに追記（分割禁止）
- 情報源にない事実・エピソード・AIの意見は **絶対禁止**
- **tldvフォルダにない一般論・業界常識・AIの知識は一切使わない**
- 会議録にある言葉だけを材料にする。新しい成功事例を作り足さない
- ただし、書籍内にこのルール自体（「会議録だけを材料にした」等）は記載しない
- **本文中に引用表記・出典表記を入れない**（`（出典: ～.md L.x）`、`ソース:`等は一切禁止。読者が読む原稿に情報源パスや行番号を残さないこと）
- 根拠箇所の参照は本文ではなく **章の提出レポートにのみ** 記載する
- テーマに必要な具体情報がtldvナレッジに不足している場合、AIが勝手に補完せず **ユーザーに質問する**

各章の提出時に添える: 要約（3〜5行）、根拠箇所の参照（提出レポート内のみ）、AI表現セルフチェック（3点）

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/writing_guidelines.md](references/writing_guidelines.md) | 文体・表現の詳細ルール（語尾、強調、口語調整等）を確認するとき |
| [references/cta_patterns.md](references/cta_patterns.md) | CTA配置・表現の型を確認するとき（特に最終章・あとがき執筆時） |
| [templates/chapter_draft.md](templates/chapter_draft.md) | 章の出力フォーマットを確認するとき |
