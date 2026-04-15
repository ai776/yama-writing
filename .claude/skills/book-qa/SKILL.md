---
name: book-qa
description: >
  書籍制作の品質保証層（校閲スキル）。全実行スキル（①〜⑭）の出力を
  校閲チェックする。誤字脱字・文体統一・論理的整合性・ファクトチェック・
  可読性・NG表現・章間整合性チェックを実施。
  AIくささ回避に重点を置いたリライト提案付きQAレポートを生成する。
tags:
  - book
  - qa
  - proofreading
  - ai-detection
  - style
  - cohesion
---

# book-qa — 品質保証層（校閲）

全実行スキルの出力を校閲する。3段階レビューチェーンの第1ゲート。

## 役割

- 全実行スキル（①〜⑭）の出力に対して校閲チェックを実施
- スキルごとに適切なチェックプロファイルを適用
- 旧 book-cohesion の章間整合チェック機能を統合

## Inputs / Outputs

- **In:** 各実行スキルの出力、`BookSpec.json`
- **Out:** `qa_report.md`（リライト提案付き）

## ワークフロー

1. **まず** references/ の style_manual.md と banned_phrases.md を読む（必須）
2. **対象スキルに応じたチェックを実施:**

| 対象スキル | チェック内容 |
|-----------|------------|
| ① book-strategy | 完全性、戦略の内部整合性 |
| ② book-spec | 完全性、strategy との整合性 |
| ③ book-ingest | クリーニング品質、情報欠落なし |
| ④ book-knowledge | 抽出正確性、網羅性、タグ分類の妥当性 |
| ⑤ book-structure | 論理構造、網羅性、バランス |
| ⑥ book-title | SEO妥当性、スコアリング検証 |
| ⑦ book-chapter-blueprint | Blueprint間の整合性、BookSpec整合性 |
| ⑧ book-heading | 階層整合性、命名規則統一 |
| ⑨ book-draft | **フルチェック:** AI表現 + 文体 + 校正 + ファクト + **章間整合** |
| ⑩ book-feedback-ingest | 分類の正確性、網羅性 |
| ⑪ book-rewrite | リライト品質の校閲 |
| ⑫ book-figdesign | 目的整合性、配置の妥当性 |
| ⑬ book-figgen | 正確性、テキスト視認性 |
| ⑭ book-export | フォーマット正確性、目次/ページ番号 |
| book-consistency | 台帳の網羅性、矛盾検出の正確性 |

3. **QAレポート生成** — 人間らしさスコア（book-draft時のみ）、チェック結果、リライト提案
4. **レビューチェーン:**
   - book-producer に提出（GQA-P: QAの網羅性確認）
   - 重要所見がある場合、著者にも提出（GQA-H）

## 参照（読み込みタイミングに注意）

| ファイル | いつ読むか |
|---------|-----------|
| [references/style_manual.md](references/style_manual.md) | **チェック開始前に必ず読む** — AI表現の特徴と回避策 |
| [references/banned_phrases.md](references/banned_phrases.md) | **チェック開始前に必ず読む** — 禁止フレーズリスト |
| [references/qa_checklist.md](references/qa_checklist.md) | チェック手順と判定基準の詳細を確認するとき |
| [templates/qa_report.md](templates/qa_report.md) | レポートのフォーマットを確認するとき |
