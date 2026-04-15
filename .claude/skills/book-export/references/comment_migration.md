# コメント移植手順 — 初稿 _commented.docx → 修正稿 _commented.docx

修正稿をエクスポートする際、初稿の `_commented.docx` に含まれる
Nano Banana Pro コメントを引き継ぐための手順。

---

## 前提知識: Word のコメント構造

Word (.docx) はZIPアーカイブであり、コメントは以下の2箇所に分散して保存される:

1. **`word/comments.xml`** — コメント定義（ID・著者・日付・本文）
2. **`word/document.xml`** — アンカーマーカー（どの段落のどの範囲にコメントが付くか）

**重要:** `comments.xml` だけコピーしてもWordはコメントを表示しない。
`document.xml` 内にアンカーマーカーが必要。

### アンカーマーカーの3要素

```xml
<!-- コメント範囲の開始 -->
<w:commentRangeStart w:id="0"/>

<!-- 段落テキスト... -->

<!-- コメント範囲の終了 -->
<w:commentRangeEnd w:id="0"/>

<!-- コメント参照（通常は同じRun内） -->
<w:r>
  <w:rPr>
    <w:rStyle w:val="CommentReference"/>
  </w:rPr>
  <w:commentReference w:id="0"/>
</w:r>
```

`w:id` は `comments.xml` 内のコメントIDと対応する。

---

## 移植手順

### Step 1: 修正稿の基本 Docx を生成

```bash
pandoc "{修正稿}.md" \
  --reference-doc="{初稿}.docx" \
  -o "{修正稿}.docx" \
  --from=markdown --to=docx
```

`--reference-doc` で初稿のスタイル（フォント・見出し・ページ設定）を継承。

### Step 2: 初稿からコメント情報を抽出

Python で初稿の `_commented.docx` を開き、以下を抽出:

```python
import zipfile
import xml.etree.ElementTree as ET

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# 1. comments.xml からコメントID一覧を取得
with zipfile.ZipFile('初稿_commented.docx', 'r') as zf:
    comments_xml = zf.read('word/comments.xml')
    doc_xml = zf.read('word/document.xml')

comments_tree = ET.fromstring(comments_xml)
comment_ids = [c.get(f'{{{W}}}id') for c in comments_tree.findall(f'{{{W}}}comment')]

# 2. document.xml から各コメントのアンカーテキストを特定
doc_tree = ET.fromstring(doc_xml)
comment_anchors = {}  # {comment_id: anchor_text}

for cid in comment_ids:
    # commentRangeStart を含む段落のテキストを取得
    for para in doc_tree.iter(f'{{{W}}}p'):
        range_starts = para.findall(f'.//{{{W}}}commentRangeStart')
        for rs in range_starts:
            if rs.get(f'{{{W}}}id') == cid:
                texts = para.findall(f'.//{{{W}}}t')
                anchor = ''.join(t.text or '' for t in texts).strip()
                comment_anchors[cid] = anchor
```

### Step 3: 修正稿にコメントを注入

```python
# 1. 修正稿 docx を ZIP として開く
with zipfile.ZipFile('修正稿.docx', 'r') as zf:
    second_doc_xml = zf.read('word/document.xml')
    existing_files = {name: zf.read(name) for name in zf.namelist()}

# 2. comments.xml を差し替え
existing_files['word/comments.xml'] = comments_xml

# 3. document.xml にアンカーマーカーを挿入
second_tree = ET.fromstring(second_doc_xml)
second_body = second_tree

for para in second_body.findall(f'.//{{{W}}}p'):
    para_text = ''.join(
        t.text or '' for t in para.findall(f'.//{{{W}}}t')
    ).strip()

    for cid, anchor_text in comment_anchors.items():
        if anchor_text and anchor_text in para_text:
            # commentRangeStart（段落先頭）
            range_start = ET.Element(f'{{{W}}}commentRangeStart')
            range_start.set(f'{{{W}}}id', cid)
            para.insert(0, range_start)

            # commentRangeEnd（段落末尾）
            range_end = ET.SubElement(para, f'{{{W}}}commentRangeEnd')
            range_end.set(f'{{{W}}}id', cid)

            # commentReference（Run要素として）
            ref_run = ET.SubElement(para, f'{{{W}}}r')
            ref_rpr = ET.SubElement(ref_run, f'{{{W}}}rPr')
            ref_style = ET.SubElement(ref_rpr, f'{{{W}}}rStyle')
            ref_style.set(f'{{{W}}}val', 'CommentReference')
            ref_elem = ET.SubElement(ref_run, f'{{{W}}}commentReference')
            ref_elem.set(f'{{{W}}}id', cid)
            break  # 1コメントにつき1段落のみマッチ

# 4. 修正済み document.xml で上書き
existing_files['word/document.xml'] = ET.tostring(second_tree, xml_declaration=True, encoding='UTF-8')

# 5. 新しい _commented.docx を書き出し
with zipfile.ZipFile('修正稿_commented.docx', 'w', zipfile.ZIP_DEFLATED) as zf_out:
    for name, data in existing_files.items():
        zf_out.writestr(name, data)
```

### Step 4: 検証

- Word で `_commented.docx` を開く
- 「校閲」タブでコメントが表示されることを確認
- コメント数が初稿と一致することを確認

---

## トラブルシューティング

| 症状 | 原因 | 対処 |
|------|------|------|
| コメントが表示されない | `document.xml` にアンカーマーカーがない | Step 3 を再実行 |
| コメント数が合わない | アンカーテキストが修正で変更された | アンカーテキストの部分一致で検索 |
| 「破損しています」エラー | XML名前空間の不整合 | `[Content_Types].xml` にコメント定義を追加 |
| ZIP重複警告 | Pandocが空の comments.xml を含む | 既存ファイル一覧をチェックして上書き |

## Content_Types.xml の確認

`[Content_Types].xml` に以下が含まれていない場合は追加:

```xml
<Override PartName="/word/comments.xml"
  ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>
```

## document.xml.rels の確認

`word/_rels/document.xml.rels` に以下が含まれていない場合は追加:

```xml
<Relationship Id="rIdComments"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
  Target="comments.xml"/>
```
