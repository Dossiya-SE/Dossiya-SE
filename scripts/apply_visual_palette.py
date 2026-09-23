#!/usr/bin/env python3
"""Apply the governed accessible scientific palette to generated SVG assets.

This post-render step separates neutral layout geometry from semantic accents:
- topology/structure: neutral charcoal/light-neutral
- viable/operational: green
- critical/constraint: red
- causal/intervention: Light Sky Blue accent family with contrast-safe light-background control structure

It also normalizes the primary coupled-network line hierarchy.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated"
PALETTE_PATH = ROOT / "data" / "visual-palette.json"


def load_palette() -> dict:
    return json.loads(PALETTE_PATH.read_text(encoding="utf-8"))


def css_vars(values: dict) -> str:
    order = [
        "bg", "panel", "ink", "muted", "line", "topology",
        "green", "green_soft", "red", "red_soft",
        "control", "control_soft", "control_ink", "ghost",
        "power", "power_soft", "transport", "transport_soft",
        "information", "information_soft", "organization", "organization_ink", "organization_soft",
        "cyan", "cyan_soft", "violet", "violet_soft", "magenta", "magenta_soft",
    ]
    return ";".join(f"--{key.replace('_','-')}:{values[key]}" for key in order)


def apply_theme_blocks(text: str, palette: dict, *, dark_file: bool, light_file: bool) -> str:
    light_vars = css_vars(palette["light"])
    dark_vars = css_vars(palette["dark"])
    root_vars = dark_vars if dark_file else light_vars
    text, n = re.subn(r":root\{[^}]*\}", f":root{{{root_vars}}}", text, count=1)
    if n != 1:
        raise ValueError("SVG does not contain a single replaceable :root palette block")

    dark_media = re.compile(r"@media\(prefers-color-scheme:dark\)\{\s*:root\{[^}]*\}\s*\}")
    if dark_media.search(text):
        text = dark_media.sub(f"@media(prefers-color-scheme:dark){{:root{{{dark_vars}}}}}", text)
    return text


def refine_coupled_network(text: str) -> str:
    replacements = {
        ".edge{fill:none;stroke:var(--ink);stroke-width:2;stroke-linecap:round;opacity:.72}":
            ".edge{fill:none;stroke:var(--topology);stroke-width:2.2;stroke-linecap:round;opacity:1}",
        ".edge-soft{fill:none;stroke:var(--ink);stroke-width:1.5;stroke-linecap:round;opacity:.38;stroke-dasharray:5 6}":
            ".edge-soft{fill:none;stroke:var(--muted);stroke-width:1.5;stroke-linecap:round;opacity:1;stroke-dasharray:5 6}",
        ".flow{fill:none;stroke:var(--green);stroke-width:3.4;stroke-linecap:round;stroke-dasharray:10 12;animation:serviceFlow 3.3s linear infinite}":
            ".flow{fill:none;stroke:var(--green);stroke-width:3;stroke-linecap:round;stroke-dasharray:10 12;animation:serviceFlow 3.3s linear infinite}",
        ".interface-flow{fill:none;stroke:var(--control);stroke-width:4;stroke-linecap:round;stroke-dasharray:9 11;animation:interfaceFlow 2.8s linear infinite}":
            ".interface-flow{fill:none;stroke:var(--control);stroke-width:3.5;stroke-linecap:round;stroke-dasharray:9 11;animation:interfaceFlow 2.8s linear infinite}",
        ".critical-demo{opacity:0;fill:none;stroke:var(--red);stroke-width:5;stroke-linecap:round;stroke-dasharray:8 8;animation:criticalPhase 20s linear infinite}":
            ".critical-demo{opacity:0;fill:none;stroke:var(--red);stroke-width:4;stroke-linecap:round;stroke-dasharray:8 8;animation:criticalPhase 20s linear infinite}",
        ".propagation-demo{opacity:0;fill:none;stroke:var(--red);stroke-width:4.5;stroke-linecap:round;stroke-dasharray:7 9;animation:propagationPhase 20s linear infinite}":
            ".propagation-demo{opacity:0;fill:none;stroke:var(--red);stroke-width:4;stroke-linecap:round;stroke-dasharray:7 9;animation:propagationPhase 20s linear infinite}",
        ".control-demo{opacity:0;fill:none;stroke:var(--control);stroke-width:4.5;stroke-linecap:round;stroke-dasharray:9 9;animation:controlPhase 20s linear infinite}":
            ".control-demo{opacity:0;fill:none;stroke:var(--control);stroke-width:3.5;stroke-linecap:round;stroke-dasharray:9 9;animation:controlPhase 20s linear infinite}",
        ".recovery-demo{opacity:0;fill:none;stroke:var(--green);stroke-width:5;stroke-linecap:round;stroke-dasharray:10 10;animation:recoveryPhase 20s linear infinite}":
            ".recovery-demo{opacity:0;fill:none;stroke:var(--green);stroke-width:3;stroke-linecap:round;stroke-dasharray:10 10;animation:recoveryPhase 20s linear infinite}",
        'fill="var(--panel)" stroke="var(--green)" stroke-width="1.8"':
            'fill="var(--panel)" stroke="var(--line)" stroke-width="1.2"',
        'class="h" fill="var(--green)"':
            'class="h" fill="var(--ink)"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def main() -> int:
    palette = load_palette()
    svgs = sorted(OUT.glob("*.svg"))
    if not svgs:
        raise SystemExit("No generated SVG assets found")

    for path in svgs:
        text = path.read_text(encoding="utf-8")
        text = apply_theme_blocks(
            text,
            palette,
            dark_file=path.name.endswith("-dark.svg"),
            light_file=path.name.endswith("-light.svg"),
        )
        if path.name in {"coupled-network-light.svg", "coupled-network-dark.svg"}:
            text = refine_coupled_network(text)
        path.write_text(text.rstrip() + "\n", encoding="utf-8")

    print(f"Applied validated neutral-semantic palette to {len(svgs)} generated SVG assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
