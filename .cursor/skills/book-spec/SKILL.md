---
name: book-spec
description: >
  書籍の制作条件を設計。ページ数・文字数・章数、トーン＆スタイル、
  禁止表現、引用ルール、図表方針、情報源タイプなど具体的な制作仕様を
  ヒアリングしProductionSpecとして出力する。
tags:
  - book
  - specification
  - production
---

# book-spec — ② 制作条件設計

書籍の「どう作るか」を具体的な数値・ルールとして定義する。

## Inputs / Outputs

- **In:** 著者の要望、StrategySpec（整合性確認用）、情報源ファイル
- **Out:** `ProductionSpec.md`, `ProductionSpec.json`

## ワークフロー

1. **ヒアリング** — 以下の6項目を著者から聞き取る
   - 情報源タイプ（seminar / youtube / reborn）
   - トーン＆スタイル（基本文体、口語許容度）
   - 禁止表現（著者固有のNGワード・トピック）
   - 分量設計（総文字数、章数、章ごと文字数予算）
   - 図表・挿絵方針（頻度、種類、配置ルール）
   - 引用ルール（source_type に応じた形式）
2. **StrategySpec との整合性確認** — ペルソナやゴールと矛盾するトーン/分量になっていないか
3. **ProductionSpec 生成** — テンプレートに情報を埋めて出力
4. **3段階レビューチェーン:**
   - book-qa に提出（G2-Q: 完全性・整合性チェック）
   - book-producer に提出（G2-P: 制作可能性チェック）
   - 著者に提出（G2-H: 最終承認）

ヒアリング完了まで ProductionSpec を生成してはならない。

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/spec_extraction_rules.md](references/spec_extraction_rules.md) | ヒアリング項目の詳細を確認するとき |
| [templates/ProductionSpec.md](templates/ProductionSpec.md) | ProductionSpec を生成するとき |
| [templates/ProductionSpec.json](templates/ProductionSpec.json) | ProductionSpec JSON を生成するとき |
