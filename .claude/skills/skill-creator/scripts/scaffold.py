#!/usr/bin/env python3
"""
Skill Scaffolder — 新しいSkillディレクトリをテンプレートから生成する

使い方:
    python scaffold.py <skill-name> [--description "説明"] [--tags tag1,tag2]

例:
    python scaffold.py book-analytics --description "原稿の文字数・構成を分析する" --tags book,analytics
"""

import argparse
import os
import sys
from pathlib import Path


SKILL_MD_TEMPLATE = '''---
name: {name}
description: >
  {description}
tags:
{tags_yaml}
---

# {name} — {short_description}

## 役割

{description}

## Inputs

| 入力 | 必須 | 説明 |
|------|------|------|
| (入力を定義してください) | YES | |

## Outputs

| 出力 | 形式 | 説明 |
|------|------|------|
| (出力を定義してください) | Markdown | |

## ワークフロー

### Step 1: (ステップを定義してください)

(このステップの内容を記述)

## 参照ファイル

- [templates/](templates/) — 出力テンプレート
- [references/](references/) — 参照ドキュメント

## 承認ゲート

| # | タイミング | 内容 |
|---|------------|------|
| G1 | (タイミングを定義) | (承認内容を定義) |
'''


def create_skill(name: str, description: str, tags: list[str]) -> Path:
    """Skillディレクトリを生成する"""
    base_dir = Path(__file__).resolve().parent.parent.parent
    skill_dir = base_dir / name

    if skill_dir.exists():
        print(f"Error: {skill_dir} already exists", file=sys.stderr)
        sys.exit(1)

    # ディレクトリ作成
    (skill_dir / "templates").mkdir(parents=True)
    (skill_dir / "references").mkdir(parents=True)

    # tags YAML
    tags_yaml = "\n".join(f"  - {tag}" for tag in tags)

    # 短い説明（descriptionの最初の20文字）
    short_description = description[:20] + ("..." if len(description) > 20 else "")

    # SKILL.md 生成
    skill_md_content = SKILL_MD_TEMPLATE.format(
        name=name,
        description=description,
        tags_yaml=tags_yaml,
        short_description=short_description,
    )

    (skill_dir / "SKILL.md").write_text(skill_md_content, encoding="utf-8")
    (skill_dir / "templates" / ".gitkeep").touch()
    (skill_dir / "references" / ".gitkeep").touch()

    return skill_dir


def main():
    parser = argparse.ArgumentParser(
        description="Claude Code Agent Skill のスキャフォールドを生成する"
    )
    parser.add_argument(
        "name",
        help="Skill名（kebab-case）",
    )
    parser.add_argument(
        "--description",
        default="(説明を記入してください)",
        help="Skillの説明",
    )
    parser.add_argument(
        "--tags",
        default="",
        help="タグ（カンマ区切り）",
    )

    args = parser.parse_args()

    # バリデーション
    if not all(c.isalnum() or c == "-" for c in args.name):
        print("Error: Skill名は kebab-case (英数字とハイフンのみ) にしてください", file=sys.stderr)
        sys.exit(1)

    tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else ["general"]

    skill_dir = create_skill(args.name, args.description, tags)
    print(f"Skill '{args.name}' を生成しました: {skill_dir}")
    print()
    print("次のステップ:")
    print(f"  1. {skill_dir}/SKILL.md を編集して詳細を記入")
    print(f"  2. {skill_dir}/templates/ に出力テンプレートを追加")
    print(f"  3. {skill_dir}/references/ に参照ドキュメントを追加")


if __name__ == "__main__":
    main()
