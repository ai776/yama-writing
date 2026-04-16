# 書籍量産 Skills — tldvナレッジ × Claude Code Agent

tldvミーティング文字起こし（約2,900件）をナレッジベースとして、
テーマを入力するだけで書籍を自動制作するClaude Code Agent Skills パッケージ。

## アーキテクチャ（4層モデル）

```
+---------------------------------------------+
|  量産層  * book-factory                      |
|  (テーマ入力→tldv検索→自動制作)              |
+--------------------+------------------------+
                     | オートパイロット
+--------------------v------------------------+
|  統括層  0 book-producer                     |
|  (オーケストレーション・プロデューサー)        |
+--------------------+------------------------+
                     | 指示・レビュー
+--------------------v------------------------+
|  実行層  1〜14                               |
|  strategy → spec → ingest → knowledge       |
|  → structure → title → chapter-blueprint    |
|  → heading → draft → feedback-ingest        |
|  → rewrite → figdesign → figgen → export   |
+--------------------+------------------------+
                     | 校閲依頼
+--------------------v------------------------+
|  品質保証層  book-qa(校閲)                    |
|             book-consistency(章間矛盾ゼロ化)  |
+---------------------------------------------+
```

## クイックスタート（量産モード）

### テーマを入力するだけ

```
/book-factory AI活用で売上を3倍にする方法
```

以下が自動実行される:
1. tldvフォルダからテーマに関連するナレッジを自動検索 → **確認**
2. BookSpec（戦略＋制作仕様）を自動生成 → **確認**
3. 目次・見出し・章設計を自動構成 → **確認**
4. 章ごとに本��を執筆
5. 完成原稿 → **確認**
6. 図表生成・エクスポート

### オプション指定

```
/book-factory
テーマ: 不用品回収ビジネスの始め方
ペルソナ: 副業を探している30代サラリーマン
```

## 手動モード（上級者向け）

### `/book-producer` から始める

```
/book-producer
```

book-strategy → book-spec の順でヒアリングし、**BookSpec**（統合版）を確定する。

### ワークフロー順に進む

```
* /book-factory             → テーマ入力→自動制作（推奨）
0 /book-producer            → BookSpec 確定（戦略＋制作条件を統合）
1 /book-strategy            → 戦略設計（ゴール・ペルソナ・KPI・魂）
2 /book-spec                → 制作条件設計（トーン・分量・引用ルール）
3 /book-ingest              → 文字起こし整形（tldvモード対応）
4 /book-knowledge           → ナレッジ生成（タグ付き構造化）※3の後工程
5 /book-structure           → 全体設計（目次＋文字数予算）
6 /book-title               → タイトル決定（4軸スコアリング）
7 /book-chapter-blueprint   → 章設計図（Blueprint）※8の前工程
8 /book-heading             → 見出し設計（H1/H2/H3階層）
9 /book-draft               → 本文執筆（章ごと、Blueprint準拠）
10 /book-feedback-ingest    → フィードバック取込 ※11の前工程
11 /book-rewrite            → リライト（修正指示書→原稿修正）※9の後工程
12 /book-figdesign          → 図表設計
13 /book-figgen             → 図表生成（Mermaid・表・画像プロンプト）
14 /book-export             → エクスポート（PDF/Docx）
   /book-review             → 原稿レビュー・修正指示書生成 ※9の後工程、11の前工程
   /book-diff-report        → 修正箇所一覧生成（初稿→修正稿の差分）※11の後工程
   /book-consistency        → 章間矛盾ゼロ化（4台帳チェック）※9の後工程
```

## 3段階レビューチェーン

すべての実行スキル出力は以下の順で通過する:

```
スキル出力 → book-qa(校閲: G{n}-Q) → book-producer(確認: G{n}-P) → 人間(承認: G{n}-H)
```

※ book-factory 量産モードでは4箇所に簡略化
※ 3 book-ingest のみ人間チェック省略

## Skill 一覧（20スキル）

### 量産層（推奨エントリーポイント）

| Skill | コマンド | 役割 |
|-------|---------|------|
| [book-factory](book-factory/) | `/book-factory テーマ名` | テーマ→tldv検索→書籍自動制作 |

### 統括層

| Skill | コマンド | 役割 |
|-------|---------|------|
| [book-producer](book-producer/) | `/book-producer` | 全体統括・BookSpec確定・プロデューサーゲート |

### 実行層（1〜14）

| # | Skill | コマンド | 役割 |
|---|-------|---------|------|
| 1 | [book-strategy](book-strategy/) | `/book-strategy` | 戦略設計（ゴール・ペルソナ・KPI・魂） |
| 2 | [book-spec](book-spec/) | `/book-spec` | 制作条件設計（トーン・分量・引用） |
| 3 | [book-ingest](book-ingest/) | `/book-ingest` | 素材整形・クリーニング（tldvモード対応） |
| 4 | [book-knowledge](book-knowledge/) | `/book-knowledge` | ナレッジ生成（タグ付き構造化） |
| 5 | [book-structure](book-structure/) | `/book-structure` | 全体設計（目次・文字数予算・ストーリーフロー） |
| 6 | [book-title](book-title/) | `/book-title` | タイトル決定（4軸スコアリング） |
| 7 | [book-chapter-blueprint](book-chapter-blueprint/) | `/book-chapter-blueprint` | 章設計図（Blueprint） |
| 8 | [book-heading](book-heading/) | `/book-heading` | 見出し設計（H1/H2/H3階層） |
| 9 | [book-draft](book-draft/) | `/book-draft` | 本文執筆（章ごと、Blueprint準拠） |
| 10 | [book-feedback-ingest](book-feedback-ingest/) | `/book-feedback-ingest` | フィードバック取込 |
| 11 | [book-rewrite](book-rewrite/) | `/book-rewrite` | リライト（修正指示書→原稿修正） |
| 12 | [book-figdesign](book-figdesign/) | `/book-figdesign` | 図表設計（目的・種類・配置） |
| 13 | [book-figgen](book-figgen/) | `/book-figgen` | 図表生成（Mermaid・表・画像プロンプト） |
| 14 | [book-export](book-export/) | `/book-export` | エクスポート（PDF/Docx） |

### レビュー・差分層

| Skill | コマンド | 役割 |
|-------|---------|------|
| [book-review](book-review/) | `/book-review` | 原稿レビュー・修正指示書生成（5軸精査） |
| [book-diff-report](book-diff-report/) | `/book-diff-report` | 修正箇所一覧生成（初稿→修正稿の差分比較） |

### 品質保証層

| Skill | コマンド | 役割 |
|-------|---------|------|
| [book-qa](book-qa/) | `/book-qa` | 校閲・AI臭さチェック・章間整合 |
| [book-consistency](book-consistency/) | `/book-consistency` | 章間矛盾ゼロ化（4台帳チェック） |

### ユーティリティ

| Skill | コマンド | 役割 |
|-------|---------|------|
| [skill-creator](skill-creator/) | `/skill-creator` | Skill量産ツール |

## BookSpec — 唯一の正

すべてのSkillは **BookSpec**（`BookSpec.md` / `BookSpec.json`）を参照して動作する。

BookSpec は StrategySpec(1) + ProductionSpec(2) を統合した書籍仕様書。

### Part A: 戦略（StrategySpec由来）
- 事業ゴール（CTA導線・バックエンド商品）
- 想定読者（ペルソナ）
- KPI
- 核心メッセージ（魂）
- 書籍の役割

### Part B: 制作条件（ProductionSpec由来）
- 情報源タイプ（seminar / youtube / reborn / **tldv**）
- トーン＆スタイル
- 分量設計（章ごと文字数予算）
- 図表方針
- 引用ルール

## 情報源タイプ

| タイプ | 説明 | 固有ルール |
|--------|------|-----------|
| `tldv` | **tldvミーティング文字起こし** | **テーマ検索→関連セグメント抽出** |
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
