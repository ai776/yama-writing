---
name: book-heading
description: >
  各章の見出し（章タイトル・小見出し）を専門的に設計するスキル。
  見出し階層の整合性、章間の論理的つながり、読者の理解順序を考慮し、
  目次と連動した最適な見出し体系を提案する。
  Blueprint（章設計図）は book-chapter-blueprint（⑦）で事前に作成済みであることが前提。
tags:
  - book
  - heading
  - hierarchy
  - structure
---

# book-heading — ⑧ 見出し専門

各章の見出し（H1/H2/H3）を設計する。
Blueprint（章設計図）は ⑦ book-chapter-blueprint で事前に作成・承認済みであることが前提。
見出しは Blueprint の「章の核心」「USP」に基づいて設計する。

## Inputs / Outputs

- **In:** `BookSpec.json`, `toc.md`, `chapter_budget.md`, `chapter_blueprints.md`（⑦の出力）, `knowledge_base.md`（あれば）
- **Out:** `heading_spec.md`（見出し設計書）

## ワークフロー

1. **chapter_blueprints.md 確認** — 承認済みBlueprintの各章の核心・USPを把握
2. **toc.md 分析** — 承認済み目次の章構成を確認
3. **knowledge_base.md 参照**（あれば）— 各章に紐付くナレッジ項目を確認
4. **見出し階層設計** — 各章のH1（章タイトル）/H2（節）/H3（小項目）を設計
5. **論理接続チェック** — 節と節のつながり（因果・時系列・対比）を検証
6. **読者理解順序の最適化** — 章内の情報提示順序を調整
7. **章間の整合性チェック** — 見出しの粒度・命名規則が全章で統一されているか
8. **3段階レビューチェーン:**
   - book-qa に提出（G8-Q: 階層整合性、命名規則チェック）
   - book-producer に提出（G8-P: 読者体験・戦略整合性チェック）
   - **著者に提出（G8-H: 見出しの最終承認）** ← 人間チェック必須

**重要:** ⑦ book-chapter-blueprint の承認後に実行すること。Blueprint 未承認の状態での見出し設計は禁止。

## 設計ルール

- H1: 章タイトル（1章1つ）— 読者の期待を設定する
- H2: 節タイトル（1章3〜6個）— 章の論理単位
- H3: 小項目（必要な場合のみ）— 節の中の具体的トピック
- 核心トピックの見出しは末尾に `*` マーキング
- 見出しは「名詞止め」「問いかけ」「行動呼びかけ」のいずれかで統一

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/heading_guidelines.md](references/heading_guidelines.md) | 見出し設計の詳細ルールを確認するとき |
| [templates/heading_spec.md](templates/heading_spec.md) | 出力フォーマットを確認するとき |
