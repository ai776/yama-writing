# エクスポート詳細手順書

## 事前準備

### 1. 環境構築

```bash
# Pandoc（必須）
brew install pandoc

# PDF生成用（日本語対応）
brew install --cask mactex

# Mermaid CLI（図表画像化用）
npm install -g @mermaid-js/mermaid-cli
```

### 2. テンプレート準備

Docx出力のスタイルを統一するため、テンプレートファイルを用意:

1. 白紙の `.docx` ファイルを作成
2. 見出し1〜3のスタイル、本文のフォント・サイズを設定
3. ヘッダー・フッター（ページ番号）を設定
4. `template.docx` として保存

## 変換手順

### Step 1: 図表の画像化

Mermaid コードを画像に変換:

```bash
# mermaid_snippets.md から各コードブロックを抽出し画像化
npx mmdc -i fig-1-1.mmd -o images/fig-1-1.png -w 800
npx mmdc -i fig-2-1.mmd -o images/fig-2-1.png -w 800
```

### Step 2: 原稿内の図表参照を画像に置換

Markdown 内の Mermaid コードブロックを画像参照に置換:

```markdown
<!-- 変換前 -->
```mermaid
flowchart TD
    A --> B
```

<!-- 変換後 -->
![図1-1: タイトル](images/fig-1-1.png)
```

### Step 3: Docx 変換

```bash
pandoc "{書籍タイトル}.md" \
  -o "{書籍タイトル}.docx" \
  --reference-doc=template.docx \
  --toc \
  --toc-depth=2 \
  -f markdown -t docx
```

### Step 4: PDF 変換

```bash
pandoc "{書籍タイトル}.md" \
  -o "{書籍タイトル}.pdf" \
  --pdf-engine=lualatex \
  -V documentclass=ltjsarticle \
  -V geometry:margin=2.5cm \
  -V fontsize=10.5pt \
  --toc \
  --toc-depth=2 \
  -f markdown -t pdf
```

### Step 5: 最終確認

変換後のファイルを開き、以下を確認:
- [ ] 目次が正しく生成されている
- [ ] 見出しのスタイルが統一されている
- [ ] 図表が正しい位置に挿入されている
- [ ] ページ番号が正しい
- [ ] 文字化けがない
- [ ] 改ページが適切な位置にある
