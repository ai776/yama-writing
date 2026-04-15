# ヒアリング項目 相互参照インデックス

book-producer は自らヒアリングを実施せず、**book-strategy** と **book-spec** に委譲する。
本ファイルは両スキルの分担を俯瞰するためのインデックスである。

---

## 戦略項目（① book-strategy が担当）

詳細: `book-strategy/references/strategy_extraction_rules.md`

| # | 項目 | 概要 |
|---|------|------|
| S1 | 事業ゴール | 最終目的・CTA導線・バックエンド商品 |
| S2 | 想定読者（ペルソナ） | 年齢層・職業・悩み・価値観・接触場面 |
| S3 | KPI | 発行部数・LINE登録率・CVR等 |
| S4 | 核心メッセージ（魂） | 1文で表す本の主張 |
| S5 | 書籍の役割 | ファネル内でのポジション |

→ 出力: `StrategySpec.md` / `StrategySpec.json`

---

## 制作条件項目（② book-spec が担当）

詳細: `book-spec/references/spec_extraction_rules.md`

| # | 項目 | 概要 |
|---|------|------|
| P1 | 情報源タイプ（source_type） | seminar / youtube / reborn |
| P2 | トーン＆スタイル | 文体・口語許容度・語りのスタイル |
| P3 | 禁止表現 | 著者固有NGワード・業界NG表現 |
| P4 | 分量設計 | 総文字数・章数・まえがき/あとがき |
| P5 | 図表・挿絵方針 | 頻度・タイプ・配置・キャプション |
| P6 | 引用ルール | source_type連動の引用形式 |

→ 出力: `ProductionSpec.md` / `ProductionSpec.json`

---

## 統合（⓪ book-producer が担当）

1. StrategySpec + ProductionSpec を受領
2. 整合性を確認（戦略と制作条件の矛盾がないか）
3. `BookSpec.md` / `BookSpec.json` に統合
4. 著者に提示し最終承認（G0-H）

### source_type 固有の追加項目

| source_type | 追加ヒアリング | 担当 |
|-------------|--------------|------|
| youtube | チャンネルURL、動画リスト、選定基準 | book-spec |
| reborn | リボーン目的、維持する魂、新ターゲット | book-strategy + book-spec |
