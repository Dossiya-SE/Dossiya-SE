#!/usr/bin/env python3
"""Validate governed RGB/sRGB palette, contrast, forbidden hues and SVG conformance."""

from __future__ import annotations

import colorsys
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE_PATH = ROOT / "data" / "visual-palette.json"
OUT = ROOT / "assets" / "generated"

FORBIDDEN_TERMS = ("gold", "yellow", "amber", "ochre")


def load() -> dict:
    return json.loads(PALETTE_PATH.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def rgb01(hex_color: str) -> tuple[float, float, float]:
    h = hex_color.lstrip("#")
    require(len(h) == 6, f"invalid hex color: {hex_color}")
    return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))


def rgb_hex(values: list[int]) -> str:
    require(len(values) == 3, f"RGB triplet must have length 3: {values}")
    require(all(isinstance(v, int) and 0 <= v <= 255 for v in values), f"invalid RGB triplet: {values}")
    return "#" + "".join(f"{v:02X}" for v in values)


def channel(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    r, g, b = rgb01(hex_color)
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hue_saturation(rgb: list[int]) -> tuple[float, float]:
    r, g, b = (v / 255 for v in rgb)
    h, s, _ = colorsys.rgb_to_hsv(r, g, b)
    return 360.0 * h, s


def validate_palette(p: dict) -> None:
    require(p.get("schema_version") == "3.0", "visual palette schema must be 3.0")
    require(p.get("color_model") == "RGB", "visual palette must explicitly use RGB model")
    require(p.get("color_space") == "sRGB", "visual palette must explicitly use sRGB color space")
    require(p.get("evidence_state") == "VALIDATED_VISUAL_DESIGN_SPECIFICATION", "invalid visual palette evidence state")

    raw = PALETTE_PATH.read_text(encoding="utf-8").lower()
    for term in FORBIDDEN_TERMS:
        # The policy list itself names forbidden terms; remove that JSON fragment before checking usage.
        scrubbed = re.sub(r'"forbidden_terms"\s*:\s*\[[^\]]*\]', '"forbidden_terms":[]', raw)
        require(term not in scrubbed, f"forbidden color-family term remains in palette contract: {term}")

    rgb_values = p.get("rgb_values", {})
    require(set(rgb_values) == {"light", "dark"}, "RGB source must define light and dark modes")
    forbidden = p["forbidden_hue_policy"]
    h0, h1 = map(float, forbidden["forbidden_hue_degrees"])
    min_sat = float(forbidden["minimum_saturation"])

    for mode in ("light", "dark"):
        values = p[mode]
        source = rgb_values[mode]
        require(set(values) == set(source), f"{mode}: hex and RGB token sets differ")
        for token, triplet in source.items():
            require(values[token] == rgb_hex(triplet), f"{mode} {token}: hex is not derived from governed RGB triplet")
            hue, sat = hue_saturation(triplet)
            if sat >= min_sat:
                require(not (h0 <= hue <= h1), f"{mode} {token}: prohibited warm hue {hue:.1f}°")

    thresholds = p["minimum_contrast"]
    text_min = float(thresholds["normal_text"])
    graphic_min = float(thresholds["meaningful_graphics"])

    text_roles = (
        "ink","muted","green","red","power","transport","information",
        "organization_ink","control_ink","cyan","violet","magenta"
    )
    graphic_roles = (
        "topology","green","red","power","transport","information",
        "organization","control","cyan","violet","magenta"
    )

    for mode in ("light", "dark"):
        c = p[mode]
        bg = c["bg"]
        for role in text_roles:
            ratio = contrast(c[role], bg)
            require(ratio >= text_min, f"{mode} {role} text contrast {ratio:.2f}:1 is below {text_min}:1")
        for role in graphic_roles:
            ratio = contrast(c[role], bg)
            require(ratio >= graphic_min, f"{mode} {role} graphic contrast {ratio:.2f}:1 is below {graphic_min}:1")

    redundancy = p.get("color_redundancy", {})
    require("directional" in redundancy.get("operational", ""), "operational state must have a non-color cue")
    require("dashed" in redundancy.get("critical", ""), "critical state must have a non-color cue")
    require("stroke" in redundancy.get("causal", "") and "label" in redundancy.get("causal", ""), "causal state must have non-color cues")
    require("shape" in redundancy.get("node_type", ""), "node types must be distinguished by geometry")
    require("POWER" in redundancy.get("power", ""), "power color must have a textual non-color cue")
    require("TRANSPORTATION" in redundancy.get("transportation", ""), "transport color must have a textual non-color cue")
    require("dashed" in redundancy.get("information", ""), "information edges must have a non-color cue")
    require("dotted" in redundancy.get("organization", ""), "organization edges must have a non-color cue")


def expected_vars(values: dict) -> dict[str, str]:
    return {key.replace("_", "-"): value for key, value in values.items()}


def validate_svg_palette(p: dict) -> None:
    files = sorted(OUT.glob("*.svg"))
    require(bool(files), "no generated SVGs found")
    for path in files:
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        for term in FORBIDDEN_TERMS:
            require(term not in lower, f"{path.name}: forbidden color-family term present: {term}")

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
        "stroke:var(--control);stroke-width:3.5",
        "stroke:var(--red);stroke-width:4",
    )
    for snippet in required_css:
        require(snippet in network, f"coupled network missing governed line hierarchy: {snippet}")
    require('stroke="var(--line)" stroke-width="1.2"' in network, "network panels must remain neutral rather than green-framed")
    require("stroke-dasharray" in network and "POWER NETWORK" in network and "TRANSPORTATION NETWORK" in network,
            "network must combine pattern, labels and color")


def main() -> int:
    p = load()
    validate_palette(p)
    validate_svg_palette(p)
    print("VISUAL RGB VALIDATION: PASS — RGB triplets, sRGB conversion, contrast, zero-gold hue policy and SVG tokens are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"VISUAL RGB VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
