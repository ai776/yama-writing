---
name: book-ingest
description: >
  テキスト・Word・PDF・音声ファイル・WebサイトURLなど
  あらゆる形式の素材を受け取り、整形・クリーニングして
  後工程が利用しやすい cleaned_transcript.md を生成する。
tags:
  - book
  - ingest
  - transcript
---

# book-ingest — ③ 素材整形

あらゆる形式の素材を読み込み、テキストに変換した上で後工程向けに整形する。

## 対応入力形式

| 形式 | 拡張子 | 変換手段 |
|------|--------|---------|
| テキスト | `.txt` `.md` | そのまま読み込み |
| Word | `.docx` `.doc` | `pandoc` でMarkdown変換 |
| PDF | `.pdf` | `pdfplumber`（Python）でテキスト抽出・途中改行結合 |
| 音声 | `.mp3` `.m4a` `.wav` `.mp4` | `whisper`（OpenAI CLI）で文字起こし |
| WebサイトURL | `https://...` | `curl` + `pandoc` でテキスト化 |

## Inputs / Outputs

- **In:** 上記いずれかの形式の素材（複数可）、`BookSpec.json`（source_type 確認用）
- **Out:** `cleaned_transcript.md`

## ワークフロー

1. 渡された素材の形式を判定（拡張子 or URL形式で自動判別）
2. 形式に応じた変換コマンドを実行してテキスト化
3. BookSpec.json の `source_type` を確認
4. source_type と形式に応じた整形処理（詳細は references 参照）
5. templates/ のフォーマットで出力
6. **レビューチェーン（人間チェック省略）:**
   - book-qa に提出（G3-Q: クリーニング品質、情報欠落なしチェック）
   - book-producer に提出（G3-P: 情報源の完全性確認）
   - ※人間チェックは省略（G3-Hなし）

## tldvモード（book-factory 連携）

source_type が `tldv` の場合、以下のフローで自動的にナレッジを検索・抽出する。

### tldv検索フロー

1. **キーワード生成** — テーマから検索キーワードを自動生成
   - 直接キーワード（テーマの中核語）
   - 関連キーワード（周辺語・同義語）
   - 人物キーワード（tldvファイル名に含まれる人物名）

2. **ファイル検索** — `tldv/` フォルダ内の全 `.txt` ファイルを対象に検索
   ```bash
   # ファイル名でのマッチ
   ls tldv/ | grep -i "キーワード"
   # ファイル内容でのマッチ
   grep -l "キーワード" tldv/*.txt
   ```

3. **関連度スコアリング** — 各ファイルのスコアを算出
   - キーワード出現回数 × 重み（直接=3, 関連=1, 人物=2）
   - 上位20ファイルを選定

4. **セグメント抽出** — 選定ファイルからテーマ関連部分のみ抽出
   - キーワード周辺の発言ブロック（前後2発言分の文脈含む）
   - タイムスタンプを保持
   - 無関係な雑談・挨拶は除外

5. **結合・整形** — 抽出セグメントを `cleaned_transcript.md` に結合
   - ファイルごとにセクション分け（出典明記）
   - 話者名を統一表記に正規化
   - 重複発言の除去

### tldvファイルの形式

```
■ ミーティング名
■ 日時
────────────────────────────────────────

[タイムスタンプ] 話者名
発言内容
```

### 出力例（tldvモード）

```markdown
# cleaned_transcript.md
## テーマ: {テーマ名}
## 使用ナレッジ: {選定ファイル数}件

---

### 出典: {ミーティング名} ({日付})

[4:33] 山本 智也
まあ ちょっと こんな感じで...

[4:38] 山本 智也
クラファンを本当はやるつもりなかったんだけど...

---

### 出典: {別のミーティング名} ({日付})
...
```

## 変換コマンド早見表

```bash
# Word → Markdown
pandoc input.docx -o output.md

# PDF → テキスト
pdftotext input.pdf output.txt
# pdftotext が使えない場合
pandoc input.pdf -o output.md

# 音声 → テキスト（faster-whisper）
# 未インストールなら自動インストール
python3 -c "import faster_whisper" 2>/dev/null || pip3 install faster-whisper
python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('medium', device='cpu', compute_type='int8')
segments, info = model.transcribe('input.m4a', language='ja')
with open('output.txt', 'w') as f:
    for segment in segments:
        f.write(f'[{int(segment.start//60):02d}:{int(segment.start%60):02d}] {segment.text}\n')
"

# WebサイトURL → テキスト
curl -s {URL} | pandoc -f html -t markdown -o output.md
```

> **注意:** 変換ツールが未インストールの場合はユーザーに通知し、
> インストール手順を案内する（自動インストールはしない）。

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/cleaning_rules.md](references/cleaning_rules.md) | 整形処理の詳細ルールを確認するとき |
| [templates/cleaned_transcript.md](templates/cleaned_transcript.md) | 出力フォーマットを確認するとき |
