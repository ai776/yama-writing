# 良い Skill の作り方ガイド

## Claude Code Agent Skills とは

Claude Code の Skill は、特定のタスクを再現性高く実行するための
**構造化されたプロンプト＋テンプレート＋参照ドキュメント** のパッケージ。

## ディレクトリ構成

```
.claude/skills/{skill-name}/
├── SKILL.md          ← 必須。frontmatter + 本文
├── templates/        ← 出力テンプレート
│   └── output.md
├── references/       ← 参照ドキュメント
│   └── rules.md
├── examples/         ← 使用例（任意）
│   └── sample.md
└── scripts/          ← 補助スクリプト（任意）
    └── helper.py
```

## SKILL.md の構成

### 1. YAML Frontmatter（必須）

```yaml
---
name: my-skill              # kebab-case。/slash-command名になる
description: >               # 具体的に。Claudeの自動ロード判断に使われる
  何をするSkillなのかを50文字以上で具体的に記述。
  曖昧な説明はClaudeが適切にロードできない原因になる。
tags:                        # 関連タグ
  - category
  - subcategory
disable-model-invocation: true  # 任意。trueで自動発火を抑制
---
```

### 2. 本文の構成要素

| セクション | 必須 | 内容 |
|-----------|------|------|
| 役割 | YES | 1パラグラフでSkillの責務を説明 |
| Inputs | YES | 入力の表（名前・必須/任意・説明） |
| Outputs | YES | 出力の表（名前・形式・説明） |
| ワークフロー | YES | ステップバイステップの手順 |
| 参照ファイル | YES | templates/references へのリンク |
| 承認ゲート | 推奨 | いつ人間に確認するかの表 |

## 良い Skill の特徴

### DO（やるべきこと）

1. **SKILL.md を短く保つ** — 詳細は references/ に分離
2. **description を具体的にする** — 「テキストを処理する」ではなく「セミナー文字起こしからフィラーワードを除去し整形済みMarkdownを生成する」
3. **承認ゲートを明示する** — 人間が介入するタイミングを明確に
4. **テンプレートを用意する** — 出力のフォーマットを統一
5. **Inputs/Outputs を明確にする** — 何が入り、何が出るか
6. **前後のSkillとの接続を意識する** — ワークフロー全体での位置付け

### DON'T（やってはいけないこと）

1. **SKILL.md に全部書かない** — 長すぎるとClaudeが全部読み切れない
2. **description を曖昧にしない** — Claudeが適切にロードできなくなる
3. **承認ゲートを省略しない** — 人間のレビューなしで進むと品質が下がる
4. **テンプレートなしで出力形式を指示しない** — 再現性が下がる
5. **name に大文字やスペースを使わない** — kebab-case 厳守

## Skill 設計のチェックリスト

- [ ] name が kebab-case か
- [ ] description が50文字以上で具体的か
- [ ] SKILL.md のファイルサイズが適切か（目安: 200行以下）
- [ ] Inputs/Outputs が表形式で明確か
- [ ] ワークフローがステップバイステップか
- [ ] 承認ゲートが定義されているか
- [ ] 参照ファイルへのリンクが正しいか
- [ ] テンプレートファイルが存在するか
- [ ] tags が適切に設定されているか
- [ ] 他のSkillとの依存関係が明確か
