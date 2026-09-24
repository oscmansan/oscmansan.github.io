#!/usr/bin/env python3
"""Render _pages/cv.md to files/Oscar_Manas_CV.pdf.

Usage (from the repo root):
    python scripts/cv_pdf.py

Requires: pip install markdown weasyprint pyyaml
"""

import re
from pathlib import Path

import markdown
import yaml
from weasyprint import HTML

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_pages" / "cv.md"
PUBS = ROOT / "_publications"
FONTS = ROOT / "scripts" / "fonts"
OUT = ROOT / "files" / "Oscar_Manas_CV.pdf"

HEADER = """
<header>
  <h1>Oscar Mañas</h1>
  <p class="role">Research Scientist · Meta Superintelligence Labs · Zurich, Switzerland</p>
  <p class="links">
    <a href="https://oscmansan.github.io">oscmansan.github.io</a> ·
    <a href="https://www.linkedin.com/in/oscmansan">linkedin.com/in/oscmansan</a> ·
    <a href="https://scholar.google.com/citations?user=Crn-tf0AAAAJ">Google Scholar</a> ·
    <a href="https://github.com/oscmansan">github.com/oscmansan</a> ·
    <a href="https://x.com/oscmansan">x.com/oscmansan</a>
  </p>
</header>
"""

CSS = f"""
@font-face {{ font-family: "Inter"; font-weight: 400; src: url("{(FONTS / 'Inter-Regular.ttf').as_uri()}"); }}
@font-face {{ font-family: "Inter"; font-weight: 600; src: url("{(FONTS / 'Inter-SemiBold.ttf').as_uri()}"); }}
@font-face {{ font-family: "Newsreader"; font-weight: 500; src: url("{(FONTS / 'Newsreader-Medium.ttf').as_uri()}"); }}
""" + """
@page { size: A4; margin: 16mm 18mm; }
body {
  font-family: "Inter", sans-serif;
  font-size: 9.5pt;
  line-height: 1.4;
  color: #1d1b18;
}
a { color: #b0492c; text-decoration: none; }
header { margin-bottom: 4mm; }
h1 { font-family: "Newsreader", serif; font-size: 24pt; font-weight: 500; margin: 0; letter-spacing: -0.01em; }
.role { margin: 1mm 0 0; font-size: 10.5pt; }
.links { margin: 1mm 0 0; color: #6b655c; font-size: 8.5pt; }
.links a { white-space: nowrap; }
h2 {
  font-size: 9pt;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #6b655c;
  border-bottom: 0.5pt solid #e0d9cc;
  padding-bottom: 1mm;
  margin: 5mm 0 2mm;
}
ul { margin: 0; padding-left: 4mm; }
li { margin: 0 0 1.2mm; }
li > ul { margin-top: 0.5mm; color: #4a453e; }
li > ul > li { margin-bottom: 0; }
.cv-date { float: right; color: #6b655c; margin-left: 4mm; }
ol.pubs { padding-left: 5mm; }
ol.pubs li { margin-bottom: 1.8mm; }
.pub-title, .pub-title a { font-weight: 600; color: #1d1b18; }
.pub-authors { color: #4a453e; }
.pub-venue { color: #6b655c; }
p { margin: 0 0 2mm; }
h2 { break-after: avoid; }
li { break-inside: avoid; }
"""


def cv_markdown() -> str:
    text = SRC.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)  # front matter
    text = re.sub(r"\{%.*?%\}", "", text)  # Liquid tags
    text = re.sub(r"^.*\n\{: \.web-only\}\n", "", text, flags=re.M)  # website-only lines
    # Jekyll's kramdown nests lists with 2-space indents; Python-Markdown needs 4.
    text = re.sub(r"^( +)(?=[*-] )", lambda m: m.group(1) * 2, text, flags=re.M)
    return text


def publications_html() -> str:
    """Publications section built from the same _publications/ files as the website."""
    pubs = []
    for path in PUBS.glob("*.md"):
        meta = yaml.safe_load(path.read_text(encoding="utf-8").split("---")[1])
        pubs.append(meta)
    pubs.sort(key=lambda m: m.get("sort_date", 0), reverse=True)

    items = []
    for m in pubs:
        title = m["title"]
        if m.get("paperurl"):
            title = f'<a href="{m["paperurl"]}">{title}</a>'
        items.append(
            f'<li><span class="pub-title">{title}</span><br>'
            f'<span class="pub-authors">{m["authors"]}</span><br>'
            f'<span class="pub-venue">{m["venue"]}</span></li>'
        )
    return '<h2>Publications</h2>\n<ol class="pubs">\n' + "\n".join(items) + "\n</ol>\n"


def main() -> None:
    body = markdown.markdown(cv_markdown(), extensions=["smarty"])
    # Publications go right after Education, before the remaining sections.
    marker = '<h2 id="technical-skills">' if '<h2 id="technical-skills">' in body else "<h2>Technical Skills</h2>"
    body = body.replace(marker, publications_html() + marker, 1)
    meta = (
        "<title>Oscar Mañas — CV</title>"
        '<meta name="author" content="Oscar Mañas">'
        '<meta name="description" content="CV of Oscar Mañas, Research Scientist at Meta Superintelligence Labs: multimodal AI, vision-language models, world models, embodied and physical AI.">'
        '<meta name="keywords" content="multimodal AI, vision-language models, vision-language-action models, world models, embodied AI, physical AI, robotics, reward models, image and video generation">'
    )
    html = f'<html><head><meta charset="utf-8">{meta}<style>{CSS}</style></head><body>{HEADER}{body}</body></html>'
    OUT.parent.mkdir(exist_ok=True)
    HTML(string=html, base_url=str(ROOT)).write_pdf(OUT)
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
