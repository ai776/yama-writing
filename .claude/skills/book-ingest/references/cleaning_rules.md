# 文字起こし整形ルール

## 共通ルール（全 source_type）

1. **文字コード**: UTF-8 に統一
2. **改行**: 意味のまとまりごとに段落分け
3. **空白**: 全角/半角スペースの統一（日本語文中は全角不要）
4. **数字**: 算用数字に統一（「三つ」→「3つ」等は文脈による判断）
5. **記号**: 「・・・」→「……」、「?」→「？」等の統一

## seminar 固有ルール

### 除去対象
- フィラーワード: 「えー」「あのー」「まあ」「ちょっと」（文脈で意味がある場合は残す）
- タイムコード: `[00:00:00]` 等の形式（行番号に変換して保持）
- 重複発言: 言い直し・繰り返し部分

### 保持対象
- 著者の特徴的な口癖（BookSpec の tone に関連）
- 具体的なエピソード・数字
- 直接引用に使える発言

### 話者分離
- 複数話者がいる場合: `**[話者名]:**` で明示
- 質疑応答: `### Q&A` セクションに分離

## youtube 固有ルール

### メタ情報の付与
各動画セクションの冒頭に:
```markdown
## [動画タイトル]
- URL: {url}
- 公開日: {date}
- 再生時間: {duration}
```

### タイムスタンプ
- `[mm:ss]` 形式で保持（引用時に使用）
- 話題の切り替わりポイントに `[mm:ss]` を記録

### 重複テーマ
- 複数動画で同じテーマが語られている場合: `<!-- OVERLAP: [テーマ名] -->` タグを付与
- 矛盾する主張がある場合: `<!-- CONFLICT: [概要] -->` タグを付与

## reborn 固有ルール

### 構造保持
- 原稿の章/節構造をそのまま保持
- 見出しに通し番号を付与: `## 1.1 [見出し]`

### ハイライト
- 著者の特徴的な表現・比喩: `**[原文表現]**` でマーキング
- 核心メッセージに関わる箇所: `<!-- CORE -->` タグを付与

---

## word 固有ルール（.docx / .doc）

### 変換コマンド
```bash
pandoc input.docx -o output.md
```

### 変換後の整形
- 見出しレベル（H1〜H3）を保持
- 太字・斜体はMarkdown記法に変換済みのためそのまま保持
- 表はMarkdown表形式に変換済みのためそのまま保持
- ヘッダー・フッター（ページ番号等）は除去
- コメント・変更履歴は除去（`<!-- comment -->` タグは削除）
- 画像は `[図: {キャプション}]` プレースホルダーに置換してログに記録

### pandocタグ残骸の除去（実証済み）

pandocがWordの書式を変換する際に以下のタグが残存するため除去する：

| 残存パターン | 原因 | 処理 |
|------------|------|------|
| `[テキスト]{.mark}` | Wordのハイライト | `[]{}` を除去してテキストのみ残す |
| `[テキスト]{.underline}` | 下線 | 同上 |
| `[テキスト]{custom-style="..."}` | カスタムスタイル | 同上 |
| `:::` で囲まれたブロック | Divブロック | `:::` 行を除去してテキストを保持 |

**除去の考え方：** `[テキスト]{.mark}` → `テキスト`（中身は保持、装飾タグのみ除去）

---

## pdf 固有ルール

### 変換コマンド

```bash
# 推奨: pdfplumber（Python製・自動インストール対応）
python3 -c "import pdfplumber" 2>/dev/null || pip3 install pdfplumber
python3 -c "
import pdfplumber, re
with pdfplumber.open('input.pdf') as pdf:
    pages = [p.extract_text() or '' for p in pdf.pages]
# 途中改行を結合（行末が句読点・括弧以外で終わる場合）
text = '\n'.join(pages)
text = re.sub(r'([^\n。、！？」）\d])\n([^\n#「（\d])', r'\1\2', text)
open('output.txt', 'w').write(text)
"

# pdfplumber が使えない場合（フォールバック）
# pdftotext -layout input.pdf output.txt
```

> **注意:** `pandoc` はPDFからの変換には対応していない（PDF生成のみ）。
> pdfplumber または pdftotext を使うこと。

### 変換後の整形
- ページ番号（単独行の数字のみの行）は除去
- ヘッダー・フッターの繰り返し文字列を除去
- **途中改行の結合（実証済み）:** PDFレイアウト由来の行中断（「根\n底から」等）を結合する
  - 結合条件: 行末が句読点・閉じ括弧・数字以外 かつ 次行頭が見出し記号・開き括弧・数字以外
- 図表キャプションは `[図: {キャプション}]` として保持
- スキャンPDF（画像PDF）の場合はユーザーに通知し処理を停止
  > ⚠️ このPDFはスキャン画像のためテキスト抽出できません。
  > OCR処理（Adobe Acrobat等）でテキスト化してから再投入してください。

---

## audio 固有ルール（.mp3 / .m4a / .wav / .mp4）

### 変換コマンド

```bash
# faster-whisper（推奨・Python 3.13対応）
python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('medium', device='cpu', compute_type='int8')
segments, info = model.transcribe('input.m4a', language='ja')
with open('output.txt', 'w') as f:
    for segment in segments:
        f.write(f'[{int(segment.start//60):02d}:{int(segment.start%60):02d}] {segment.text}\n')
"
```

### インストール確認・自動インストール

```bash
python3 -c "import faster_whisper" 2>/dev/null || pip3 install faster-whisper
```

> **SkillがClaude Code上で実行する場合：**
> 上記コマンドで `faster_whisper` が未インストールなら自動的に `pip3 install faster-whisper` を実行する。
> `openai-whisper` はPython 3.13で `pkg_resources` エラーが出るため使用しない。

### 変換後の整形
- タイムスタンプは `[mm:ss]` 形式で保持
- seminar 固有ルールと同様にフィラーワード除去・重複発言を整理
- 複数話者がいる場合: `**[話者{n}]:**` で明示（自動判別不可のためユーザーに話者名確認を促す）
- 音質が悪く文字起こし精度が低い箇所には `<!-- UNCERTAIN -->` タグを付与

---

## url 固有ルール（WebサイトURL）

### 変換コマンド
```bash
curl -s {URL} | pandoc -f html -t markdown -o output.md
```

### 変換後の整形
- ナビゲーション・サイドバー・フッター等のサイト共通UIは除去
- 広告・バナー相当の短いリンク群は除去
- 画像は `[画像: {alt属性またはキャプション}]` プレースホルダーに置換
- メタ情報を冒頭に付与:
  ```markdown
  ## [ページタイトル]
  - URL: {url}
  - 取得日: {date}
  ```
- ページネーション（複数ページにわたる記事）がある場合はユーザーに全ページURLの追加投入を促す
- アクセス制限（403/404等）の場合はユーザーに通知し処理をスキップ

---

## url サイトマップ巡回ルール（複数ページ取得）

トップページ1枚ではコンテンツが少ない場合、内部リンクを自動収集してサイト全体を巡回する。

### Step 1: 内部リンクの収集

```bash
# トップページから内部リンクを全て抽出
BASE_URL="https://example.com"
curl -s "$BASE_URL" \
  | grep -oE "href=\"${BASE_URL}[^\"]*\"" \
  | sed 's/href="//;s/"//' \
  | sort -u
```

### Step 2: 除外フィルタリング

抽出したURLから以下を除外する：

| 除外パターン | 理由 |
|------------|------|
| `/feed/` `/comments/feed/` | RSSフィード（HTMLではない） |
| `/wp-json/` `/xmlrpc.php` | WordPress API・システム系 |
| `/wp-content/uploads/` | 画像・メディアファイル |
| `.png` `.jpg` `.pdf` `.zip` | バイナリファイル |
| `?` を含むURL | クエリパラメータ付き（重複ページ） |

### Step 3: コンテンツページの優先順位付け

残ったURLを以下の優先度で処理する：

| 優先度 | URLパターン例 | 理由 |
|--------|-------------|------|
| 高 | `/about/` `/service/` `/profile/` | 著者・サービス情報 |
| 高 | `/blog/` `/column/` `/post-*/` | 記事・コラム |
| 中 | `/faq/` `/news/` | Q&A・更新情報 |
| 低 | `/contact/` `/privacy/` `/recruit/` | 問い合わせ・規約系（原則スキップ） |

### Step 4: 全ページ一括取得・結合

```bash
# コンテンツページを順に取得してまとめる
for URL in $CONTENT_URLS; do
  echo "## $URL"
  curl -s "$URL" | pandoc -f html -t plain 2>/dev/null
  echo "---"
done
```

### 巡回時の注意

- 巡回前にユーザーへ確認：「○○ページ見つかりました。全ページ取得しますか？」
- 1サイトあたりの上限は **20ページ** とする（超過分はユーザーに選択を委ねる）
- 取得間隔は **1秒以上** あける（サーバー負荷軽減）
- JavaScriptで動的生成されるページは `curl` では取得不可 → ユーザーに通知
