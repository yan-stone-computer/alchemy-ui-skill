#!/usr/bin/env python3
"""Render one or more palette JSON files (from palette.py) as a visual card PNG.

Usage:
    python palette_card.py --json h5/design-tokens.json miniapp/design-tokens.json \
        --out premium-palette-card.png
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def load_font(size: int):
    for candidate in (r"C:\Windows\Fonts\msyh.ttc", r"C:\Windows\Fonts\simsun.ttc", r"C:\Windows\Fonts\arial.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_card(palettes: list[dict], out: Path) -> None:
    swatch = 230
    gap = 18
    label_w = 340
    row_h = 190
    pad = 46
    rows = len(palettes)
    width = pad * 2 + label_w + 5 * swatch + 4 * gap
    height = pad * 2 + rows * (row_h + 18) - 18
    img = Image.new("RGB", (width, height), "#171310")
    d = ImageDraw.Draw(img)
    title_font = load_font(30)
    label_font = load_font(22)
    hex_font = load_font(17)

    d.text((pad, pad - 26), "ui-alchemy premium palettes", font=title_font, fill="#E8DCC8")

    for i, palette in enumerate(palettes):
        y = pad + i * (row_h + 18)
        d.text((pad, y + 8), palette["name"], font=label_font, fill="#F3ECDD")
        d.text((pad, y + 52), palette.get("accent", ""), font=hex_font, fill="#A8B49E")
        semantic = palette["semantic"]["light"]
        keys = ["surface", "surface-raised", "primary", "accent", "text-primary"]
        for j, key in enumerate(keys):
            x = pad + label_w + j * (swatch + gap)
            color = semantic[key]
            d.rounded_rectangle([x, y, x + swatch, y + row_h], radius=14, fill=color, outline="#3A3229", width=1)
            label = f"{key}\n{color}"
            lines = label.split("\n")
            for k, line in enumerate(lines):
                d.text((x + 14, y + 16 + k * 30), line, font=hex_font, fill="#F3ECDD")
    img.save(out, "PNG")
    print(f"wrote {out} ({width}x{height})")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", nargs="+", required=True, help="palette JSON files")
    parser.add_argument("--out", default="premium-palette-card.png")
    args = parser.parse_args(argv)
    palettes = []
    for path in args.json:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        palettes.append(
            {
                "name": payload["name"],
                "accent": payload["accent"],
                "semantic": payload["semantic"],
            }
        )
    draw_card(palettes, Path(args.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
