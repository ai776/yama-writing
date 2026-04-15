#!/usr/bin/env python3
"""
Nano Banana Pro プロンプトを Docx のコメントとして挿入するスクリプト。

使い方:
  python3 add_nano_banana_comments.py <docx_path> <figure_gen_output_md_path> [output_path]

例:
  python3 add_nano_banana_comments.py "書籍.docx" "figure_gen_output.md"
  python3 add_nano_banana_comments.py "書籍.docx" "figure_gen_output.md" "書籍_with_comments.docx"

出力パスを省略すると、元のファイル名に _commented を付けて保存する。

依存:
  pip install python-docx
"""

import re
import shutil
import sys
import zipfile
from datetime import datetime
from io import BytesIO
from pathlib import Path
from xml.etree import ElementTree as ET

# Word XML namespaces
NAMESPACES = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006",
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
REL_TYPE_COMMENTS = (
    "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"
)
CT_COMMENTS = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"
)


def parse_figure_prompts(md_path: str) -> dict[str, str]:
    """figure_gen_output.md から fig-ID → Nano Banana プロンプトの辞書を返す。"""
    text = Path(md_path).read_text(encoding="utf-8")
    figures = {}
    sections = re.split(r"(?=^## fig-)", text, flags=re.MULTILINE)

    for section in sections:
        header_match = re.match(r"^## (fig-\d+-\d+):\s*(.+)", section)
        if not header_match:
            continue

        fig_id = header_match.group(1)
        prompt_match = re.search(
            r"\*\*NANO_BANANA_PROMPT:\*\*\s*```(.*?)```",
            section,
            re.DOTALL,
        )
        if prompt_match:
            figures[fig_id] = prompt_match.group(1).strip()

    return figures


def _build_comments_xml(comments_data: list[dict]) -> bytes:
    """コメントデータからword/comments.xmlのバイト列を生成する。"""
    root = ET.Element(f"{{{W}}}comments")
    root.set(f"xmlns:w", W)
    root.set(
        f"xmlns:r",
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    )

    for cdata in comments_data:
        comment = ET.SubElement(root, f"{{{W}}}comment")
        comment.set(f"{{{W}}}id", str(cdata["id"]))
        comment.set(f"{{{W}}}author", cdata["author"])
        comment.set(f"{{{W}}}date", cdata["date"])
        comment.set(f"{{{W}}}initials", cdata["author"][0])

        for line in cdata["text"].split("\n"):
            p = ET.SubElement(comment, f"{{{W}}}p")
            r = ET.SubElement(p, f"{{{W}}}r")
            t = ET.SubElement(r, f"{{{W}}}t")
            t.set("xml:space", "preserve")
            t.text = line

    ET.indent(root, space="  ")
    xml_bytes = ET.tostring(root, encoding="UTF-8", xml_declaration=True)
    return xml_bytes


def _inject_comment_markers(doc_xml: bytes, marker_map: dict[str, int]) -> bytes:
    """document.xml内の図キャプション段落にコメントマーカーを挿入する。"""
    ET.register_namespace("w", W)
    ET.register_namespace(
        "r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    )
    ET.register_namespace(
        "mc", "http://schemas.openxmlformats.org/markup-compatibility/2006"
    )
    ET.register_namespace(
        "wp", "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
    )
    ET.register_namespace(
        "a", "http://schemas.openxmlformats.org/drawingml/2006/main"
    )
    ET.register_namespace("wps", "http://schemas.microsoft.com/office/word/2010/wordprocessingShape")
    ET.register_namespace("w14", "http://schemas.microsoft.com/office/word/2010/wordml")
    ET.register_namespace("w15", "http://schemas.microsoft.com/office/word/2012/wordml")

    tree = ET.ElementTree(ET.fromstring(doc_xml))
    root = tree.getroot()

    fig_pattern = re.compile(r"図(\d+)-(\d+)")
    inserted = 0

    for para in root.iter(f"{{{W}}}p"):
        full_text = ""
        for t_elem in para.iter(f"{{{W}}}t"):
            if t_elem.text:
                full_text += t_elem.text

        match = fig_pattern.search(full_text)
        if not match:
            continue

        fig_id = f"fig-{match.group(1)}-{match.group(2)}"
        if fig_id not in marker_map:
            continue

        comment_id = marker_map[fig_id]

        range_start = ET.Element(f"{{{W}}}commentRangeStart")
        range_start.set(f"{{{W}}}id", str(comment_id))

        range_end = ET.Element(f"{{{W}}}commentRangeEnd")
        range_end.set(f"{{{W}}}id", str(comment_id))

        ref_run = ET.Element(f"{{{W}}}r")
        ref_rpr = ET.SubElement(ref_run, f"{{{W}}}rPr")
        ref_style = ET.SubElement(ref_rpr, f"{{{W}}}rStyle")
        ref_style.set(f"{{{W}}}val", "CommentReference")
        ref_elem = ET.SubElement(ref_run, f"{{{W}}}commentReference")
        ref_elem.set(f"{{{W}}}id", str(comment_id))

        para.insert(0, range_start)
        para.append(range_end)
        para.append(ref_run)

        inserted += 1
        del marker_map[fig_id]

    output = BytesIO()
    tree.write(output, encoding="UTF-8", xml_declaration=True)
    return output.getvalue(), inserted


def _ensure_comments_relationship(rels_xml: bytes) -> bytes:
    """word/_rels/document.xml.rels にコメントリレーションシップを追加する。"""
    tree = ET.ElementTree(ET.fromstring(rels_xml))
    root = tree.getroot()

    for rel in root:
        if rel.get("Type") == REL_TYPE_COMMENTS:
            return rels_xml

    max_id = 0
    for rel in root:
        rid = rel.get("Id", "")
        if rid.startswith("rId"):
            try:
                num = int(rid[3:])
                if num > max_id:
                    max_id = num
            except ValueError:
                pass

    new_rel = ET.SubElement(root, "Relationship")
    new_rel.set("Id", f"rId{max_id + 1}")
    new_rel.set("Type", REL_TYPE_COMMENTS)
    new_rel.set("Target", "comments.xml")

    output = BytesIO()
    tree.write(output, encoding="UTF-8", xml_declaration=True)
    return output.getvalue()


def _ensure_content_type(ct_xml: bytes) -> bytes:
    """[Content_Types].xml にコメントのContent Typeを追加する。"""
    tree = ET.ElementTree(ET.fromstring(ct_xml))
    root = tree.getroot()

    ns = "http://schemas.openxmlformats.org/package/2006/content-types"
    for override in root.findall(f"{{{ns}}}Override"):
        if override.get("PartName") == "/word/comments.xml":
            return ct_xml

    new_override = ET.SubElement(root, f"{{{ns}}}Override")
    new_override.set("PartName", "/word/comments.xml")
    new_override.set("ContentType", CT_COMMENTS)

    output = BytesIO()
    tree.write(output, encoding="UTF-8", xml_declaration=True)
    return output.getvalue()


def add_comments_to_docx(
    docx_path: str,
    figure_prompts: dict[str, str],
    output_path: str,
    author: str = "Nano Banana Pro",
) -> int:
    """Docx内の図キャプション段落にNano Bananaプロンプトをコメントとして挿入する。"""
    date_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    comments_data = []
    marker_map = {}
    for i, (fig_id, prompt) in enumerate(figure_prompts.items()):
        comments_data.append(
            {
                "id": i,
                "author": author,
                "date": date_str,
                "text": prompt,
            }
        )
        marker_map[fig_id] = i

    comments_xml = _build_comments_xml(comments_data)

    with zipfile.ZipFile(docx_path, "r") as zin:
        doc_xml = zin.read("word/document.xml")
        rels_xml = zin.read("word/_rels/document.xml.rels")
        ct_xml = zin.read("[Content_Types].xml")

        modified_doc, inserted = _inject_comment_markers(doc_xml, dict(marker_map))
        modified_rels = _ensure_comments_relationship(rels_xml)
        modified_ct = _ensure_content_type(ct_xml)

        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "word/document.xml":
                    zout.writestr(item, modified_doc)
                elif item.filename == "word/_rels/document.xml.rels":
                    zout.writestr(item, modified_rels)
                elif item.filename == "[Content_Types].xml":
                    zout.writestr(item, modified_ct)
                elif item.filename == "word/comments.xml":
                    continue
                else:
                    zout.writestr(item, zin.read(item.filename))

            zout.writestr("word/comments.xml", comments_xml)

    return inserted


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    docx_path = sys.argv[1]
    md_path = sys.argv[2]

    if len(sys.argv) >= 4:
        output_path = sys.argv[3]
    else:
        p = Path(docx_path)
        output_path = str(p.with_stem(p.stem + "_commented"))

    figure_prompts = parse_figure_prompts(md_path)
    print(f"Parsed {len(figure_prompts)} figures from {md_path}")

    count = add_comments_to_docx(docx_path, figure_prompts, output_path)
    print(f"Inserted {count} comments into {output_path}")

    remaining = len(figure_prompts) - count
    if remaining > 0:
        print(f"Warning: {remaining} figures not matched in docx")


if __name__ == "__main__":
    main()
