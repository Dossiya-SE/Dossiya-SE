#!/usr/bin/env python3
"""G5 quantitative visual-quality validation for SCIENTIFIC-GEOMETRY-V3."""

from __future__ import annotations
import json,sys
from pathlib import Path
from shapely.geometry import box

ROOT=Path(__file__).resolve().parents[1]
LAYOUT=ROOT/"artifacts"/"visual-layout-v3.json"

def require(ok,msg):
    if not ok: raise ValueError(msg)

def min_distance(rects):
    shapes=[box(*r) for r in rects]
    d=float("inf")
    for i,a in enumerate(shapes):
        for b in shapes[i+1:]:
            d=min(d,a.distance(b))
    return d

def inside(rect,container,margin=0.0):
    x0,y0,x1,y1=rect
    a0,b0,a1,b1=container
    return x0>=a0+margin and y0>=b0+margin and x1<=a1-margin and y1<=b1-margin

def inside_viewbox(rect,vb,margin=0.0):
    _,_,w,h=vb
    return inside(rect,[0,0,w,h],margin)

def rect_size(r):
    return (float(r[2]-r[0]),float(r[3]-r[1]))

def main():
    d=json.loads(LAYOUT.read_text(encoding="utf-8"))
    require(d.get("contract_id")=="SCIENTIFIC-GEOMETRY-V3","layout contract mismatch")
    figs=d["figures"]
    typography=d["typography"]

    # Mobile-width typography gate. Effective sizes are SVG user-unit sizes
    # multiplied by the 640 px / viewBox-width scale.
    for name,fig in figs.items():
        width=float(fig["viewbox"][2])
        scale=640.0/width
        require(float(typography["title"])*scale>=13.0,f"{name}: title typography too small at 640px")
        require(float(typography["label"])*scale>=7.0,f"{name}: essential label typography too small at 640px")
        require(float(typography["small"])*scale>=6.0,f"{name}: secondary typography too small at 640px")
        require(float(typography["micro"])*scale>=5.5,f"{name}: micro typography too small at 640px")
        require(float(typography["project_name"])*scale>=6.4,f"{name}: project-name typography too small at 640px")

    thresholds={
      "research-question.svg":70.0,
      "project-system.svg":120.0,
      "research-pipeline.svg":45.0,
      "research-state-light.svg":25.0,
      "research-state-dark.svg":25.0,
    }
    for name,dist in thresholds.items():
        rects=figs[name]["major"]
        require(all(inside_viewbox(r,figs[name]["viewbox"],8) for r in rects),f"{name}: major geometry escapes viewBox")
        require(min_distance(rects)>=dist,f"{name}: minimum major-object spacing below {dist}px")

    q=figs["research-question.svg"]
    require(all(inside_viewbox(r,q["viewbox"],4) for r in q.get("labels",[])),
            "research-question.svg: label box escapes viewBox")

    # Project signatures: exact mathematical area is tested in G3. G5 tests
    # identical layout cells, containment and comparable optical footprint.
    proj=figs["project-system.svg"]
    cells=proj["cells"]; centers=proj["centers"]; shapes=proj["major"]
    require(len(cells)==len(shapes)==len(centers)==4,"project-system.svg: expected four cells/signatures")
    cell_sizes=[rect_size(r) for r in cells]
    require(max(abs(w-cell_sizes[0][0])+abs(h-cell_sizes[0][1]) for w,h in cell_sizes)<1e-9,
            "project-system.svg: project layout cells must be identical")
    for cell,shape,center in zip(cells,shapes,centers):
        require(inside(shape,cell,8),"project-system.svg: signature escapes its equal layout cell")
        cx=(cell[0]+cell[2])/2; cy=(cell[1]+cell[3])/2
        require(abs(cx-center[0])<1e-9 and abs(cy-center[1])<1e-9,
                "project-system.svg: governed centroid not aligned to cell center")
    footprints=[max(*rect_size(r)) for r in shapes]
    require(max(footprints)/min(footprints)<=1.30,
            "project-system.svg: equal-area signatures exceed optical-footprint ratio 1.30")
    project_labels=proj.get("labels",[])
    require(len(project_labels)==8,"project-system.svg: expected name + signature label for each project")
    require(all(inside_viewbox(r,proj["viewbox"],8) for r in project_labels),
            "project-system.svg: project label escapes viewBox")
    require(min_distance(project_labels)>=3.0,
            "project-system.svg: project labels overlap or are too tightly packed")

    for name in ("research-hero-light.svg","research-hero-dark.svg",
                 "coupled-network-3d-light.svg","coupled-network-3d-dark.svg",
                 "graph-to-viability.svg"):
        require(all(inside_viewbox(r,figs[name]["viewbox"],4) for r in figs[name]["major"]),
                f"{name}: computed panel geometry escapes canvas")

    print("VISUAL GEOMETRY QUALITY: PASS — spacing, containment, equal cells, optical footprint and 640px typography satisfy V3 thresholds.")

if __name__=="__main__":
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:
        print(f"VISUAL GEOMETRY QUALITY: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
