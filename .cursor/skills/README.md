# 書籍制作 Skills — Claude Code Agent

セミナー文字起こし・YouTube動画・既存原稿から書籍を制作するための
Claude Code Agent Skills パッケージ。

## アーキテクチャ（3層モデル）

```
┌─────────────────────────────────────────┐
│  統括層  ⓪ book-producer               │
│  （オーケストレーション・プロデューサー）  │
└────────────────┬────────────────────────┘
                 │ 指示・レビュー
┌────────────────▼────────────────────────┐
│  実行層  ①〜⑩                           │
│  strategy → spec → ingest → structure  │
│  → title → heading → draft             │
│  → figdesign → figgen → export         │
└────────────────┬────────────────────────┘
                 │ 校閲依頼
┌────────────────▼────────────────────────┐
│  品質保証層  book-qa（校閲）             │
└─────────────────────────────────────────┘
```

## 3段階レビューチェーン

すべての実行スキル出力は以下の順で通過する:

```
スキル出力 → book-qa（校閲: G{n}-Q）→ book-producer（確認: G{n}-P）→ 人間（承認: G{n}-H）
```

※ ⑨ book-ingest のみ人間チェック省略

## クイックスタート

### 1. `/book-producer` から始める

```
/book-producer
```

book-strategy → book-spec の順でヒアリングし、**BookSpec**（統合版）を確定する。

### 2. ワークフロー順に進む

```
⓪ /book-producer   → BookSpec 確定（戦略＋制作条件を統合）
① /book-strategy   → 戦略設計（ゴール・ペルソナ・KPI・魂）
② /book-spec       → 制作条件設計（トーン・分量・引用ルール）
⑨ /book-ingest     → 文字起こし整形
③ /book-structure   → 全体設計（目次＋文字数予算）
④ /book-title       → タイトル決定（4軸スコアリング）
⑤ /book-heading     → 見出し設計（H1/H2/H3階層）
⑥ /book-draft       → 本文執筆（章ごと）
⑦ /book-figdesign   → 図表設計
⑧ /book-figgen      → 図表生成（Mermaid・表・画像プロンプト）
⑩ /book-export      → エクスポート（PDF/Docx）
```

### 3. 3段階レビューを守る

各工程で QA → プロデューサー → 人間 の3段階を通過してから次へ進む。

## Skill 一覧（12スキル）

### 統括層

| Skill | コマンド | 役割 |
|-------|---------|------|
| [book-producer](book-producer/) | `/book-producer` | 全体統括・BookSpec確定・プロデューサーゲート |

### 実行層（①〜⑩）

| # | Skill | コマンド | 役割 |
|---|-------|---------|------|
| ① | [book-strategy](book-strategy/) | `/book-strategy` | 戦略設計（ゴール・ペルソナ・KPI・魂） |
| ② | [book-spec](book-spec/) | `/book-spec` | 制作条件設計（トーン・分量・引用） |
| ③ | [book-structure](book-structure/) | `/book-structure` | 全体設計（目次・文字数予算・ストーリーフロー） |
| ④ | [book-title](book-title/) | `/book-title` | タイトル決定（4軸スコアリング） |
| ⑤ | [book-heading](book-heading/) | `/book-heading` | 見出し設計（H1/H2/H3階層） |
| ⑥ | [book-draft](book-draft/) | `/book-draft` | 本文執筆（章ごと） |
| ⑦ | [book-figdesign](book-figdesign/) | `/book-figdesign` | 図表設計（目的・種類・配置） |
| ⑧ | [book-figgen](book-figgen/) | `/book-figgen` | 図表生成（Mermaid・表・画像プロンプト） |
| ⑨ | [book-ingest](book-ingest/) | `/book-ingest` | 素材整形・クリーニング |
| ⑩ | [book-export](book-export/) | `/book-export` | エクスポート（PDF/Docx） |

### 品質保証層

| Skill | コマンド | 役割 |
|-------|---------|------|
| [book-qa](book-qa/) | `/book-qa` | 校閲・AI臭さチェック・章間整合 |

### ユーティリティ

| Skill | コマンド | 役割 |
|-------|---------|------|
| [skill-creator](skill-creator/) | `/skill-creator` | Skill量産ツール |

## BookSpec — 唯一の正

すべてのSkillは **BookSpec**（`BookSpec.md` / `BookSpec.json`）を参照して動作する。

BookSpec は StrategySpec（①）+ ProductionSpec（②）を統合した書籍仕様書。

### Part A: 戦略（StrategySpec由来）
- 事業ゴール（CTA導線・バックエンド商品）
- 想定読者（ペルソナ）
- KPI
- 核心メッセージ（魂）
- 書籍の役割

### Part B: 制作条件（ProductionSpec由来）
- 情報源タイプ（seminar / youtube / reborn）
- トーン＆スタイル
- 分量設計（章ごと文字数予算）
- 図表方針
- 引用ルール

## 情報源タイプ

| タイプ | 説明 | 固有ルール |
|--------|------|-----------|
| `seminar` | セミナー文字起こし | 行番号による引用 |
| `youtube` | YouTube動画 | タイムスタンプ `[mm:ss]` 必須 |
| `reborn` | 既存原稿のリボーン | 原稿の魂を維持 |

## AI臭さ回避

`book-qa` Skill が以下をチェック:
- 禁止フレーズ（「羅針盤」「鍵となる」「安心してください」等）
- 接続詞の過多
- 「あなた」の過度な使用
- 定型三段構成
- 曖昧語尾の連続
- 抽象語の連発

詳細: [book-qa/references/style_manual.md](book-qa/references/style_manual.md)

## 新しいSkillを作るには

```
/skill-creator
```

詳細: [skill-creator/references/how_to_write_skills.md](skill-creator/references/how_to_write_skills.md)
