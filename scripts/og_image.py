#!/usr/bin/env python3
"""Generate the 1200x630 social share card (og:image) into images/og-card.jpg.

This is the preview LinkedIn, Slack, X, etc. show for links to the site.
Text on the left (name, role, topics, URL), portrait on the right, in the
Sonoma palette. images/og-image.jpg stays the square portrait used by JSON-LD.

Usage (from the repo root):
    python scripts/og_image.py

Requires: pip install pillow
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "scripts" / "fonts"
PHOTO = ROOT / "images" / "og-image.jpg"
OUT = ROOT / "images" / "og-card.jpg"

W, H = 1200, 630
PHOTO_W = 470  # portrait column on the right
PAPER, INK, MUTED = "#f5f7fb", "#151c33", "#5b6478"
INDIGO, GREEN = "#3a47b3", "#36773f"

NAME = "Oscar Mañas"
ROLE = ["Research Scientist", "Meta Superintelligence Labs"]
TOPICS = "Multimodal AI · Vision-language models · World models · Embodied AI"
URL = "oscmansan.github.io"


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def wrap(draw, text, fnt, width):
    """Greedy wrap on the ' · ' separators so topics never split mid-phrase."""
    lines, cur = [], ""
    for part in text.split(" · "):
        trial = f"{cur} · {part}" if cur else part
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = part
    return lines + [cur]


def main():
    card = Image.new("RGB", (W, H), PAPER)

    photo = Image.open(PHOTO).convert("RGB")
    photo = ImageOps.fit(photo, (PHOTO_W, H), Image.LANCZOS, centering=(0.5, 0.35))
    card.paste(photo, (W - PHOTO_W, 0))

    d = ImageDraw.Draw(card)
    x, text_w = 72, W - PHOTO_W - 72 - 48

    d.rectangle([x, 92, x + 56, 98], fill=INDIGO)  # heading bar, as on the site
    d.text((x, 122), NAME, font=font("Newsreader-Medium.ttf", 84), fill=INK)

    y = 250
    role_font = font("Inter-SemiBold.ttf", 32)
    for line in ROLE:
        d.text((x, y), line, font=role_font, fill=INK)
        y += 44

    y += 26
    topic_font = font("Inter-Regular.ttf", 26)
    for line in wrap(d, TOPICS, topic_font, text_w):
        d.text((x, y), line, font=topic_font, fill=MUTED)
        y += 38

    d.text((x, H - 96), URL, font=font("Inter-SemiBold.ttf", 28), fill=GREEN)

    card.save(OUT, quality=88, optimize=True, progressive=True)
    print(f"wrote {OUT.relative_to(ROOT)} ({W}x{H})")


if __name__ == "__main__":
    main()
