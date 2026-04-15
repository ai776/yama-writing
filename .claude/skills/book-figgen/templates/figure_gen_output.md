# 図表生成物 — {書籍タイトル}

> 生成日: {date} | 総図表数: {total_figures}

---

## fig-1-1: {キャプション}

**NANO_BANANA_PROMPT:**（必須 — 各図セクションの先頭に配置すること）
```
Subject: {図解の主題}
Composition: {レイアウト}
Aspect Ratio: {16:9 / 4:3 / 1:1}
Style: {フラット / ベクター / ミニマル / ブランド調}

Text Integration:
  - Title: "{タイトルテキスト}" — position: {top-center}
  - Label 1: "{ラベル1}" — position: {要素1の近く}
  - Font: bold, large (min 14pt equivalent), sans-serif
  - Language: Japanese

Visual Elements:
  - {要素の視覚表現}

Color Palette: {色指定}
Background: white / light gray
Constraints:
  - Factual: {正確性制約}
  - No small text — all labels must be clearly readable

Prompt:
"{最終プロンプト文}"
```

**NANO_BANANA_VARIATIONS:**（任意 — 3案）

| # | バリエーション | 特徴 |
|---|--------------|------|
| 1 | 最小構成 | 要素を絞り、余白多め |
| 2 | ブランド強め | ブランドカラー適用 |
| 3 | 情報量多め | 補足ラベル追加 |

**Mermaid:**（任意 — 構造化データで表現可能な場合のみ）
```mermaid
{コード}
```

**Table:**（任意 — 表で表現可能な場合のみ）

| {列1} | {列2} | {列3} |
|--------|--------|--------|
| {値} | {値} | {値} |

---

<!-- 以下、全図について同形式で続く -->

---

## 生成サマリー

| ID | キャプション | Mermaid | Table | Nano Banana |
|----|-------------|---------|-------|-------------|
| fig-1-1 | {キャプション} | {有/無} | {有/無} | {有} |
