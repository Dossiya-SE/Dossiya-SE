#!/usr/bin/env python3
"""Render a deterministic isometric 3D research hero for the profile README.

Depth encodes declared multilayer separation only. It is not geography, elevation,
telemetry, or calibrated infrastructure state. The figure is static by design because
GitHub does not guarantee SVG animation in its image viewer.
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
    order = ["bg","panel","ink","muted","line","topology","green","green_soft","red","red_soft","yellow","yellow_soft","yellow_ink","ghost"]
    return ";".join(f"--{k.replace('_','-')}:{p[k]}" for k in order)


def project(u: float, v: float, z: float) -> tuple[float, float]:
    # Oblique/isometric-style projection used only for explanatory layer separation.
    return 300 + 520*u - 220*v, 500 + 135*u + 105*v - z


def norm_positions(layer: dict, z: float) -> dict[str, tuple[float,float]]:
    xs=[float(n["x"]) for n in layer["nodes"]]; ys=[float(n["y"]) for n in layer["nodes"]]
    minx,maxx,miny,maxy=min(xs),max(xs),min(ys),max(ys)
    out={}
    for n in layer["nodes"]:
        if n["id"] == "C1":
            u,v=.53,.46
        else:
            u=.08+.84*(float(n["x"])-minx)/(maxx-minx)
            v=.10+.80*(float(n["y"])-miny)/(maxy-miny)
        out[n["id"]]=project(u,v,z)
    return out


def node(parts: list[str], n: dict, x: float, y: float) -> None:
    t=n["type"]
    parts.append(f'<line x1="{x:.1f}" y1="{y+12:.1f}" x2="{x:.1f}" y2="{y+25:.1f}" stroke="var(--line)" stroke-width="1.2"/>')
    parts.append(f'<ellipse cx="{x:.1f}" cy="{y+26:.1f}" rx="14" ry="5" fill="var(--ghost)" stroke="var(--line)"/>')
    fill,stroke="var(--panel)","var(--topology)"
    if t in {"generator","hub","origin","destination"}: fill,stroke="var(--green-soft)","var(--green)"
    if t=="interface": fill,stroke="var(--yellow-soft)","var(--yellow)"
    if t in {"generator","load","origin","destination","hub"}:
        parts.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="15" ry="10" fill="{fill}" stroke="{stroke}" stroke-width="2.2"/>')
    elif t in {"substation","intersection"}:
        pts=f"{x:.1f},{y-12:.1f} {x+16:.1f},{y:.1f} {x:.1f},{y+12:.1f} {x-16:.1f},{y:.1f}"
        parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2.2"/>')
    elif t=="interface":
        pts=f"{x:.1f},{y-15:.1f} {x+20:.1f},{y:.1f} {x:.1f},{y+15:.1f} {x-20:.1f},{y:.1f}"
        parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2.8"/>')
    elif t=="terminal":
        pts=f"{x:.1f},{y-15:.1f} {x+16:.1f},{y+11:.1f} {x-16:.1f},{y+11:.1f}"
        parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="2.2"/>')
    parts.append(f'<text x="{x:.1f}" y="{y+4:.1f}" text-anchor="middle" class="node">{escape(n["id"])}</text>')


def layer_plane(parts: list[str], z: float, label: str, symbol: str, *, power: bool) -> None:
    pts=[project(0,0,z),project(1,0,z),project(1,1,z),project(0,1,z)]
    poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
    parts.append(f'<polygon points="{poly}" fill="var(--panel)" fill-opacity=".88" stroke="var(--line)" stroke-width="1.5"/>')
    # Sparse grid gives spatial depth without implying GIS coordinates.
    for q in (.25,.5,.75):
        a,b=project(q,0,z),project(q,1,z); c,d=project(0,q,z),project(1,q,z)
        parts.append(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}M{c[0]:.1f} {c[1]:.1f}L{d[0]:.1f} {d[1]:.1f}" stroke="var(--line)" stroke-width=".8" opacity=".45"/>')
    lx,ly=project(.03,.03,z)
    parts.append(f'<text x="{lx:.1f}" y="{ly-20:.1f}" class="layer">{escape(label)} <tspan class="math">{symbol}</tspan></text>')
    parts.append(f'<text x="{lx:.1f}" y="{ly-2:.1f}" class="small">{("electrical service topology" if power else "mobility service topology")}</text>')


def edges(parts: list[str], layer: dict, pos: dict[str,tuple[float,float]], *, selected: set[str]) -> None:
    for e in layer["edges"]:
        a,b=pos[e["source"]],pos[e["target"]]
        cls="edge-soft" if e["type"] in {"distribution","logistics"} else "edge"
        parts.append(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" class="{cls}"/>')
        if e["id"] in selected:
            parts.append(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" class="service"/>')


def viability(parts: list[str]) -> None:
    x0,y0=1040,430
    parts.append('<text x="1032" y="160" class="eyebrow">STATE / VIABILITY GEOMETRY</text>')
    parts.append('<text x="1032" y="194" class="small">pseudo-3D state space · explanatory geometry</text>')
    # Axes triad.
    parts.append(f'<path d="M{x0} {y0}L1455 510M{x0} {y0}L1220 295M{x0} {y0}L{x0} 215" class="axis"/>')
    parts.append('<text x="1465" y="516" class="small">x₁</text><text x="1226" y="290" class="small">x₂</text><text x="1027" y="207" class="small">x₃</text>')
    # Stacked contours produce a deterministic 3D volume illusion.
    contours=[(0,0,185,64,.28),(0,-28,156,55,.22),(0,-54,124,44,.18),(0,-78,88,32,.14)]
    for i,(dx,dy,rx,ry,op) in enumerate(contours):
        fill='var(--green-soft)' if i==0 else 'none'
        parts.append(f'<ellipse cx="{1220+dx}" cy="{430+dy}" rx="{rx}" ry="{ry}" fill="{fill}" fill-opacity="{op}" stroke="var(--green)" stroke-width="{2.3 if i==0 else 1.2}" opacity=".9"/>')
    # Meridians/wireframe.
    parts.append('<path d="M1038 430C1085 374 1126 337 1220 352C1314 337 1355 374 1402 430" fill="none" stroke="var(--green)" stroke-width="1.1" opacity=".32"/>')
    parts.append('<path d="M1120 392C1154 362 1180 343 1220 352C1260 343 1286 362 1320 392" fill="none" stroke="var(--green)" stroke-width="1.1" opacity=".28"/>')
    # Critical boundary, state, margin, control.
    parts.append('<ellipse cx="1220" cy="430" rx="196" ry="70" fill="none" stroke="var(--red)" stroke-width="3" stroke-dasharray="9 8"/>')
    parts.append('<text x="1360" y="385" class="math red">∂𝒱</text>')
    parts.append('<text x="1245" y="455" class="math green">𝒱ₛᵤₛ</text>')
    parts.append('<circle cx="1184" cy="370" r="8" fill="var(--green)" stroke="var(--panel)" stroke-width="2"/>')
    parts.append('<text x="1198" y="366" class="math">Y(t)</text>')
    parts.append('<path d="M1190 375L1363 418" stroke="var(--red)" stroke-width="2.3" stroke-dasharray="6 6"/>')
    parts.append('<text x="1270" y="388" class="math red">ρ_g</text>')
    parts.append('<path d="M1190 365Q1238 322 1295 338" fill="none" stroke="var(--yellow)" stroke-width="3.5" stroke-dasharray="9 8"/>')
    star="1295,326 1299,335 1309,336 1301,343 1303,353 1295,348 1287,353 1289,343 1281,336 1291,335"
    parts.append(f'<polygon points="{star}" fill="var(--yellow-soft)" stroke="var(--yellow)" stroke-width="2"/>')
    parts.append('<text x="1315" y="344" class="math yellow">u*</text>')
    parts.append('<text x="1032" y="575" class="math-sm">Ẏ = F_𝒢(Y,u,η;θ)</text>')
    parts.append('<text x="1032" y="606" class="math-sm green">Y(t) ∈ 𝒱ₛᵤₛ(t)</text>')
    parts.append('<text x="1032" y="637" class="math-sm red">ρ_g(Y)=d_g(Y,∂𝒱)</text>')


def render(power: dict, transport: dict, palette: dict, dark: bool) -> str:
    p=palette["dark" if dark else "light"]
    css=f'''<style>
:root{{{vars_for(p)}}}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:20px}} .math-sm{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:17px}}
.title{{font-size:34px;font-weight:820;letter-spacing:-.02em}} .eyebrow{{font-size:12px;font-weight:800;letter-spacing:.14em;fill:var(--muted)}}
.layer{{font-size:19px;font-weight:780}} .small{{font-size:12px;fill:var(--muted)}} .node{{font-size:10px;font-weight:800;fill:var(--ink)}}
.edge{{fill:none;stroke:var(--topology);stroke-width:2.2;stroke-linecap:round}} .edge-soft{{fill:none;stroke:var(--muted);stroke-width:1.5;stroke-dasharray:5 6}}
.service{{fill:none;stroke:var(--green);stroke-width:3;stroke-linecap:round}} .interface{{fill:none;stroke:var(--yellow);stroke-width:3.5;stroke-dasharray:8 7}}
.axis{{fill:none;stroke:var(--topology);stroke-width:1.6}} .green{{fill:var(--green)}} .red{{fill:var(--red)}} .yellow{{fill:var(--yellow-ink)}}
@media(prefers-reduced-motion:reduce){{}}
</style>'''
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 760" role="img" aria-labelledby="title desc">',
           '<title id="title">Isometric 3D coupled Power–Transportation research geometry</title>',
           '<desc id="desc">Static isometric multilayer infrastructure geometry. Power and Transportation are separated by visual depth, C1 links the layer representations, and a pseudo-3D viability geometry shows Y(t), the critical boundary, resilience margin and intervention. Depth is explanatory, not geographic elevation or telemetry.</desc>',css,
           '<rect x="1" y="1" width="1598" height="758" rx="30" fill="var(--bg)" stroke="var(--line)"/>',
           '<text x="50" y="58" class="title">Coupled Power–Transportation · Isometric Research Geometry</text>',
           '<text x="50" y="87" class="small">typed multilayer topology · explicit physical interface · state/viability geometry</text>',
           '<text x="1550" y="58" text-anchor="end" class="eyebrow">3D SCHEMATIC · NOT GIS ELEVATION</text>']

    zt,zp=0,230
    # Depth pillars at plane corners.
    for u,v in ((0,0),(1,0),(1,1),(0,1)):
        a,b=project(u,v,zt),project(u,v,zp)
        parts.append(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" stroke="var(--line)" stroke-width="1" stroke-dasharray="4 6"/>')
    layer_plane(parts,zt,"TRANSPORTATION NETWORK","𝓖_T",power=False)
    layer_plane(parts,zp,"POWER NETWORK","𝓖_P",power=True)
    ppos=norm_positions(power,zp); tpos=norm_positions(transport,zt)
    edges(parts,power,ppos,selected={"P01","P03","P06","P08"})
    edges(parts,transport,tpos,selected={"T01","T03","T08","T11"})
    for n in power["nodes"]: node(parts,n,*ppos[n["id"]])
    for n in transport["nodes"]: node(parts,n,*tpos[n["id"]])
    # Shared physical interface column between layer representations.
    a,b=tpos["C1"],ppos["C1"]
    parts.append(f'<path d="M{a[0]:.1f} {a[1]-16:.1f}L{b[0]:.1f} {b[1]+16:.1f}" class="interface"/>')
    mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
    parts.append(f'<rect x="{mx+18:.1f}" y="{my-27:.1f}" width="158" height="50" rx="12" fill="var(--yellow-soft)" stroke="var(--yellow)"/>')
    parts.append(f'<text x="{mx+97:.1f}" y="{my-6:.1f}" text-anchor="middle" class="math yellow">𝔐I_PT</text>'.replace('𝔐I','𝔐I'))
    # overwrite weird glyph with rigorous object in a safe text node
    parts[-1]=f'<text x="{mx+97:.1f}" y="{my-6:.1f}" text-anchor="middle" class="math yellow">𝕀_PT</text>'
    parts.append(f'<text x="{mx+97:.1f}" y="{my+13:.1f}" text-anchor="middle" class="small">same physical asset · C1</text>')
    parts.append('<text x="54" y="706" class="small">Green = admissible service · Red = critical boundary · Light yellow/ochre = causal interface or intervention · Charcoal = physical topology</text>')
    viability(parts)
    parts.append('<text x="1548" y="735" text-anchor="end" class="small">Visual depth encodes layer separation only; coordinates are explanatory and uncalibrated.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def main() -> int:
    power=load("power-network.json"); transport=load("transport-network.json"); palette=load("visual-palette.json")
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"coupled-network-3d-light.svg").write_text(render(power,transport,palette,False)+"\n",encoding="utf-8")
    (OUT/"coupled-network-3d-dark.svg").write_text(render(power,transport,palette,True)+"\n",encoding="utf-8")
    print("Rendered governed static isometric 3D network hero assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
