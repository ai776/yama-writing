---
name: book-producer
description: >
  書籍制作の全体統括プロデューサー。14の実行スキルと2つの品質保証スキルを
  オーケストレーションし、3段階レビューチェーン（QA→プロデューサー→人間）
  を統括する。BookSpec（戦略＋制作仕様の統合版）の最終承認と全工程の品質管理を担当。
tags:
  - book
  - production
  - orchestration
---

# book-producer — ⓪ プロデューサー（統括層）

制作ワークフロー全体を統括し、3段階レビューチェーンのプロデューサーゲートを担う。

## 役割

- 全体ゴール・方針・優先順位を保持（ブレ防止）
- 各工程の入出力をレビュー（品質／整合性／目的適合）
- 差し戻し判断（再生成／修正指示／追加調査）
- 工程間の矛盾解消（タイトル↔構成↔本文↔図解）
- 制作停止・方針転換判断（時間／品質／コスト基準）
- book-qa にチェックを依頼（必要に応じて）
- book-rewrite にリライトを指示（修正指示書がある場合）
- book-consistency に矛盾チェックを依頼（原稿完成時）
- 人間のチェック（重要判断のみ）

## Inputs / Outputs

- **In:** 著者の要望、StrategySpec（①から）、ProductionSpec（②から）、全スキル出力
- **Out:** `BookSpec.md`/`BookSpec.json`（統合版）、プロデューサーレビュー判定、ワークフロー進行ログ

## ワークフロー

1. 著者の要望を受け、制作スコープを把握
2. **book-strategy** に戦略設計を指示 → StrategySpec を受領
3. **book-spec** に制作条件設計を指示 → ProductionSpec を受領
4. StrategySpec + ProductionSpec を統合し **BookSpec** を生成
5. 著者に BookSpec の最終承認を求める（G0-H）
6. BookSpec 承認後、実行スキルを順次オーケストレーション
7. 各スキルの出力に対しプロデューサーゲート（G{n}-P）を実施

BookSpec 承認まで実行スキルを呼び出してはならない。

## オートパイロットモード（book-factory 連携）

book-factory から呼び出された場合、以下のルールでオートパイロット動作する:

### 変更点

1. **ヒアリング省略** — book-strategy / book-spec のヒアリングは省略し、テーマとtldvナレッジから自動推論
2. **承認ゲート簡略化** — 4箇所のみ（G-0: ナレッジ選定, G-1: BookSpec, G-3: 構成, G-4: 完成原稿）
3. **QAセルフチェック** — book-qa は実行するが、プロデューサーゲート(G{n}-P)は自動パスする
4. **出力先** — `output/{テーマスラッグ}/` に全成果物を集約

### オートパイロット時のワークフロー

```
テーマ受領 → tldv検索(G-0) → BookSpec自動生成(G-1)
→ ingest → knowledge → structure → title
→ chapter-blueprint → heading(G-3)
→ draft(章ごと) → consistency → figdesign → figgen(G-4)
→ export
```

### 判定基準

- book-factory から `mode: "autopilot"` が指定されている場合に適用
- ユーザーが「全部自動で」と指示した場合は G-0〜G-3 も省略可

## 工程別の重要注意事項

### ④ book-knowledge（ナレッジ生成）
- ③ book-ingest の後工程。cleaned_transcript.md から構造化ナレッジを生成する。
- タグ付き抽出（主張・理由・具体例・数値・反論・比喩・体験談・感情トーン・思想軸）。
- book-draft / book-heading が参照する情報源の精度を大幅に向上させる。
- ナレッジ生成後は著者承認（G4-H）を通過させること。

### ⑦ book-chapter-blueprint（章設計図）
- ⑤ book-structure の後工程。各章のBlueprint（章設計図）を作成する。
- 章の核心・壊す誤解・USP・禁止事項・必要要素・ストーリー構造を定義する。
- **⑧ book-heading より先に実行すること。Blueprint 未承認で見出し設計は禁止。**
- 著者承認（G7-H）を通過させること。

### ⑩ book-feedback-ingest（フィードバック取込）
- 編集者・校閲者のフィードバックを構造化し、⑪ book-rewrite の前工程。
- 修正指示の分類（全体方針/章単位/箇所単位/形式）と優先度判定（MUST/SHOULD/COULD）。
- 著者承認（G10-H）を通過させること（特に全体方針の変更時は必須）。

### ⑪ book-rewrite（リライト）
- 修正指示書（レビューシート）がある場合に使用。⑨ book-draft の後工程。
- 修正指示の分類・適用方針を人間に確認してからリライトに着手すること（G11-H）。
- リライト後は book-qa → book-producer → 人間 の3段階レビューを通過させる。
- 著者のトーン・パーソナリティの維持を最重要視する。

### ⑬ book-figgen（図表生成）
- **Nano Banana Pro プロンプトは全図で必須。** Markdown表の原稿挿入だけで完了としないこと。
- `figure_gen_output.md` には各図セクションの**先頭に**Nano Bananaプロンプトを配置すること。
- G13-Q/G13-P で Nano Banana プロンプトの存在と完全性を必ず確認すること。

### book-consistency（章間矛盾ゼロ化・品質保証層）
- ⑨ book-draft の後工程（全章完成後に実行）。
- 4つの台帳（定義・ルール・数値・推奨）を作成し、機械的に矛盾を検出する。
- 矛盾候補のペアと統一案を出力する。
- 統一案の採用は著者判断が必須。

## 3段階レビューチェーン

すべての実行スキル出力は以下の順で通過する:

```
スキル出力 → book-qa（校閲: G{n}-Q）→ book-producer（確認: G{n}-P）→ 人間（承認: G{n}-H）
```

※③ book-ingest のみ人間チェック省略

## 参照（必要なときだけ読み込む）

| ファイル | いつ読むか |
|---------|-----------|
| [references/approval_gates.md](references/approval_gates.md) | 承認ゲートの定義を確認するとき |
| [references/operational_rules.md](references/operational_rules.md) | 運用ルール（情報源厳守等）を確認するとき |
| [references/extraction_rules.md](references/extraction_rules.md) | ヒアリング項目の相互参照を確認するとき |
| [templates/BookSpec.md](templates/BookSpec.md) | BookSpec 統合版を生成するとき |
| [templates/BookSpec.json](templates/BookSpec.json) | BookSpec JSON を生成するとき |
| [examples/BookSpec_sample.md](examples/BookSpec_sample.md) | 記入例を見せたいとき |
| [examples/workflow_example.md](examples/workflow_example.md) | 全体の進行例を確認するとき |
