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

def inside_viewbox(rect,vb,margin=0.0):
    x0,y0,x1,y1=rect
    _,_,w,h=vb
    return x0>=margin and y0>=margin and x1<=w-margin and y1<=h-margin

def main():
    d=json.loads(LAYOUT.read_text(encoding="utf-8"))
    require(d.get("contract_id")=="SCIENTIFIC-GEOMETRY-V3","layout contract mismatch")
    figs=d["figures"]

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

    # Label containment is explicitly checked on the small-width-sensitive research-question figure.
    q=figs["research-question.svg"]
    require(all(inside_viewbox(r,q["viewbox"],4) for r in q.get("labels",[])),"research-question.svg: label box escapes viewBox")

    # Major scientific panels must themselves remain contained.
    for name in ("research-hero-light.svg","research-hero-dark.svg","coupled-network-3d-light.svg","coupled-network-3d-dark.svg","graph-to-viability.svg"):
        require(all(inside_viewbox(r,figs[name]["viewbox"],4) for r in figs[name]["major"]),f"{name}: computed panel geometry escapes canvas")

    print("VISUAL GEOMETRY QUALITY: PASS — quantitative spacing, containment and major-layout bounds satisfy V3 thresholds.")

if __name__=="__main__":
    try: raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:
        print(f"VISUAL GEOMETRY QUALITY: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
