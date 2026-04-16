---
description: tldvナレッジから書籍を自動制作する
argument-hint: [テーマ・オプション]
allowed-tools: [Read, Glob, Grep, Bash, Write, Edit]
---

# /book-factory

既存の `book-factory` Skill を使い、テーマから書籍制作一式を作成する。

## Arguments

The user invoked this command with: $ARGUMENTS

- `$ARGUMENTS` を書籍テーマとして扱う。
- `$ARGUMENTS` が空の場合は、実行前に以下だけを簡潔にヒアリングする。
  - テーマ（必須）
  - ペルソナ（任意）
  - 分量または章数（任意。未指定ならSkillのデフォルト）
- `$ARGUMENTS` に「全部自動で」が含まれる場合は、G-0〜G-3の確認を省略し、完成原稿の段階だけ確認する。

## Required Reads

実行前に必ず以下を読む。

1. `AGENTS.md`
2. `.agents/skills/book-factory/SKILL.md`
3. 必要に応じて `.agents/skills/book-factory/SKILL.md` の「参照」にある下位Skill
4. `◆ AI生成文章の特徴と執筆のポイント.md`

## Execution Rules

- `tldv/` は情報源として読むだけで、絶対に編集しない。
- 情報源にない事実・エピソード・AIの推測を本文に入れない。
- 本文には出典、ファイルパス、行番号、タイムスタンプ参照を書かない。
- 根拠箇所は本文ではなく提出レポートや確認メモにだけ書く。
- 出力先は `output/{テーマスラッグ}/` にする。
- 既存の `.claude/skills/` はSkillの正本として扱い、Codexからは `.agents/skills/` 経由で参照する。

## Workflow

1. `$ARGUMENTS` からテーマ、ペルソナ、オプションを抽出する。
2. `book-factory` Skill のPhase 0〜5に従って進める。
3. 通常モードでは以下の確認ゲートを挟む。
   - G-0: tldv検索後、使用するナレッジファイル一覧
   - G-1: BookSpec生成後、戦略＋制作仕様
   - G-3: 構成設計後、目次＋タイトル＋見出し
   - G-4: 原稿完成後、完成原稿
4. 「全部自動で」モードではG-0〜G-3を省略し、G-4のみ実施する。
5. 最後に出力ファイル一覧、未完了項目、確認が必要な箇所を簡潔に報告する。
