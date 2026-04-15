# エクスポート詳細手順書

## 推奨ルート（A/B選択）

| ルート | 必要ツール | ディスク容量 | PDF化方法 |
|-------|-----------|------------|----------|
| **A: 直接PDF** | Pandoc + MacTeX | 約6GB | Pandocで直接PDF生成 |
| **B: Docx経由（推奨）** | Pandocのみ | 約180MB | Docx → Word/PagesでPDF書き出し |

> **実績:** MacTeX（約5GB）はディスク容量不足で失敗しやすい。ルートBが確実。

## 事前準備

### 1. 環境構築

```bash
# Pandoc（必須・約180MB）
brew install pandoc

# --- ルートAのみ ---
# PDF直接生成用（日本語対応・約5GB）
brew install --cask mactex

# --- Mermaidコードブロックがある場合のみ ---
# Mermaid CLI（図表画像化用）
npm install -g @mermaid-js/mermaid-cli
```

### 2. テンプレート準備（任意）

Docx出力のスタイルを統一するため、テンプレートファイルを用意:

1. 白紙の `.docx` ファイルを作成
2. 見出し1〜3のスタイル、本文のフォント・サイズを設定
3. ヘッダー・フッター（ページ番号）を設定
4. `template.docx` として保存

テンプレートなしでも変換は可能（デフォルトスタイルが適用される）。

## 変換手順

### Step 1: Mermaid図の画像化（該当がある場合のみ）

原稿内にMermaidコードブロックがある場合、画像に変換:

```bash
npx mmdc -i fig-4-2.mmd -o images/fig-4-2.png -w 800
```

原稿内のMermaidブロックを画像参照に置換:

```markdown
<!-- 変換前 -->
```mermaid
flowchart TD
    A --> B
```

<!-- 変換後 -->
![図4-2: タイトル](images/fig-4-2.png)
```

### Step 2: Docx 変換（ルートA・B共通）

```bash
# テンプレートなし（最小構成）
pandoc "{書籍タイトル}.md" \
  -o "{書籍タイトル}.docx" \
  --toc --toc-depth=2 \
  -f markdown -t docx

# テンプレートあり（スタイル統一）
pandoc "{書籍タイトル}.md" \
  -o "{書籍タイトル}.docx" \
  --reference-doc=template.docx \
  --toc --toc-depth=2 \
  -f markdown -t docx
```

### Step 2.5: Nano Banana コメント挿入（任意・推奨）

`figure_gen_output.md` のNano Bananaプロンプトを、Docx内の各図キャプション段落にWordコメントとして挿入する。
Wordで開くと、各図の横にコメント吹き出しでプロンプトが表示される。

```bash
# python-docx インストール（初回のみ）
pip install python-docx

# コメント挿入
python3 .claude/skills/book-export/references/add_nano_banana_comments.py \
  "{書籍タイトル}.docx" \
  "figure_gen_output.md"

# → {書籍タイトル}_commented.docx が生成される
```

**仕組み:**
- `figure_gen_output.md` から `## fig-X-Y:` セクションの `**NANO_BANANA_PROMPT:**` コードブロックを解析
- Docx内で「図X-Y」を含む段落を検索し、Word XMLレベルでコメントを挿入
- `word/comments.xml`、Content-Type、Relationship を自動生成

**互換性:** Python + python-docx のみ。Mac / Windows / Linux で動作。Word未インストールでも実行可能。

---

### Step 3: PDF化

**ルートA（MacTeX使用）:**

```bash
pandoc "{書籍タイトル}.md" \
  -o "{書籍タイトル}.pdf" \
  --pdf-engine=lualatex \
  -V documentclass=ltjsarticle \
  -V geometry:margin=2.5cm \
  -V fontsize=10.5pt \
  --toc --toc-depth=2 \
  -f markdown -t pdf
```

**ルートB（Docx経由）:**

1. Step 2 で生成した `.docx` を Word または Pages で開く
2. ファイル → PDF として書き出し（または プリント → PDF保存）

### Step 4: 最終確認

変換後のファイルを開き、以下を確認:
- [ ] 目次が正しく生成されている
- [ ] 見出しのスタイルが統一されている
- [ ] 図表（Markdown表 / 画像）が正しい位置にある
- [ ] ページ番号が正しい
- [ ] 文字化けがない
- [ ] 改ページが適切な位置にある

## トラブルシューティング

| 問題 | 原因 | 対処 |
|-----|------|------|
| MacTeXダウンロード失敗 | ディスク容量不足（5GB必要） | ルートBに切り替え |
| `curl: (23) Failure writing output` | ディスク満杯 | `rm ~/Library/Caches/Homebrew/downloads/*mactex*.incomplete` で不完全ファイル削除 |
| 日本語文字化け（PDF） | LaTeXエンジン設定 | `--pdf-engine=lualatex -V documentclass=ltjsarticle` を指定 |
| Markdown表が崩れる | Pandoc変換の仕様 | Docx上で手動調整、または画像差し替え |
