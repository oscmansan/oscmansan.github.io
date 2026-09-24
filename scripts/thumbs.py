#!/usr/bin/env python3
"""Generate web-sized copies of the publication figures and the profile photo.

The originals in images/pubs/ are full-resolution figure exports (up to several
MB); the site shows them at ~150-220px wide. This writes small WebP copies to
images/pubs/thumbs/ (used by _includes/archive-single.html) and a 400px avatar.
Re-run after adding or changing a publication image.

Usage (from the repo root):
    python scripts/thumbs.py

Requires: pip install pillow
"""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
PUBS = ROOT / "images" / "pubs"
THUMBS = PUBS / "thumbs"
AVATAR_SRC = ROOT / "images" / "Oscar Mañas-19.jpg"
AVATAR_OUT = ROOT / "images" / "avatar-400.jpg"

THUMB_WIDTH = 480  # 2x the largest display width (220px on mobile)
AVATAR_SIZE = 400  # 2x the largest display size (175px in the sidebar)


def main() -> None:
    THUMBS.mkdir(exist_ok=True)
    for src in sorted(PUBS.iterdir()):
        if src.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        im = Image.open(src)
        im = im.convert("RGBA") if im.mode in ("P", "LA") else im
        if im.width > THUMB_WIDTH:
            im = im.resize((THUMB_WIDTH, round(im.height * THUMB_WIDTH / im.width)), Image.LANCZOS)
        out = THUMBS / (src.stem + ".webp")
        im.save(out, "WEBP", quality=85, method=6)
        print(f"{src.name}: {src.stat().st_size // 1024} KB -> {out.stat().st_size // 1024} KB")

    im = Image.open(AVATAR_SRC).convert("RGB")
    im.thumbnail((AVATAR_SIZE, AVATAR_SIZE), Image.LANCZOS)
    im.save(AVATAR_OUT, "JPEG", quality=85, optimize=True, progressive=True)
    print(f"{AVATAR_SRC.name}: {AVATAR_SRC.stat().st_size // 1024} KB -> {AVATAR_OUT.name} {AVATAR_OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
