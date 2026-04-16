---
name: book-strategy
description: >
  書籍の戦略設計を担当。事業ゴール（CTA導線）、想定読者ペルソナ、
  KPI設定、核心メッセージ（魂）、書籍の役割定義をヒアリングし
  StrategySpecとして出力する。
tags:
  - book
  - strategy
  - planning
---

# book-strategy — ① 戦略設計

書籍の「なぜ作るか」「誰に届けるか」「何を伝えるか」を定義する。

## Inputs / Outputs

- **In:** 著者の要望（口頭/テキスト）、市場文脈
- **Out:** `StrategySpec.md`, `StrategySpec.json`

## ワークフロー

1. **ヒアリング** — 以下の5項目を著者から聞き取る
   - 事業ゴール（書籍の最終目的、CTA導線設計）
   - 想定読者ペルソナ（年齢/職業/悩み/価値観/接点）
   - KPI設計（CV率/流入経路/読了率など）
   - 書籍の役割定義（リード獲得/権威性証明/営業資料代替など）
   - 核心メッセージ（魂）— この本で一つだけ伝えるなら何か
2. **StrategySpec 生成** — テンプレートに情報を埋めて出力
3. **3段階レビューチェーン:**
   - book-qa に提出（G1-Q: 完全性・整合性チェック）
   - book-producer に提出（G1-P: 戦略的妥当性チェック）
   - 著者に提出（G1-H: 最終承認）

ヒアリング完了まで StrategySpec を生成してはならない。

## オートモード（book-factory 連携）

book-factory から `mode: "autopilot"` で呼び出された場合、ヒアリングを省略し
テーマとtldvナレッジから自動推論で StrategySpec を生成する。

### 自動推論ルール

| 項目 | 推論ロジック |
|------|-------------|
| 事業ゴール | テーマの業種・内容から推測。ビジネス系→コンサル誘導、スキル系→セミナー集客、実績系→権威性構築 |
| ペルソナ | テーマのターゲット層を推測（ユーザー指定があればそれを優先） |
| KPI | デフォルト: Amazon販売100部/月、メルマガ登録率5%、セミナー申込率3% |
| 書籍の役割 | テーマから最適な役割を選定（リード獲得/権威性証明/営業資料代替） |
| 核心メッセージ | tldvナレッジ内の最頻出主張（knowledge_base.md がない場合は cleaned_transcript.md から抽出） |

### オートモード時の制約

- 推論結果はユーザー確認ゲート（G-1）で承認を得る
- ユーザーが「全部自動で」と指定した場合のみ確認を省略
- 推論の根拠（参照したtldvファイル名・該当箇所）を StrategySpec に付記する

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/strategy_extraction_rules.md](references/strategy_extraction_rules.md) | ヒアリング項目の詳細を確認するとき |
| [references/failure_patterns.md](references/failure_patterns.md) | StrategySpec のレビュー時に失敗パターンをチェックするとき |
| [templates/StrategySpec.md](templates/StrategySpec.md) | StrategySpec を生成するとき |
| [templates/StrategySpec.json](templates/StrategySpec.json) | StrategySpec JSON を生成するとき |
