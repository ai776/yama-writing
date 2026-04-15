---
name: book-structure
description: >
  書籍全体の設計を担当。章構成・文字数予算配分に加えて、
  論理構造の設計、ストーリーフロー（読者体験の流れ）の設計を行い、
  目次案と文字数予算表を出力する。
tags:
  - book
  - structure
  - outline
  - design
---

# book-structure — ⑤ 全体設計

章構成・文字数予算・論理構造・ストーリーフローを設計する。

## Inputs / Outputs

- **In:** `BookSpec.json`（統合版）、`cleaned_transcript.md`
- **Out:** `toc.md`（目次構成案）、`chapter_budget.md`（文字数予算）

## ワークフロー

1. **cleaned_transcript.md を通読** — 主要トピックを抽出
2. **構成パターン選定** — BookSpec の「書籍の役割」と情報源タイプに基づき、最適な構成パターンを選択（structure_guidelines.md の選定基準表を参照）
3. **論理構造設計** — 選定パターンに沿って、議論の因果関係・前提→結論の流れを整理
4. **ストーリーフロー設計** — 読者の感情・理解の流れ（共感→発見→行動）
5. **章構成作成** — 読者の理解が進む論理順に並べ、目次を作成
6. **文字数予算配分** — 核心トピックに傾斜配分
6. **3段階レビューチェーン:**
   - book-qa に提出（G5-Q: 論理構造・網羅性・バランスチェック）
   - book-producer に提出（G5-P: 戦略整合性・読者体験チェック）
   - 著者に提出（G5-H: 章構成＋予算の最終承認）

## 目次の条件

- 章: `# 第〇章 [タイトル]` / 小見出し: `## [タイトル]`
- 核心トピックの小見出しは末尾に `*`
- 各小見出しに対応する情報源箇所を注記

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/structure_guidelines.md](references/structure_guidelines.md) | 構成パターン選定・論理構造・ストーリーフロー設計のルールを確認するとき |
| [templates/toc.md](templates/toc.md) | 目次のフォーマットを確認するとき |
| [templates/chapter_budget.md](templates/chapter_budget.md) | 文字数予算の配分ルールを確認するとき |
