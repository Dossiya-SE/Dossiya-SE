#!/usr/bin/env python3
"""Generate the publication TikZ representation from computed geometry V3."""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"computed-geometry-v3.json"
OUT=ROOT/"mathematical-art"/"profile-geometry"/"overleaf"/"profile_geometry_v3.tex"

def fmt_points(points,scale=1.0,ox=0.0,oy=0.0):
    return " -- ".join(f"({ox+scale*float(x):.5f},{oy+scale*float(y):.5f})" for x,y in points)

def main():
    g=json.loads(DATA.read_text(encoding="utf-8"))
    v=g["viability"]
    if v.get("distance_metric")!="euclidean_L2":
        raise ValueError("V3 TikZ renderer requires viability metric euclidean_L2")
    gamma=g["pipeline"]["gamma"]
    anchors=g["pipeline"]["anchors"]
    tex=r"""\documentclass[tikz,border=8pt]{standalone}
\usetikzlibrary{arrows.meta,calc}
% SCIENTIFIC-GEOMETRY-V3
% Generated from data/computed-geometry-v3.json; do not hand-edit geometry.
\definecolor{Power}{HTML}{C8102E}
\definecolor{Transport}{HTML}{16823A}
\definecolor{Info}{HTML}{1D4ED8}
\definecolor{Cyan}{HTML}{007A88}
\definecolor{Green}{HTML}{16823A}
\definecolor{Red}{HTML}{CF222E}
\definecolor{Violet}{HTML}{6D28D9}
\begin{document}
\begin{tikzpicture}[>=Latex,line cap=round,line join=round]
"""
    tex += "% Computed viability set and exact Euclidean nearest-boundary projection\n"
    tex += "\\begin{scope}[xshift=0cm,yshift=0cm,scale=1.6]\n"
    tex += "\\filldraw[fill=Green!8,draw=Green,thick] " + fmt_points(v["vertices"]) + " -- cycle;\n"
    s=v["state"]; q=v["boundary_point"]; seg=v["active_segment"]
    tex += f"\\draw[Red,thick,dashed] ({seg[0][0]:.5f},{seg[0][1]:.5f}) -- ({seg[1][0]:.5f},{seg[1][1]:.5f});\n"
    tex += f"\\fill[Info] ({s[0]:.5f},{s[1]:.5f}) circle (1.4pt) node[above right] {{$Y(t)$}};\n"
    tex += f"\\draw[Cyan,thick,->] ({s[0]:.5f},{s[1]:.5f}) -- ({q[0]:.5f},{q[1]:.5f}) node[midway,below] {{$\\rho_2$}};\n"
    tex += "\\end{scope}\n"

    tex += "% Continuous seven-stage trajectory gamma(t)\n"
    tex += "\\begin{scope}[xshift=8cm,yshift=0cm,xscale=7,yscale=5]\n"
    tex += "\\draw[Violet,thick] " + fmt_points(gamma) + ";\n"
    for i,(x,y) in enumerate(anchors,1):
        tex += f"\\filldraw[fill=white,draw=Violet] ({x:.5f},{y:.5f}) circle (1.6pt) node[above] {{{i}}};\n"
    tex += "\\end{scope}\n"
    tex += "\\end{tikzpicture}\n\\end{document}\n"
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(tex,encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} from computed geometry.")

if __name__=="__main__":
    main()
