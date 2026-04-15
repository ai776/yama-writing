---
name: book-export
description: >
  完成Markdown原稿をDocx/PDF形式にエクスポートするための手順書を提供する。
  手動実行専用。
disable-model-invocation: true
tags:
  - book
  - export
  - manual
---

# book-export — ⑩ PDF化専門（手動実行専用）

完成原稿の Markdown → Docx/PDF 変換手順を提供する。

## Inputs / Outputs

- **In:** `{書籍タイトル}.md`, `figure_gen_output.md`（任意）, `mermaid_snippets.md`（任意）
- **Out:** エクスポート手順の提示

## ワークフロー

1. references/ の手順書を読み込んで提示
2. **3段階レビューチェーン:**
   - book-qa に提出（G10-Q: フォーマット正確性、目次/ページ番号チェック）
   - book-producer に提出（G10-P: 最終品質サインオフ）
   - 著者に提出（G10-H: 最終稿の承認）

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/export_playbook.md](references/export_playbook.md) | エクスポート手順の詳細を確認するとき |
