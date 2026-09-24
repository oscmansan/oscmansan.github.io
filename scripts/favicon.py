"""Generate the "OM" monogram favicon set into images/.

Usage (from the repo root):
    python scripts/favicon.py

Requires: pip install fonttools pillow
"""
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images"
BG, FG = "#b0492c", "#faf8f3"  # terracotta accent, paper
FONT = str(ROOT / "scripts" / "fonts" / "Newsreader-Medium.ttf")
# Heavier cut, set larger, for 16-48px where thin serifs wash out
SMALL_FONT = str(ROOT / "scripts" / "fonts" / "Newsreader-Bold.ttf")

# --- SVG with letters as outlines (no font dependency) ---
font = TTFont(FONT)
gs, cmap = font.getGlyphSet(), font.getBestCmap()
upm = font["head"].unitsPerEm
paths, x, tracking = [], 0, -0.02 * upm
for ch in "OM":
    g = cmap[ord(ch)]
    pen = SVGPathPen(gs); gs[g].draw(pen)
    paths.append((x, pen.getCommands())); x += gs[g].width + tracking
width = x - tracking
bp = BoundsPen(gs); gs[cmap[ord("O")]].draw(bp); cap_top = bp.bounds[3]
bp = BoundsPen(gs); gs[cmap[ord("M")]].draw(bp); cap_top = max(cap_top, bp.bounds[3])
# Fit text to 64% of the 32px tile width, centred on cap height
scale = 32 * 0.64 / width
tx = (32 - width * scale) / 2
ty = (32 + cap_top * scale) / 2
glyphs = "".join(f'<path transform="translate({tx + gx*scale:.3f} {ty:.3f}) scale({scale:.5f} {-scale:.5f})" d="{d}"/>' for gx, d in paths)
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="7" fill="{BG}"/><g fill="{FG}">{glyphs}</g></svg>\n'
(OUT / "favicon.svg").write_text(svg)

# --- Raster sizes, drawn at 1024 and downsampled ---
def tile(size, radius_ratio=7/32, full_bleed=False, small=False):
    font_path, fill = (SMALL_FONT, 0.8) if small else (FONT, 0.64)
    big = 1024
    im = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if full_bleed:  # iOS applies its own mask; no transparent corners
        d.rectangle([0, 0, big, big], fill=BG)
    else:
        d.rounded_rectangle([0, 0, big - 1, big - 1], radius=int(big * radius_ratio), fill=BG)
    f = ImageFont.truetype(font_path, 100)
    l, t, r, b = d.textbbox((0, 0), "OM", font=f)
    fsize = int(100 * big * fill / (r - l))
    f = ImageFont.truetype(font_path, fsize)
    l, t, r, b = d.textbbox((0, 0), "OM", font=f)
    d.text(((big - (r - l)) / 2 - l, (big - (b - t)) / 2 - t), "OM", font=f, fill=FG)
    return im.resize((size, size), Image.LANCZOS)

tile(32, small=True).save(f"{OUT}/favicon-32x32.png")
for n in (192, 512):
    tile(n).save(f"{OUT}/favicon-{n}x{n}.png")
tile(180, full_bleed=True).convert("RGB").save(f"{OUT}/apple-touch-icon-180x180.png")
tile(256, small=True).save(f"{OUT}/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("done")
