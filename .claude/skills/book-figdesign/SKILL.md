---
name: book-figdesign
description: >
  各章の図表の設計を専門的に担当。図が必要な箇所を特定し、
  各図の目的・種類・配置位置・キャプション・要素構成を
  設計書として出力する。生成は book-figgen に委譲する。
tags:
  - book
  - visual
  - design
  - figure
---

# book-figdesign — ⑫ 図解・挿絵設計

各章の図表について設計書を作成する。生成（Mermaid/Nano Banana等）は book-figgen に委譲。

## Inputs / Outputs

- **In:** `BookSpec.json`（図表方針）、`{書籍タイトル}.md`、`toc.md`
- **Out:** `figure_design_spec.md`（設計書のみ — 生成物は含まない）

## ワークフロー

1. **各章を通読** — 図表が有効な箇所を特定
2. **図の必要箇所を抽出** — 複雑な概念、プロセス、比較、数値データ
3. **各図の設計** — 目的（理解促進/説得/記憶）、種類、配置位置、キャプション
4. **要素構成の定義** — ノード/ラベル/関係/接続先を一覧化
5. **図の主張を1文で定義** — この図が伝える核心メッセージ
6. **3段階レビューチェーン:**
   - book-qa に提出（G12-Q: 目的整合性、配置の妥当性チェック）
   - book-producer に提出（G12-P: ビジュアル戦略の一貫性チェック）
   - 著者に提出（G12-H: 図表設計の最終承認）

設計が承認されたら book-figgen に引き渡す。

> **⚠️ figgen への引き渡し時の注意:** book-figgen では全図に Nano Banana Pro プロンプトの生成が必須。Markdown表の原稿挿入だけでは完了とならない。

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/visual_types.md](references/visual_types.md) | 図の種類・選定基準を確認するとき |
| [templates/figure_design_spec.md](templates/figure_design_spec.md) | 設計書のフォーマットを確認するとき |
