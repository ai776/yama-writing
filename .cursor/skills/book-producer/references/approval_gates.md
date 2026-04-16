# 承認ゲート定義（3段階レビューチェーン）

書籍制作の全工程において、**3段階レビューチェーン**を必ず通過すること。

```
スキル出力 → book-qa（校閲: G{n}-Q）→ book-producer（確認: G{n}-P）→ 人間（承認: G{n}-H）
```

## ゲート一覧

### 統括層

| ゲートID | スキル | ステージ | タイミング | 承認内容 |
|---------|--------|---------|-----------|---------|
| G0-H | book-producer | 人間 | BookSpec統合・提示時 | 統合BookSpecの最終承認 |

### 実行層（①〜⑭）

| ゲートID | スキル | ステージ | タイミング | 承認内容 |
|---------|--------|---------|-----------|---------|
| G1-Q | book-strategy | QA | 戦略設計完了 | 完全性・内部整合性チェック |
| G1-P | book-strategy | Producer | QA通過後 | 戦略的妥当性チェック |
| G1-H | book-strategy | 人間 | Producer通過後 | ゴール・ペルソナ・魂の承認 |
| G2-Q | book-spec | QA | 制作条件完了 | 完全性・strategy整合性チェック |
| G2-P | book-spec | Producer | QA通過後 | 制作可能性チェック |
| G2-H | book-spec | 人間 | Producer通過後 | 制作条件の承認 |
| G3-Q | book-ingest | QA | 整形完了 | クリーニング品質・情報欠落なし |
| G3-P | book-ingest | Producer | QA通過後 | 情報源の完全性確認 |
| ~~G3-H~~ | _(省略)_ | — | — | 人間チェック不要 |
| G4-Q | book-knowledge | QA | ナレッジ生成完了 | 抽出正確性・網羅性・タグ分類 |
| G4-P | book-knowledge | Producer | QA通過後 | 戦略整合性・核心メッセージ対応 |
| G4-H | book-knowledge | 人間 | Producer通過後 | ナレッジ内容の承認 |
| G5-Q | book-structure | QA | 全体設計完了 | 論理構造・網羅性・バランス |
| G5-P | book-structure | Producer | QA通過後 | 戦略整合性・読者体験 |
| G5-H | book-structure | 人間 | Producer通過後 | 章構成＋予算の承認 |
| G6-Q | book-title | QA | タイトル案完了 | SEOチェック・スコアリング検証 |
| G6-P | book-title | Producer | QA通過後 | 戦略適合性・市場ポジショニング |
| G6-H | book-title | 人間 | Producer通過後 | 最終タイトル決定 |
| G7-Q | book-chapter-blueprint | QA | Blueprint完了 | Blueprint間の整合性、BookSpec整合性 |
| G7-P | book-chapter-blueprint | Producer | QA通過後 | 戦略整合性、読者体験の設計 |
| G7-H | book-chapter-blueprint | 人間 | Producer通過後 | Blueprint の最終承認 |
| G8-Q | book-heading | QA | 見出し設計完了 | 階層整合性・命名規則 |
| G8-P | book-heading | Producer | QA通過後 | 読者理解順序・戦略整合性 |
| G8-H | book-heading | 人間 | Producer通過後 | 見出し体系の承認 |
| G9-Q | book-draft | QA | サンプル/各章/あとがき | AI表現＋文体＋校正＋ファクト＋章間整合 |
| G9-P | book-draft | Producer | QA通過後 | 情報源遵守・戦略整合性 |
| G9-H | book-draft | 人間 | Producer通過後 | 各章の内容承認 |
| G10-Q | book-feedback-ingest | QA | フィードバック取込完了 | 分類の正確性、網羅性 |
| G10-P | book-feedback-ingest | Producer | QA通過後 | 修正方針の妥当性 |
| G10-H | book-feedback-ingest | 人間 | Producer通過後 | 修正方針の承認 |
| G11-Q | book-rewrite | QA | リライト完了 | リライト品質の校閲 |
| G11-P | book-rewrite | Producer | QA通過後 | 全体整合性の確認 |
| G11-H | book-rewrite | 人間 | Producer通過後 | 最終承認 |
| G12-Q | book-figdesign | QA | 図表設計完了 | 目的整合性・配置妥当性 |
| G12-P | book-figdesign | Producer | QA通過後 | ビジュアル戦略の一貫性 |
| G12-H | book-figdesign | 人間 | Producer通過後 | 図表設計の承認 |
| G13-Q | book-figgen | QA | 図表生成完了 | 正確性・テキスト視認性・**Nano Banana Proプロンプトの完全性** |
| G13-P | book-figgen | Producer | QA通過後 | ブランド一貫性・品質・**Nano Bananaプロンプトが全図に存在すること** |
| G13-H | book-figgen | 人間 | Producer通過後 | 生成物の承認 |
| G14-Q | book-export | QA | エクスポート完了 | フォーマット正確性 |
| G14-P | book-export | Producer | QA通過後 | 最終品質サインオフ |
| G14-H | book-export | 人間 | Producer通過後 | 最終稿の承認 |

### 品質保証層（ゲート番号なし）

| ゲートID | スキル | ステージ | タイミング | 承認内容 |
|---------|--------|---------|-----------|---------|
| GC-Q | book-consistency | QA | 矛盾チェック完了 | 台帳の網羅性・矛盾検出の正確性 |
| GC-P | book-consistency | Producer | QA通過後 | 統一案の妥当性・戦略整合性 |
| GC-H | book-consistency | 人間 | Producer通過後 | 統一案の承認・採用判断 |

### 品質保証層

| ゲートID | スキル | ステージ | タイミング | 承認内容 |
|---------|--------|---------|-----------|---------|
| GQA-P | book-qa | Producer | QAレポート生成後 | QAの網羅性確認 |
| GQA-H | book-qa | 人間 | 重要所見がある場合 | QA所見の確認・修正承認 |

## 運用ルール

1. 各ゲートで明示的な承認（「OK」「承認」「進めてください」等）が出るまで待機する
2. フィードバックが出た場合は修正し、**QAゲートから**再度通す
3. 承認ゲートをスキップする場合は、著者からの明示的な指示が必要
4. ゲートの結果（承認/差し戻し/条件付き承認）は進行ログに記録する
5. 差し戻しが3回連続した場合、book-producer が方針転換を提案する
