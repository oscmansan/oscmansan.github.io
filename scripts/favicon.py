#!/usr/bin/env python3
"""Generate the Penrose-triangle favicon set into images/.

Two variants of the same figure on the terracotta tile:
  - outline (white strokes)            -> large icons: 180/192/512 px
  - tinted faces (three white tints)   -> browser tab: favicon.svg, .ico, 32 px
The outline's many parallel lines blur together at tab size; filled faces keep
the "impossible" shape legible down to 16 px.

The geometry was computed by isometrically projecting three square beams and
applying the Penrose occlusion at the closing corner; coordinates are in
isometric units (beam width 1, outer side 6).

Usage (from the repo root):
    python scripts/favicon.py

Requires: pip install pillow
"""

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "images"
BG, FG = "#b0492c", (250, 248, 243)  # terracotta accent, paper
RADIUS = 7 / 32  # tile corner radius as a fraction of the size

# Visible edges (polylines) of the Penrose triangle
SEGS = [
    [(2.5, -4.3301), (1.5, -4.3301)], [(1.5, -4.3301), (3.5, -0.866)],
    [(3.5, -0.866), (2.5, -0.866)], [(2.5, -0.866), (1.5, -0.866)],
    [(1.5, -0.866), (1.0, 0.0)], [(1.0, 0.0), (5.0, 0.0)],
    [(5.0, 0.0), (4.5, -0.866), (2.5, -4.3301)], [(1.5, -2.5981), (0.0, 0.0)],
    [(0.0, 0.0), (-0.5, 0.866)], [(-0.5, 0.866), (4.5, 0.866), (5.0, 0.0)],
    [(1.5, -0.866), (2.0, -1.7321)], [(2.0, -1.7321), (1.5, -2.5981)],
    [(1.0, -3.4641), (2.0, -1.7321)], [(2.0, -1.7321), (2.5, -0.866)],
    [(1.5, -4.3301), (1.0, -3.4641)], [(-1.0, 0.0), (-0.5, 0.866)],
    [(1.5, -2.5981), (1.0, -3.4641)], [(1.0, -3.4641), (-1.0, 0.0)],
]
# Faces as (polygon, opacity): light, mid and dark sides of the beams
FACES = [
    ([(2.5, -4.3301), (1.5, -4.3301), (3.5, -0.866), (1.5, -0.866), (1.0, 0.0), (5.0, 0.0), (4.5, -0.866)], 1.0),
    ([(1.5, -2.5981), (0.0, 0.0), (-0.5, 0.866), (4.5, 0.866), (5.0, 0.0), (1.0, 0.0), (2.0, -1.7321)], 0.72),
    ([(1.0, -3.4641), (2.5, -0.866), (3.5, -0.866), (1.5, -4.3301)], 0.45),
    ([(-1.0, 0.0), (-0.5, 0.866), (1.5, -2.5981), (1.0, -3.4641)], 0.45),
]

_pts = [p for s in SEGS for p in s]
_xs, _ys = [p[0] for p in _pts], [p[1] for p in _pts]
CX, CY = (min(_xs) + max(_xs)) / 2, (min(_ys) + max(_ys)) / 2
SPAN = max(max(_xs) - min(_xs), max(_ys) - min(_ys))


def mapper(size, fill):
    s = size * fill / SPAN
    return lambda p: (size / 2 + (p[0] - CX) * s, size / 2 + (p[1] - CY) * s)


def svg_tinted():
    tr = mapper(32, 0.8)
    polys = "".join(
        f'<polygon points="{" ".join(f"{x:.3f},{y:.3f}" for x, y in map(tr, poly))}" fill-opacity="{op}"/>'
        for poly, op in FACES
    )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        f'<rect width="32" height="32" rx="7" fill="{BG}"/>'
        f'<g fill="rgb{FG}">{polys}</g></svg>\n'
    )


def tile(size, variant):
    big = 1024
    im = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, big - 1, big - 1], radius=int(big * RADIUS), fill=BG)
    if variant == "outline":
        tr, w = mapper(big, 0.72), int(big * 0.032)
        d = ImageDraw.Draw(im)
        for seg in SEGS:
            q = [tr(p) for p in seg]
            d.line(q, fill=FG, width=w, joint="curve")
            for x, y in q:  # round caps
                d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=FG)
    else:
        tr = mapper(big, 0.8)
        for poly, op in FACES:
            layer = Image.new("RGBA", (big, big), (0, 0, 0, 0))
            ImageDraw.Draw(layer).polygon([tr(p) for p in poly], fill=FG + (round(255 * op),))
            im = Image.alpha_composite(im, layer)
    return im.resize((size, size), Image.LANCZOS)


def main() -> None:
    (OUT / "favicon.svg").write_text(svg_tinted())
    tile(256, "tinted").save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    tile(32, "tinted").save(OUT / "favicon-32x32.png")
    for n in (192, 512):
        tile(n, "outline").save(OUT / f"favicon-{n}x{n}.png")
    # iOS masks the corners itself: square, opaque tile
    ios = Image.new("RGB", (180, 180), BG)
    t = tile(180, "outline")
    ios.paste(t, (0, 0), t)
    ios.save(OUT / "apple-touch-icon-180x180.png")
    print("done")


if __name__ == "__main__":
    main()
