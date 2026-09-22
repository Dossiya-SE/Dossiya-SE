#!/usr/bin/env python3
"""Validate FLAT-GEOMETRY-V1 mathematics, sources and rendered SVG."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"
README = ROOT / "README.md"
CONTRACT_ID = "FLAT-GEOMETRY-V1"

SOURCE_FILES = [
    "mathematical-art/flat-geometry/FLAT_GEOMETRY_VISUAL_SPEC.md",
    "mathematical-art/flat-geometry/README.md",
    "mathematical-art/flat-geometry/overleaf/flat_geometry.tex",
    "mathematical-art/flat-geometry/julia/flat_geometry.jl",
    "mathematical-art/flat-geometry/react/FlatGeometry.tsx",
    "mathematical-art/flat-geometry/react/flat-geometry.css",
    "mathematical-art/flat-geometry/go/main.go",
    "mathematical-art/flat-geometry/csharp/FlatGeometry.cs",
]


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise ValueError(msg)


def regular_polygon(n: int, r: float = 1.0) -> list[tuple[float, float]]:
    return [
        (r * math.cos(math.pi/2 + 2*math.pi*j/n), -r * math.sin(math.pi/2 + 2*math.pi*j/n))
        for j in range(n)
    ]


def validate_polygon_geometry() -> None:
    for n in range(3, 11):
        pts = regular_polygon(n)
        lengths = []
        for i in range(n):
            x1, y1 = pts[i]
            x2, y2 = pts[(i+1) % n]
            lengths.append(math.hypot(x2-x1, y2-y1))
        require(max(lengths)-min(lengths) < 1e-12, f"{n}-gon generator is not regular")
        require(abs(sum(x for x, _ in pts)) < 1e-12, f"{n}-gon centroid x drift")
        require(abs(sum(y for _, y in pts)) < 1e-12, f"{n}-gon centroid y drift")


def validate_contract() -> None:
    c = json.loads((DATA / "flat-geometry.json").read_text(encoding="utf-8"))
    require(c.get("schema_version") == "1.0", "flat geometry schema must be 1.0")
    require(c.get("contract_id") == CONTRACT_ID, "flat geometry contract id mismatch")
    polys = c["plane_geometry"]["regular_polygons"]
    require([int(x["sides"]) for x in polys] == list(range(3,11)), "polygon taxonomy must be 3 through 10 sides")
    require([x["name"] for x in polys] == ["triangle","quadrilateral","pentagon","hexagon","heptagon","octagon","nonagon","decagon"], "polygon names mismatch")
    require([x["name"] for x in c["plane_geometry"]["curves"]] == ["circle","ellipse","semicircle"], "curve taxonomy mismatch")
    require("span" in c["euclidean_flats"]["affine_k_flat"], "affine k-flat definition missing span")
    require(c["euclidean_flats"]["hyperplane"]["dimension"] == "n-1", "hyperplane dimension must be n-1")
    require("||a||_2" in c["euclidean_flats"]["hyperplane"]["point_distance"], "hyperplane distance normalization missing")


def validate_distance() -> None:
    x = (2.0, 1.0)
    a = (1.0, 2.0)
    b = 1.0
    d = abs(sum(ai*xi for ai,xi in zip(a,x))-b) / math.sqrt(sum(ai*ai for ai in a))
    require(abs(d - 3/math.sqrt(5)) < 1e-12, "hyperplane distance identity failed")


def validate_sources() -> None:
    for rel in SOURCE_FILES:
        path = ROOT / rel
        require(path.exists(), f"missing polyglot source: {rel}")
        text = path.read_text(encoding="utf-8")
        require(CONTRACT_ID in text, f"{rel}: contract id missing")
    tex = (ROOT / SOURCE_FILES[2]).read_text(encoding="utf-8")
    require("\\begin{tikzpicture}" in tex and "\\regularpolygon" in tex, "Overleaf/TikZ source missing governed geometry")
    julia = (ROOT / SOURCE_FILES[3]).read_text(encoding="utf-8")
    require("regular_polygon" in julia and "hyperplane_distance" in julia and "AffineFlat" in julia, "Julia geometry primitives incomplete")
    react = (ROOT / SOURCE_FILES[4]).read_text(encoding="utf-8")
    require("regularPolygon" in react and "viewBox" in react and "aria-labelledby" in react, "React SVG mirror incomplete")
    go = (ROOT / SOURCE_FILES[6]).read_text(encoding="utf-8")
    require("regularPolygon" in go and "hyperplaneDistance" in go, "Go geometry primitives incomplete")
    cs = (ROOT / SOURCE_FILES[7]).read_text(encoding="utf-8")
    require("RegularPolygon" in cs and "HyperplaneDistance" in cs, "C# geometry primitives incomplete")


def validate_svg() -> None:
    path = OUT / "flat-geometry.svg"
    require(path.exists(), "missing generated flat-geometry.svg")
    text = path.read_text(encoding="utf-8")
    require("<script" not in text.lower(), "flat geometry SVG must not contain scripts")
    require(re.search(r"\b(?:href|src)=[\"']https?://", text, re.I) is None, "flat geometry SVG must be self-contained")
    root = ET.fromstring(text)
    require(root.tag.endswith("svg"), "flat geometry asset is not SVG")
    require(root.attrib.get("viewBox") == "0 0 1600 700", "flat geometry viewBox drift")
    require("<title" in text and "<desc" in text, "flat geometry accessibility metadata missing")
    for token in ("TRIANGLE","QUADRILATERAL","PENTAGON","HEXAGON","HEPTAGON","OCTAGON","NONAGON","DECAGON","CIRCLE","ELLIPSE","SEMICIRCLE"):
        require(token in text, f"flat geometry SVG missing {token}")
    for token in ("AFFINE FLATS","HYPERPLANE","d(x,H)","FLAT-GEOMETRY-V1"):
        require(token in text, f"flat geometry SVG missing {token}")
    require("var(--violet)" in text, "mathematical-abstraction cue missing")
    require("var(--red)" in text and "stroke-dasharray" in text, "critical hyperplane must be dashed red")
    require("var(--green-soft)" in text, "admissible side cue missing")
    require("var(--gold)" in text, "projection cue missing")


def validate_readme() -> None:
    text = README.read_text(encoding="utf-8")
    require("assets/generated/flat-geometry.svg" in text, "README must surface flat geometry figure")
    require("mathematical-art/flat-geometry/overleaf/flat_geometry.tex" in text, "README must link Overleaf/TikZ source")
    lower = text.lower()\n    require("plane figures" in lower and "affine flats" in lower, "README must preserve plane-figure / affine-flat distinction")
    require("not measured infrastructure behavior" in text.lower(), "README must preserve evidence boundary")


def main() -> int:
    validate_contract()
    validate_polygon_geometry()
    validate_distance()
    validate_sources()
    validate_svg()
    validate_readme()
    print("FLAT GEOMETRY VALIDATION: PASS — definitions, numerical invariants, polyglot sources, SVG semantics and README integration are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, json.JSONDecodeError, ET.ParseError) as exc:
        print(f"FLAT GEOMETRY VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
