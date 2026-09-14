#!/usr/bin/env python3
"""Render the governed static isometric 3D research hero for the profile README.

The renderer is optimized for the actual GitHub profile width. Visual depth encodes
multilayer separation only; it is not geography, elevation, telemetry, or a calibrated
state coordinate. SVG mathematics uses renderer-portable serif symbols and explicit
`dy` subscripts rather than TeX-like underscores, script-plane Unicode glyphs, or
`baseline-shift`, all of which proved unstable across renderers.
"""

from __future__ import annotations

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def vars_for(p: dict) -> str:
    order = [
        "bg", "panel", "ink", "muted", "line", "topology", "green",
        "green_soft", "red", "red_soft", "yellow", "yellow_soft",
        "yellow_ink", "ghost",
    ]
    return ";".join(f"--{k.replace('_', '-')}:{p[k]}" for k in order)


def sub(base: str, index: str) -> str:
    # Explicit vertical offsets are more portable than SVG baseline-shift.
    return f'{base}<tspan dy="5" font-size="13">{index}</tspan><tspan dy="-5"></tspan>'


def project(u: float, v: float, z: float) -> tuple[float, float]:
    # Oblique/isometric-style projection used only for explanatory layer separation.
    return 275 + 545 * u - 205 * v, 475 + 120 * u + 92 * v - z


def norm_positions(layer: dict, z: float) -> dict[str, tuple[float, float]]:
    xs = [float(n["x"]) for n in layer["nodes"]]
    ys = [float(n["y"]) for n in layer["nodes"]]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    out: dict[str, tuple[float, float]] = {}
    for n in layer["nodes"]:
        if n["id"] == "C1":
            u, v = 0.55, 0.46
        else:
            u = 0.09 + 0.82 * (float(n["x"]) - minx) / (maxx - minx)
            v = 0.10 + 0.78 * (float(n["y"]) - miny) / (maxy - miny)
        out[n["id"]] = project(u, v, z)
    return out


def node(parts: list[str], n: dict, x: float, y: float) -> None:
    t = n["type"]
    parts.append(
        f'<line x1="{x:.1f}" y1="{y+14:.1f}" x2="{x:.1f}" y2="{y+27:.1f}" '
        'stroke="var(--line)" stroke-width="1.3"/>'
    )
    parts.append(
        f'<ellipse cx="{x:.1f}" cy="{y+29:.1f}" rx="16" ry="5.5" '
        'fill="var(--ghost)" stroke="var(--line)"/>'
    )

    fill, stroke = "var(--panel)", "var(--topology)"
    if t == "interface":
        fill, stroke = "var(--yellow-soft)", "var(--yellow)"

    if t in {"generator", "load", "origin", "destination", "hub"}:
        parts.append(
            f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="18" ry="12" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="2.4"/>'
        )
    elif t in {"substation", "intersection"}:
        pts = f"{x:.1f},{y-14:.1f} {x+18:.1f},{y:.1f} {x:.1f},{y+14:.1f} {x-18:.1f},{y:.1f}"
        parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>')
    elif t == "interface":
        pts = f"{x:.1f},{y-17:.1f} {x+22:.1f},{y:.1f} {x:.1f},{y+17:.1f} {x-22:.1f},{y:.1f}"
        parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')
    elif t == "terminal":
        pts = f"{x:.1f},{y-17:.1f} {x+18:.1f},{y+13:.1f} {x-18:.1f},{y+13:.1f}"
        parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>')

    parts.append(
        f'<text x="{x:.1f}" y="{y+5:.1f}" text-anchor="middle" class="node">{escape(n["id"])}</text>'
    )


def plane(parts: list[str], z: float) -> None:
    pts = [project(0, 0, z), project(1, 0, z), project(1, 1, z), project(0, 1, z)]
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    parts.append(
        f'<polygon points="{poly}" fill="var(--panel)" fill-opacity=".94" '
        'stroke="var(--line)" stroke-width="1.7"/>'
    )
    for q in (1 / 3, 2 / 3):
        a, b = project(q, 0, z), project(q, 1, z)
        c, d = project(0, q, z), project(1, q, z)
        parts.append(
            f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}'
            f'M{c[0]:.1f} {c[1]:.1f}L{d[0]:.1f} {d[1]:.1f}" '
            'stroke="var(--line)" stroke-width="1" opacity=".45"/>'
        )


def layer_label(parts: list[str], *, power: bool) -> None:
    if power:
        x, y = 58, 205
        title = f'POWER NETWORK {sub("G", "P")}'
        subtitle = "electrical service topology"
        target = project(0.02, 0.04, 218)
    else:
        # The transport label sits in the inter-layer gap, not on top of O1 or a road node.
        x, y = 58, 465
        title = f'TRANSPORTATION NETWORK {sub("G", "T")}'
        subtitle = "mobility service topology"
        target = project(0.02, 0.04, 0)

    parts.append(f'<rect x="{x}" y="{y-30}" width="285" height="64" rx="13" class="label-box"/>')
    parts.append(f'<text x="{x+18}" y="{y-3}" class="layer">{title}</text>')
    parts.append(f'<text x="{x+18}" y="{y+20}" class="small">{subtitle}</text>')
    parts.append(
        f'<path d="M{x+285} {y+2}L{target[0]-14:.1f} {target[1]:.1f}" '
        'stroke="var(--line)" stroke-width="1.5"/>'
    )


def edges(parts: list[str], layer: dict, pos: dict[str, tuple[float, float]], *, selected: set[str]) -> None:
    for e in layer["edges"]:
        a, b = pos[e["source"]], pos[e["target"]]
        cls = "edge-soft" if e["type"] in {"distribution", "logistics"} else "edge"
        parts.append(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" class="{cls}"/>')
        if e["id"] in selected:
            parts.append(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" class="service"/>')


def interface_callout(parts: list[str], p: tuple[float, float], t: tuple[float, float]) -> None:
    parts.append(
        f'<path d="M{p[0]:.1f} {p[1]+19:.1f}L{t[0]:.1f} {t[1]-19:.1f}" class="interface"/>'
    )
    midx, midy = (p[0] + t[0]) / 2, (p[1] + t[1]) / 2
    bx, by = 665, 412
    parts.append(
        f'<path d="M{midx+10:.1f} {midy:.1f}L{bx-12} {by+37}" '
        'stroke="var(--yellow)" stroke-width="1.8" fill="none"/>'
    )
    parts.append(f'<rect x="{bx}" y="{by}" width="270" height="86" rx="15" class="interface-box"/>')
    parts.append(f'<text x="{bx+18}" y="{by+24}" class="eyebrow yellow-text">SHARED PHYSICAL INTERFACE</text>')
    parts.append(f'<text x="{bx+18}" y="{by+51}" class="callout">C1 · EV charging asset</text>')
    parts.append(
        f'<text x="{bx+18}" y="{by+74}" class="math-small yellow-text">{sub("I", "PT")} · Power ⇄ Transport</text>'
    )


def viability(parts: list[str]) -> None:
    parts.append('<rect x="1015" y="125" width="530" height="535" rx="22" class="side-panel"/>')
    parts.append('<text x="1050" y="165" class="eyebrow">STATE / VIABILITY GEOMETRY</text>')
    parts.append('<text x="1050" y="193" class="side-title">State-space margin to criticality</text>')
    parts.append('<text x="1050" y="217" class="small">schematic geometry · not calibrated</text>')

    x0, y0 = 1080, 446
    parts.append(f'<path d="M{x0} {y0}L1465 515M{x0} {y0}L1250 302M{x0} {y0}L{x0} 255" class="axis"/>')
    parts.append('<text x="1474" y="522" class="axis-label">x1</text>')
    parts.append('<text x="1256" y="298" class="axis-label">x2</text>')
    parts.append('<text x="1064" y="249" class="axis-label">x3</text>')

    contours = [(1260, 438, 178, 61, .25), (1260, 410, 148, 51, .16), (1260, 382, 116, 40, .11)]
    for i, (cx, cy, rx, ry, op) in enumerate(contours):
        fill = "var(--green-soft)" if i == 0 else "none"
        parts.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" '
            f'fill-opacity="{op}" stroke="var(--green)" stroke-width="{2.4 if i == 0 else 1.3}"/>'
        )

    parts.append('<ellipse cx="1260" cy="438" rx="194" ry="70" fill="none" class="critical"/>')
    parts.append('<text x="1430" y="405" class="math red-text">∂V</text>')
    parts.append(f'<text x="1300" y="472" class="math green-text">{sub("V", "sus")}</text>')

    parts.append('<circle cx="1214" cy="386" r="9" fill="var(--green)" stroke="var(--panel)" stroke-width="3"/>')
    parts.append('<text x="1180" y="365" class="math">Y(t)</text>')
    parts.append('<path d="M1224 390L1418 426" class="margin"/>')
    parts.append(f'<text x="1310" y="396" class="math red-text">{sub("ρ", "g")}</text>')

    parts.append('<path d="M1218 376Q1270 330 1332 344" class="control"/>')
    parts.append('<polygon points="1332,331 1337,341 1348,342 1339,350 1342,361 1332,355 1322,361 1325,350 1316,342 1327,341" fill="var(--yellow-soft)" stroke="var(--yellow)" stroke-width="2.2"/>')
    parts.append('<text x="1352" y="350" class="math yellow-text">u*</text>')

    parts.append(f'<text x="1050" y="566" class="equation">dY/dt = {sub("F", "G")}(Y,u,η;θ)</text>')
    parts.append(f'<text x="1050" y="598" class="equation green-text">Y(t) ∈ {sub("V", "sus")}(t)</text>')
    parts.append(
        f'<text x="1050" y="630" class="equation red-text">{sub("ρ", "g")}(Y) = {sub("d", "g")}(Y,∂V)</text>'
    )


def render(power: dict, transport: dict, palette: dict, dark: bool) -> str:
    p = palette["dark" if dark else "light"]
    css = f'''<style>
:root{{{vars_for(p)}}}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math,.equation,.math-small{{font-family:"DejaVu Serif","Liberation Serif",serif;font-style:italic}}
.title{{font-size:38px;font-weight:820;letter-spacing:-.025em}}
.subtitle{{font-size:17px;fill:var(--muted)}}
.eyebrow{{font-size:13px;font-weight:800;letter-spacing:.12em;fill:var(--muted)}}
.layer{{font-size:19px;font-weight:790}} .side-title{{font-size:22px;font-weight:760}}
.small{{font-size:17px;fill:var(--muted)}} .axis-label{{font-size:17px;fill:var(--muted)}}
.node{{font-size:16px;font-weight:820;fill:var(--ink)}} .callout{{font-size:18px;font-weight:760}}
.math{{font-size:22px}} .math-small{{font-size:17px}} .equation{{font-size:20px}}
.label-box{{fill:var(--bg);stroke:var(--line);stroke-width:1.4}}
.side-panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.5}}
.interface-box{{fill:var(--yellow-soft);stroke:var(--yellow);stroke-width:1.8}}
.edge{{fill:none;stroke:var(--topology);stroke-width:2.2;stroke-linecap:round}}
.edge-soft{{fill:none;stroke:var(--muted);stroke-width:1.5;stroke-dasharray:5 6}}
.service{{fill:none;stroke:var(--green);stroke-width:3.2;stroke-linecap:round}}
.interface{{fill:none;stroke:var(--yellow);stroke-width:3.8;stroke-dasharray:9 7}}
.axis{{fill:none;stroke:var(--topology);stroke-width:1.7}}
.critical{{stroke:var(--red);stroke-width:3.2;stroke-dasharray:10 8}}
.margin{{fill:none;stroke:var(--red);stroke-width:2.5;stroke-dasharray:6 6}}
.control{{fill:none;stroke:var(--yellow);stroke-width:3.5;stroke-dasharray:9 7}}
.green-text{{fill:var(--green)}} .red-text{{fill:var(--red)}} .yellow-text{{fill:var(--yellow-ink)}}
.legend{{font-size:15px;fill:var(--muted)}}
</style>'''

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 760" role="img" aria-labelledby="title desc">',
        '<title id="title">Coupled Power–Transportation multilayer research geometry</title>',
        '<desc id="desc">Static isometric multilayer infrastructure geometry with typed Power and Transportation networks, a shared EV charging interface C1, and a separate pseudo-3D viability panel. Depth encodes layer separation only and is not geographic elevation, GIS height, telemetry, or a calibrated state coordinate.</desc>',
        css,
        '<rect x="1" y="1" width="1598" height="758" rx="28" fill="var(--bg)" stroke="var(--line)"/>',
        '<text x="48" y="58" class="title">Coupled Power–Transportation Systems</text>',
        '<text x="48" y="88" class="subtitle">Isometric multilayer topology · shared physical interface · viability geometry</text>',
        '<text x="1550" y="56" text-anchor="end" class="eyebrow">STATIC 3D SCHEMATIC · NOT GIS ELEVATION</text>',
        '<path d="M985 120L985 662" stroke="var(--line)" stroke-width="1.4"/>',
    ]

    zt, zp = 0, 218
    for u, v in ((0, 0), (1, 0), (1, 1), (0, 1)):
        a, b = project(u, v, zt), project(u, v, zp)
        parts.append(
            f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" '
            'stroke="var(--line)" stroke-width="1.1" stroke-dasharray="4 7"/>'
        )

    plane(parts, zt)
    plane(parts, zp)
    layer_label(parts, power=True)
    layer_label(parts, power=False)

    ppos = norm_positions(power, zp)
    tpos = norm_positions(transport, zt)
    edges(parts, power, ppos, selected={"P01", "P03", "P06", "P08"})
    edges(parts, transport, tpos, selected={"T01", "T03", "T08", "T11"})

    for n in power["nodes"]:
        node(parts, n, *ppos[n["id"]])
    for n in transport["nodes"]:
        node(parts, n, *tpos[n["id"]])

    interface_callout(parts, ppos["C1"], tpos["C1"])
    viability(parts)

    parts.extend([
        '<text x="48" y="708" class="legend">Green solid path = admissible service · Ochre dashed rail = causal interface · Red dashed boundary = criticality · Charcoal = physical topology</text>',
        '<text x="48" y="738" class="legend">Coordinates and depth are explanatory and uncalibrated.</text>',
        '</svg>',
    ])
    return "\n".join(parts) + "\n"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    power = load("power-network.json")
    transport = load("transport-network.json")
    palette = load("visual-palette.json")
    (OUT / "coupled-network-3d-light.svg").write_text(render(power, transport, palette, False), encoding="utf-8")
    (OUT / "coupled-network-3d-dark.svg").write_text(render(power, transport, palette, True), encoding="utf-8")
    print("Rendered portable, legible static isometric 3D network hero assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
