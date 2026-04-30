#!/usr/bin/env python3
"""Generate a simple Word document from the edited RFP markdown file.

The script intentionally uses only the Python standard library so the document
can be regenerated in minimal CI or cloud-agent environments.
"""

from __future__ import annotations

import html
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "cagri-merkezi-rfp-duzenlenmis-ozet.md"
OUTPUT = ROOT / "docs" / "cagri-merkezi-rfp-duzenlenmis-ozet.docx"


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""

APP_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
  xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Cursor Cloud Agent</Application>
</Properties>
"""

CORE_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/"
  xmlns:dcmitype="http://purl.org/dc/dcmitype/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Çağrı Merkezi Projesi RFP Dokümanı</dc:title>
  <dc:subject>Düzenlenmiş ve özetlenmiş RFP dokümanı</dc:subject>
  <dc:creator>Cursor Cloud Agent</dc:creator>
  <cp:keywords>RFP;Çağrı Merkezi;Yetkilendirme;Güvenlik Seviyesi</cp:keywords>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-04-30T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-04-30T00:00:00Z</dcterms:modified>
</cp:coreProperties>
"""

STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr>
    <w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/><w:sz w:val="22"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Title">
    <w:name w:val="Title"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:after="240"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="34"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="360" w:after="160"/><w:outlineLvl w:val="0"/></w:pPr>
    <w:rPr><w:b/><w:color w:val="1F4E79"/><w:sz w:val="30"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="240" w:after="120"/><w:outlineLvl w:val="1"/></w:pPr>
    <w:rPr><w:b/><w:color w:val="2F75B5"/><w:sz w:val="26"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListParagraph">
    <w:name w:val="List Paragraph"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr>
  </w:style>
</w:styles>
"""


def inline_runs(text: str) -> str:
    """Convert a small subset of Markdown inline syntax into Word runs."""
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    runs: list[str] = []
    for part in parts:
        if not part:
            continue
        bold = part.startswith("**") and part.endswith("**")
        value = part[2:-2] if bold else part
        value = value.replace("  ", " ")
        escaped = html.escape(value, quote=False)
        preserve = ' xml:space="preserve"' if escaped.startswith(" ") or escaped.endswith(" ") else ""
        if bold:
            runs.append(f"<w:r><w:rPr><w:b/></w:rPr><w:t{preserve}>{escaped}</w:t></w:r>")
        else:
            runs.append(f"<w:r><w:t{preserve}>{escaped}</w:t></w:r>")
    return "".join(runs)


def paragraph(text: str, style: str | None = None, indent_level: int = 0) -> str:
    style_xml = f'<w:pStyle w:val="{style}"/>' if style else ""
    indent_xml = ""
    if indent_level:
        left = 720 + (indent_level - 1) * 360
        indent_xml = f'<w:ind w:left="{left}" w:hanging="360"/>'
    ppr = f"<w:pPr>{style_xml}{indent_xml}</w:pPr>" if style_xml or indent_xml else ""
    return f"<w:p>{ppr}{inline_runs(text)}</w:p>"


def render_markdown(markdown: str) -> str:
    body: list[str] = []
    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        if not line:
            body.append("<w:p/>")
            continue
        if line.startswith("# "):
            body.append(paragraph(line[2:], "Title"))
        elif line.startswith("## "):
            body.append(paragraph(line[3:], "Heading1"))
        elif line.startswith("### "):
            body.append(paragraph(line[4:], "Heading2"))
        elif line.lstrip().startswith("- "):
            leading_spaces = len(line) - len(line.lstrip(" "))
            indent_level = 1 + leading_spaces // 2
            body.append(paragraph("• " + line.lstrip()[2:], "ListParagraph", indent_level))
        else:
            body.append(paragraph(line))
    return "\n".join(body)


def build_document_xml(markdown: str) -> str:
    rendered = render_markdown(markdown)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {rendered}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
"""


def main() -> None:
    markdown = SOURCE.read_text(encoding="utf-8")
    document_xml = build_document_xml(markdown)

    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", ROOT_RELS)
        docx.writestr("docProps/app.xml", APP_XML)
        docx.writestr("docProps/core.xml", CORE_XML)
        docx.writestr("word/_rels/document.xml.rels", DOC_RELS)
        docx.writestr("word/styles.xml", STYLES_XML)
        docx.writestr("word/document.xml", document_xml)

    print(f"Generated {OUTPUT}")


if __name__ == "__main__":
    main()
