#!/usr/bin/env python3
"""Validate the computed multilayer scene with PyVista and Trimesh."""

from __future__ import annotations
import json
import math
import sys
from pathlib import Path

import numpy as np
import pyvista as pv
import trimesh

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"computed-geometry-v3.json"

def require(ok,msg):
    if not ok:
        raise ValueError(msg)

def plane_mesh(corners):
    c=np.asarray(corners,dtype=float)
    faces=np.hstack([[4,0,1,2,3]])
    pvmesh=pv.PolyData(c,faces)
    trimesh_mesh=trimesh.Trimesh(vertices=c,faces=[[0,1,2],[0,2,3]],process=False)
    return pvmesh,trimesh_mesh

def main():
    g=json.loads(DATA.read_text(encoding="utf-8"))
    c=g["coupled"]
    P=np.asarray(c["power_nodes_3d"],dtype=float)
    T=np.asarray(c["transport_nodes_3d"],dtype=float)
    R=np.asarray(g["projection_matrix"],dtype=float)
    p2=np.asarray(c["power_nodes_2d"],dtype=float)
    t2=np.asarray(c["transport_nodes_2d"],dtype=float)

    require(P.shape[1]==3 and T.shape[1]==3,"3D nodes must be R^3")
    require(np.all(np.isfinite(P)) and np.all(np.isfinite(T)),"3D nodes must be finite")
    require(abs(np.linalg.det(R)-1.0)<1e-10,"projection rotation must be proper orthogonal rotation")
    require(np.linalg.norm(R.T@R-np.eye(3))<1e-10,"projection rotation must be orthonormal")
    require(np.max(np.abs((P@R.T)[:,:2]-p2))<1e-10,"power 3D→2D projection drift")
    require(np.max(np.abs((T@R.T)[:,:2]-t2))<1e-10,"transport 3D→2D projection drift")

    cloud=pv.PolyData(np.vstack([P,T]))
    require(cloud.n_points==len(P)+len(T),"PyVista point count mismatch")
    require(all(math.isfinite(v) for v in cloud.bounds),"PyVista scene bounds invalid")

    for key in ("power_plane","transport_plane"):
        corners=g["hero"][key]["corners_3d"]
        pvmesh,tm=plane_mesh(corners)
        require(pvmesh.n_cells==1 and pvmesh.area>0,"PyVista plane mesh degenerate")
        require(tm.area>0 and np.all(np.isfinite(tm.face_normals)),"Trimesh plane mesh degenerate")

    seg=np.asarray(c["interface_segment_3d"],dtype=float)
    require(np.linalg.norm(seg[1]-seg[0])>0,"shared interface segment must span the two layers")

    print("3D COMPUTATIONAL GEOMETRY VALIDATION: PASS — PyVista/Trimesh scene, planes, projection and interface are non-degenerate.")

if __name__=="__main__":
    try:
        raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:
        print(f"3D COMPUTATIONAL GEOMETRY VALIDATION: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
