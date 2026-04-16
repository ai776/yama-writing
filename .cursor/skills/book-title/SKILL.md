---
name: book-title
description: >
  書籍タイトルの専門スキル。メインタイトル・サブタイトルの候補を複数生成し、
  SEO観点・訴求力・ペルソナ適合性・市場差別化の4軸でスコアリングを行う。
  BookSpecの戦略と制作条件に基づいた最適なタイトルを提案する。
tags:
  - book
  - title
  - seo
  - naming
---

# book-title — ⑥ タイトル専門

メインタイトルとサブタイトルの候補を生成し、4軸スコアリングで最適案を提案する。

## Inputs / Outputs

- **In:** `BookSpec.json`（統合版 — 特に goal, persona, core_message）
- **Out:** `title_proposal.md`（3〜5候補 + スコアリング + 推奨案）

## ワークフロー

1. **BookSpec 分析** — 戦略（ゴール・ペルソナ・核心メッセージ）を読み込み
2. **キーワード調査** — ペルソナが検索しそうなキーワード・競合タイトルを分析
3. **候補生成** — メインタイトル + サブタイトルを3〜5案生成
4. **4軸スコアリング** — 各候補を評価
5. **推奨案の提示** — トップ1〜2案に推薦理由を添える
6. **3段階レビューチェーン:**
   - book-qa に提出（G6-Q: SEOチェック、スコアリング妥当性検証）
   - book-producer に提出（G6-P: 戦略適合性、市場ポジショニング確認）
   - 著者に提出（G6-H: 最終タイトル決定）

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/title_criteria.md](references/title_criteria.md) | スコアリング基準・SEOガイドラインを確認するとき |
| [templates/title_proposal.md](templates/title_proposal.md) | 出力フォーマットを確認するとき |
