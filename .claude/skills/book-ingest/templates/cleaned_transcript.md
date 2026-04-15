# 整形済みテキスト — {書籍タイトル}

## メタ情報

| 項目 | 内容 |
|------|------|
| 情報源タイプ | {source_type} |
| 入力形式 | {input_format} ※ txt / md / docx / pdf / audio / url |
| ファイル数 | {file_count} |
| 総文字数（原文） | {original_chars} |
| 総文字数（整形後） | {cleaned_chars} |
| 整形日 | {date} |

## 変換ログ

| # | ファイル / URL | 入力形式 | 変換コマンド | ステータス |
|---|--------------|---------|------------|---------|
| 1 | {filename_or_url} | {format} | {command} | ✅ 成功 / ⚠️ 要確認 / ❌ 失敗 |

### 変換時の注意・スキップ事項

- {スキャンPDF・アクセス制限・未インストールツール等の通知をここに記録}

## 整形ログ

- 除去したフィラーワード数: {filler_count}
- 画像プレースホルダー数: {image_placeholder_count}
- 不確実箇所（UNCERTAIN）数: {uncertain_count}
- 重複テーマ: {overlap_count} 件
- 矛盾箇所: {conflict_count} 件

---

## 本文

{整形済みテキスト本文}

---

## 付録: 重複テーマ一覧

| # | テーマ | 出現箇所 |
|---|--------|----------|
| 1 | {theme} | {locations} |

## 付録: 矛盾箇所一覧

| # | 概要 | 情報源A | 情報源B |
|---|------|---------|---------|
| 1 | {summary} | {source_a} | {source_b} |
