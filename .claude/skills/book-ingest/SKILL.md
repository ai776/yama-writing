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
