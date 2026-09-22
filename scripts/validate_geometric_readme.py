#!/usr/bin/env python3
"""Validate GEOMETRIC-README-V2 final README visuals."""
from __future__ import annotations
import json,re,sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"assets"/"generated"
README=ROOT/"README.md"
CONTRACT=ROOT/"data"/"geometric-readme.json"
FILES=[
"research-hero-light.svg","research-hero-dark.svg","research-question.svg",
"coupled-network-3d-light.svg","coupled-network-3d-dark.svg",
"graph-to-viability.svg","research-state-light.svg","research-state-dark.svg",
"project-system.svg","research-pipeline.svg"
]

def require(ok,msg):
    if not ok: raise ValueError(msg)

def read_svg(name):
    p=OUT/name
    require(p.exists(),f"missing final visual: {name}")
    t=p.read_text(encoding="utf-8")
    r=ET.fromstring(t)
    require(r.tag.endswith("svg"),f"{name}: root not SVG")
    require(r.attrib.get("viewBox"),f"{name}: viewBox missing")
    require("<title" in t and "<desc" in t,f"{name}: accessibility metadata missing")
    require("<script" not in t.lower(),f"{name}: script prohibited")
    require("prefers-reduced-motion:reduce" in t,f"{name}: reduced-motion fallback missing")
    for token in ("--power:","--transport:","--information:","--organization:","--violet:","--green:","--red:","--gold:"):
        require(token in t,f"{name}: governed palette token missing {token}")
    return t

def main():
    c=json.loads(CONTRACT.read_text(encoding="utf-8"))
    require(c.get("contract_id")=="GEOMETRIC-README-V2","contract id mismatch")
    readme=README.read_text(encoding="utf-8")
    require("flat-geometry.svg" not in readme,"standalone flat-geometry figure must not appear in README")
    require("Reproducible flat-geometry sources" not in readme,"tool list must not appear in public README")

    hero=read_svg("research-hero-light.svg")
    for s in ("affine layer P","affine layer T","C₁ · shared physical interface","critical hyperplane","orthogonal intervention"):
        require(s in hero,f"hero missing geometric role: {s}")
    require(hero.count("<polygon")>=12,"hero needs typed polygonal topology")
    require(hero.count("<ellipse")>=2,"hero needs viability ellipses")

    q=read_svg("research-question.svg")
    for s in ("PHYSICAL SYSTEM","CAUSAL INTERFACE","DYNAMICS","VIABILITY"):
        require(s in q,f"research question missing stage {s}")
    require(q.count("<polygon")>=3 and "<ellipse" in q,"research question geometric progression incomplete")

    net=read_svg("coupled-network-3d-light.svg")
    for s in ("POWER NETWORK · plane P","TRANSPORTATION NETWORK · plane T","C₁ · EV charging asset","STATE / VIABILITY GEOMETRY"):
        require(s in net,f"coupled system missing {s}")
    require(net.count('class="plane"')>=2,"coupled system must use two affine planes")

    gv=read_svg("graph-to-viability.svg")
    for s in ("GRAPH / MODEL SPACE","STATE / VIABILITY SPACE","affine model plane","ρ_g","∂V"):
        require(s in gv,f"graph-to-viability missing {s}")
    require('class="critical"' in gv and 'class="control"' in gv,"boundary/projection grammar missing")

    st=read_svg("research-state-light.svg")
    for s in ("CURRENT SCIENTIFIC TRANSITION","CAUSAL","COUPLED HYBRID","MATHEMATICAL STATE"):
        require(s in st,f"research state missing {s}")
    require(st.count("<polygon")>=4 and "<ellipse" in st,"research state geometric phase grammar incomplete")

    pr=read_svg("project-system.svg")
    require("FEATURED RESEARCH SYSTEMS · GEOMETRIC INDEX" in pr,"project geometric index missing")
    require(pr.count("<polygon")>=4,"project systems need four geometric signatures")
    require("navigation only" in pr,"project shapes must disclaim ranking")

    pipe=read_svg("research-pipeline.svg")
    require("SEVEN-STAGE RESEARCH ARCHITECTURE" in pipe,"pipeline title missing")
    require(pipe.count("<polygon")>=6 and "<ellipse" in pipe,"seven-stage geometric path incomplete")
    require("Geometry is a navigation grammar, not an ontology or evidence scale." in pipe,"pipeline evidence boundary missing")

    print("GEOMETRIC README VALIDATION: PASS — all existing README visuals use governed geometric structure with scientific boundaries intact.")
    return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError,ET.ParseError) as e:
        print(f"GEOMETRIC README VALIDATION: FAIL — {e}",file=sys.stderr); raise SystemExit(1)
