#!/usr/bin/env python3
"""Validate palette contrast, redundant semantics, and generated SVG conformance."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE_PATH = ROOT / "data" / "visual-palette.json"
OUT = ROOT / "assets" / "generated"


def load() -> dict:
    return json.loads(PALETTE_PATH.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def rgb(hex_color: str) -> tuple[float, float, float]:
    h = hex_color.lstrip("#")
    require(len(h) == 6, f"invalid hex color: {hex_color}")
    return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))


def channel(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    r, g, b = rgb(hex_color)
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def validate_palette(p: dict) -> None:
    require(p.get("schema_version") == "1.0", "visual palette schema must be 1.0")
    require(p.get("evidence_state") == "VALIDATED_VISUAL_DESIGN_SPECIFICATION", "invalid visual palette evidence state")
    thresholds = p["minimum_contrast"]
    text_min = float(thresholds["normal_text"])
    graphic_min = float(thresholds["meaningful_graphics"])

    for mode in ("light", "dark"):
        c = p[mode]
        bg = c["bg"]
        # These colors are used as normal-size text somewhere in the profile.
        for role in ("ink", "muted", "green", "red", "yellow"):
            ratio = contrast(c[role], bg)
            require(ratio >= text_min, f"{mode} {role} text contrast {ratio:.2f}:1 is below {text_min}:1")
        # Meaningful network geometry must remain visible even when color perception is limited.
        for role in ("topology", "green", "red", "yellow"):
            ratio = contrast(c[role], bg)
            require(ratio >= graphic_min, f"{mode} {role} graphic contrast {ratio:.2f}:1 is below {graphic_min}:1")

    redundancy = p.get("color_redundancy", {})
    require("directional" in redundancy.get("operational", ""), "operational state must have a non-color cue")
    require("dashed" in redundancy.get("critical", ""), "critical state must have a non-color cue")
    require("stroke" in redundancy.get("causal", "") and "label" in redundancy.get("causal", ""), "causal state must have non-color cues")
    require("shape" in redundancy.get("node_type", ""), "node types must be distinguished by geometry")


def expected_vars(values: dict) -> dict[str, str]:
    return {
        "bg": values["bg"], "panel": values["panel"], "ink": values["ink"],
        "muted": values["muted"], "line": values["line"], "topology": values["topology"],
        "green": values["green"], "green-soft": values["green_soft"],
        "red": values["red"], "red-soft": values["red_soft"],
        "yellow": values["yellow"], "yellow-soft": values["yellow_soft"],
        "yellow-ink": values["yellow_ink"], "ghost": values["ghost"],
    }


def validate_svg_palette(p: dict) -> None:
    files = sorted(OUT.glob("*.svg"))
    require(bool(files), "no generated SVGs found")
    for path in files:
        text = path.read_text(encoding="utf-8")
        root_match = re.search(r":root\{([^}]*)\}", text)
        require(root_match is not None, f"{path.name}: missing :root palette")
        root_css = root_match.group(1)
        mode = "dark" if path.name.endswith("-dark.svg") else "light"
        for key, value in expected_vars(p[mode]).items():
            require(f"--{key}:{value}" in root_css, f"{path.name}: palette token --{key} does not match governed {mode} value")

        if not path.name.endswith("-dark.svg"):
            dark_media = re.search(r"@media\(prefers-color-scheme:dark\)\{:root\{([^}]*)\}\}", text)
            if dark_media:
                for key, value in expected_vars(p["dark"]).items():
                    require(f"--{key}:{value}" in dark_media.group(1), f"{path.name}: dark media token --{key} mismatch")

    network = (OUT / "coupled-network-light.svg").read_text(encoding="utf-8")
    required_css = (
        "stroke:var(--topology);stroke-width:2.2",
        "stroke:var(--muted);stroke-width:1.5",
        "stroke:var(--green);stroke-width:3",
        "stroke:var(--yellow);stroke-width:3.5",
        "stroke:var(--red);stroke-width:4",
    )
    for snippet in required_css:
        require(snippet in network, f"coupled network missing governed line hierarchy: {snippet}")
    require('stroke="var(--line)" stroke-width="1.2"' in network, "network panels must remain neutral rather than green-framed")
    require("stroke-dasharray" in network and "POWER NETWORK" in network and "TRANSPORTATION NETWORK" in network, "network must combine pattern, labels and color")


def main() -> int:
    p = load()
    validate_palette(p)
    validate_svg_palette(p)
    print("VISUAL PALETTE VALIDATION: PASS — contrast, neutral hierarchy, redundant semantics and generated SVG tokens are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"VISUAL PALETTE VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
