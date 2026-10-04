#!/usr/bin/env python3
"""Generate the 1200x630 social share card (og:image) into images/og-card.jpg.

This is the preview LinkedIn, Slack, X, etc. show for links to the site.
Text on the left (name, role, URL), portrait on the right, in the
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
PAPER, INK = "#f5f7fb", "#151c33"
INDIGO, GREEN = "#3a47b3", "#36773f"

NAME = "Oscar Mañas"
ROLE = "Research Scientist at Meta"
URL = "oscmansan.github.io"


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def main():
    card = Image.new("RGB", (W, H), PAPER)

    photo = Image.open(PHOTO).convert("RGB")
    photo = ImageOps.fit(photo, (PHOTO_W, H), Image.LANCZOS, centering=(0.5, 0.35))
    card.paste(photo, (W - PHOTO_W, 0))

    d = ImageDraw.Draw(card)
    x = 72

    # Block of bar + name + role, vertically centred; URL pinned to the bottom
    d.rectangle([x, 196, x + 56, 202], fill=INDIGO)  # heading bar, as on the site
    d.text((x, 226), NAME, font=font("Newsreader-Medium.ttf", 88), fill=INK)
    d.text((x, 352), ROLE, font=font("Inter-SemiBold.ttf", 34), fill=INK)
    d.text((x, H - 96), URL, font=font("Inter-SemiBold.ttf", 28), fill=GREEN)

    card.save(OUT, quality=88, optimize=True, progressive=True)
    print(f"wrote {OUT.relative_to(ROOT)} ({W}x{H})")


if __name__ == "__main__":
    main()
