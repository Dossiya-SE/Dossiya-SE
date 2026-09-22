#!/usr/bin/env python3
"""Runtime raster validation for FLAT-GEOMETRY-V1 at GitHub profile widths."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SVG = ROOT / "assets" / "generated" / "flat-geometry.svg"
PREVIEW = ROOT / "artifacts" / "flat-geometry-preview"
VIEW_W, VIEW_H = 1600, 700
TARGET_WIDTHS = (980, 640)


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)


def rgb(value: str) -> tuple[int, int, int]:
    h = value.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def materialize(svg: str, palette: dict) -> str:
    def repl(match: re.Match[str]) -> str:
        key = match.group(1).replace("-", "_")
        require(key in palette, f"unresolved palette token --{match.group(1)}")
        return palette[key]
    out = re.sub(r"var\(--([a-z0-9-]+)\)", repl, svg, flags=re.I)
    require("var(--" not in out, "unresolved CSS variable remains")
    return out


def color_pixels(image: Image.Image, target: tuple[int, int, int], tol: int = 22) -> int:
    count = 0
    for px in image.convert("RGB").getdata():
        if max(abs(px[i] - target[i]) for i in range(3)) <= tol:
            count += 1
    return count


def non_background_fraction(image: Image.Image, background: tuple[int, int, int], crop: tuple[int,int,int,int]) -> float:
    region = image.convert("RGB").crop(crop)
    pixels = list(region.getdata())
    changed = 0
    for px in pixels:
        if math.sqrt(sum((px[i]-background[i])**2 for i in range(3))) > 18:
            changed += 1
    return changed / max(1, len(pixels))


def validate_mode(svg_text: str, palette: dict, mode: str) -> None:
    p = palette[mode]
    source = materialize(svg_text, p).encode("utf-8")
    bg = rgb(p["bg"])
    semantic = {
        "violet": rgb(p["violet"]),
        "red": rgb(p["red"]),
        "green": rgb(p["green"]),
        "gold": rgb(p["gold"]),
    }
    PREVIEW.mkdir(parents=True, exist_ok=True)

    for width in TARGET_WIDTHS:
        height = round(width * VIEW_H / VIEW_W)
        out = PREVIEW / f"flat-geometry-{mode}-{width}px.png"
        cairosvg.svg2png(bytestring=source, write_to=str(out), output_width=width, output_height=height)
        with Image.open(out) as image:
            require(image.size == (width, height), f"{mode}: raster size mismatch at {width}px")
            require(image.getbbox() is not None, f"{mode}: blank raster at {width}px")

            left = (int(width*.02), int(height*.16), int(width*.45), int(height*.91))
            center = (int(width*.45), int(height*.16), int(width*.71), int(height*.91))
            right = (int(width*.71), int(height*.16), int(width*.98), int(height*.91))
            require(non_background_fraction(image, bg, left) > .025, f"{mode}: plane-geometry field too sparse at {width}px")
            require(non_background_fraction(image, bg, center) > .025, f"{mode}: affine-flat field too sparse at {width}px")
            require(non_background_fraction(image, bg, right) > .025, f"{mode}: hyperplane field too sparse at {width}px")

            min_pixels = max(10, int(width*height*0.000025))
            for label, target in semantic.items():
                require(color_pixels(image, target) >= min_pixels, f"{mode}: {label} cue lost at {width}px")


def main() -> int:
    require(SVG.exists(), "flat-geometry.svg missing")
    svg_text = SVG.read_text(encoding="utf-8")
    palette = json.loads((DATA / "visual-palette.json").read_text(encoding="utf-8"))
    for mode in ("light", "dark"):
        validate_mode(svg_text, palette, mode)
    print("FLAT GEOMETRY RUNTIME VALIDATION: PASS — light/dark rasterization, panel density and semantic cues survive at GitHub widths.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"FLAT GEOMETRY RUNTIME VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
