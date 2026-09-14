#!/usr/bin/env python3
"""Runtime render validation for the governed 3D GitHub profile hero.

This test complements source/semantic validation by actually rasterizing the light and
dark SVGs at representative GitHub widths, checking that the render is non-empty,
preserving semantic colors, and keeping governed annotation containers disjoint from
projected physical nodes. It also writes PNG previews for CI artifacts.

CairoSVG does not reliably resolve CSS custom properties in this SVG context, while
GitHub's renderer does. The test therefore materializes the already-governed `:root`
color variables into concrete hex values in an in-memory copy before rasterization.
The repository SVG itself is not altered by this compatibility step.
"""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated"
DATA = ROOT / "data"
PREVIEW = ROOT / "artifacts" / "runtime-preview"
SVG_NS = "{http://www.w3.org/2000/svg}"
TARGET_WIDTHS = (980, 640)
VIEW_W, VIEW_H = 1600, 760


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def as_float(value: str | None, what: str) -> float:
    require(value is not None, f"missing numeric SVG attribute: {what}")
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"invalid numeric SVG attribute {what}: {value}") from exc


def rect_box(el: ET.Element) -> tuple[float, float, float, float]:
    x = as_float(el.get("x"), "x")
    y = as_float(el.get("y"), "y")
    w = as_float(el.get("width"), "width")
    h = as_float(el.get("height"), "height")
    return x, y, x + w, y + h


def point_in(box: tuple[float, float, float, float], x: float, y: float, pad: float = 0.0) -> bool:
    x0, y0, x1, y1 = box
    return x0 - pad <= x <= x1 + pad and y0 - pad <= y <= y1 + pad


def boxes_overlap(a: tuple[float, float, float, float], b: tuple[float, float, float, float], pad: float = 0.0) -> bool:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    return not (ax1 + pad <= bx0 or bx1 + pad <= ax0 or ay1 + pad <= by0 or by1 + pad <= ay0)


def css_font_px(svg_text: str, selector: str) -> float:
    pattern = rf"\.{re.escape(selector)}\{{[^}}]*font-size:([0-9.]+)px"
    match = re.search(pattern, svg_text)
    require(match is not None, f"missing governed font size for .{selector}")
    return float(match.group(1))


def materialize_css_vars(svg_text: str) -> str:
    declarations = dict(re.findall(r"--([a-z0-9-]+):([^;}{]+)", svg_text, flags=re.IGNORECASE))
    require(declarations, "runtime rasterizer could not find governed CSS custom properties")

    def replace(match: re.Match[str]) -> str:
        token = match.group(1)
        require(token in declarations, f"runtime rasterizer found unresolved CSS token --{token}")
        return declarations[token].strip()

    resolved = re.sub(r"var\(--([a-z0-9-]+)\)", replace, svg_text, flags=re.IGNORECASE)
    require("var(--" not in resolved, "runtime rasterizer left unresolved CSS variables")
    return resolved


def rgb(hex_value: str) -> tuple[int, int, int]:
    value = hex_value.lstrip("#")
    require(len(value) == 6, f"expected six-digit color, got {hex_value}")
    return tuple(int(value[i:i+2], 16) for i in (0, 2, 4))


def color_pixels(image: Image.Image, target: tuple[int, int, int], tol: int = 20) -> int:
    count = 0
    for px in image.convert("RGB").getdata():
        if max(abs(px[i] - target[i]) for i in range(3)) <= tol:
            count += 1
    return count


def non_background_fraction(image: Image.Image, background: tuple[int, int, int], crop: tuple[int, int, int, int]) -> float:
    region = image.convert("RGB").crop(crop)
    pixels = list(region.getdata())
    diff = 0
    for px in pixels:
        if math.sqrt(sum((px[i] - background[i]) ** 2 for i in range(3))) > 18:
            diff += 1
    return diff / max(1, len(pixels))


def validate_geometry(root: ET.Element, name: str) -> None:
    rects = root.findall(f".//{SVG_NS}rect")
    label_boxes = [r for r in rects if r.get("class") == "label-box"]
    interface_boxes = [r for r in rects if r.get("class") == "interface-box"]
    side_panels = [r for r in rects if r.get("class") == "side-panel"]
    require(len(label_boxes) == 2, f"{name}: expected two layer label boxes")
    require(len(interface_boxes) == 1, f"{name}: expected one interface callout box")
    require(len(side_panels) == 1, f"{name}: expected one viability panel")

    boxes = [rect_box(r) for r in label_boxes]
    interface = rect_box(interface_boxes[0])
    side = rect_box(side_panels[0])
    require(not boxes_overlap(boxes[0], boxes[1], pad=8), f"{name}: layer label boxes overlap")
    for i, box in enumerate(boxes):
        require(not boxes_overlap(box, interface, pad=8), f"{name}: layer label {i+1} overlaps interface callout")
        require(not boxes_overlap(box, side, pad=8), f"{name}: layer label {i+1} overlaps viability panel")
    require(not boxes_overlap(interface, side, pad=12), f"{name}: interface callout overlaps viability panel")

    node_texts = [t for t in root.findall(f".//{SVG_NS}text") if t.get("class") == "node"]
    require(len(node_texts) >= 10, f"{name}: too few typed nodes in 3D hero")
    for node in node_texts:
        x = as_float(node.get("x"), "node x")
        y = as_float(node.get("y"), "node y") - 5.0
        label = "".join(node.itertext()).strip()
        for j, box in enumerate(boxes):
            require(not point_in(box, x, y, pad=20), f"{name}: node {label} intrudes into layer-label container {j+1}")
        require(not point_in(interface, x, y, pad=16), f"{name}: node {label} intrudes into interface-callout container")
        require(not point_in(side, x, y, pad=8), f"{name}: physical node {label} intrudes into viability panel")


def validate_profile_scale(svg_text: str, name: str) -> None:
    desktop = 980 / VIEW_W
    effective = {
        "node": css_font_px(svg_text, "node") * desktop,
        "small": css_font_px(svg_text, "small") * desktop,
        "equation": css_font_px(svg_text, "equation") * desktop,
        "layer": css_font_px(svg_text, "layer") * desktop,
    }
    require(effective["node"] >= 9.0, f"{name}: node labels render below 9 px at 980 px GitHub width ({effective['node']:.2f}px)")
    require(effective["small"] >= 10.0, f"{name}: explanatory text renders below 10 px at 980 px GitHub width ({effective['small']:.2f}px)")
    require(effective["equation"] >= 12.0, f"{name}: equations render below 12 px at 980 px GitHub width ({effective['equation']:.2f}px)")
    require(effective["layer"] >= 11.0, f"{name}: layer labels render below 11 px at 980 px GitHub width ({effective['layer']:.2f}px)")


def render_and_validate(svg_path: Path, svg_text: str, palette: dict, theme: str) -> None:
    PREVIEW.mkdir(parents=True, exist_ok=True)
    background = rgb(palette[theme]["bg"])
    semantic = [rgb(palette[theme][key]) for key in ("green", "red", "yellow")]
    raster_source = materialize_css_vars(svg_text).encode("utf-8")

    for width in TARGET_WIDTHS:
        height = round(width * VIEW_H / VIEW_W)
        out = PREVIEW / f"{svg_path.stem}-{width}px.png"
        cairosvg.svg2png(bytestring=raster_source, write_to=str(out), output_width=width, output_height=height)
        with Image.open(out) as image:
            require(image.size == (width, height), f"{svg_path.name}: raster size mismatch at {width}px")
            require(image.getbbox() is not None, f"{svg_path.name}: blank raster at {width}px")

            left = (0, int(height * .14), int(width * .61), int(height * .94))
            right = (int(width * .63), int(height * .14), width, int(height * .91))
            require(non_background_fraction(image, background, left) > .035, f"{svg_path.name}: left network region too sparse/blank at {width}px")
            require(non_background_fraction(image, background, right) > .035, f"{svg_path.name}: viability region too sparse/blank at {width}px")

            min_pixels = max(12, int(width * height * 0.00004))
            for target, label in zip(semantic, ("green", "red", "yellow")):
                require(color_pixels(image, target) >= min_pixels, f"{svg_path.name}: {label} semantic accent lost during rasterization at {width}px")


def validate(name: str, palette: dict, theme: str) -> None:
    path = OUT / name
    require(path.exists(), f"missing 3D hero asset: {name}")
    text = path.read_text(encoding="utf-8")
    root = ET.fromstring(text)
    validate_geometry(root, name)
    validate_profile_scale(text, name)
    render_and_validate(path, text, palette, theme)


def main() -> int:
    palette = json.loads((DATA / "visual-palette.json").read_text(encoding="utf-8"))
    validate("coupled-network-3d-light.svg", palette, "light")
    validate("coupled-network-3d-dark.svg", palette, "dark")
    print("3D RUNTIME VALIDATION: PASS — rasterization, profile-scale legibility, semantic colors and collision geometry are valid.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f"3D RUNTIME VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
