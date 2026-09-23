#!/usr/bin/env python3
"""Render rigorous, data-driven coupled Power–Transportation network SVGs.

Scientific visual grammar
-------------------------
charcoal     = neutral physical topology
 green       = viable / sustainable / admissible service flow
 red         = active constraint / disturbance / critical boundary
 Light Sky Blue accent = causal interface / highlighted mechanism / decision path

The animation is explanatory model semantics, not live infrastructure telemetry.
Coordinates are declared visual-layout coordinates, not geographic locations.
"""

from __future__ import annotations

import json
import math
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def write(name: str, text: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(text.rstrip() + "\n", encoding="utf-8")


def style(dark: bool | None = None) -> str:
    palette = load("visual-palette.json")
    order = [
        "bg","panel","ink","muted","line","topology",
        "green","green_soft","red","red_soft","ghost",
        "power","power_soft","transport","transport_soft",
        "information","information_soft",
        "organization","organization_ink","organization_soft",
        "control","control_ink","control_soft",
        "cyan","cyan_soft","violet","violet_soft","magenta","magenta_soft",
    ]
    def css(values: dict) -> str:
        return ";".join(f"--{k.replace('_','-')}:{values[k]}" for k in order)

    light, darkv = css(palette["light"]), css(palette["dark"])
    if dark is True:
        root, media = darkv, ""
    elif dark is False:
        root, media = light, ""
    else:
        root, media = light, f'@media(prefers-color-scheme:dark){{:root{{{darkv}}}}}'
    return f'''<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:Georgia,"STIX Two Text","Times New Roman",serif}}
.title{{font-size:34px;font-weight:820;letter-spacing:-.02em}}
.h{{font-size:23px;font-weight:780}} .k{{font-size:12px;font-weight:800;letter-spacing:.13em}}
.m{{font-size:14px;fill:var(--muted)}} .s{{font-size:11px;fill:var(--muted)}} .node-label{{font-size:13px;font-weight:760}}
.edge{{fill:none;stroke:var(--ink);stroke-width:2;stroke-linecap:round;opacity:.72}}
.edge-soft{{fill:none;stroke:var(--ink);stroke-width:1.5;stroke-linecap:round;opacity:.38;stroke-dasharray:5 6}}
.flow{{fill:none;stroke:var(--green);stroke-width:3.4;stroke-linecap:round;stroke-dasharray:10 12;animation:serviceFlow 3.3s linear infinite}}
.interface-flow{{fill:none;stroke:var(--control);stroke-width:4;stroke-linecap:round;stroke-dasharray:9 11;animation:interfaceFlow 2.8s linear infinite}}
.critical-demo{{opacity:0;fill:none;stroke:var(--red);stroke-width:5;stroke-linecap:round;stroke-dasharray:8 8;animation:criticalPhase 20s linear infinite}}
.propagation-demo{{opacity:0;fill:none;stroke:var(--red);stroke-width:4.5;stroke-linecap:round;stroke-dasharray:7 9;animation:propagationPhase 20s linear infinite}}
.control-demo{{opacity:0;fill:none;stroke:var(--control);stroke-width:4.5;stroke-linecap:round;stroke-dasharray:9 9;animation:controlPhase 20s linear infinite}}
.recovery-demo{{opacity:0;fill:none;stroke:var(--green);stroke-width:5;stroke-linecap:round;stroke-dasharray:10 10;animation:recoveryPhase 20s linear infinite}}
.critical-node{{opacity:0;fill:var(--red);animation:criticalPhase 20s linear infinite}}
.control-node{{opacity:0;fill:var(--control);animation:controlPhase 20s linear infinite}}
@keyframes serviceFlow{{to{{stroke-dashoffset:-44}}}} @keyframes interfaceFlow{{to{{stroke-dashoffset:-40}}}}
@keyframes criticalPhase{{0%,19%,60%,100%{{opacity:0}}22%,55%{{opacity:1}}}}
@keyframes propagationPhase{{0%,36%,60%,100%{{opacity:0}}40%,56%{{opacity:1}}}}
@keyframes controlPhase{{0%,56%,81%,100%{{opacity:0}}61%,76%{{opacity:1}}}}
@keyframes recoveryPhase{{0%,76%,100%{{opacity:0}}81%,96%{{opacity:1}}}}
@media(prefers-reduced-motion:reduce){{.flow,.interface-flow,.critical-demo,.propagation-demo,.control-demo,.recovery-demo,.critical-node,.control-node{{animation:none!important}}.critical-demo,.propagation-demo,.control-demo,.recovery-demo,.critical-node,.control-node{{opacity:0!important}}}}
</style>'''

def svg_open(width: int, height: int, title: str, desc: str, css: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
{css}'''


def line_path(a: tuple[float, float], b: tuple[float, float]) -> str:
    return f"M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}"


def diamond_points(x: float, y: float, r: float) -> str:
    return f"{x:.1f},{y-r:.1f} {x+r:.1f},{y:.1f} {x:.1f},{y+r:.1f} {x-r:.1f},{y:.1f}"


def triangle_points(x: float, y: float, r: float) -> str:
    return f"{x:.1f},{y-r:.1f} {x+r:.1f},{y+r*.82:.1f} {x-r:.1f},{y+r*.82:.1f}"


def draw_node(parts: list[str], node: dict, x: float, y: float, *, layer: str) -> None:
    t = node["type"]
    fill, stroke = "var(--panel)", "var(--ink)"
    if t in {"generator", "hub", "origin", "destination"}:
        fill, stroke = "var(--green-soft)", "var(--green)"
    if t == "interface":
        fill, stroke = "var(--control-soft)", "var(--control-ink)"
    if t == "load":
        fill, stroke = "var(--ghost)", "var(--ink)"
    if t in {"generator", "load", "origin", "destination", "hub"}:
        parts.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>')
    elif t in {"substation", "intersection"}:
        parts.append(f'<rect x="{x-13}" y="{y-13}" width="26" height="26" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>')
    elif t == "interface":
        parts.append(f'<polygon points="{diamond_points(x,y,18)}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
    elif t == "terminal":
        parts.append(f'<polygon points="{triangle_points(x,y,17)}" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>')
    else:
        parts.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    parts.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" class="node-label">{escape(node["id"])}</text>')
    yoff = 33 if layer == "power" else 34
    parts.append(f'<text x="{x}" y="{y+yoff}" text-anchor="middle" class="s">{escape(t)}</text>')


def render_network(power: dict, transport: dict, interfaces: dict, dynamics: dict, *, dark: bool) -> str:
    css = style(dark)
    parts = [svg_open(
        1600, 760,
        "Coupled Power–Transportation network geometry",
        "Data-driven multilayer network figure. Power and transportation remain separate typed layers; shared charging interface C1 carries bidirectional causal mechanisms. Green motion denotes admissible service flow, red transient overlays illustrate a declared disturbance/propagation scenario, and the Light Sky Blue accent family denotes the causal interface and control path. Animation is explanatory, not measured infrastructure telemetry.",
        css,
    )]
    parts.append('<rect x="1" y="1" width="1598" height="758" rx="30" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="52" y="58" class="title">Coupled Power–Transportation Network Geometry</text>')
    parts.append('<text x="52" y="88" class="m">topology first · typed nodes and edges · explicit shared interface · explanatory dynamics</text>')
    parts.append('<text x="1548" y="58" text-anchor="end" class="k" fill="var(--green)">PHYSICS-GROUNDED SUSTAINABLE ENGINEERING</text>')

    # Layer panels
    px, py, pw, ph = 52, 125, 1000, 250
    tx, ty, tw, th = 52, 430, 1000, 250
    parts.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="22" fill="var(--panel)" stroke="var(--green)" stroke-width="1.8"/>')
    parts.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="22" fill="var(--panel)" stroke="var(--green)" stroke-width="1.8"/>')
    parts.append(f'<text x="{px+24}" y="{py+34}" class="h" fill="var(--green)">POWER NETWORK 𝓖<tspan baseline-shift="sub" font-size="13">P</tspan></text>')
    parts.append(f'<text x="{px+24}" y="{py+56}" class="s">𝓖<tspan baseline-shift="sub" font-size="9">P</tspan>=(V<tspan baseline-shift="sub" font-size="9">P</tspan>,E<tspan baseline-shift="sub" font-size="9">P</tspan>) · generation → substations → interface / loads</text>')
    parts.append(f'<text x="{tx+24}" y="{ty+34}" class="h" fill="var(--green)">TRANSPORTATION NETWORK 𝓖<tspan baseline-shift="sub" font-size="13">T</tspan></text>')
    parts.append(f'<text x="{tx+24}" y="{ty+56}" class="s">𝓖<tspan baseline-shift="sub" font-size="9">T</tspan>=(V<tspan baseline-shift="sub" font-size="9">T</tspan>,E<tspan baseline-shift="sub" font-size="9">T</tspan>) · origins → intersections → shared interface / hub → terminals</text>')

    def place(layer: dict, panel_x: float, panel_y: float, panel_w: float, panel_h: float) -> dict[str, tuple[float,float]]:
        xs = [float(n["x"]) for n in layer["nodes"]]; ys = [float(n["y"]) for n in layer["nodes"]]
        minx,maxx,miny,maxy = min(xs),max(xs),min(ys),max(ys)
        out = {}
        for n in layer["nodes"]:
            nx = panel_x + 50 + (float(n["x"])-minx)/(maxx-minx) * (panel_w-100)
            ny = panel_y + 82 + (float(n["y"])-miny)/(maxy-miny) * (panel_h-125)
            out[n["id"]] = (nx,ny)
        return out

    ppos = place(power, px, py, pw, ph)
    tpos = place(transport, tx, ty, tw, th)

    def draw_edges(layer: dict, pos: dict[str, tuple[float,float]], layer_name: str) -> None:
        for e in layer["edges"]:
            a,b = pos[e["source"]], pos[e["target"]]
            cls = "edge-soft" if e["type"] in {"distribution","logistics"} else "edge"
            parts.append(f'<path id="{escape(e["id"])}" d="{line_path(a,b)}" class="{cls}"/>')
        selected = [e for e in layer["edges"] if e["state"] == "operational" and e["id"] in ({"P01","P03","P06","P08"} if layer_name=="power" else {"T01","T03","T08","T11"})]
        for e in selected:
            parts.append(f'<path d="{line_path(pos[e["source"]],pos[e["target"]])}" class="flow"/>')

    draw_edges(power, ppos, "power")
    draw_edges(transport, tpos, "transport")
    for n in power["nodes"]: draw_node(parts,n,*ppos[n["id"]],layer="power")
    for n in transport["nodes"]: draw_node(parts,n,*tpos[n["id"]],layer="transport")

    # Shared physical interface bridge: same C1 in both layer coordinate systems.
    cpt, ctt = ppos["C1"], tpos["C1"]
    parts.append(f'<path d="M{cpt[0]:.1f} {cpt[1]+20:.1f}L{ctt[0]:.1f} {ctt[1]-20:.1f}" class="interface-flow"/>')
    mx,my = (cpt[0]+ctt[0])/2,(cpt[1]+ctt[1])/2
    parts.append(f'<rect x="{mx-72:.1f}" y="{my-25:.1f}" width="144" height="50" rx="12" fill="var(--control-soft)" stroke="var(--control)"/>')
    parts.append(f'<text x="{mx:.1f}" y="{my-3:.1f}" text-anchor="middle" class="math" font-size="18" fill="var(--control-ink)">𝕀<tspan baseline-shift="sub" font-size="11">PT</tspan></text>')
    parts.append(f'<text x="{mx:.1f}" y="{my+16:.1f}" text-anchor="middle" class="s">shared physical asset · C1</text>')

    # Dynamic explanatory overlays.
    p05 = next(e for e in power["edges"] if e["id"]=="P05")
    parts.append(f'<path d="{line_path(ppos[p05["source"]],ppos[p05["target"]])}" class="critical-demo"/>')
    parts.append(f'<circle cx="{cpt[0]}" cy="{cpt[1]}" r="24" class="critical-node" opacity="0"/>')
    parts.append(f'<path d="M{cpt[0]:.1f} {cpt[1]:.1f}L{ctt[0]:.1f} {ctt[1]:.1f}L{tpos["H1"][0]:.1f} {tpos["H1"][1]:.1f}" class="propagation-demo"/>')
    control_path = f'M{ppos["S2"][0]:.1f} {ppos["S2"][1]:.1f}Q{mx+80:.1f} {my:.1f} {tpos["H1"][0]:.1f} {tpos["H1"][1]:.1f}'
    parts.append(f'<path d="{control_path}" class="control-demo"/>')
    parts.append(f'<circle cx="{tpos["H1"][0]:.1f}" cy="{tpos["H1"][1]:.1f}" r="23" class="control-node" opacity="0"/>')
    parts.append(f'<path d="M{tpos["H1"][0]:.1f} {tpos["H1"][1]:.1f}L{tpos["D1"][0]:.1f} {tpos["D1"][1]:.1f}" class="recovery-demo"/>')

    # Right formal panel
    rx,ry,rw,rh = 1090,125,458,555
    parts.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="22" fill="var(--panel)" stroke="var(--line)"/>')
    parts.append(f'<text x="{rx+24}" y="{ry+38}" class="k" fill="var(--control-ink)">FORMAL COUPLING OBJECT</text>')
    parts.append(f'<text x="{rx+24}" y="{ry+78}" class="math" font-size="23">𝓖=(𝓖<tspan baseline-shift="sub" font-size="13">P</tspan>,𝓖<tspan baseline-shift="sub" font-size="13">T</tspan>,𝕀<tspan baseline-shift="sub" font-size="13">PT</tspan>)</text>')
    parts.append(f'<text x="{rx+24}" y="{ry+116}" class="math" font-size="17">𝕀<tspan baseline-shift="sub" font-size="11">PT</tspan><tspan baseline-shift="super" font-size="11">(1)</tspan>=(E<tspan baseline-shift="sub" font-size="10">i</tspan><tspan baseline-shift="super" font-size="10">P</tspan>, E<tspan baseline-shift="sub" font-size="10">j</tspan><tspan baseline-shift="super" font-size="10">T</tspan>, M<tspan baseline-shift="sub" font-size="10">ij</tspan>, …, ℋ<tspan baseline-shift="sub" font-size="10">t</tspan>)</text>')
    parts.append(f'<text x="{rx+24}" y="{ry+154}" class="math" font-size="19">Ẏ=F<tspan baseline-shift="sub" font-size="11">𝓖</tspan>(Y,u,η;θ)</text>')
    parts.append(f'<path d="M{rx+24} {ry+178}H{rx+rw-24}" stroke="var(--line)"/>')
    mechanisms = [
        ("P → T", "electricity supply", "var(--green)"),
        ("T → P", "charging demand", "var(--red)"),
        ("T → P", "conditional V2G support", "var(--control-ink)"),
    ]
    yy = ry+218
    for direction, label, color in mechanisms:
        parts.append(f'<rect x="{rx+24}" y="{yy-22}" width="72" height="28" rx="8" fill="var(--ghost)" stroke="var(--line)"/>')
        parts.append(f'<text x="{rx+60}" y="{yy-3}" text-anchor="middle" class="k" fill="{color}">{direction}</text>')
        parts.append(f'<text x="{rx+112}" y="{yy-3}" class="m">{escape(label)}</text>')
        yy += 50
    parts.append(f'<path d="M{rx+24} {yy-14}H{rx+rw-24}" stroke="var(--line)"/>')
    parts.append(f'<text x="{rx+24}" y="{yy+24}" class="k" fill="var(--green)">EXPLANATORY DYNAMIC CYCLE</text>')
    cycle = [
        ("01", "Nominal", "var(--green)"),
        ("02", "Disturbance", "var(--red)"),
        ("03", "Propagation", "var(--red)"),
        ("04", "Control", "var(--control-ink)"),
        ("05", "Recovery", "var(--green)"),
    ]
    cy = yy+58
    for idx,(num,label,color) in enumerate(cycle):
        xx = rx+28 + idx*82
        parts.append(f'<circle cx="{xx}" cy="{cy}" r="17" fill="var(--panel)" stroke="{color}" stroke-width="2"/>')
        parts.append(f'<text x="{xx}" y="{cy+4}" text-anchor="middle" class="k" fill="{color}">{num}</text>')
        parts.append(f'<text x="{xx}" y="{cy+37}" text-anchor="middle" class="s">{label}</text>')
        if idx < len(cycle)-1:
            parts.append(f'<path d="M{xx+20} {cy}H{xx+62}" stroke="var(--line)"/>')
    parts.append(f'<text x="{rx+24}" y="{ry+520}" class="s">Animation = model semantics; timing ≠ measured event duration.</text>')
    parts.append('<text x="52" y="720" class="s">Green = viable/service flow · Red = active constraint/critical propagation · Light Sky Blue = causal interface/control · Charcoal = topology.</text>')
    parts.append('<text x="1548" y="720" text-anchor="end" class="s">Coordinates and scenario timing are explanatory, not GIS or telemetry.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def warped_loop(cx: float, cy: float, rx: float, ry: float, phase: float, n: int = 100) -> str:
    pts = []
    for k in range(n):
        t = 2*math.pi*k/n
        m = 1 + .06*math.sin(3*t+phase) + .025*math.cos(5*t-.6*phase)
        x = cx + rx*m*math.cos(t) + .04*rx*math.sin(2*t+phase)
        y = cy + ry*m*math.sin(t) + .03*ry*math.cos(3*t-phase)
        pts.append((x,y))
    return "M" + "L".join(f"{x:.1f},{y:.1f}" for x,y in pts) + "Z"


def render_viability() -> str:
    css = style(None)
    parts = [svg_open(1400, 450, "Graph to viability transformation", "Mathematical transformation from multilayer topology and interface object to coupled dynamics, viability geometry, resilience margin and engineering decision. Green is viable, red is critical boundary, Light Sky Blue is causal/decision. Geometry is explanatory, not fitted data.", css)]
    parts.append('<rect x="1" y="1" width="1398" height="448" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="44" y="52" class="k" fill="var(--green)">GRAPH → DYNAMICS → VIABILITY → DECISION</text>')
    labels = [(110,"𝓖","topology"),(300,"𝕀","causal interface"),(490,"F𝓖","coupled dynamics"),(680,"Y(t)","state trajectory")]
    for i,(x,sym,lab) in enumerate(labels):
        fill = "var(--control-soft)" if sym=="𝕀" else "var(--panel)"
        stroke = "var(--control)" if sym=="𝕀" else "var(--line)"
        parts.append(f'<circle cx="{x}" cy="155" r="42" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
        parts.append(f'<text x="{x}" y="163" text-anchor="middle" class="math" font-size="26">{sym}</text>')
        parts.append(f'<text x="{x}" y="218" text-anchor="middle" class="s">{lab}</text>')
        if i < len(labels)-1:
            parts.append(f'<path d="M{x+48} 155H{labels[i+1][0]-48}" class="interface-flow"/>')
    # viability inset
    cx,cy=1055,225
    for idx,sc in enumerate((1.0,.82,.64,.48)):
        parts.append(f'<path d="{warped_loop(cx,cy,220*sc,120*sc,.4+idx*.3)}" fill="{("var(--green-soft)" if idx==0 else "none")}" stroke="var(--green)" stroke-width="{2.2 if idx==0 else 1.2}" opacity="{.9 if idx==0 else .28}"/>')
    outer = warped_loop(cx,cy,232,128,.58)
    parts.append(f'<path d="{outer}" fill="none" stroke="var(--red)" stroke-width="3" stroke-dasharray="9 8"/>')
    yx,yy = 990,220
    bx,by = 1240,190
    parts.append(f'<circle cx="{yx}" cy="{yy}" r="9" fill="var(--green)"/>')
    parts.append(f'<text x="{yx+16}" y="{yy+5}" class="math" font-size="18">Y(t)</text>')
    parts.append(f'<path d="M{yx+12} {yy-6}L{bx-8} {by+3}" stroke="var(--red)" stroke-width="2.4" stroke-dasharray="6 6"/>')
    parts.append(f'<text x="{1120}" y="{187}" class="math" font-size="17" fill="var(--red)">ρ<tspan baseline-shift="sub" font-size="10">g</tspan></text>')
    parts.append(f'<text x="{1245}" y="{176}" class="math" font-size="20" fill="var(--red)">∂𝒱</text>')
    sx,sy = 1138,292
    star = []
    for k in range(10):
        a=-math.pi/2+k*math.pi/5; r=15 if k%2==0 else 6.5; star.append((sx+r*math.cos(a),sy+r*math.sin(a)))
    parts.append('<polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in star)+'" fill="var(--control)" stroke="var(--control-ink)"/>')
    parts.append(f'<path d="M{yx+10} {yy+12}Q1070 285 {sx-20} {sy-5}" class="control-demo" style="opacity:1;animation:serviceFlow 4s linear infinite"/>')
    parts.append(f'<text x="{sx+20}" y="{sy+5}" class="math" font-size="18" fill="var(--control-ink)">u*</text>')
    parts.append(f'<text x="{980}" y="{350}" class="math" font-size="17">Y∈𝒱,  ρ<tspan baseline-shift="sub" font-size="10">g</tspan>=d<tspan baseline-shift="sub" font-size="10">g</tspan>(Y,∂𝒱)</text>')
    parts.append('<text x="44" y="400" class="s">The transformation is conceptual: topology constrains coupled dynamics; viability defines admissible operation; control selects an intervention. No empirical validity is implied by the geometry alone.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def main() -> int:
    power = load("power-network.json")
    transport = load("transport-network.json")
    interfaces = load("interfaces.json")
    dynamics = load("network-dynamics.json")
    write("coupled-network-light.svg", render_network(power, transport, interfaces, dynamics, dark=False))
    write("coupled-network-dark.svg", render_network(power, transport, interfaces, dynamics, dark=True))
    write("graph-to-viability.svg", render_viability())
    print("Rendered governed coupled-network and graph-to-viability SVGs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
