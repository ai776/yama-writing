---
name: book-figgen
description: >
  承認済みの図表設計書に基づき、Mermaidコード・Markdown表・SVG・
  Nano Banana Pro画像生成プロンプトを生成する。
  設計は book-figdesign が担当し、本スキルは生成のみを行う。
tags:
  - book
  - visual
  - generation
  - mermaid
  - nano-banana
---

# book-figgen — ⑬ 図解生成

承認済みの設計書（figure_design_spec.md）をもとに、実際の図表を生成する。

## Inputs / Outputs

- **In:** `figure_design_spec.md`（承認済み）、`BookSpec.json`
- **Out:** `figure_gen_output.md`（Mermaid + Table + Nano Banana プロンプト）、`mermaid_snippets.md`

## ワークフロー

1. **figure_design_spec.md を読み込み** — 承認済みの設計を確認
2. **各図について生成（出力順序を厳守）:**
   - **Nano Banana Pro プロンプト** — 全図で必須。**各図セクションの先頭に配置**（最も重要な成果物のため、誰が見てもすぐ見つけられるようにする）
   - **Nano Banana Variations** — 任意（3案）
   - **Mermaid** — 構造化データで表現可能なら併記
   - **Markdown Table** — 表形式で表現可能なら併記
3. **出力ファイルにまとめる**
4. **3段階レビューチェーン:**
   - book-qa に提出（G13-Q: 正確性、テキスト視認性チェック）
   - book-producer に提出（G13-P: ブランド一貫性、品質チェック）
   - 著者に提出（G13-H: 生成物の最終承認）

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/nano_banana_prompting.md](references/nano_banana_prompting.md) | Nano Banana Pro プロンプトの書き方を確認するとき |
| [templates/figure_gen_output.md](templates/figure_gen_output.md) | 出力フォーマットを確認するとき |
| [templates/mermaid_snippets.md](templates/mermaid_snippets.md) | Mermaidテンプレートを確認するとき |
