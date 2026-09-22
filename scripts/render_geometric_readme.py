#!/usr/bin/env python3
"""Render the complete geometry-driven GitHub README visual system.

GEOMETRIC-README-V2
The existing README visuals are redesigned using mathematically meaningful
plane geometry and affine-flat constructions. Shapes are structural, not decorative.
"""

from __future__ import annotations
import json, math
from html import escape
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
OUT=ROOT/"assets"/"generated"

ASSETS=[
    "research-hero-light.svg","research-hero-dark.svg","research-question.svg",
    "coupled-network-3d-light.svg","coupled-network-3d-dark.svg",
    "graph-to-viability.svg","research-state-light.svg","research-state-dark.svg",
    "project-system.svg","research-pipeline.svg"
]

def load(name):
    return json.loads((DATA/name).read_text(encoding="utf-8"))

def vars_for(p):
    keys=("bg","panel","ink","muted","line","topology","green","green_soft","red","red_soft",
          "yellow","yellow_soft","yellow_ink","ghost","power","power_soft","transport","transport_soft",
          "information","information_soft","organization","organization_ink","organization_soft",
          "cyan","cyan_soft","violet","violet_soft","magenta","magenta_soft","gold","gold_soft")
    return ";".join(f"--{k.replace('_','-')}:{p[k]}" for k in keys)

def style(palette, mode=None):
    light=vars_for(palette["light"]); dark=vars_for(palette["dark"])
    root=dark if mode=="dark" else light
    media="" if mode else f"@media(prefers-color-scheme:dark){{:root{{{dark}}}}}"
    return f"""<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:"DejaVu Serif","Liberation Serif",Georgia,serif}}
.title{{font-size:34px;font-weight:820;letter-spacing:-.02em}}
.h2{{font-size:22px;font-weight:780}}
.label{{font-size:15px;font-weight:720}}
.small{{font-size:13px;fill:var(--muted)}}
.micro{{font-size:11px;fill:var(--muted);letter-spacing:.08em}}
.panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
.plane{{fill:var(--ghost);stroke:var(--line);stroke-width:1.3}}
.power{{fill:none;stroke:var(--power);stroke-width:3}}
.transport{{fill:none;stroke:var(--transport);stroke-width:3}}
.info{{fill:none;stroke:var(--information);stroke-width:2;stroke-dasharray:8 7}}
.org{{fill:none;stroke:var(--organization);stroke-width:2;stroke-dasharray:2 6}}
.model{{fill:none;stroke:var(--violet);stroke-width:2.3}}
.viable{{fill:var(--green-soft);stroke:var(--green);stroke-width:2.2}}
.critical{{fill:none;stroke:var(--red);stroke-width:3;stroke-dasharray:10 8}}
.control{{fill:none;stroke:var(--gold);stroke-width:3;stroke-dasharray:8 6}}
.state{{fill:var(--cyan);stroke:var(--panel);stroke-width:2}}
.node{{fill:var(--panel);stroke-width:2.4}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>"""

def svg_open(w,h,title,desc,palette,mode=None):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>{style(palette,mode)}'

def polygon(n,cx,cy,r,rotation=-math.pi/2):
    return " ".join(f"{cx+r*math.cos(rotation+2*math.pi*j/n):.1f},{cy+r*math.sin(rotation+2*math.pi*j/n):.1f}" for j in range(n))

def arrow(x1,y1,x2,y2,klass):
    ang=math.atan2(y2-y1,x2-x1); s=11
    p1=(x2-s*math.cos(ang-.55), y2-s*math.sin(ang-.55))
    p2=(x2-s*math.cos(ang+.55), y2-s*math.sin(ang+.55))
    return f'<path d="M{x1} {y1}L{x2} {y2}M{p1[0]:.1f} {p1[1]:.1f}L{x2} {y2}L{p2[0]:.1f} {p2[1]:.1f}" class="{klass}"/>'

def hero(palette,mode):
    p=[svg_open(1600,620,"Dossiya Dakou — geometric research portrait",
        "Geometry-driven research portrait: Power and Transportation occupy two affine planes; a shared hexagonal interface couples them; state-space ellipses, a dashed critical hyperplane and an orthogonal intervention projection encode the mathematical research direction.",palette,mode)]
    p += [
      '<rect x="1" y="1" width="1598" height="618" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
      '<text x="56" y="62" class="title">Dossiya Dakou</text>',
      '<text x="56" y="94" class="small">Physics-grounded mathematical engineering · geometry as structure, not decoration</text>',
      '<line x1="56" y1="116" x2="1544" y2="116" stroke="var(--line)"/>',
      '<text x="60" y="153" class="micro">COUPLED PHYSICAL SYSTEM</text>',
      '<polygon points="90,205 575,165 700,270 215,310" class="plane"/>',
      '<polygon points="115,360 600,320 725,425 240,465" class="plane"/>',
      '<text x="115" y="198" class="label" fill="var(--power)">POWER · affine layer P</text>',
      '<text x="140" y="354" class="label" fill="var(--transport)">TRANSPORTATION · affine layer T</text>',
      '<path d="M155 260L260 222L365 255L480 210L610 252" class="power"/>',
      '<path d="M180 415L300 372L410 410L535 365L660 405" class="transport"/>',
    ]
    for x,y,n,color in [(155,260,3,"power"),(260,222,4,"power"),(365,255,5,"power"),(480,210,6,"power"),(610,252,4,"power"),
                        (180,415,4,"transport"),(300,372,6,"transport"),(410,410,5,"transport"),(535,365,3,"transport"),(660,405,6,"transport")]:
        p.append(f'<polygon points="{polygon(n,x,y,13)}" class="node" stroke="var(--{color})"/>')
    p += [
      '<polygon points="'+polygon(6,520,316,28)+'" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="3"/>',
      '<text x="555" y="321" class="label" fill="var(--gold)">C₁ · shared physical interface</text>',
      '<path d="M520 287L520 345" class="control"/>',
      '<path d="M320 242C410 278 445 295 492 307" class="info"/>',
      '<path d="M352 395C430 365 462 344 497 326" class="org"/>',
      '<line x1="760" y1="142" x2="760" y2="540" stroke="var(--line)"/>',
      '<text x="805" y="153" class="micro">STATE / VIABILITY GEOMETRY</text>',
      '<ellipse cx="1160" cy="338" rx="300" ry="150" class="viable"/>',
      '<ellipse cx="1160" cy="338" rx="226" ry="104" class="model"/>',
      '<path d="M930 455L1395 215" class="critical"/>',
      '<text x="1370" y="225" class="label" fill="var(--red)">∂V · critical hyperplane</text>',
      '<circle cx="1045" cy="270" r="9" class="state"/>',
      '<text x="1062" y="264" class="math label">Y(t)</text>',
      '<path d="M1045 270L1123 310" class="control"/>',
      '<circle cx="1123" cy="310" r="6" fill="var(--gold)"/>',
      '<text x="1065" y="315" class="small" fill="var(--gold)">orthogonal intervention / margin direction</text>',
      '<path d="M1000 382C1060 348 1105 380 1158 344S1275 285 1335 332" fill="none" stroke="var(--cyan)" stroke-width="3"/>',
      '<polygon points="'+polygon(3,940,190,22)+'" fill="var(--power-soft)" stroke="var(--power)" stroke-width="2"/>',
      '<polygon points="'+polygon(4,1000,190,22,math.pi/4)+'" fill="var(--transport-soft)" stroke="var(--transport)" stroke-width="2"/>',
      '<polygon points="'+polygon(5,1060,190,22)+'" fill="var(--information-soft)" stroke="var(--information)" stroke-width="2"/>',
      '<polygon points="'+polygon(6,1120,190,22)+'" fill="var(--organization-soft)" stroke="var(--organization)" stroke-width="2"/>',
      '<text x="1180" y="195" class="small">triangle → quadrilateral → pentagon → hexagon</text>',
      '<text x="56" y="585" class="small">Planes encode layer separation; polygons encode typed structure; ellipses encode bounded state regions; dashed line encodes a critical boundary. None is measured telemetry.</text>',
      '</svg>'
    ]
    return "\n".join(p)

def research_question(palette):
    p=[svg_open(1600,420,"Research question as geometric progression",
        "A geometric progression from coupled physical structure through causal mechanism and hybrid dynamics into viability: triangle, hexagonal interface, pentagonal dynamics object and elliptical admissible set.",palette)]
    p += ['<rect x="1" y="1" width="1598" height="418" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
          '<text x="48" y="58" class="micro">RESEARCH QUESTION · GEOMETRIC LOGIC</text>']
    centers=[(175,220),(515,220),(860,220),(1240,220)]
    shapes=[(3,"power","PHYSICAL SYSTEM","Power ↔ Transportation"),
            (6,"gold","CAUSAL INTERFACE","typed coupling C₁"),
            (5,"information","DYNAMICS","Ẏ = F_G(Y,u,η;θ)")]
    for (x,y),(n,col,title,sub) in zip(centers[:3],shapes):
        p.append(f'<polygon points="{polygon(n,x,y,72)}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="3"/>')
        p.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" class="label">{title}</text><text x="{x}" y="{y+118}" text-anchor="middle" class="small">{sub}</text>')
    p += [
      '<ellipse cx="1240" cy="220" rx="125" ry="76" class="viable"/>',
      '<ellipse cx="1240" cy="220" rx="78" ry="42" class="model"/>',
      '<path d="M1140 285L1355 160" class="critical"/>',
      '<text x="1240" y="225" text-anchor="middle" class="label">VIABILITY</text>',
      '<text x="1240" y="338" text-anchor="middle" class="small">Y(t) ∈ V · maximize ρ_g</text>'
    ]
    for a,b in zip(centers[:-1],centers[1:]):
        p.append(arrow(a[0]+95,a[1],b[0]-105,b[1],"control"))
    p += ['<text x="48" y="390" class="small">Question: which physically defensible interfaces generate dynamics that can be controlled away from critical boundaries?</text>','</svg>']
    return "\n".join(p)

def coupled(palette,mode):
    p=[svg_open(1600,760,"Coupled Power–Transportation geometry",
        "Static multilayer schematic using two affine planes, typed polygonal nodes, a shared hexagonal physical interface and a separate viability geometry. Depth encodes layer separation only, not geographic elevation or measured flow.",palette,mode)]
    p += ['<rect x="1" y="1" width="1598" height="758" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
          '<text x="48" y="55" class="title">Coupled Power–Transportation System</text>',
          '<text x="48" y="84" class="small">affine layers · polygonal typed nodes · shared physical intersection · viability side-panel</text>',
          '<polygon points="90,190 800,135 900,280 190,335" class="plane"/>',
          '<polygon points="125,410 835,355 935,500 225,555" class="plane"/>',
          '<rect x="1015" y="132" width="520" height="478" rx="16" class="panel"/>',
          '<text x="112" y="176" class="label" fill="var(--power)">POWER NETWORK · plane P</text>',
          '<text x="146" y="396" class="label" fill="var(--transport)">TRANSPORTATION NETWORK · plane T</text>']
    P=[(180,250,3),(320,210,4),(465,245,5),(610,195,6),(770,245,4)]
    T=[(215,475,4),(360,430,6),(510,472,5),(655,420,3),(820,465,6)]
    p.append('<path d="M180 250L320 210L465 245L610 195L770 245" class="power"/>')
    p.append('<path d="M215 475L360 430L510 472L655 420L820 465" class="transport"/>')
    for x,y,n in P: p.append(f'<polygon points="{polygon(n,x,y,17)}" class="node" stroke="var(--power)"/>')
    for x,y,n in T: p.append(f'<polygon points="{polygon(n,x,y,17)}" class="node" stroke="var(--transport)"/>')
    p += [
      '<polygon points="'+polygon(6,590,334,34)+'" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="3"/>',
      '<text x="636" y="339" class="label" fill="var(--gold)">C₁ · EV charging asset</text>',
      '<path d="M590 299L590 369" class="control"/>',
      '<path d="M465 245C505 274 548 296 571 311" class="info"/>',
      '<path d="M510 472C545 424 564 382 580 359" class="org"/>',
      '<text x="1042" y="170" class="micro">STATE / VIABILITY GEOMETRY</text>',
      '<ellipse cx="1275" cy="365" rx="200" ry="125" class="viable"/>',
      '<ellipse cx="1275" cy="365" rx="142" ry="80" class="model"/>',
      '<path d="M1105 500L1455 225" class="critical"/>',
      '<circle cx="1215" cy="315" r="9" class="state"/>',
      '<path d="M1215 315L1286 371" class="control"/>',
      '<circle cx="1286" cy="371" r="6" fill="var(--gold)"/>',
      '<text x="1320" y="230" class="label" fill="var(--red)">∂V</text>',
      '<text x="1042" y="575" class="small">STATIC 3D SCHEMATIC · NOT GIS ELEVATION</text>',
      '<text x="1042" y="596" class="small">Coordinates and depth are explanatory and uncalibrated.</text>',
      '<text x="48" y="705" class="small">The same physical object C₁ intersects both layers. Vertical separation is a visual encoding of multilayer structure and is not geographic elevation.</text>',
      '</svg>']
    return "\n".join(p)

def graph_viability(palette):
    p=[svg_open(1600,560,"Graph to dynamics to viability",
        "A polygonal graph complex maps through an affine model plane into an elliptical viable set with a dashed critical hyperplane and exact normal projection from the current state.",palette)]
    p += ['<rect x="1" y="1" width="1598" height="558" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
          '<text x="48" y="56" class="micro">GRAPH → DYNAMICS → VIABILITY</text>',
          '<text x="70" y="100" class="label">GRAPH / MODEL SPACE</text>',
          '<polygon points="60,145 580,125 635,360 115,380" class="plane"/>']
    nodes=[(150,250,3,"power"),(280,190,4,"transport"),(390,280,5,"information"),(520,200,6,"organization")]
    p += ['<path d="M150 250L280 190L390 280L520 200L280 190L390 280" fill="none" stroke="var(--topology)" stroke-width="2"/>']
    for x,y,n,c in nodes: p.append(f'<polygon points="{polygon(n,x,y,22)}" fill="var(--{c}-soft)" stroke="var(--{c})" stroke-width="2.5"/>')
    p += ['<text x="110" y="420" class="math label">G + I → F_G</text>',
          '<path d="M675 270L840 270" class="control"/>',
          '<polygon points="690,185 830,165 855,335 715,355" fill="var(--violet-soft)" stroke="var(--violet)" stroke-width="2.2"/>',
          '<text x="772" y="248" text-anchor="middle" class="math label">Ẏ=F_G</text>',
          '<text x="772" y="292" text-anchor="middle" class="small">affine model plane</text>',
          '<text x="960" y="100" class="label">STATE / VIABILITY SPACE</text>',
          '<ellipse cx="1240" cy="285" rx="280" ry="155" class="viable"/>',
          '<ellipse cx="1240" cy="285" rx="205" ry="104" class="model"/>',
          '<path d="M1020 420L1485 150" class="critical"/>',
          '<circle cx="1130" cy="250" r="9" class="state"/>',
          '<path d="M1130 250L1210 305" class="control"/>',
          '<circle cx="1210" cy="305" r="6" fill="var(--gold)"/>',
          '<text x="1150" y="230" class="math label">Y(t)</text>',
          '<text x="1230" y="332" class="math label" fill="var(--gold)">ρ_g</text>',
          '<text x="1445" y="172" class="math label" fill="var(--red)">∂V</text>',
          '<text x="48" y="520" class="small">No empirical validity is implied: the polygons, affine plane, ellipse and hyperplane are mathematical representations whose physical meaning requires calibration and validation.</text>',
          '</svg>']
    return "\n".join(p)

def state_visual(palette,mode):
    p=[svg_open(1600,420,"Current research state as geometric phase diagram",
        "Current research state shown as a geometric phase diagram: a gold hexagonal causal interface transitions into a blue pentagonal coupled-dynamics object, embedded between Power and Transportation sector markers.",palette,mode)]
    p += ['<rect x="1" y="1" width="1598" height="418" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
          '<text x="48" y="56" class="micro">CURRENT SCIENTIFIC TRANSITION</text>',
          '<polygon points="'+polygon(3,170,210,62)+'" fill="var(--power-soft)" stroke="var(--power)" stroke-width="3"/>',
          '<text x="170" y="216" text-anchor="middle" class="label">POWER</text>',
          '<polygon points="'+polygon(4,350,210,62,math.pi/4)+'" fill="var(--transport-soft)" stroke="var(--transport)" stroke-width="3"/>',
          '<text x="350" y="216" text-anchor="middle" class="label">TRANSPORT</text>',
          '<path d="M430 210L600 210" class="control"/>',
          '<polygon points="'+polygon(6,710,210,82)+'" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="3"/>',
          '<text x="710" y="204" text-anchor="middle" class="label">CAUSAL</text><text x="710" y="226" text-anchor="middle" class="label">MECHANISMS</text>',
          '<path d="M805 210L965 210" class="control"/>',
          '<polygon points="'+polygon(5,1080,210,88)+'" fill="var(--information-soft)" stroke="var(--information)" stroke-width="3"/>',
          '<text x="1080" y="198" text-anchor="middle" class="label">COUPLED HYBRID</text><text x="1080" y="220" text-anchor="middle" class="label">MULTISCALE</text><text x="1080" y="242" text-anchor="middle" class="label">DYNAMICS</text>',
          '<ellipse cx="1395" cy="210" rx="125" ry="72" class="viable"/>',
          '<text x="1395" y="206" text-anchor="middle" class="label">NEXT</text><text x="1395" y="228" text-anchor="middle" class="small">viability / control</text>',
          '<text x="48" y="380" class="small">MATHEMATICAL STATE · structure → mechanism → dynamics → admissible-state geometry. Polygon type is navigation, not evidence strength.</text>',
          '</svg>']
    return "\n".join(p)

def projects(palette):
    items=[("Africa Energy Dignity",3,"power"),("Mathematics Exploration",6,"violet"),
           ("Optimization for Sustainability",4,"transport"),("Mathematical Surface Engineering",5,"cyan")]
    p=[svg_open(1600,500,"Featured research systems as geometric signatures",
        "Four featured research systems represented by distinct geometric signatures: triangle, hexagon, quadrilateral and pentagon. Shape differentiates systems without implying scientific ranking.",palette),
       '<rect x="1" y="1" width="1598" height="498" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="58" class="micro">FEATURED RESEARCH SYSTEMS · GEOMETRIC INDEX</text>']
    xs=[220,600,980,1360]
    for x,(name,n,col) in zip(xs,items):
        p.append(f'<polygon points="{polygon(n,x,210,76)}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="3"/>')
        p.append(f'<text x="{x}" y="324" text-anchor="middle" class="label">{escape(name)}</text>')
        p.append(f'<text x="{x}" y="351" text-anchor="middle" class="small">{n}-vertex signature · navigation only</text>')
    p += ['<line x1="48" y1="402" x2="1552" y2="402" stroke="var(--line)"/>',
          '<text x="48" y="435" class="micro" fill="var(--gold)">MOST RECENT PUBLIC CHANGE</text>',
          '<text x="280" y="435" class="small">recency is metadata, not scientific importance or validation; shape and color are navigation only.</text>',
          '</svg>']
    return "\n".join(p)

def pipeline(palette):
    stages=[("1","STRUCTURE",3,"power"),("2","MECHANISM",6,"organization"),("3","DYNAMICS",5,"information"),
            ("4","CONTROL",4,"cyan"),("5","VIABILITY",0,"green"),("6","INTERFACE",8,"magenta"),("7","TRANSFORM",10,"violet")]
    p=[svg_open(1800,420,"Seven-stage research architecture as a continuous geometric path",
        "Seven-stage architecture encoded by a continuous sequence of geometric objects from triangle and hexagon through pentagon, quadrilateral, ellipse, octagon and decagon. The active transition is stages two to three.",palette),
       '<rect x="1" y="1" width="1798" height="418" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="56" class="micro">SEVEN-STAGE RESEARCH ARCHITECTURE · CONTINUOUS GEOMETRIC PATH</text>']
    xs=[140,390,640,890,1140,1390,1640]
    for i,(num,name,n,col) in enumerate(stages):
        x=xs[i]
        if i:
            klass="control" if i==2 else "model"
            p.append(arrow(xs[i-1]+78,210,x-78,210,klass))
        if n==0:
            p.append(f'<ellipse cx="{x}" cy="210" rx="72" ry="52" class="viable"/>')
        else:
            p.append(f'<polygon points="{polygon(n,x,210,66)}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="3"/>')
        p.append(f'<text x="{x}" y="207" text-anchor="middle" class="label">{num}</text><text x="{x}" y="232" text-anchor="middle" class="small">{name}</text>')
    p += ['<text x="48" y="372" class="small">Active transition: CAUSAL MECHANISMS → COUPLED HYBRID MULTISCALE DYNAMICS. Geometry is a navigation grammar, not an ontology or evidence scale.</text>','</svg>']
    return "\n".join(p)

def main():
    palette=load("visual-palette.json")
    OUT.mkdir(parents=True,exist_ok=True)
    generated={
      "research-hero-light.svg":hero(palette,"light"),
      "research-hero-dark.svg":hero(palette,"dark"),
      "research-question.svg":research_question(palette),
      "coupled-network-3d-light.svg":coupled(palette,"light"),
      "coupled-network-3d-dark.svg":coupled(palette,"dark"),
      "graph-to-viability.svg":graph_viability(palette),
      "research-state-light.svg":state_visual(palette,"light"),
      "research-state-dark.svg":state_visual(palette,"dark"),
      "project-system.svg":projects(palette),
      "research-pipeline.svg":pipeline(palette),
    }
    for name,content in generated.items():
        (OUT/name).write_text(content+"\n",encoding="utf-8")
    print("Rendered GEOMETRIC-README-V2 across all primary README visuals.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
