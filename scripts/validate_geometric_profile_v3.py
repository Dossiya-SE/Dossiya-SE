#!/usr/bin/env python3
"""Validate PROFILE-GEOMETRY-V3 contract, polyglot sources and rendered assets."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
OUT=ROOT/"assets"/"generated"
README=ROOT/"README.md"
CONTRACT="PROFILE-GEOMETRY-V3"

SOURCES=[
    "mathematical-art/profile-visuals/PROFILE_GEOMETRY_V3.md",
    "mathematical-art/profile-visuals/overleaf/profile_visuals.tex",
    "mathematical-art/profile-visuals/julia/profile_geometry.jl",
    "mathematical-art/profile-visuals/react/ProfileGeometry.tsx",
    "mathematical-art/profile-visuals/react/profile-geometry.css",
    "mathematical-art/profile-visuals/go/main.go",
    "mathematical-art/profile-visuals/csharp/ProfileGeometry.cs",
]

ASSETS=[
    "research-hero-light.svg","research-hero-dark.svg","research-question.svg",
    "coupled-network-3d-light.svg","coupled-network-3d-dark.svg",
    "graph-to-viability.svg","research-state-light.svg","research-state-dark.svg",
    "project-system.svg","research-pipeline.svg",
]

def require(ok:bool,msg:str)->None:
    if not ok:
        raise ValueError(msg)

def read(path:str)->str:
    return (ROOT/path).read_text(encoding="utf-8")

def validate_contract()->None:
    c=json.loads((DATA/"profile-visual-geometry.json").read_text(encoding="utf-8"))
    require(c.get("schema_version")=="3.0","profile geometry schema must be 3.0")
    require(c.get("contract_id")==CONTRACT,"profile geometry contract id mismatch")
    require(set(c.get("public_assets",{}))=={
        "research-hero","research-question","coupled-network-3d","graph-to-viability",
        "research-state","project-system","research-pipeline"
    },"public visual geometry registry mismatch")
    rule=c.get("non_inference_rule","").lower()
    for word in ("importance","evidence","validity"):
        require(word in rule,f"non-inference rule missing {word}")

def validate_sources()->None:
    for rel in SOURCES:
        path=ROOT/rel
        require(path.exists(),f"missing geometry source: {rel}")
        require(CONTRACT in path.read_text(encoding="utf-8"),f"{rel}: contract id missing")
    tex=read(SOURCES[1])
    require("\\begin{tikzpicture}" in tex and "\\regpoly" in tex,"TikZ publication geometry incomplete")
    julia=read(SOURCES[2])
    for token in ("regular_polygon","AffineFlat","project_hyperplane","hyperplane_distance"):
        require(token in julia,f"Julia source missing {token}")
    react=read(SOURCES[3])
    for token in ("AffinePlane","TypedNode","ViabilityGeometry","StageMarker"):
        require(token in react,f"React geometry mirror missing {token}")
    go=read(SOURCES[5])
    require("RegularPolygon" in go and "HyperplaneDistance" in go,"Go geometry exporter incomplete")
    cs=read(SOURCES[6])
    require("ProjectToHyperplane" in cs and "RegularPolygon" in cs,"C# geometry integration incomplete")

def svg(name:str)->str:
    path=OUT/name
    require(path.exists(),f"missing redesigned visual: {name}")
    text=path.read_text(encoding="utf-8")
    root=ET.fromstring(text)
    require(root.tag.endswith("svg"),f"{name}: invalid SVG root")
    require(root.attrib.get("viewBox"),f"{name}: missing viewBox")
    require("<title" in text and "<desc" in text,f"{name}: accessibility metadata missing")
    require("<script" not in text.lower(),f"{name}: embedded scripts forbidden")
    for token in ("--power:","--transport:","--information:","--violet:","--control:"):
        require(token in text,f"{name}: governed palette token missing {token}")
    return text

def validate_assets()->None:
    rendered={name:svg(name) for name in ASSETS}

    for name in ("research-hero-light.svg","research-hero-dark.svg"):
        t=rendered[name]
        for token in ("power-plane","transport-plane","level-set","critical-boundary","projection","SYSTEM CHANNELS"):
            require(token in t,f"{name}: missing geometric hero object {token}")
        require(t.count("<polygon")>=6,f"{name}: insufficient typed polygon geometry")

    q=rendered["research-question.svg"]
    for token in ("Power ↔ Transportation interfaces","typed shared asset","Coupled dynamics","Sustainable viability","Y(t) ∈ V"):
        require(token in q,f"research-question missing {token}")
    require(q.count("<ellipse")>=1 and q.count("<polygon")>=4,"research-question geometry incomplete")

    for name in ("coupled-network-3d-light.svg","coupled-network-3d-dark.svg"):
        t=rendered[name]
        for token in ("two affine 2-flats","POWER NETWORK","TRANSPORTATION NETWORK","SHARED PHYSICAL INTERFACE","STATE / VIABILITY GEOMETRY"):
            require(token in t,f"{name}: missing multilayer geometry semantic {token}")
        require(t.count('class="plane ')>=2,f"{name}: two affine layer windows required")
        require(t.count("<polygon")>=6,f"{name}: typed polygon nodes missing")

    v=rendered["graph-to-viability.svg"]
    for token in ("GRAPH / MODEL SPACE","STATE / VIABILITY SPACE","critical-boundary","projection","∂V","ρ_g","u*"):
        require(token in v,f"graph-to-viability missing {token}")
    require("graph embedded on an affine model window" in v,"graph flat interpretation missing")

    for name in ("research-state-light.svg","research-state-dark.svg"):
        t=rendered[name]
        require("Causal Mechanisms" in t and "Coupled Hybrid Multiscale Dynamics" in t,f"{name}: transition endpoints missing")
        require("<ellipse" in t and "<polygon" in t,f"{name}: polygon-to-continuous-state geometry missing")

    projects=rendered["project-system.svg"]
    require(projects.count('class="panel research-card"')==4,"project system must retain four bounded systems")
    require(projects.count("<polygon")>=3 and projects.count("<ellipse")>=1,"project domains must use mixed bounded geometry")
    require("shape is navigation only" in projects,"project shape non-inference rule missing")

    pipeline=rendered["research-pipeline.svg"]
    require(pipeline.count("<polygon")>=7,"pipeline must contain seven polygon stage markers")
    require("Polygon side count indexes stage number only" in pipeline,"pipeline shape-index rule missing")
    require("does not encode complexity" in pipeline,"pipeline non-inference rule incomplete")

def validate_readme()->None:
    text=README.read_text(encoding="utf-8")
    lower=text.lower()
    require("assets/generated/flat-geometry.svg" not in text,"standalone flat-geometry figure must not remain in public README")
    require("reproducible flat-geometry sources" not in lower,"standalone flat-geometry disclosure must not remain in README")
    for name in (
        "research-hero-light.svg","research-question.svg","coupled-network-3d-light.svg",
        "graph-to-viability.svg","research-state-light.svg","project-system.svg","research-pipeline.svg"
    ):
        require(f"assets/generated/{name}" in text,f"README missing redesigned asset {name}")

def main()->int:
    validate_contract()
    validate_sources()
    validate_assets()
    validate_readme()
    print("PROFILE GEOMETRY V3 VALIDATION: PASS — semantic geometry, polyglot responsibilities, accessibility and README integration are consistent.")
    return 0

if __name__=="__main__":
    try:
        raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError,ET.ParseError) as exc:
        print(f"PROFILE GEOMETRY V3 VALIDATION: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
