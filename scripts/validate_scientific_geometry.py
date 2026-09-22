#!/usr/bin/env python3
"""G1–G3 numerical and geometric validation for SCIENTIFIC-GEOMETRY-V3."""

from __future__ import annotations
import json
import math
import sys
import tomllib
from pathlib import Path

import numpy as np
from shapely.geometry import Point, Polygon

ROOT=Path(__file__).resolve().parents[1]
COMPUTED=ROOT/"data"/"computed-geometry-v3.json"
JULIA=ROOT/"artifacts"/"julia-geometry-check.toml"

def require(ok,msg):
    if not ok:
        raise ValueError(msg)

def main():
    g=json.loads(COMPUTED.read_text(encoding="utf-8"))
    require(g.get("contract_id")=="SCIENTIFIC-GEOMETRY-V3","computed contract id mismatch")

    # G1 — mathematical correctness.
    for name in ("power_plane","transport_plane"):
        p=g["hero"][name]
        B=np.asarray(p["basis"],dtype=float)
        Q=np.asarray(p["Q"],dtype=float)
        require(int(p["rank"])==2,f"{name}: rank must be 2")
        require(np.linalg.matrix_rank(B)==2,f"{name}: numerical rank drift")
        require(np.linalg.norm(Q.T@Q-np.eye(2))<1e-10,f"{name}: Q not orthonormal")
        require(float(p["condition_number"])<10.0,f"{name}: ill-conditioned basis")

    hp=g["hero"]["state_geometry"]
    require(float(hp["boundary_residual"])<1e-10,"hero projection not on critical hyperplane")
    require(float(hp["orthogonality_residual"])<1e-10,"hero projection is not orthogonal")

    v=g["viability"]
    require(float(v["boundary_residual"])<1e-8,"viability nearest point not on active boundary")
    require(float(v["orthogonality_residual"])<1e-8,"rho direction not normal to active boundary")\n    require(1 <= int(v["active_constraint_index"]) <= len(v["constraints"]),"active constraint index out of range")

    # G2 — numerical correctness and independent Julia cross-check.
    with JULIA.open("rb") as f:
        j=tomllib.load(f)
    require(j.get("contract_id")=="SCIENTIFIC-GEOMETRY-V3","Julia contract mismatch")
    pyq=np.asarray(hp["projection"],dtype=float)
    jq=np.asarray([j["projection_x"],j["projection_y"]],dtype=float)
    require(np.linalg.norm(pyq-jq)<1e-10,"Python/Julia hero projection disagreement")
    require(abs(float(hp["distance"])-float(j["distance"]))<1e-10,"Python/Julia distance disagreement")
    require(float(j["max_project_area_error"])<1e-8,"Julia equal-area verification failed")

    s=np.asarray(g["research_state"]["singular_values"],dtype=float)
    require(np.all(s[:-1]>=s[1:]-1e-12),"SVD singular values not ordered")
    require(s[1]>1e-8,"research-state projection needs at least rank 2")
    ev=np.asarray(g["research_state"]["explained_variance_ratio"],dtype=float)
    require(abs(float(ev.sum())-1.0)<1e-10,"explained variance ratio must sum to one")
    projected=np.asarray(g["research_state"]["projected_2d"],dtype=float)
    order=np.arange(len(projected),dtype=float)
    require(float(np.dot(projected[:,0]-projected[:,0].mean(),order-order.mean()))>=-1e-12,
            "research-state component 1 orientation must be canonicalized with stage order")

    # G3 — computational geometry correctness.
    poly=Polygon(v["vertices"])
    state=Point(v["state"])
    q=Point(v["boundary_point"])
    require(poly.is_valid and poly.area>0,"viability polygon invalid")
    require(poly.covers(state),"state must lie in viability region")
    require(poly.boundary.distance(q)<1e-8,"rho endpoint must lie on viability boundary")
    require(abs(state.distance(poly.boundary)-float(v["rho"]))<1e-8,"rho does not equal nearest-boundary distance")

    target=float(g["projects"]["target_area"])
    for item in g["projects"]["items"]:
        p=Polygon(item["vertices"])
        require(p.is_valid,"project signature polygon invalid")
        require(abs(p.area-target)/target<1e-10,"project signature area normalization failed")
        require(math.hypot(*item["centroid"])<1e-10,"project signature centroid drift")

    pipe=g["pipeline"]
    require(float(pipe["max_anchor_residual"])<1e-12,"continuous gamma(t) misses stage anchors")
    gamma=np.asarray(pipe["gamma"],dtype=float)
    jumps=np.linalg.norm(np.diff(gamma,axis=0),axis=1)
    require(float(jumps.max())<0.03,"gamma(t) sampling has discontinuity-like jump")

    print("SCIENTIFIC GEOMETRY VALIDATION: PASS — G1 mathematics, G2 numerical cross-verification and G3 computational geometry are consistent.")

if __name__=="__main__":
    try:
        raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:
        print(f"SCIENTIFIC GEOMETRY VALIDATION: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
