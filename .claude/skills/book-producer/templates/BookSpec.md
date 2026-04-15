# BookSpec — 書籍仕様書（統合版）

> StrategySpec（①）+ ProductionSpec（②）を book-producer が統合したもの。
> 全スキルの共通参照ドキュメント。

---

## Part A: 戦略（StrategySpec より）

### 基本情報

| 項目 | 内容 |
|------|------|
| 書籍タイトル（仮） | {title} |
| 著者名 | {author} |
| 制作開始日 | {start_date} |

### 事業ゴール

- **最終目的:** {goal_purpose}
- **CTA導線:** {cta_flow}
- **バックエンド商品:** {backend_product}

### 想定読者（ペルソナ）

| 項目 | 内容 |
|------|------|
| 年齢層 | {age_range} |
| 職業・立場 | {occupation} |
| 主な悩み | {pain_points} |
| 価値観 | {values} |
| 書籍を手にする場面 | {context} |

### KPI

| 指標 | 目標値 |
|------|--------|
| {kpi_1_name} | {kpi_1_target} |
| {kpi_2_name} | {kpi_2_target} |

### 核心メッセージ（魂）

> {core_message}

### 書籍の役割

> {book_role}

---

## Part B: 制作条件（ProductionSpec より）

### 情報源タイプ

| 項目 | 内容 |
|------|------|
| source_type | {source_type: seminar / youtube / reborn} |

### トーン＆スタイル

- **基本文体:** {tone_base}
- **口語許容度:** {colloquial_level}（低/中/高）
- **禁止表現（著者固有）:** {banned_expressions}

### 分量設計

| 項目 | 値 |
|------|-----|
| 総文字数目安 | {total_chars} |
| 章数 | {chapter_count} |
| 章ごと文字数予算 | {chars_per_chapter} |
| まえがき | {preface_chars}字 |
| あとがき | {afterword_chars}字 |

### 図表・挿絵方針

| 項目 | 設定 |
|------|------|
| 挿入頻度 | {visual_frequency} |
| 図のタイプ | {visual_types} |
| 挿入位置ルール | {visual_placement} |
| キャプション | {caption_style} |

### 引用ルール

| source_type | 引用形式 |
|-------------|----------|
| seminar | 発言者名、行番号 or 章節名 |
| youtube | 発言者名、動画タイトル、タイムスタンプ |
| reborn | 原稿の章/節番号、ページ番号 |

**現在の設定:** {citation_format}

### 情報源ファイル

| # | ファイル名 | 説明 |
|---|-----------|------|
| 1 | {source_file_1} | {description_1} |

---

## 運用ルール

- [ ] 単一Markdownファイル運用（原稿は1ファイルに追記）
- [ ] 情報源厳守（ファイル外の知識・推測の追加は禁止）
- [ ] 3段階レビューチェーン遵守（QA→プロデューサー→人間）
- [ ] AI表現回避（book-qa で担保）
- [ ] 本文中に引用表記・出典表記を入れない
