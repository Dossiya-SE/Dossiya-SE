#!/usr/bin/env python3
"""Validate the static isometric 3D profile hero, legibility and evidence boundary."""

from __future__ import annotations

import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated"
README = ROOT / "README.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_svg(name: str) -> None:
    path = OUT / name
    require(path.exists(), f"missing 3D hero asset: {name}")
    text = path.read_text(encoding="utf-8")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"invalid SVG XML: {name}: {exc}") from exc

    require(root.tag.endswith("svg"), f"{name}: root must be SVG")
    require(root.attrib.get("viewBox") == "0 0 1600 760", f"{name}: governed 3D viewBox changed")
    require("<title" in text and "<desc" in text, f"{name}: accessibility metadata missing")
    require("<script" not in text.lower(), f"{name}: scripts are forbidden")
    require("@keyframes" not in text, f"{name}: README 3D hero must not depend on SVG animation")

    for phrase in (
        "POWER NETWORK",
        "TRANSPORTATION NETWORK",
        "SHARED PHYSICAL INTERFACE",
        "STATE / VIABILITY GEOMETRY",
        "C1 · EV charging asset",
        "∂V",
        "STATIC 3D SCHEMATIC · NOT GIS ELEVATION",
        "Coordinates and depth are explanatory and uncalibrated.",
    ):
        require(phrase in text, f"{name}: missing governed 3D semantic: {phrase}")

    # SVG text is not TeX. Raw underscore notation was visibly broken in GitHub.
    for broken in ("G_", "I_", "ρ_", "d_", "F_"):
        require(broken not in text, f"{name}: raw TeX-like underscore leaked into SVG text: {broken}")

    # Cross-renderer portability: avoid unstable script-plane math glyphs and
    # baseline-shift. Subscripts must use explicit dy offsets.
    for unstable in ("𝒢", "𝕀", "𝒱", 'baseline-shift="sub"'):
        require(unstable not in text, f"{name}: unstable SVG math construct present: {unstable}")
    require(text.count('dy="5" font-size="13"') >= 6, f"{name}: portable explicit SVG subscripts missing")
    require('font-family:"DejaVu Serif","Liberation Serif",serif' in text, f"{name}: portable math font stack missing")

    # Collision-safe architecture: layer labels, interface callout and viability geometry
    # must occupy separate governed containers. Runtime geometry checks are performed
    # separately by validate_network_3d_runtime.py.
    require('class="label-box"' in text, f"{name}: layer-label containers missing")
    require('class="interface-box"' in text, f"{name}: offset interface callout missing")
    require('class="side-panel"' in text, f"{name}: independent viability panel missing")
    require(text.count('class="label-box"') == 2, f"{name}: exactly two physical layer labels required")

    # Minimum source sizes. The runtime validator converts these to effective pixels
    # at the observed ~980 px GitHub profile width.
    require(".node{font-size:16px" in text, f"{name}: node labels below governed source size")
    require(".small{font-size:17px" in text, f"{name}: explanatory text below governed source size")
    require(".equation{font-size:20px" in text, f"{name}: equations below governed source size")

    require("stroke-dasharray" in text, f"{name}: non-color semantic redundancy missing")
    require("var(--yellow)" in text and "var(--green)" in text and "var(--red)" in text, f"{name}: semantic palette missing")
    require("Depth encodes layer separation only" in text, f"{name}: depth interpretation missing from accessible description")


def validate_readme() -> None:
    text = README.read_text(encoding="utf-8")
    lower = text.lower()
    require("coupled-network-3d-light.svg" in text and "coupled-network-3d-dark.svg" in text, "README must use light/dark 3D hero")
    require("static isometric 3d" in lower, "README alt text must describe static isometric 3D")
    require("visual encoding of multilayer structure" in lower, "README must explain the meaning of depth")
    require("not geographic elevation" in lower, "README must reject geographic interpretation of 3D depth")
    require("github should not be treated as guaranteeing svg animation" in lower, "README must preserve GitHub static-rendering boundary")
    require("# dossiya dakou" not in lower, "README must not repeat a large H1 identity directly below the hero")


def main() -> int:
    validate_svg("coupled-network-3d-light.svg")
    validate_svg("coupled-network-3d-dark.svg")
    validate_readme()
    print("3D HERO VALIDATION: PASS — portable math, source legibility, collision-safe architecture, multilayer semantics and evidence boundaries are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"3D HERO VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
