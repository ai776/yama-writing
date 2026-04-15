# ProductionSpec — 制作条件設計書

## 基本情報

| 項目 | 内容 |
|------|------|
| 書籍タイトル（仮） | {title} |
| 著者名 | {author} |
| 制作開始日 | {start_date} |
| 情報源タイプ | {source_type: seminar / youtube / reborn} |

## トーン＆スタイル

- **基本文体:** {tone_base}（例: です/ます調ベース、語りかけ風）
- **口語許容度:** {colloquial_level}（例: 中程度 — 「〜たんです」OK、「しょうがねえ」はNG）
- **禁止表現（著者固有）:** {banned_expressions}

## 分量設計

| 項目 | 値 |
|------|-----|
| 総文字数目安 | {total_chars}（例: 40,000〜45,000字） |
| 章数 | {chapter_count} |
| 章ごと文字数予算 | {chars_per_chapter}（例: 各章 4,000〜5,000字） |
| まえがき | {preface_chars}字 |
| あとがき | {afterword_chars}字 |

## 図表・挿絵方針

| 項目 | 設定 |
|------|------|
| 挿入頻度 | {visual_frequency}（例: 各章に1〜2点） |
| 図のタイプ | {visual_types}（例: フロー図、比較表、Mermaid） |
| 挿入位置ルール | {visual_placement}（例: 各節の冒頭 or 末尾） |
| キャプション | {caption_style}（例: 「図X-Y: タイトル」形式） |

## 引用ルール

| source_type | 引用形式 |
|-------------|----------|
| seminar | 発言者名、開始〜終了の行番号 or 章節名 |
| youtube | 発言者名、動画タイトル、タイムスタンプ `[mm:ss]` |
| reborn | 原稿の章/節番号、ページ番号 |

**現在の設定:** {citation_format}

## 情報源ファイル

| # | ファイル名 | 説明 |
|---|-----------|------|
| 1 | {source_file_1} | {description_1} |
| 2 | {source_file_2} | {description_2} |

## 運用ルール

- [ ] 単一Markdownファイル運用（原稿は1ファイルに追記）
- [ ] 情報源厳守（ファイル外の知識・推測の追加は禁止）
- [ ] 承認ゲート遵守（各フェーズで著者承認を得る）
- [ ] AI表現回避（book-qa Skill で担保）
