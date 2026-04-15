# 書籍制作ワークフロー — 進行例（12スキル・3段階レビュー版）

## 想定シナリオ

セミナー文字起こしから書籍を作成する場合の典型的な進行例。
各ステップで **3段階レビューチェーン**（QA→プロデューサー→人間）を通過する。

---

### Step 0: `/book-producer` で制作開始

```
ユーザー: /book-producer
```

**book-producer のアクション:**
1. 著者の要望を受け、制作スコープを把握
2. book-strategy を呼び出し → StrategySpec を受領
3. book-spec を呼び出し → ProductionSpec を受領
4. StrategySpec + ProductionSpec を統合 → BookSpec を生成
5. 著者に BookSpec の最終承認を求める（G0-H）

```
AI: BookSpec を作成しました。以下の内容でよろしいでしょうか？
（BookSpec の内容を表示）
ご確認いただけましたら「承認」とお伝えください。
```

---

### Step 1: `/book-strategy` — 戦略設計

**3段階レビュー:**
- book-qa が校閲（G1-Q: 完全性・内部整合性）
- book-producer が確認（G1-P: 戦略的妥当性）
- 著者が承認（G1-H: ゴール・ペルソナ・魂の承認）

→ 出力: `StrategySpec.md` / `StrategySpec.json`

---

### Step 2: `/book-spec` — 制作条件設計

**3段階レビュー:**
- book-qa が校閲（G2-Q: 完全性・strategy整合性）
- book-producer が確認（G2-P: 制作可能性）
- 著者が承認（G2-H: 制作条件の承認）

→ 出力: `ProductionSpec.md` / `ProductionSpec.json`

---

### Step 3: `/book-ingest` — 素材整形

```
ユーザー: /book-ingest
（文字起こしファイルをアップロード）
```

**レビュー（人間チェック省略）:**
- book-qa が校閲（G9-Q: クリーニング品質・情報欠落なし）
- book-producer が確認（G9-P: 情報源の完全性）
- ※人間チェックは省略

→ 出力: `cleaned_transcript.md`

---

### Step 4: `/book-structure` — 全体設計

**3段階レビュー:**
- book-qa が校閲（G3-Q: 論理構造・網羅性・バランス）
- book-producer が確認（G3-P: 戦略整合性・読者体験）
- 著者が承認（G3-H: 章構成＋予算の承認）

→ 出力: `toc.md`, `chapter_budget.md`

---

### Step 5: `/book-title` — タイトル決定

**3段階レビュー:**
- book-qa が校閲（G4-Q: SEOチェック・スコアリング検証）
- book-producer が確認（G4-P: 戦略適合性・市場ポジショニング）
- 著者が承認（G4-H: 最終タイトル決定）

→ 出力: `title_proposal.md`

---

### Step 6: `/book-heading` — 見出し設計

**3段階レビュー:**
- book-qa が校閲（G5-Q: 階層整合性・命名規則）
- book-producer が確認（G5-P: 読者理解順序・戦略整合性）
- 著者が承認（G5-H: 見出し体系の承認）

→ 出力: `heading_spec.md`

---

### Step 7: `/book-draft` — 本文執筆（章ごと）

```
ユーザー: /book-draft
→ サンプル本文を提出 → 3段階レビュー → 文体確定
→ 第1章を執筆 → 3段階レビュー → 承認
→ 第2章を執筆 → 3段階レビュー → 承認
→ ...（繰り返し）
→ あとがきを執筆 → 3段階レビュー → 承認
```

**各章の3段階レビュー:**
- book-qa が校閲（G6-Q: AI表現＋文体＋校正＋ファクト＋章間整合）
- book-producer が確認（G6-P: 情報源遵守・戦略整合性）
- 著者が承認（G6-H: 各章の内容承認）

→ 出力: `{書籍タイトル}.md`（単一ファイルに追記）

---

### Step 8: `/book-figdesign` — 図表設計

**3段階レビュー:**
- book-qa が校閲（G7-Q: 目的整合性・配置妥当性）
- book-producer が確認（G7-P: ビジュアル戦略の一貫性）
- 著者が承認（G7-H: 図表設計の承認）

→ 出力: `figure_design_spec.md`

---

### Step 9: `/book-figgen` — 図表生成

**重要: Nano Banana Pro プロンプトは全図で必須。**
各図セクションの先頭にNano Bananaプロンプトを配置し、その後にMermaid/Tableを併記する。
Markdown表の原稿挿入だけで完了としないこと。

**成果物（2つ）:**
1. `figure_gen_output.md` — Nano Bananaプロンプト（必須）+ Mermaid/Table（任意）
2. 原稿への図表挿入 — Markdown表/Mermaidを本文に直接挿入

**3段階レビュー:**
- book-qa が校閲（G8-Q: 正確性・テキスト視認性・Nano Bananaプロンプトの完全性）
- book-producer が確認（G8-P: ブランド一貫性・品質）
- 著者が承認（G8-H: 生成物の承認）

→ 出力: `figure_gen_output.md`, `mermaid_snippets.md`

---

### Step 10: `/book-export` — エクスポート

**Pandocで直接変換を実行可能。** CLIから `pandoc` コマンドで Docx を生成する。

**推奨ルート（ルートB: Docx経由）:**
1. `brew install pandoc`（約180MB）
2. `pandoc "{書籍タイトル}.md" -o "{書籍タイトル}.docx" --toc --toc-depth=2`
3. Nano Banana コメント挿入（任意・推奨）:
   ```
   pip install python-docx
   python3 .claude/skills/book-export/references/add_nano_banana_comments.py \
     "{書籍タイトル}.docx" "figure_gen_output.md"
   ```
4. Docx を Word/Pages で開き、PDF として書き出し

> **注意:** PDF直接変換（ルートA）にはMacTeX（約5GB）が必要。ディスク容量不足で失敗しやすいため、ルートBを推奨。

**3段階レビュー:**
- book-qa が校閲（G10-Q: フォーマット正確性）
- book-producer が確認（G10-P: 最終品質サインオフ）
- 著者が承認（G10-H: 最終稿の承認）

→ 出力: `{書籍タイトル}_commented.docx` / `{書籍タイトル}.pdf`
