---
name: book-ingest
description: >
  文字起こしテキストや動画内容を整形・クリーニングし、
  後工程が利用しやすい cleaned_transcript.md を生成する。
tags:
  - book
  - ingest
  - transcript
---

# book-ingest — ⑨ 素材整形

生テキスト（文字起こし/動画字幕/既存原稿）を読み込み、後工程向けに整形する。

## Inputs / Outputs

- **In:** `BookSpec.json`（source_type 確認用）、生テキストファイル
- **Out:** `cleaned_transcript.md`

## ワークフロー

1. BookSpec.json の `source_type` を確認
2. 情報源ファイルを読み込み
3. source_type に応じた整形処理（詳細は references 参照）
4. templates/ のフォーマットで出力
5. **レビューチェーン（人間チェック省略）:**
   - book-qa に提出（G9-Q: クリーニング品質、情報欠落なしチェック）
   - book-producer に提出（G9-P: 情報源の完全性確認）
   - ※人間チェックは省略（G9-Hなし）

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/cleaning_rules.md](references/cleaning_rules.md) | 整形処理の詳細ルールを確認するとき |
| [templates/cleaned_transcript.md](templates/cleaned_transcript.md) | 出力フォーマットを確認するとき |
