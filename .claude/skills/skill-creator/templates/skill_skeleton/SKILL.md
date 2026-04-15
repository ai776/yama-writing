---
name: {skill-name}
description: >
  {Skillの具体的な説明。Claudeが自動ロード判断に使うので、
  何をするSkillなのかを50文字以上で具体的に記述する。}
tags:
  - {tag1}
  - {tag2}
---

# {skill-name} — {Skillの短い名前}

## 役割

{このSkillが何を担当するかを2〜3文で説明}

## Inputs

| 入力 | 必須 | 説明 |
|------|------|------|
| {入力1} | YES/NO | {説明} |
| {入力2} | YES/NO | {説明} |

## Outputs

| 出力 | 形式 | 説明 |
|------|------|------|
| {出力1} | {Markdown/JSON/etc} | {説明} |

## ワークフロー

### Step 1: {ステップ名}

{このステップで何をするか}

### Step 2: {ステップ名}

{このステップで何をするか}

## 参照ファイル

- [templates/{template_file}](templates/{template_file}) — {説明}
- [references/{reference_file}](references/{reference_file}) — {説明}

## 承認ゲート

| # | タイミング | 内容 |
|---|------------|------|
| G{n} | {タイミング} | {承認内容} |
