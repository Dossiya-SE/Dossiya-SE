#!/usr/bin/env python3
"""Render the governed FLAT-GEOMETRY-V1 mathematical figure.

The figure distinguishes bounded plane figures from affine flats. It is mathematical
art / definition, not empirical infrastructure data or calibrated state geometry.
"""

from __future__ import annotations

import json
import math
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"
CONTRACT_ID = "FLAT-GEOMETRY-V1"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def vars_for(p: dict) -> str:
    keys = (
        "bg","panel","ink","muted","line","topology",
        "green","green_soft","red","red_soft","yellow","yellow_soft","yellow_ink","ghost",
        "power","power_soft","transport","transport_soft",
        "information","information_soft","organization","organization_ink","organization_soft",
        "cyan","cyan_soft","violet","violet_soft","magenta","magenta_soft","gold","gold_soft"
    )
    return ";".join(f"--{k.replace('_','-')}:{p[k]}" for k in keys)


def regular_polygon(n: int, cx: float, cy: float, r: float) -> list[tuple[float, float]]:
    return [
        (
            cx + r * math.cos(math.pi / 2 + 2 * math.pi * j / n),
            cy - r * math.sin(math.pi / 2 + 2 * math.pi * j / n),
        )
        for j in range(n)
    ]


def polygon_points(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def render(contract: dict, palette: dict) -> str:
    light = vars_for(palette["light"])
    dark = vars_for(palette["dark"])
    polygons = contract["plane_geometry"]["regular_polygons"]

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 700" role="img" aria-labelledby="flat-title flat-desc">',
        '<title id="flat-title">Geometry of flats — plane figures, affine subspaces and a hyperplane</title>',
        '<desc id="flat-desc">A rigorous mathematical visual separating bounded plane figures from affine flats. Regular polygons from triangle through decagon, circle, ellipse and semicircle appear on the left; point, line, plane and the affine k-flat definition appear in the center; a hyperplane and point-to-hyperplane distance appear on the right.</desc>',
        f'''<style>
:root{{{light}}}
@media(prefers-color-scheme:dark){{:root{{{dark}}}}}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:Georgia,"STIX Two Text","Times New Roman",serif}}
.title{{font-size:34px;font-weight:820;letter-spacing:-.02em}}
.eyebrow{{font-size:12px;font-weight:800;letter-spacing:.13em;fill:var(--muted)}}
.label{{font-size:13px;font-weight:650}}
.small{{font-size:12px;fill:var(--muted)}}
.eq{{font-size:19px}}
.panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
.math-shape{{fill:none;stroke:var(--violet);stroke-width:2.2;stroke-linejoin:round}}
.math-fill{{fill:var(--violet-soft);stroke:var(--violet);stroke-width:2.2}}
.topology{{fill:none;stroke:var(--topology);stroke-width:2}}
.critical{{fill:none;stroke:var(--red);stroke-width:3;stroke-dasharray:10 8}}
.projection{{fill:none;stroke:var(--cyan);stroke-width:4.2;stroke-dasharray:8 7}}
.admissible{{fill:var(--green-soft);stroke:var(--green);stroke-width:2}}
.state{{fill:var(--violet);stroke:var(--panel);stroke-width:3}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>''',
        '<rect x="1" y="1" width="1598" height="698" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
        '<text x="48" y="58" class="title">Geometry of Flats</text>',
        '<text x="48" y="88" class="small">plane figures → affine subspaces → hyperplane distance · mathematical definition, not empirical calibration</text>',
        '<line x1="48" y1="108" x2="1552" y2="108" stroke="var(--line)"/>',

        '<rect x="48" y="132" width="660" height="492" rx="16" class="panel"/>',
        '<text x="74" y="168" class="eyebrow">PLANE GEOMETRY · ℝ²</text>',
        '<text x="74" y="194" class="small">bounded figures and exact curves · violet = mathematical abstraction</text>',
    ]

    xs = [130, 285, 440, 595]
    ys = [272, 407]
    for i, item in enumerate(polygons):
        x, y = xs[i % 4], ys[i // 4]
        n = int(item["sides"])
        name = str(item["name"]).upper()
        pts = polygon_points(regular_polygon(n, x, y, 43))
        parts.append(f'<polygon points="{pts}" class="math-shape"/>')
        parts.append(f'<text x="{x}" y="{y+67}" text-anchor="middle" class="small">{escape(name)} · n={n}</text>')

    # Curved plane figures.
    parts += [
        '<circle cx="150" cy="548" r="38" class="math-shape"/>',
        '<text x="150" y="603" text-anchor="middle" class="small">CIRCLE</text>',
        '<ellipse cx="355" cy="548" rx="55" ry="34" class="math-shape"/>',
        '<text x="355" y="603" text-anchor="middle" class="small">ELLIPSE</text>',
        '<path d="M515 570A46 46 0 0 1 607 570Z" class="math-shape"/>',
        '<text x="561" y="603" text-anchor="middle" class="small">SEMICIRCLE</text>',

        '<rect x="730" y="132" width="382" height="492" rx="16" class="panel"/>',
        '<text x="756" y="168" class="eyebrow">AFFINE FLATS</text>',
        '<text x="756" y="194" class="math eq">F = x₀ + span{v₁,…,vₖ}</text>',

        '<circle cx="790" cy="250" r="7" fill="var(--violet)"/>',
        '<text x="816" y="255" class="label">0D · point</text>',

        '<path d="M770 326H1070" class="topology"/>',
        '<path d="M770 326l14 -8v16zM1070 326l-14 -8v16z" fill="var(--topology)"/>',
        '<text x="816" y="310" class="label">1D · line</text>',

        '<polygon points="785,445 1042,472 995,530 738,503" class="math-fill"/>',
        '<text x="760" y="430" class="label">2D · plane</text>',

        '<line x1="758" y1="560" x2="1080" y2="560" stroke="var(--line)"/>',
        '<text x="756" y="589" class="small">v₁,…,vₖ linearly independent</text>',
        '<text x="756" y="611" class="small">dim F = k · ambient space ℝⁿ</text>',

        '<rect x="1134" y="132" width="418" height="492" rx="16" class="panel"/>',
        '<text x="1160" y="168" class="eyebrow">HYPERPLANE · (n−1)-FLAT</text>',
        '<text x="1160" y="194" class="math eq">H = {x ∈ ℝⁿ : aᵀx = b}, a ≠ 0</text>',

        '<rect x="1175" y="226" width="338" height="265" rx="10" class="admissible"/>',
        '<circle cx="1192" cy="250" r="6" fill="var(--green)"/>',
        '<text x="1208" y="254" class="small" fill="var(--green)">admissible side</text>',
        '<path d="M1210 468L1480 250" class="critical"/>',
        '<text x="1450" y="276" class="math eq" fill="var(--red)">H</text>',

        '<circle cx="1275" cy="292" r="9" class="state"/>',
        '<text x="1292" y="286" class="math eq">x</text>',
        '<path d="M1275 292L1335.4 366.8" class="projection"/>',
        '<circle cx="1335.4" cy="366.8" r="6" fill="var(--cyan)" stroke="var(--panel)" stroke-width="2"/>',
        '<text x="1288" y="340" class="math" font-size="16" fill="var(--cyan)">d(x,H)</text>',

        '<line x1="1160" y1="524" x2="1525" y2="524" stroke="var(--line)"/>',
        '<text x="1160" y="560" class="math eq">d(x,H) = |aᵀx − b| / ‖a‖₂</text>',
        '<text x="1160" y="590" class="small">red dashed = boundary · cyan dashed = orthogonal projection</text>',

        '<line x1="48" y1="648" x2="1552" y2="648" stroke="var(--line)"/>',
        '<text x="48" y="676" class="small">Plane figures and affine flats are distinct objects. The visual bridge is constraint and state-space geometry. Contract: FLAT-GEOMETRY-V1.</text>',
        '</svg>',
    ]
    return "\n".join(parts) + "\n"


def main() -> int:
    contract = load("flat-geometry.json")
    palette = load("visual-palette.json")
    if contract.get("contract_id") != CONTRACT_ID:
        raise ValueError("unexpected flat-geometry contract id")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "flat-geometry.svg").write_text(render(contract, palette), encoding="utf-8")
    print("Rendered FLAT-GEOMETRY-V1 publication SVG.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
