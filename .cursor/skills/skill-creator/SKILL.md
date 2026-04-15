---
name: skill-creator
description: >
  Claude Code Agent Skillsを量産するメタSkill。
  設計・スキャフォールディング・品質チェックを支援する。
disable-model-invocation: true
tags:
  - meta
  - skill
  - generator
---

# skill-creator — Skill 量産ツール（手動実行専用）

新しい Skill を設計・生成するためのメタSkill。

## Inputs / Outputs

- **In:** Skill名（kebab-case）、目的、Inputs/Outputs の定義
- **Out:** Skillディレクトリ一式（SKILL.md + templates/ + references/）

## ワークフロー

1. ヒアリング（名前・目的・I/O・承認ゲート・参照ファイル）
2. templates/skill_skeleton/ をベースにスキャフォールド生成
3. 品質チェック（frontmatter・description・I/O・承認ゲートの存在確認）

CLI でも実行可:
```bash
python .claude/skills/skill-creator/scripts/scaffold.py my-skill --description "説明" --tags tag1,tag2
```

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/how_to_write_skills.md](references/how_to_write_skills.md) | 良いSkillの設計基準を確認するとき |
| [templates/skill_skeleton/SKILL.md](templates/skill_skeleton/SKILL.md) | テンプレートを確認するとき |
