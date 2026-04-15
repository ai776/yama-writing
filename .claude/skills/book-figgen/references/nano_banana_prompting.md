# Nano Banana Pro プロンプトガイドライン

book-figgen Skill が各図の画像生成プロンプトを作成する際のルール。
Nano Banana Pro はテキスト描画・インフォグラフィック/図解・aspect ratio 制御が
強化されている前提で設計する。

---

## 基本構成要素（必須）

すべてのプロンプトに以下の5要素を明示する:

| 要素 | 説明 | 例 |
|------|------|-----|
| **Subject** | 図解の主題 | 「足首の3関節の連動メカニズム」 |
| **Composition** | レイアウト構成 | 左右分割 / 中央放射 / 上下フロー / グリッド / ピラミッド |
| **Action** | 図が示す動き・関係 | 「上から下へ力が伝達される様子」 |
| **Location** | 図の文脈・配置 | 「書籍本文中のインフォグラフィック」 |
| **Style** | 仕上げスタイル | フラット / ベクター / ミニマル / ブランド調 |

## 追加必須要素（図解特化）

### Composition + Aspect Ratio

- aspect ratio は **必ず** 指定: `16:9` / `4:3` / `1:1`
- 書籍用途では `4:3` または `16:9` が一般的
- 縦長が必要な場合は `3:4` や `9:16` も可

### Text Integration（テキスト描画）

図解には日本語テキストを画像内に入れる前提で設計する:

```
Text Integration:
  - Title: "タイトル文字列" — position: top-center, size: large, weight: bold
  - Label 1: "ラベル文字列" — position: near element 1
  - Label 2: "ラベル文字列" — position: near element 2
  - Annotation: "注釈文字列" — position: bottom-right, size: small
  - Font: bold, sans-serif, large (min 14pt equivalent)
  - Language: Japanese
```

**ルール:**
- タイトルは図の上部に大きく配置
- ラベルは対応する要素の近くに配置
- 小さすぎる文字は避ける（「文字は大きめ」を明示）
- フォントは太め・サンセリフを推奨
- 日本語であることを必ず明記

### Factual Constraints（正確性の担保）

図解は "正確性" が重要。入力自体が正しい前提で、以下を明記:

```
Constraints:
  - Factual: "3つの関節は 距腿関節 → 距骨下関節 → ショパール関節 の順に並ぶ"
  - Factual: "力の伝達方向は上から下"
  - Order matters: elements must appear in specified sequence
```

**ルール:**
- 要素の順序が重要な場合は明示
- 因果関係・包含関係がある場合は明示
- 数値がある場合は正確な数値を記載

## 推奨スタイル設定

書籍挿入用の図解として、以下を推奨:

| 項目 | 推奨値 | 理由 |
|------|--------|------|
| 背景 | 白 or 薄いグレー | 印刷・電子書籍の両方に対応 |
| 余白 | 多め（generous whitespace） | 読みやすさ・視認性 |
| デザイン | フラット / ベクター風 | クリーンで情報伝達に最適 |
| フォント | 太め・サンセリフ | 小さくても読みやすい |
| 色数 | 3〜5色以内 | 情報過多を避ける |
| ラベル | 短く（10文字以内推奨） | 図の中で読み切れる長さ |

## プロンプトの最終形式

上記の要素をすべて盛り込んだ上で、最終的に **自然な英文1段落** にまとめる:

```
Prompt:
"Create a clean, flat-design infographic showing [subject]. Layout: [composition],
aspect ratio [ratio]. Include Japanese text labels: '[ラベル1]' near [position],
'[ラベル2]' near [position]. Title '[タイトル]' at top-center in bold sans-serif.
Use [color palette] on white background with generous whitespace.
[Factual constraints]. All text must be clearly readable, no small fonts."
```

## 生成後の注意事項

- **誤字チェック必須:** AI画像生成はテキスト描画で誤字が発生しやすい。生成後に必ず日本語テキストの正確性を目視確認する
- **再生成の覚悟:** テキスト部分が不正確な場合は再生成する。プロンプトの Text Integration セクションをより詳細にすると改善しやすい
- **後処理の選択肢:** テキスト部分だけ画像編集ソフトで差し替えるのも有効な手段

## NANO_BANANA_VARIATIONS の作り方

3つのバリエーションを作る場合:

| # | バリエーション | 方針 |
|---|--------------|------|
| 1 | **最小構成** | 要素を最重要の2〜3個に絞る。余白最大。テキスト最小限。「一目で伝わる」が目標 |
| 2 | **ブランド強め** | 著者/書籍のブランドカラーを適用。ロゴ的な統一感。シリーズ展開を意識したレイアウト |
| 3 | **情報量多め** | 補足ラベル・注釈・サブテキストを追加。1枚で完結する「リファレンスカード」を目指す |
