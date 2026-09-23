#!/usr/bin/env python3
"""Render SCIENTIFIC-GEOMETRY-V3 into deterministic GitHub SVG assets.

Scientific coordinates come only from data/computed-geometry-v3.json.
Manual coordinates are limited to page composition, typography and framing.
"""

from __future__ import annotations
import json, math
from html import escape
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
OUT=ROOT/"assets"/"generated"
ART=ROOT/"artifacts"

TYPE={"title":38,"h2":26,"label":20,"small":18,"micro":16,"project_name":18}

def load_json(name):
    return json.loads((DATA/name).read_text(encoding="utf-8"))

def vars_for(p):
    keys=("bg","panel","ink","muted","line","topology","green","green_soft","red","red_soft",
          "yellow","yellow_soft","yellow_ink","ghost","power","power_soft","transport","transport_soft",
          "information","information_soft","organization","organization_ink","organization_soft",
          "cyan","cyan_soft","violet","violet_soft","magenta","magenta_soft","gold","gold_soft")
    return ";".join(f"--{k.replace('_','-')}:{p[k]}" for k in keys)

def style(palette,mode=None):
    light=vars_for(palette["light"]); dark=vars_for(palette["dark"])
    root=dark if mode=="dark" else light
    media="" if mode else f"@media(prefers-color-scheme:dark){{:root{{{dark}}}}}"
    return f"""<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:"DejaVu Serif","Liberation Serif",Georgia,serif}}
.title{{font-size:{TYPE["title"]}px;font-weight:820;letter-spacing:-.02em}}
.h2{{font-size:{TYPE["h2"]}px;font-weight:780}}
.label{{font-size:{TYPE["label"]}px;font-weight:720}}
.small{{font-size:{TYPE["small"]}px;fill:var(--muted)}}
.micro{{font-size:{TYPE["micro"]}px;fill:var(--muted);letter-spacing:.08em}}
.project-name{{font-size:{TYPE["project_name"]}px;font-weight:720}}
.panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
.plane{{fill:var(--ghost);stroke:var(--line);stroke-width:1.4}}
.power{{fill:none;stroke:var(--power);stroke-width:3}}
.transport{{fill:none;stroke:var(--transport);stroke-width:3}}
.info{{fill:none;stroke:var(--information);stroke-width:2;stroke-dasharray:8 7}}
.org{{fill:none;stroke:var(--organization);stroke-width:2;stroke-dasharray:2 6}}
.model{{fill:none;stroke:var(--violet);stroke-width:2.4}}
.viable{{fill:var(--green-soft);stroke:var(--green);stroke-width:2.4}}
.critical{{fill:none;stroke:var(--red);stroke-width:3.2;stroke-dasharray:10 8}}
.control{{fill:none;stroke:var(--gold);stroke-width:3.2;stroke-dasharray:8 6}}
.state{{fill:var(--cyan);stroke:var(--panel);stroke-width:2}}
.node{{fill:var(--panel);stroke-width:2.4}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>"""

def svg_open(w,h,title,desc,palette,mode=None):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>{style(palette,mode)}'

def regular_polygon(n,cx,cy,r,phase=-math.pi/2):
    return [(cx+r*math.cos(phase+2*math.pi*j/n),cy+r*math.sin(phase+2*math.pi*j/n)) for j in range(n)]

def pts(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x,y in points)

def path(points):
    return "M"+"L".join(f"{x:.1f},{y:.1f}" for x,y in points)

def arrow(x1,y1,x2,y2,klass):
    ang=math.atan2(y2-y1,x2-x1); s=11
    p1=(x2-s*math.cos(ang-.55),y2-s*math.sin(ang-.55))
    p2=(x2-s*math.cos(ang+.55),y2-s*math.sin(ang+.55))
    return f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}M{p1[0]:.1f} {p1[1]:.1f}L{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}" class="{klass}"/>'

_SUBSCRIPT_TRANSLATION=str.maketrans("0123456789-","₀₁₂₃₄₅₆₇₈₉₋")

def subscript_int(value):
    """Render an integer as deterministic Unicode subscript digits for SVG labels."""
    return str(int(value)).translate(_SUBSCRIPT_TRANSLATION)

def make_fit(all_points,x0,y0,x1,y1,pad=0.06):
    flat=[p for group in all_points for p in group]
    xs=[float(p[0]) for p in flat]; ys=[float(p[1]) for p in flat]
    xmin,xmax=min(xs),max(xs); ymin,ymax=min(ys),max(ys)
    dx=max(xmax-xmin,1e-9); dy=max(ymax-ymin,1e-9)
    W=(x1-x0)*(1-2*pad); H=(y1-y0)*(1-2*pad)
    scale=min(W/dx,H/dy)
    cx=(xmin+xmax)/2; cy=(ymin+ymax)/2
    sx=(x0+x1)/2; sy=(y0+y1)/2
    def tr(p):
        return (sx+scale*(float(p[0])-cx),sy-scale*(float(p[1])-cy))
    return tr

def bbox(points):
    xs=[p[0] for p in points]; ys=[p[1] for p in points]
    return [min(xs),min(ys),max(xs),max(ys)]

def text_box(x,y,text,font=None,anchor="middle"):
    font=TYPE["label"] if font is None else font
    width=max(8.0,0.58*font*len(text)); height=1.25*font
    if anchor=="middle": x0=x-width/2
    elif anchor=="end": x0=x-width
    else: x0=x
    return [x0,y-height,width+x0,y+0.25*height]

def draw_viability(g,x0,y0,x1,y1):
    v=g["viability"]
    groups=[v["vertices"],[v["state"]],[v["boundary_point"]],v["active_segment"]]
    tr=make_fit(groups,x0,y0,x1,y1,pad=.10)
    poly=[tr(p) for p in v["vertices"]]
    state=tr(v["state"]); q=tr(v["boundary_point"]); seg=[tr(p) for p in v["active_segment"]]
    markup=[
        f'<polygon points="{pts(poly)}" class="viable"/>',
        f'<path d="M{seg[0][0]:.1f} {seg[0][1]:.1f}L{seg[1][0]:.1f} {seg[1][1]:.1f}" class="critical"/>',
        f'<circle cx="{state[0]:.1f}" cy="{state[1]:.1f}" r="9" class="state"/>',
        arrow(state[0],state[1],q[0],q[1],"control"),
        f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="6" fill="var(--gold)"/>',
        f'<text x="{state[0]+14:.1f}" y="{state[1]-12:.1f}" class="math label">Y(t)</text>',
        f'<text x="{(state[0]+q[0])/2+10:.1f}" y="{(state[1]+q[1])/2-8:.1f}" class="math label" fill="var(--gold)">ρ₂</text>',
        f'<text x="{seg[1][0]-6:.1f}" y="{seg[1][1]-12:.1f}" text-anchor="end" class="math label" fill="var(--red)">∂V</text>',
    ]
    return markup,{"region":bbox(poly),"state":[state[0]-9,state[1]-9,state[0]+9,state[1]+9],"projection":[min(state[0],q[0]),min(state[1],q[1]),max(state[0],q[0]),max(state[1],q[1])]}

def hero(g,palette,mode):
    w,h=1600,620
    c=g["coupled"]
    all_left=[c["power_plane_2d"],c["transport_plane_2d"],c["power_nodes_2d"],c["transport_nodes_2d"],c["interface_segment_2d"]]
    tr=make_fit(all_left,65,145,755,505,pad=.05)
    pp=[tr(p) for p in c["power_plane_2d"]]; tp=[tr(p) for p in c["transport_plane_2d"]]
    pn=[tr(p) for p in c["power_nodes_2d"]]; tn=[tr(p) for p in c["transport_nodes_2d"]]
    inter=[tr(p) for p in c["interface_segment_2d"]]
    p=[svg_open(w,h,"Dossiya Dakou — computational geometry research portrait",
        "Computed affine Power and Transportation layers with a shared interlayer interface and a Shapely-derived viability region. The displayed resilience margin is the exact Euclidean nearest-boundary normal projection.",palette,mode),
       '<rect x="1" y="1" width="1598" height="618" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="56" y="62" class="title">Dossiya Dakou</text>',
       '<text x="56" y="94" class="small">Physics-grounded mathematical engineering · computed geometry → verified SVG</text>',
       '<line x1="56" y1="116" x2="1544" y2="116" stroke="var(--line)"/>',
       '<text x="62" y="148" class="micro">COMPUTED AFFINE MULTILAYER SYSTEM</text>',
       f'<polygon points="{pts(pp)}" class="plane"/>',
       f'<polygon points="{pts(tp)}" class="plane"/>']
    for edges,nodes,klass in [(c["power_edges"],pn,"power"),(c["transport_edges"],tn,"transport")]:
        for a,b in edges:
            p.append(f'<path d="M{nodes[a][0]:.1f} {nodes[a][1]:.1f}L{nodes[b][0]:.1f} {nodes[b][1]:.1f}" class="{klass}"/>')
    kinds=[3,4,5,6,4]
    for i,(x,y) in enumerate(pn):
        p.append(f'<polygon points="{pts(regular_polygon(kinds[i],x,y,13))}" class="node" stroke="var(--power)"/>')
    for i,(x,y) in enumerate(tn):
        p.append(f'<polygon points="{pts(regular_polygon(kinds[::-1][i],x,y,13))}" class="node" stroke="var(--transport)"/>')
    p += [
      f'<path d="M{inter[0][0]:.1f} {inter[0][1]:.1f}L{inter[1][0]:.1f} {inter[1][1]:.1f}" class="control"/>',
      f'<polygon points="{pts(regular_polygon(6,(inter[0][0]+inter[1][0])/2,(inter[0][1]+inter[1][1])/2,24))}" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="3"/>',
      '<text x="96" y="188" class="label" fill="var(--power)">POWER · affine layer P</text>',
      '<text x="96" y="476" class="label" fill="var(--transport)">TRANSPORTATION · affine layer T</text>',
      '<line x1="800" y1="142" x2="800" y2="535" stroke="var(--line)"/>',
      '<text x="850" y="148" class="micro">COMPUTED VIABILITY GEOMETRY</text>'
    ]
    vm,vl=draw_viability(g,850,165,1515,505); p.extend(vm)
    p += [
      '<text x="56" y="568" class="small">Affine coordinates are computed from rank-2 plane bases; layer separation is schematic, not geographic elevation.</text>',
      '<text x="56" y="594" class="small">The green set is a computed constraint intersection; ρ₂ is the exact Euclidean nearest-boundary distance (g=I).</text>',
      '</svg>'
    ]
    return "\n".join(p),{"viewbox":[0,0,w,h],"major":[bbox(pp),bbox(tp),vl["region"]]}

def research_question(g,palette):
    w,h=1600,420
    centers=[(175,220),(515,220),(860,220),(1240,220)]
    specs=[(3,"power","PHYSICAL SYSTEM","P ↔ T","Power ↔ Transportation"),
           (6,"gold","CAUSAL INTERFACE","C₁","typed coupling"),
           (5,"information","DYNAMICS","F_G","coupled hybrid dynamics")]
    p=[svg_open(w,h,"Research question as minimal geometric logic",
        "Minimal mathematical reasoning diagram from the coupled physical system through a causal interface and coupled dynamics to the viability objective.",palette),
       '<rect x="1" y="1" width="1598" height="418" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="58" class="micro">RESEARCH QUESTION · MINIMAL GEOMETRIC LOGIC</text>']
    boxes=[]; labels=[]
    for (x,y),(n,col,title,symbol,sub) in zip(centers[:3],specs):
        poly=regular_polygon(n,x,y,72); boxes.append(bbox(poly))
        p += [f'<text x="{x}" y="{y-106}" text-anchor="middle" class="label">{title}</text>',
              f'<polygon points="{pts(poly)}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="3"/>',
              f'<text x="{x}" y="{y+7}" text-anchor="middle" class="math h2">{symbol}</text>',
              f'<text x="{x}" y="{y+118}" text-anchor="middle" class="small">{sub}</text>']
        labels += [text_box(x,y-106,title),text_box(x,y+118,sub,TYPE["small"])]
    p += ['<text x="1240" y="114" text-anchor="middle" class="label">VIABILITY</text>',
          '<ellipse cx="1240" cy="220" rx="125" ry="76" class="viable"/>',
          '<text x="1240" y="227" text-anchor="middle" class="math h2">V</text>',
          '<text x="1240" y="338" text-anchor="middle" class="small">Y(t) ∈ V · maximize ρ₂</text>']
    boxes.append([1115,144,1365,296]); labels += [text_box(1240,114,"VIABILITY"),text_box(1240,338,"Y(t) ∈ V · maximize ρ₂",TYPE["small"])]
    for a,b in zip(centers[:-1],centers[1:]):
        p.append(arrow(a[0]+95,a[1],b[0]-105,b[1],"control"))
    p += ['<text x="48" y="390" class="small">Which physically defensible interfaces generate dynamics that can be controlled away from critical boundaries?</text>','</svg>']
    return "\n".join(p),{"viewbox":[0,0,w,h],"major":boxes,"labels":labels}

def coupled(g,palette,mode):
    w,h=1600,760
    c=g["coupled"]
    all_left=[c["power_plane_2d"],c["transport_plane_2d"],c["power_nodes_2d"],c["transport_nodes_2d"],c["interface_segment_2d"]]
    tr=make_fit(all_left,65,130,965,585,pad=.06)
    pp=[tr(p) for p in c["power_plane_2d"]]; tp=[tr(p) for p in c["transport_plane_2d"]]
    pn=[tr(p) for p in c["power_nodes_2d"]]; tn=[tr(p) for p in c["transport_nodes_2d"]]; inter=[tr(p) for p in c["interface_segment_2d"]]
    p=[svg_open(w,h,"Computed coupled Power–Transportation multilayer geometry",
        "Static projection of a computed 3D two-layer affine system. PyVista and Trimesh validate the 3D scene; the SVG is a deterministic orthographic projection, not GIS elevation.",palette,mode),
       '<rect x="1" y="1" width="1598" height="758" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="55" class="title">Coupled Power–Transportation System</text>',
       '<text x="48" y="84" class="small">R³ affine embedding → verified 3D scene → deterministic 2D publication projection</text>',
       f'<polygon points="{pts(pp)}" class="plane"/>',f'<polygon points="{pts(tp)}" class="plane"/>']
    for edges,nodes,klass in [(c["power_edges"],pn,"power"),(c["transport_edges"],tn,"transport")]:
        for a,b in edges:
            p.append(f'<path d="M{nodes[a][0]:.1f} {nodes[a][1]:.1f}L{nodes[b][0]:.1f} {nodes[b][1]:.1f}" class="{klass}"/>')
    for i,(x,y) in enumerate(pn): p.append(f'<polygon points="{pts(regular_polygon([3,4,5,6,4][i],x,y,16))}" class="node" stroke="var(--power)"/>')
    for i,(x,y) in enumerate(tn): p.append(f'<polygon points="{pts(regular_polygon([4,6,5,3,6][i],x,y,16))}" class="node" stroke="var(--transport)"/>')
    mid=((inter[0][0]+inter[1][0])/2,(inter[0][1]+inter[1][1])/2)
    p += [f'<path d="M{inter[0][0]:.1f} {inter[0][1]:.1f}L{inter[1][0]:.1f} {inter[1][1]:.1f}" class="control"/>',
          f'<polygon points="{pts(regular_polygon(6,mid[0],mid[1],30))}" fill="var(--gold-soft)" stroke="var(--gold)" stroke-width="3"/>',
          '<text x="86" y="154" class="label" fill="var(--power)">POWER NETWORK · plane P</text>',
          '<text x="86" y="556" class="label" fill="var(--transport)">TRANSPORTATION NETWORK · plane T</text>',
          '<rect x="1030" y="128" width="505" height="490" rx="16" class="panel"/>',
          '<text x="1060" y="164" class="micro">STATE / VIABILITY GEOMETRY</text>']
    vm,vl=draw_viability(g,1050,180,1515,575); p.extend(vm)
    p += ['<text x="48" y="690" class="small">STATIC 3D SCHEMATIC · NOT GIS ELEVATION. The separation h is a visual layer coordinate; it is not physical height, measured flow, or live telemetry.</text>',
          '<text x="48" y="718" class="small">The shared interface is the segment between corresponding layer states, validated as non-degenerate in R³.</text>','</svg>']
    return "\n".join(p),{"viewbox":[0,0,w,h],"major":[bbox(pp),bbox(tp),vl["region"]]}

def graph_viability(g,palette):
    w,h=1600,560
    p=[svg_open(w,h,"Graph to dynamics to computed viability",
        "A typed polygonal graph maps through an affine model plane into a Shapely-computed feasible region. The displayed ρ₂ margin is the exact Euclidean nearest-boundary distance and normal projection.",palette),
       '<rect x="1" y="1" width="1598" height="558" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="56" class="micro">GRAPH → DYNAMICS → COMPUTED VIABILITY</text>',
       '<text x="70" y="100" class="label">GRAPH / MODEL SPACE</text>',
       '<polygon points="60,145 580,125 635,360 115,380" class="plane"/>',
       '<path d="M150 250L280 190L390 280L520 200L280 190L390 280" fill="none" stroke="var(--topology)" stroke-width="2"/>']
    nodes=[(150,250,3,"power"),(280,190,4,"transport"),(390,280,5,"information"),(520,200,6,"organization")]
    for x,y,n,col in nodes: p.append(f'<polygon points="{pts(regular_polygon(n,x,y,22))}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="2.5"/>')
    p += ['<text x="110" y="420" class="math label">G + I → F_G</text>',
          '<polygon points="690,185 830,165 855,335 715,355" fill="var(--violet-soft)" stroke="var(--violet)" stroke-width="2.2"/>',
          '<text x="772" y="248" text-anchor="middle" class="math label">Ẏ=F_G</text>',
          '<text x="772" y="292" text-anchor="middle" class="small">affine model plane</text>',
          arrow(650,270,675,270,"control"),
          arrow(870,270,930,270,"control"),
          '<text x="955" y="100" class="label">STATE / VIABILITY SPACE</text>']
    vm,vl=draw_viability(g,945,125,1540,440); p.extend(vm)
    active_label="g"+subscript_int(g["viability"]["active_constraint_index"])+"(Y)=0"
    p += [f'<text x="965" y="468" class="small">V = intersection of {len(g["viability"]["constraints"])} governed constraints</text>',
          f'<text x="965" y="493" class="small">active boundary: {active_label}</text>',
          '<text x="48" y="535" class="small">The feasible set, nearest boundary point and Euclidean ρ₂ are computed objects; a non-Euclidean ρ_g requires a separately justified metric.</text>','</svg>']
    return "\n".join(p),{"viewbox":[0,0,w,h],"major":[[60,125,635,420],[690,165,855,355],vl["region"]]}

def research_state(g,palette,mode):
    w,h=1600,500
    rs=g["research_state"]; pts2=rs["projected_2d"]
    tr=make_fit([pts2],165,120,1450,380,pad=.12)
    p2=[tr(x) for x in pts2]
    p=[svg_open(w,h,"Current research state as SVD-projected conceptual state space",
        "Five explicitly conceptual four-dimensional research-state vectors projected by SVD into two dimensions. The highlighted transition is mechanism to dynamics; coordinates are not empirical measurements.",palette,mode),
       '<rect x="1" y="1" width="1598" height="498" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="56" class="micro">CURRENT RESEARCH STATE · SVD PROJECTION OF CONCEPTUAL 4D STATE</text>',
       '<line x1="120" y1="400" x2="1490" y2="400" stroke="var(--line)"/>',
       '<line x1="120" y1="100" x2="120" y2="420" stroke="var(--line)"/>',
       '<text x="1490" y="425" text-anchor="end" class="small">component 1</text>',
       '<text x="92" y="112" class="small">component 2</text>']
    for a,b in zip(p2[:-1],p2[1:]): p.append(f'<path d="M{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}" class="model"/>')
    boxes=[]
    for i,((x,y),label) in enumerate(zip(p2,rs["labels"])):
        r=18 if i not in (rs["current_index"],rs["target_index"]) else 24
        col="gold" if i==rs["current_index"] else ("information" if i==rs["target_index"] else "violet")
        poly=regular_polygon(5 if i==rs["target_index"] else 6,x,y,r)
        boxes.append(bbox(poly))
        p += [f'<polygon points="{pts(poly)}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="3"/>',
              f'<text x="{x:.1f}" y="{y-34:.1f}" text-anchor="middle" class="label">{escape(label)}</text>']
    a=p2[rs["current_index"]]; b=p2[rs["target_index"]]; p.append(arrow(a[0],a[1],b[0],b[1],"control"))
    ev=rs["explained_variance_ratio"]
    p += [f'<text x="48" y="452" class="small">Conceptual normalized state r=(r_s,r_c,r_d,r_v); SVD projection only.</text>',
          f'<text x="48" y="478" class="small">First two components explain {(ev[0]+ev[1])*100:.1f}% of configured conceptual variance; coordinates are not empirical measurements.</text>','</svg>']
    return "\n".join(p),{"viewbox":[0,0,w,h],"major":boxes}

def projects(g,palette):
    w,h=1600,500
    items=g["projects"]["items"]; centers=[220,600,980,1360]; cols=["power","violet","transport","cyan"]
    p=[svg_open(w,h,"Featured research systems with equal-area geometric signatures",
        "Four research systems shown with equal-area regular polygons. Shape and color are navigation only and do not encode rank, evidence strength or scientific importance.",palette),
       '<rect x="1" y="1" width="1598" height="498" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="58" class="micro">FEATURED RESEARCH SYSTEMS · EQUAL-AREA GEOMETRIC INDEX</text>']
    boxes=[]
    label_boxes=[]
    cells=[[x-150,110,x+150,310] for x in centers]
    for x,item,col in zip(centers,items,cols):
        poly=[(x+vx,210+vy) for vx,vy in item["vertices"]]; boxes.append(bbox(poly))
        p += [f'<polygon points="{pts(poly)}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="3"/>',
              f'<text x="{x}" y="322" text-anchor="middle" class="project-name">{escape(item["name"])}</text>',
              f'<text x="{x}" y="354" text-anchor="middle" class="small">{item["sides"]}-vertex signature</text>']
        label_boxes += [text_box(x,322,item["name"],TYPE["project_name"]),
                        text_box(x,354,f'{item["sides"]}-vertex signature',TYPE["small"])]
    p += ['<line x1="48" y1="402" x2="1552" y2="402" stroke="var(--line)"/>',
          '<text x="48" y="435" class="small">All signatures have the same computed area; shape/color do not encode rank, maturity, scientific importance or validation.</text>','</svg>']
    return "\n".join(p),{"viewbox":[0,0,w,h],"major":boxes,"cells":cells,"centers":[[x,210] for x in centers],"labels":label_boxes}

def pipeline(g,palette):
    w,h=1800,460
    pipe=g["pipeline"]; gamma=pipe["gamma"]; anchors=pipe["anchors"]
    def tr(p): return (120+1560*float(p[0]),235-520*float(p[1]))
    curve=[tr(p) for p in gamma]; stage=[tr(p) for p in anchors]
    cols=["power","organization","information","cyan","green","magenta","violet"]
    p=[svg_open(w,h,"Seven-stage research architecture as continuous gamma trajectory",
        "The seven stages are landmarks on a continuous cubic-spline trajectory gamma(t). Shape differentiates stages; the active mechanism-to-dynamics transition is highlighted.",palette),
       '<rect x="1" y="1" width="1798" height="458" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
       '<text x="48" y="56" class="micro">SEVEN-STAGE RESEARCH ARCHITECTURE · CONTINUOUS γ(t)</text>',
       f'<path d="{path(curve)}" fill="none" stroke="var(--violet)" stroke-width="3"/>']
    boxes=[]
    for i,((x,y),label,n,col) in enumerate(zip(stage,pipe["labels"],pipe["sides"],cols)):
        if int(n)==0:
            p.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="58" ry="42" class="viable"/>'); boxes.append([x-58,y-42,x+58,y+42])
        else:
            poly=regular_polygon(int(n),x,y,58); boxes.append(bbox(poly))
            p.append(f'<polygon points="{pts(poly)}" fill="var(--{col}-soft)" stroke="var(--{col})" stroke-width="3"/>')
        p += [f'<text x="{x:.1f}" y="{y+5:.1f}" text-anchor="middle" class="label">{i+1}</text>',
              f'<text x="{x:.1f}" y="{y+86:.1f}" text-anchor="middle" class="label">{escape(label)}</text>']
    a=stage[1]; b=stage[2]; p.append(arrow(a[0]+60,a[1],b[0]-60,b[1],"control"))
    p += ['<text x="48" y="426" class="small">γ:[0,1]→R² is continuous and satisfies γ(t_i)=S_i at all seven stage anchors. Geometry is navigation, not ontology or evidence scale.</text>','</svg>']
    return "\n".join(p),{"viewbox":[0,0,w,h],"major":boxes,"curve":bbox(curve)}

def main():
    g=load_json("computed-geometry-v3.json")
    if g.get("contract_id")!="SCIENTIFIC-GEOMETRY-V3":
        raise ValueError("computed geometry v3 missing")
    if g.get("viability",{}).get("distance_metric")!="euclidean_L2":
        raise ValueError("V3 SVG renderer requires viability metric euclidean_L2")
    palette=load_json("visual-palette.json")
    OUT.mkdir(parents=True,exist_ok=True); ART.mkdir(parents=True,exist_ok=True)
    rendered={}
    layouts={}
    for name,fn,args in [
        ("research-hero-light.svg",hero,(g,palette,"light")),
        ("research-hero-dark.svg",hero,(g,palette,"dark")),
        ("research-question.svg",research_question,(g,palette)),
        ("coupled-network-3d-light.svg",coupled,(g,palette,"light")),
        ("coupled-network-3d-dark.svg",coupled,(g,palette,"dark")),
        ("graph-to-viability.svg",graph_viability,(g,palette)),
        ("research-state-light.svg",research_state,(g,palette,"light")),
        ("research-state-dark.svg",research_state,(g,palette,"dark")),
        ("project-system.svg",projects,(g,palette)),
        ("research-pipeline.svg",pipeline,(g,palette)),
    ]:
        svg,layout=fn(*args)
        (OUT/name).write_text(svg+"\n",encoding="utf-8")
        layouts[name]=layout
    (ART/"visual-layout-v3.json").write_text(json.dumps({"contract_id":"SCIENTIFIC-GEOMETRY-V3","typography":TYPE,"figures":layouts},indent=2)+"\n",encoding="utf-8")
    print("Rendered SCIENTIFIC-GEOMETRY-V3 across all primary README visuals.")

if __name__=="__main__":
    main()
