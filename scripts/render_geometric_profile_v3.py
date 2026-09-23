#!/usr/bin/env python3
"""Render PROFILE-GEOMETRY-V3 README visuals.

This renderer replaces the displayed profile visuals with a common geometric grammar:
affine planes, typed polygons, ellipses, hyperplanes and orthogonal projections.

Geometry is explanatory unless the underlying repository data states otherwise.
"""

from __future__ import annotations

import json
import math
from datetime import datetime
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"
CONTRACT_ID = "PROFILE-GEOMETRY-V3"

PALETTE_KEYS = (
    "bg","panel","ink","muted","line","topology",
    "green","green_soft","red","red_soft","control","control_soft","control_ink","ghost",
    "power","power_soft","transport","transport_soft","information","information_soft",
    "organization","organization_ink","organization_soft","cyan","cyan_soft",
    "violet","violet_soft","magenta","magenta_soft",
)

def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def write(name: str, content: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(content.rstrip() + "\n", encoding="utf-8")

def vars_for(values: dict) -> str:
    return ";".join(f"--{k.replace('_','-')}:{values[k]}" for k in PALETTE_KEYS)

def style(palette: dict, dark: bool | None = None, motion: bool = True) -> str:
    root = vars_for(palette["dark"] if dark else palette["light"])
    media = "" if dark is not None else f"@media(prefers-color-scheme:dark){{:root{{{vars_for(palette['dark'])}}}}}"
    motion_css = "@keyframes drift{0%,100%{opacity:.94}50%{opacity:1}}\n.motion{animation:drift 7s ease-in-out infinite}" if motion else ""
    return f'''<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:"DejaVu Serif","Liberation Serif",serif}}
.title{{font-size:34px;font-weight:820;letter-spacing:-.02em}}
.eyebrow{{font-size:12px;font-weight:820;letter-spacing:.14em;fill:var(--muted)}}
.label{{font-size:15px;font-weight:700}}
.node{{font-size:16px;font-weight:700}}
.small{{font-size:17px;fill:var(--muted)}}
.tiny{{font-size:13px;fill:var(--muted)}}
.equation{{font-size:20px}}
.layer{{font-size:18px;font-weight:820;letter-spacing:.08em}}
.legend{{font-size:15px;fill:var(--muted)}}
.panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
.plane{{stroke-width:1.6;stroke-linejoin:round}}
.power-plane{{fill:var(--power-soft);stroke:var(--power)}}
.transport-plane{{fill:var(--transport-soft);stroke:var(--transport)}}
.power-edge{{fill:none;stroke:var(--power);stroke-width:2.4;stroke-linecap:round}}
.transport-edge{{fill:none;stroke:var(--transport);stroke-width:2.4;stroke-linecap:round}}
.service-power{{fill:none;stroke:var(--power);stroke-width:3.1;stroke-linecap:round}}
.service-transport{{fill:none;stroke:var(--transport);stroke-width:3.1;stroke-linecap:round}}
.info-edge{{fill:none;stroke:var(--information);stroke-width:2;stroke-dasharray:8 7}}
.org-edge{{fill:none;stroke:var(--organization);stroke-width:2;stroke-dasharray:2 7}}
.interface{{fill:var(--control-soft);stroke:var(--control);stroke-width:3}}
.viable{{fill:var(--green-soft);stroke:var(--green);stroke-width:2.2}}
.critical-boundary{{fill:none;stroke:var(--red);stroke-width:3.2;stroke-dasharray:10 8}}
.flow-red{{stroke:var(--red)}}
.flow-green{{fill:none;stroke:var(--green);stroke-width:3}}
.flow-control{{fill:none;stroke:var(--control);stroke-width:3;stroke-dasharray:8 7}}
.projection{{fill:none;stroke:var(--control);stroke-width:3.2;stroke-dasharray:8 7}}
.model{{fill:var(--violet-soft);stroke:var(--violet);stroke-width:2.2}}
.state{{fill:var(--violet);stroke:var(--panel);stroke-width:3}}
.label-box{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
.interface-box{{fill:var(--control-soft);stroke:var(--control);stroke-width:1.5}}
.side-panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
.research-card{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
{motion_css}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>'''

def svg_open(width: int, height: int, title: str, desc: str, css: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(desc)}</desc>',
        css,
        f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
    ]

def wrap_words(text: str, max_chars: int = 28, max_lines: int = 2) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else current + " " + word
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
            if len(lines) == max_lines - 1:
                break
    if current and len(lines) < max_lines:
        lines.append(current)
    return lines[:max_lines]

def regular_polygon(n: int, cx: float, cy: float, r: float, phase: float = -math.pi/2) -> str:
    pts = []
    for j in range(n):
        t = phase + 2*math.pi*j/n
        pts.append(f"{cx+r*math.cos(t):.1f},{cy+r*math.sin(t):.1f}")
    return " ".join(pts)

def polygon(n: int, cx: float, cy: float, r: float, cls: str, phase: float=-math.pi/2) -> str:
    return f'<polygon points="{regular_polygon(n,cx,cy,r,phase)}" class="{cls}"/>'

def arrow(x1: float,y1: float,x2: float,y2: float,stroke: str,width: float=2.4,dash: str|None=None) -> str:
    dx,dy=x2-x1,y2-y1
    ang=math.atan2(dy,dx)
    hx=x2-12*math.cos(ang)
    hy=y2-12*math.sin(ang)
    left=(hx+7*math.cos(ang+2.35),hy+7*math.sin(ang+2.35))
    right=(hx+7*math.cos(ang-2.35),hy+7*math.sin(ang-2.35))
    d=f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" fill="none" stroke="{stroke}" stroke-width="{width}"{d}/>'
        f'<path d="M{x2:.1f} {y2:.1f}L{left[0]:.1f} {left[1]:.1f}M{x2:.1f} {y2:.1f}L{right[0]:.1f} {right[1]:.1f}" '
        f'fill="none" stroke="{stroke}" stroke-width="{width}"/>'
    )

def map_plane(x: float, y: float, layer: str) -> tuple[float,float]:
    # Affine map from explanatory network layout to a projected 2-flat.
    base_y = 150 if layer == "power" else 405
    return 340 + 0.58*x + 0.10*y, base_y + 0.03*x + 0.50*y

def node_shape(node_type: str, x: float, y: float, color: str) -> str:
    if node_type in {"generator","origin"}:
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="var(--panel)" stroke="{color}" stroke-width="2.4"/>'
    if node_type in {"substation","terminal"}:
        return f'<rect x="{x-10:.1f}" y="{y-10:.1f}" width="20" height="20" fill="var(--panel)" stroke="{color}" stroke-width="2.4"/>'
    if node_type in {"intersection"}:
        return polygon(4,x,y,13,"",0).replace('class=""',f'fill="var(--panel)" stroke="{color}" stroke-width="2.4"')
    if node_type in {"hub"}:
        return polygon(6,x,y,14,"").replace('class=""',f'fill="var(--panel)" stroke="{color}" stroke-width="2.4"')
    if node_type in {"load","destination"}:
        return polygon(3,x,y,14,"").replace('class=""',f'fill="var(--panel)" stroke="{color}" stroke-width="2.4"')
    if node_type == "interface":
        return polygon(6,x,y,16,"interface")
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="var(--panel)" stroke="{color}" stroke-width="2.2"/>'

def render_hero(palette: dict, dark: bool) -> str:
    p=svg_open(
        1600,640,
        "Dossiya Dakou — geometric research portrait",
        "Physics-grounded mathematical engineering: Power and Transportation are shown as affine layers feeding a state-space viability ellipse with a critical hyperplane and orthogonal resilience margin. Vector arrows and trajectories are explanatory mathematical art, not a measured flow.",
        style(palette,dark),
    )
    p += [
        '<text x="52" y="62" class="title">Dossiya Dakou</text>',
        '<text x="52" y="94" class="small">Physics-grounded mathematical engineering for sustainable infrastructure</text>',
        '<line x1="52" y1="118" x2="1548" y2="118" stroke="var(--line)"/>',
        '<text x="60" y="154" class="eyebrow">PHYSICAL / INFORMATIONAL LAYERS</text>',
        '<polygon points="80,210 690,236 770,356 160,330" class="plane power-plane"/>',
        '<polygon points="80,372 690,398 770,518 160,492" class="plane transport-plane"/>',
        '<text x="105" y="245" class="layer" fill="var(--power)">POWER</text>',
        '<text x="105" y="410" class="layer" fill="var(--transport)">TRANSPORTATION</text>',
        '<path d="M210 278L340 257L470 300L610 270" class="power-edge"/>',
        '<circle cx="210" cy="278" r="9" fill="var(--panel)" stroke="var(--power)" stroke-width="2"/>',
        polygon(4,340,257,11,"").replace('class=""','fill="var(--panel)" stroke="var(--power)" stroke-width="2"'),
        polygon(6,470,300,13,"interface"),
        polygon(3,610,270,12,"").replace('class=""','fill="var(--panel)" stroke="var(--power)" stroke-width="2"'),
        '<path d="M210 447L330 428L470 460L610 438" class="transport-edge"/>',
        '<circle cx="210" cy="447" r="9" fill="var(--panel)" stroke="var(--transport)" stroke-width="2"/>',
        polygon(4,330,428,11,"",0).replace('class=""','fill="var(--panel)" stroke="var(--transport)" stroke-width="2"'),
        polygon(6,470,460,13,"interface"),
        polygon(6,610,438,12,"").replace('class=""','fill="var(--panel)" stroke="var(--transport)" stroke-width="2"'),
        '<path d="M470 300L470 460" class="flow-control"/>',
        '<text x="492" y="386" class="label" fill="var(--control)">shared interface</text>',
        '<path d="M300 206C360 170 420 170 480 206" class="info-edge"/>',
        '<text x="360" y="182" class="label" fill="var(--information)">INFORMATION</text>',
        '<path d="M250 510C330 548 420 548 500 510" class="org-edge"/>',
        '<text x="320" y="566" class="label" fill="var(--organization-ink)">ORGANIZATION</text>',
        '<text x="60" y="610" class="eyebrow">SYSTEM CHANNELS</text>',
        '<circle cx="230" cy="606" r="6" fill="var(--power)"/><text x="244" y="612" class="label">Power</text>',
        '<circle cx="330" cy="606" r="6" fill="var(--transport)"/><text x="344" y="612" class="label">Transportation</text>',
        '<circle cx="485" cy="606" r="6" fill="var(--information)"/><text x="499" y="612" class="label">Information</text>',
        '<circle cx="610" cy="606" r="6" fill="var(--organization)"/><text x="624" y="612" class="label">Organization</text>',

        '<text x="850" y="154" class="eyebrow">STATE / VIABILITY GEOMETRY</text>',
        '<ellipse cx="1190" cy="350" rx="260" ry="175" class="viable level-set"/>',
        '<ellipse cx="1190" cy="350" rx="205" ry="132" fill="none" stroke="var(--violet)" stroke-width="1.3" class="level-set"/>',
        '<ellipse cx="1190" cy="350" rx="145" ry="92" fill="none" stroke="var(--cyan)" stroke-width="1.1" class="level-set"/>',
        '<g class="vector-field" opacity=".28">',
    ]
    for yy in (260,315,370,425):
        for xx in (1030,1110,1190,1270,1350):
            p.append(arrow(xx-10,yy+5,xx+12,yy-7,"var(--violet)",1.0))
    p += [
        '</g>',
        '<path d="M1010 480L1390 190" class="critical-boundary flow-red"/>',
        '<text x="1370" y="206" class="label" fill="var(--red)">critical hyperplane ∂V</text>',
        '<circle cx="1090" cy="250" r="10" class="state"/>',
        '<text x="1108" y="246" class="equation math">Y(t)</text>',
        '<path d="M1090 250L1170 312" class="projection flow-control"/>',
        '<circle cx="1170" cy="312" r="6" fill="var(--control)"/>',
        '<text x="1095" y="310" class="equation math" fill="var(--control)">ρ<tspan dy="5" font-size="13">g</tspan></text>',
        '<path d="M1120 420C1160 395 1210 392 1260 405C1310 420 1340 398 1370 370" class="flow-green motion"/>',
        '<text x="1260" y="455" class="label" fill="var(--green)">viable state evolution</text>',
        '<text x="850" y="555" class="equation math">G → F<tspan dy="5" font-size="13">G</tspan> → Y(t) → V → u*</text>',
        '<text x="850" y="590" class="small">Affine layers, trajectories and boundaries are explanatory.</text>',
        '<text x="850" y="616" class="small">No measured flow or empirical validation is implied.</text>',
        '</svg>',
    ]
    return "\n".join(p)

def render_question(palette: dict) -> str:
    p=svg_open(
        1400,420,
        "Current research question",
        "Power and Transportation affine layers meet at a shared interface, map into coupled dynamics, and are evaluated against a sustainable viability region.",
        style(palette,None),
    )
    p += [
        '<text x="48" y="54" class="eyebrow">RESEARCH QUESTION</text>',
        '<text x="48" y="88" class="title">How do supported interfaces generate coupled state evolution?</text>',
        '<line x1="48" y1="112" x2="1352" y2="112" stroke="var(--line)"/>',

        '<text x="70" y="150" class="label">Power ↔ Transportation interfaces</text>',
        '<polygon points="70,180 380,196 430,270 120,254" class="plane power-plane"/>',
        '<polygon points="70,262 380,278 430,352 120,336" class="plane transport-plane"/>',
        polygon(6,250,266,24,"interface"),
        '<path d="M250 222L250 310" class="flow-control"/>',
        '<text x="280" y="270" class="small">typed shared asset</text>',

        '<text x="520" y="150" class="label">Coupled dynamics</text>',
        '<polygon points="520,190 790,190 835,330 565,330" class="model"/>',
        '<path d="M570 295C620 220 690 340 760 235" fill="none" stroke="var(--information)" stroke-width="3"/>',
        '<circle cx="570" cy="295" r="7" fill="var(--power)"/>',
        '<circle cx="760" cy="235" r="7" fill="var(--transport)"/>',
        '<text x="600" y="360" class="equation math">Ẏ = F<tspan dy="5" font-size="13">G</tspan>(Y,u,η;θ)</text>',

        '<text x="930" y="150" class="label">Sustainable viability</text>',
        '<ellipse cx="1120" cy="265" rx="180" ry="105" class="viable"/>',
        '<path d="M1000 355L1235 160" class="critical-boundary"/>',
        '<circle cx="1070" cy="230" r="8" class="state"/>',
        '<path d="M1070 230L1122 273" class="projection"/>',
        '<text x="1040" y="330" class="equation math">Y(t) ∈ V<tspan dy="5" font-size="12">sus</tspan></text>',

        arrow(440,266,500,266,"var(--control)",2.8),
        arrow(845,266,920,266,"var(--information)",2.8),
        '<text x="48" y="402" class="small">Geometry encodes interface, model space, constraint and viability — not evidence strength.</text>',
        '</svg>',
    ]
    return "\n".join(p)

def render_network_3d(palette: dict, dark: bool, power: dict, transport: dict) -> str:
    p=svg_open(
        1600,760,
        "Coupled Power and Transportation network on affine layers",
        "Static 3D schematic of Power and Transportation topology embedded on two affine 2-flats with a shared EV charging interface and separate state-space viability geometry. Depth encodes layer separation only; it is not GIS elevation.",
        style(palette,dark,motion=False),
    )
    p += [
        '<text x="48" y="54" class="title">Coupled infrastructure geometry</text>',
        '<text x="48" y="86" class="small">two affine 2-flats · typed topology · shared physical interface · independent viability geometry</text>',
        '<rect x="62" y="108" width="320" height="66" rx="10" class="label-box"/>',
        '<text x="82" y="137" class="layer" fill="var(--power)">POWER NETWORK</text>',
        '<text x="82" y="160" class="equation math">G<tspan dy="5" font-size="13">P</tspan></text>',
        '<rect x="62" y="394" width="320" height="66" rx="10" class="label-box"/>',
        '<text x="82" y="423" class="layer" fill="var(--transport)">TRANSPORTATION NETWORK</text>',
        '<text x="82" y="446" class="equation math">G<tspan dy="5" font-size="13">T</tspan></text>',

        '<polygon points="120,185 920,215 1045,365 245,335" class="plane power-plane"/>',
        '<polygon points="120,440 920,470 1045,620 245,590" class="plane transport-plane"/>',
    ]
    for net, layer, color, edge_cls, service_cls in (
        (power,"power","var(--power)","power-edge","service-power"),
        (transport,"transport","var(--transport)","transport-edge","service-transport"),
    ):
        node_map={n["id"]:map_plane(float(n["x"]),float(n["y"]),layer) for n in net["nodes"]}
        for e in net["edges"]:
            x1,y1=node_map[e["source"]]
            x2,y2=node_map[e["target"]]
            cls=service_cls if e.get("type") in {"distribution","transit","rail"} else edge_cls
            p.append(f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" class="{cls}"/>')
        for n in net["nodes"]:
            x,y=node_map[n["id"]]
            p.append(node_shape(str(n["type"]),x,y,color))
            p.append(f'<text x="{x+15:.1f}" y="{y-8:.1f}" class="node">{escape(str(n["id"]))}</text>')

    cp=map_plane(520,155,"power")
    ct=map_plane(400,72,"transport")
    p += [
        f'<path d="M{cp[0]:.1f} {cp[1]:.1f}L{ct[0]:.1f} {ct[1]:.1f}" class="flow-control"/>',
        '<rect x="800" y="330" width="270" height="80" rx="12" class="interface-box"/>',
        '<text x="820" y="358" class="eyebrow" fill="var(--control)">SHARED PHYSICAL INTERFACE</text>',
        '<text x="820" y="386" class="label">C1 · EV charging asset</text>',
        '<text x="820" y="405" class="equation math">I<tspan dy="5" font-size="13">PT</tspan></text>',

        '<rect x="1120" y="112" width="430" height="510" rx="16" class="side-panel"/>',
        '<text x="1148" y="150" class="eyebrow">STATE / VIABILITY GEOMETRY</text>',
        '<ellipse cx="1330" cy="350" rx="155" ry="120" class="viable"/>',
        '<ellipse cx="1330" cy="350" rx="105" ry="78" fill="none" stroke="var(--violet)" stroke-width="1.4"/>',
        '<path d="M1200 475L1458 230" class="critical-boundary"/>',
        '<text x="1420" y="250" class="equation math" fill="var(--red)">∂V</text>',
        '<circle cx="1255" cy="280" r="9" class="state"/>',
        '<path d="M1255 280L1320 342" class="projection"/>',
        '<circle cx="1320" cy="342" r="5" fill="var(--control)"/>',
        '<text x="1235" y="337" class="equation math">ρ<tspan dy="5" font-size="13">g</tspan></text>',
        '<path d="M1260 430C1300 402 1360 405 1410 368" class="flow-green"/>',
        '<text x="1170" y="558" class="equation math">F<tspan dy="5" font-size="13">G</tspan> → V<tspan dy="5" font-size="13">sus</tspan></text>',
        '<text x="1148" y="596" class="small">separate schematic state space</text>',

        '<text x="48" y="700" class="legend">STATIC 3D SCHEMATIC · NOT GIS ELEVATION · Depth encodes layer separation only.</text>',
        '<text x="48" y="732" class="legend">Coordinates and depth are explanatory and uncalibrated. Shape identifies node type; color never acts alone.</text>',
        '</svg>',
    ]
    return "\n".join(p)

def render_viability(palette: dict) -> str:
    p=svg_open(
        1400,500,
        "Graph to dynamics to viability",
        "A graph embedded on an affine model flat maps through coupled dynamics into an elliptical state-space viability region with a critical hyperplane, orthogonal margin and intervention vector.",
        style(palette,None),
    )
    p += [
        '<text x="48" y="54" class="eyebrow">GRAPH / MODEL SPACE</text>',
        '<text x="780" y="54" class="eyebrow">STATE / VIABILITY SPACE</text>',
        '<polygon points="70,130 520,150 620,390 170,370" class="model"/>',
        '<text x="90" y="105" class="equation math">G + I</text>',
        '<path d="M160 250L260 205L350 270L455 215L520 310" fill="none" stroke="var(--topology)" stroke-width="2.5"/>',
        '<circle cx="160" cy="250" r="10" fill="var(--power)"/>',
        polygon(4,260,205,12,"").replace('class=""','fill="var(--panel)" stroke="var(--topology)" stroke-width="2"'),
        polygon(6,350,270,14,"interface"),
        polygon(4,455,215,12,"",0).replace('class=""','fill="var(--panel)" stroke="var(--topology)" stroke-width="2"'),
        polygon(3,520,310,14,"").replace('class=""','fill="var(--transport)" stroke="var(--panel)" stroke-width="2"'),
        '<text x="185" y="342" class="small">graph embedded on an affine model window</text>',
        arrow(635,255,745,255,"var(--information)",3.0),
        '<text x="650" y="224" class="equation math">F<tspan dy="5" font-size="13">G</tspan></text>',
        '<ellipse cx="1030" cy="270" rx="245" ry="150" class="viable"/>',
        '<path d="M835 430L1230 108" class="critical-boundary"/>',
        '<text x="1190" y="132" class="equation math" fill="var(--red)">∂V</text>',
        '<circle cx="935" cy="170" r="10" class="state"/>',
        '<text x="952" y="166" class="equation math">Y(t)</text>',
        '<path d="M935 170L1030 248" class="projection"/>',
        '<circle cx="1030" cy="248" r="6" fill="var(--control)"/>',
        '<text x="940" y="245" class="equation math" fill="var(--control)">ρ_g</text>',
        '<path d="M970 350C1015 320 1080 335 1140 292" class="flow-green"/>',
        arrow(1100,360,1170,320,"var(--control)",3.0,"8 7"),
        '<text x="1165" y="365" class="equation math" fill="var(--control)">u*</text>',
        '<text x="48" y="472" class="small">No empirical validity is implied by a coherent graph, trajectory, ellipse, metric or boundary; each requires physical interpretation and validation.</text>',
        '</svg>',
    ]
    return "\n".join(p)

def render_state(palette: dict, dark: bool) -> str:
    p=svg_open(
        1400,360,
        "Current scientific transition",
        "The current research state moves from causal mechanisms to coupled hybrid multiscale dynamics using a geometric transition from a bounded causal polygon to a continuous dynamics ellipse.",
        style(palette,dark),
    )
    p += [
        '<text x="48" y="52" class="eyebrow">CURRENT SCIENTIFIC TRANSITION</text>',
        '<text x="48" y="88" class="title">Causal Mechanisms → Coupled Hybrid Multiscale Dynamics</text>',
        polygon(6,285,215,90,"model"),
        '<text x="285" y="210" text-anchor="middle" class="label">Causal Mechanisms</text>',
        '<text x="285" y="236" text-anchor="middle" class="small">typed interface + mechanism</text>',
        '<circle cx="248" cy="174" r="7" fill="var(--power)"/>',
        '<circle cx="322" cy="174" r="7" fill="var(--transport)"/>',
        '<path d="M255 176L315 176" class="flow-control"/>',
        arrow(410,215,620,215,"var(--control)",3.2),
        '<text x="470" y="188" class="label" fill="var(--control)">derive dynamics</text>',
        '<ellipse cx="855" cy="215" rx="205" ry="105" fill="var(--information-soft)" stroke="var(--information)" stroke-width="2.2"/>',
        '<path d="M720 240C765 160 820 275 885 180C930 120 980 255 1015 205" fill="none" stroke="var(--cyan)" stroke-width="3"/>',
        '<text x="855" y="210" text-anchor="middle" class="label">Coupled Hybrid Multiscale Dynamics</text>',
        '<text x="855" y="240" text-anchor="middle" class="equation math">Ẏ = F<tspan dy="5" font-size="13">G</tspan>(Y,u,η;θ)</text>',
        '<text x="1110" y="162" class="eyebrow">MATHEMATICAL STATE</text>',
        '<text x="1110" y="196" class="equation math">R → C → G → F<tspan dy="5" font-size="13">G</tspan></text>',
        '<text x="1110" y="230" class="small">active stages 2 → 3</text>',
        '<text x="1110" y="264" class="small">Power <tspan fill="var(--power)">●</tspan> · Transportation <tspan fill="var(--transport)">●</tspan></text>',
        '<text x="1110" y="296" class="small">Information <tspan fill="var(--information)">●</tspan></text>',
        '</svg>',
    ]
    return "\n".join(p)

def latest_public(observed: dict) -> str:
    best=None
    for r in observed.get("repositories",[]):
        raw=(r.get("latest_commit") or {}).get("date") or r.get("pushed_at") or ""
        try:
            t=datetime.fromisoformat(str(raw).replace("Z","+00:00")).timestamp()
        except ValueError:
            t=0
        if best is None or t>best[0]:
            best=(t,str(r.get("short_name") or r.get("repository") or "not observed"))
    return best[1] if best else "not observed"

def render_projects(palette: dict, projects: dict, observed: dict) -> str:
    featured=sorted([p for p in projects.get("projects",[]) if p.get("featured")],key=lambda x:int(x.get("profile_order",999)))[:4]
    colors=["violet","information","transport","cyan"]
    shapes=[("ellipse",0),("poly",6),("poly",4),("poly",5)]
    centers=[(250,245),(555,245),(860,245),(1165,245)]
    p=svg_open(
        1400,500,
        "Featured research systems as bounded geometric domains",
        "Four featured public research systems are represented as bounded geometric domains. Shape and accent color are navigation only, not evidence status or scientific importance.",
        style(palette,None),
    )
    p += [
        '<text x="48" y="54" class="eyebrow">FEATURED RESEARCH SYSTEMS</text>',
        '<text x="48" y="88" class="small">bounded research domains · shape is navigation only</text>',
    ]
    for i,item in enumerate(featured):
        cx,cy=centers[i]
        color=colors[i]
        p.append(f'<rect x="{cx-135}" y="125" width="270" height="245" rx="16" class="panel research-card" opacity=".001"/>')
        kind,n=shapes[i]
        if kind=="ellipse":
            p.append(f'<ellipse cx="{cx}" cy="{cy}" rx="118" ry="92" fill="var(--{color}-soft)" stroke="var(--{color})" stroke-width="2.4"/>')
        else:
            p.append(polygon(n,cx,cy,112,"").replace('class=""',f'fill="var(--{color}-soft)" stroke="var(--{color})" stroke-width="2.4"'))
        name=escape(str(item.get("short_name") or item.get("name") or "research system"))
        role=str(item.get("research_role") or "")
        role_lines=wrap_words(role, max_chars=27, max_lines=2)
        p.append(f'<text x="{cx}" y="{cy-18}" text-anchor="middle" class="label">{name}</text>')
        if role_lines:
            p.append(f'<text x="{cx}" y="{cy+10}" text-anchor="middle" class="tiny">{escape(role_lines[0])}</text>')
        if len(role_lines) > 1:
            p.append(f'<text x="{cx}" y="{cy+30}" text-anchor="middle" class="tiny">{escape(role_lines[1])}</text>')
    recent=escape(latest_public(observed))
    p += [
        '<line x1="48" y1="404" x2="1352" y2="404" stroke="var(--line)"/>',
        '<text x="48" y="438" class="eyebrow" fill="var(--control-ink)">MOST RECENT PUBLIC CHANGE</text>',
        f'<text x="310" y="438" class="small">{recent}</text>',
        '<text x="48" y="472" class="small">recency is metadata, not scientific importance or validation; bounded shape and accent are navigation only.</text>',
        '</svg>',
    ]
    return "\n".join(p)

def render_pipeline(palette: dict, framework: dict) -> str:
    stages=framework.get("stages",[])[:7]
    colors=["power","organization","transport","cyan","information","magenta","violet"]
    xs=[115,330,545,760,975,1190,1405]
    short_labels=[
        ("Multilayer","Structure"),
        ("Causal","Mechanisms"),
        ("Coupled Hybrid","Dynamics"),
        ("Feedback","Control"),
        ("Viability",""),
        ("Resilience ↔","Sustainability"),
        ("Transformation","Pathways"),
    ]
    p=svg_open(
        1540,460,
        "Seven-stage research architecture as an affine geometric progression",
        "Seven regular polygons lie on one affine progression line. Polygon side count indexes stage only and does not encode complexity, evidence strength or importance.",
        style(palette,None),
    )
    p += [
        '<text x="48" y="52" class="eyebrow">SEVEN-STAGE RESEARCH ARCHITECTURE</text>',
        '<path d="M95 210H1445" fill="none" stroke="var(--topology)" stroke-width="2"/>',
    ]
    for i,stage in enumerate(stages):
        x=xs[i]
        n=i+3
        color=colors[i]
        cls="model" if color=="violet" else ""
        if cls:
            p.append(polygon(n,x,210,34,cls))
        else:
            p.append(polygon(n,x,210,34,"").replace('class=""',f'fill="var(--{color}-soft)" stroke="var(--{color})" stroke-width="2.4"'))
        p.append(f'<text x="{x}" y="172" text-anchor="middle" class="eyebrow">STAGE {i+1}</text>')
        first,rest=short_labels[i]
        p.append(f'<text x="{x}" y="275" text-anchor="middle" class="label">{escape(first)}</text>')
        if rest:
            p.append(f'<text x="{x}" y="298" text-anchor="middle" class="label">{escape(rest)}</text>')
    p += [
        '<path d="M370 210L515 210" class="flow-control"/>',
        '<text x="395" y="190" class="small" fill="var(--control)">active transition 2 → 3</text>',
        '<circle cx="110" cy="360" r="6" fill="var(--green)"/><text x="124" y="366" class="small">viability state</text>',
        '<path d="M300 360H350" class="critical-boundary"/><text x="365" y="366" class="small">critical boundary</text>',
        '<text x="550" y="356" class="small">RGB progression is a visual navigation system; it is not a scientific ontology or evidence scale.</text>',
        '<text x="550" y="388" class="small">Polygon side count indexes stage number only; it does not encode complexity,</text>',
        '<text x="550" y="420" class="small">importance, evidence strength or validation.</text>',
        '</svg>',
    ]
    return "\n".join(p)

def main() -> int:
    contract=load("profile-visual-geometry.json")
    if contract.get("contract_id") != CONTRACT_ID:
        raise ValueError("profile geometry contract mismatch")
    palette=load("visual-palette.json")
    state=load("research-state.json")
    projects=load("projects.json")
    observed=load("public-github-state.json")
    framework=load("framework.json")
    power=load("power-network.json")
    transport=load("transport-network.json")

    write("research-hero-light.svg",render_hero(palette,False))
    write("research-hero-dark.svg",render_hero(palette,True))
    write("research-question.svg",render_question(palette))
    write("coupled-network-3d-light.svg",render_network_3d(palette,False,power,transport))
    write("coupled-network-3d-dark.svg",render_network_3d(palette,True,power,transport))
    write("graph-to-viability.svg",render_viability(palette))
    write("research-state-light.svg",render_state(palette,False))
    write("research-state-dark.svg",render_state(palette,True))
    write("project-system.svg",render_projects(palette,projects,observed))
    write("research-pipeline.svg",render_pipeline(palette,framework))

    print("Rendered PROFILE-GEOMETRY-V3 across all README visual surfaces.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
