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

### 実行層（①〜⑩）

| ゲートID | スキル | ステージ | タイミング | 承認内容 |
|---------|--------|---------|-----------|---------|
| G1-Q | book-strategy | QA | 戦略設計完了 | 完全性・内部整合性チェック |
| G1-P | book-strategy | Producer | QA通過後 | 戦略的妥当性チェック |
| G1-H | book-strategy | 人間 | Producer通過後 | ゴール・ペルソナ・魂の承認 |
| G2-Q | book-spec | QA | 制作条件完了 | 完全性・strategy整合性チェック |
| G2-P | book-spec | Producer | QA通過後 | 制作可能性チェック |
| G2-H | book-spec | 人間 | Producer通過後 | 制作条件の承認 |
| G3-Q | book-structure | QA | 全体設計完了 | 論理構造・網羅性・バランス |
| G3-P | book-structure | Producer | QA通過後 | 戦略整合性・読者体験 |
| G3-H | book-structure | 人間 | Producer通過後 | 章構成＋予算の承認 |
| G4-Q | book-title | QA | タイトル案完了 | SEOチェック・スコアリング検証 |
| G4-P | book-title | Producer | QA通過後 | 戦略適合性・市場ポジショニング |
| G4-H | book-title | 人間 | Producer通過後 | 最終タイトル決定 |
| G5-Q | book-heading | QA | 見出し設計完了 | 階層整合性・命名規則 |
| G5-P | book-heading | Producer | QA通過後 | 読者理解順序・戦略整合性 |
| G5-H | book-heading | 人間 | Producer通過後 | 見出し体系の承認 |
| G6-Q | book-draft | QA | サンプル/各章/あとがき | AI表現＋文体＋校正＋ファクト＋章間整合 |
| G6-P | book-draft | Producer | QA通過後 | 情報源遵守・戦略整合性 |
| G6-H | book-draft | 人間 | Producer通過後 | 各章の内容承認 |
| G7-Q | book-figdesign | QA | 図表設計完了 | 目的整合性・配置妥当性 |
| G7-P | book-figdesign | Producer | QA通過後 | ビジュアル戦略の一貫性 |
| G7-H | book-figdesign | 人間 | Producer通過後 | 図表設計の承認 |
| G8-Q | book-figgen | QA | 図表生成完了 | 正確性・テキスト視認性 |
| G8-P | book-figgen | Producer | QA通過後 | ブランド一貫性・品質 |
| G8-H | book-figgen | 人間 | Producer通過後 | 生成物の承認 |
| G9-Q | book-ingest | QA | 整形完了 | クリーニング品質・情報欠落なし |
| G9-P | book-ingest | Producer | QA通過後 | 情報源の完全性確認 |
| ~~G9-H~~ | _(省略)_ | — | — | 人間チェック不要 |
| G10-Q | book-export | QA | エクスポート完了 | フォーマット正確性 |
| G10-P | book-export | Producer | QA通過後 | 最終品質サインオフ |
| G10-H | book-export | 人間 | Producer通過後 | 最終稿の承認 |

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
