---
name: book-export
description: >
  完成Markdown原稿をDocx/PDF形式にエクスポートする。
  Pandocがインストール済みであればCLI上で直接変換を実行可能。
tags:
  - book
  - export
---

# book-export — ⑭ エクスポート（Docx/PDF変換）

完成原稿の Markdown → Docx/PDF 変換を行う。

## Inputs / Outputs

- **In:** `{書籍タイトル}.md`, `figure_gen_output.md`（任意）, `mermaid_snippets.md`（任意）
- **Out:** `{書籍タイトル}.docx` および/または `{書籍タイトル}.pdf`

## ワークフロー

1. **環境確認** — `which pandoc` でPandocの有無を確認。未インストールなら `brew install pandoc` を実行。
2. **Docx変換（推奨・軽量）:**
   ```bash
   pandoc "{書籍タイトル}.md" \
     -o "{書籍タイトル}.docx" \
     --toc --toc-depth=2 \
     -f markdown -t docx
   ```
3. **PDF変換（MacTeX必須・約5GB）:**
   ```bash
   pandoc "{書籍タイトル}.md" \
     -o "{書籍タイトル}.pdf" \
     --pdf-engine=lualatex \
     -V documentclass=ltjsarticle \
     -V geometry:margin=2.5cm \
     -V fontsize=10.5pt \
     --toc --toc-depth=2
   ```
4. **Nano Banana コメント挿入（任意・推奨）:**
   ```bash
   pip install python-docx
   python3 .claude/skills/book-export/references/add_nano_banana_comments.py \
     "{書籍タイトル}.docx" "figure_gen_output.md"
   ```
   → `{書籍タイトル}_commented.docx` が生成される。各図のキャプション段落にNano Banana ProプロンプトがWordコメントとして付与される。
5. **リファレンスDocxからのコメント移植（修正稿エクスポート時）:**
   修正稿を初稿のスタイルでエクスポートし、初稿の Nano Banana コメントを引き継ぐ場合:
   ```bash
   # Step 1: 初稿をリファレンスにしてDocx変換
   pandoc "{修正稿}.md" \
     --reference-doc="{初稿}.docx" \
     -o "{修正稿}.docx" \
     --from=markdown --to=docx

   # Step 2: _commented.docx を生成（コメント移植）
   ```
   コメント移植の手順:
   1. 初稿 `_commented.docx` から `word/comments.xml` を抽出
   2. 初稿の `word/document.xml` から各コメントのアンカーテキスト（`commentRangeStart`〜`commentRangeEnd` 間のテキスト）を特定
   3. 修正稿の Docx を ZIP として開き、`word/comments.xml` を差し替え
   4. 修正稿の `word/document.xml` 内で、アンカーテキストに一致する段落を検索
   5. 一致した段落に `commentRangeStart`、`commentRangeEnd`、`commentReference` の3要素を挿入
   6. `[Content_Types].xml` と `word/_rels/document.xml.rels` にコメント関連の定義が含まれていることを確認

   **重要:** Word がコメントを表示するには、`comments.xml`（コメント定義）と `document.xml`（アンカーマーカー）の両方が必要。`comments.xml` だけでは表示されない。

   詳細: [references/comment_migration.md](references/comment_migration.md)
6. **3段階レビューチェーン:**
   - book-qa に提出（G14-Q: フォーマット正確性、目次/ページ番号チェック）
   - book-producer に提出（G14-P: 最終品質サインオフ）
   - 著者に提出（G14-H: 最終稿の承認）

## 実行時の注意事項

- **Docx変換はPandocのみで完結する。** MacTeX不要、ディスク消費も最小。
- **PDF直接変換にはMacTeX（約5GB）が必要。** ディスク容量不足の場合は Docx → Word/PagesでPDF書き出し の2段階が現実的。
- **スタイルテンプレート（`--reference-doc=template.docx`）** を使えば見出し・フォント・ページ番号を統一できる。

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/export_playbook.md](references/export_playbook.md) | エクスポート手順の詳細を確認するとき |
| [references/add_nano_banana_comments.py](references/add_nano_banana_comments.py) | Nano BananaプロンプトをDocxコメントに挿入するとき |
| [references/comment_migration.md](references/comment_migration.md) | 初稿のコメントを修正稿に移植するとき |
