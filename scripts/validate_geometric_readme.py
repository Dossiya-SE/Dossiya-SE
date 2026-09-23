#!/usr/bin/env python3
"""G4 semantic validation for GEOMETRIC-README-V3 final README visuals."""

from __future__ import annotations
import json,sys
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
    require("<script" not in t.lower(),f"{name}: scripts prohibited")
    require("prefers-reduced-motion:reduce" in t,f"{name}: reduced-motion fallback missing")
    for token in ("--power:","--transport:","--information:","--organization:","--violet:","--green:","--red:","--gold:"):
        require(token in t,f"{name}: governed palette token missing {token}")
    return t

def main():
    c=json.loads(CONTRACT.read_text(encoding="utf-8"))
    require(c.get("contract_id")=="GEOMETRIC-README-V3","visual contract id mismatch")
    require(c.get("scientific_geometry_contract")=="SCIENTIFIC-GEOMETRY-V3","scientific geometry contract link missing")

    readme=README.read_text(encoding="utf-8").lower()
    require("flat-geometry.svg" not in readme,"standalone flat-geometry lesson must not reappear")

    hero=read_svg("research-hero-light.svg")
    for token in ("COMPUTED AFFINE MULTILAYER SYSTEM","COMPUTED VIABILITY GEOMETRY","exact Euclidean nearest-boundary distance","not geographic elevation"):
        require(token in hero,f"hero semantic boundary missing: {token}")
    require("<polygon" in hero and "ρ₂" in hero and "∂V" in hero and "g=I" in hero,"hero computed Euclidean geometry incomplete")

    q=read_svg("research-question.svg")
    for token in ("PHYSICAL SYSTEM","CAUSAL INTERFACE","DYNAMICS","VIABILITY","P ↔ T","C₁","F_G"):
        require(token in q,f"research question missing {token}")

    net=read_svg("coupled-network-3d-light.svg")
    for token in ("R³ affine embedding","verified 3D scene","NOT GIS ELEVATION","shared interface"):
        require(token in net,f"coupled system semantic missing: {token}")

    gv=read_svg("graph-to-viability.svg")
    for token in ("COMPUTED VIABILITY","ρ₂","∂V","active boundary:","computed objects","non-Euclidean ρ_g"):
        require(token in gv,f"graph-to-viability semantic missing: {token}")
    require("<ellipse" not in gv,"graph-to-viability must not use a decorative ellipse as the feasible set")

    st=read_svg("research-state-light.svg")
    st_lower=st.lower()
    for token in ("svd projection","conceptual 4d state","not empirical measurement"):
        require(token in st_lower,f"research-state evidence boundary missing: {token}")

    pr=read_svg("project-system.svg")
    pr_semantic=pr.lower().replace("–","-").replace("—","-")
    require("equal-area geometric index" in pr_semantic,
            "project-system normalization title must state equal-area geometry")
    require(("same computed area" in pr_semantic) or ("equal computed area" in pr_semantic),
            "project-system must explicitly state equal computed area")
    require("do not encode rank" in pr_semantic,
            "project-system must state that geometry does not encode rank")

    pipe=read_svg("research-pipeline.svg")
    for token in ("CONTINUOUS γ(t)","γ:[0,1]→R²","γ(t_i)=S_i"):
        require(token in pipe,f"pipeline continuity semantic missing: {token}")

    print("GEOMETRIC README V3 SEMANTICS: PASS — computed geometry, evidence boundaries and non-color semantics are explicit.")

if __name__=="__main__":
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError,ET.ParseError) as exc:
        print(f"GEOMETRIC README V3 SEMANTICS: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
