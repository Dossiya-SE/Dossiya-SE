#!/usr/bin/env python3
"""Compute mathematically governed geometry for every README visual.

SCIENTIFIC-GEOMETRY-V3
Source: data/scientific-geometry-v3.toml
Authorities: SymPy, NumPy/SciPy, Shapely.
The output is machine-readable geometry consumed by the SVG and TikZ renderers.
"""

from __future__ import annotations

import json
import math
import tomllib
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.interpolate import CubicSpline
from scipy.linalg import qr, svd
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import nearest_points

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "scientific-geometry-v3.toml"
OUT = ROOT / "data" / "computed-geometry-v3.json"


def arr(x):
    return np.asarray(x, dtype=float)


def clean(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    return value


def regular_polygon(n: int, radius: float, phase: float = -math.pi / 2) -> list[list[float]]:
    return [
        [radius * math.cos(phase + 2 * math.pi * j / n),
         radius * math.sin(phase + 2 * math.pi * j / n)]
        for j in range(n)
    ]


def equal_area_radius(n: int, area: float) -> float:
    return math.sqrt(2.0 * area / (n * math.sin(2.0 * math.pi / n)))


def rotation_matrix(yaw_deg: float, pitch_deg: float) -> np.ndarray:
    yaw = math.radians(yaw_deg)
    pitch = math.radians(pitch_deg)
    rz = np.array([
        [math.cos(yaw), -math.sin(yaw), 0.0],
        [math.sin(yaw),  math.cos(yaw), 0.0],
        [0.0, 0.0, 1.0],
    ])
    rx = np.array([
        [1.0, 0.0, 0.0],
        [0.0, math.cos(pitch), -math.sin(pitch)],
        [0.0, math.sin(pitch),  math.cos(pitch)],
    ])
    return rx @ rz


def orthonormal_plane(origin, b1, b2):
    B = np.column_stack([arr(b1), arr(b2)])
    rank = int(np.linalg.matrix_rank(B))
    if rank != 2:
        raise ValueError("affine plane basis must have rank 2")
    Q, _ = qr(B, mode="economic")
    return {
        "origin": arr(origin),
        "basis": B,
        "Q": Q,
        "rank": rank,
        "condition_number": float(np.linalg.cond(B)),
    }


def plane_point(plane, uv):
    return plane["origin"] + plane["basis"] @ arr(uv)


def plane_corners(plane):
    uv = [(-1.65, -0.62), (1.65, -0.62), (1.65, 0.62), (-1.65, 0.62)]
    return np.vstack([plane_point(plane, p) for p in uv])


def project_3d(points, R):
    pts = np.asarray(points, dtype=float)
    return (pts @ R.T)[:, :2]


def hyperplane_projection(state, normal, b):
    x = arr(state)
    a = arr(normal)
    denom = float(a @ a)
    if denom <= 0:
        raise ValueError("hyperplane normal must be nonzero")
    q = x - ((float(a @ x) - float(b)) / denom) * a

    # Independent symbolic construction from the same source values.
    ax, ay = map(sp.nsimplify, a.tolist())
    sx, sy = map(sp.nsimplify, x.tolist())
    bb = sp.nsimplify(b)
    den = sp.simplify(ax**2 + ay**2)
    lam = sp.simplify((ax*sx + ay*sy - bb) / den)
    qx = sp.simplify(sx - lam*ax)
    qy = sp.simplify(sy - lam*ay)

    return {
        "state": x,
        "normal": a,
        "b": float(b),
        "projection": q,
        "distance": abs(float(a @ x) - float(b)) / math.sqrt(denom),
        "symbolic_projection": [str(qx), str(qy)],
        "orthogonality_residual": abs(float((q - x) @ np.array([-a[1], a[0]]))),
        "boundary_residual": abs(float(a @ q) - float(b)),
    }


def halfplane_polygon(a: float, b: float, c: float, L: float) -> Polygon:
    n = np.array([a, b], dtype=float)
    nn = float(n @ n)
    if nn <= 0:
        raise ValueError("half-plane normal must be nonzero")
    unit_n = n / math.sqrt(nn)
    t = np.array([-unit_n[1], unit_n[0]])
    p0 = (c / nn) * n
    # a*x+b*y <= c is the negative-normal side.
    pts = [
        p0 + L*t,
        p0 - L*t,
        p0 - L*t - 2*L*unit_n,
        p0 + L*t - 2*L*unit_n,
    ]
    return Polygon(pts)


def line_segment_for_constraint(a: float, b: float, c: float, region: Polygon, L: float = 100.0):
    """Return the portion of an active constraint carried by the feasible polygon.

    Prefer vertices lying on the active line; this is numerically more robust than
    intersecting a floating-point polygon with the exact supporting line.
    """
    coords=np.asarray(region.exterior.coords[:-1],dtype=float)
    residual=np.abs(a*coords[:,0]+b*coords[:,1]-c)
    tol=max(1e-9,1e-8*max(1.0,abs(c)))
    on=coords[residual<=tol]
    if len(on)>=2:
        # Choose the farthest pair so the full active edge is represented.
        best=None; best_d=-1.0
        for i in range(len(on)):
            for j in range(i+1,len(on)):
                d=float(np.linalg.norm(on[i]-on[j]))
                if d>best_d:
                    best_d=d; best=(on[i],on[j])
        return np.vstack(best)

    # Fallback: intersect a tiny strip around the supporting line with the region,
    # then use the two most separated points from that contact geometry.
    n=np.array([a,b],dtype=float)
    nn=float(n@n)
    if nn<=0:
        raise ValueError("line normal must be nonzero")
    p0=(c/nn)*n
    t=np.array([-n[1],n[0]],dtype=float); t=t/np.linalg.norm(t)
    line=LineString([p0-L*t,p0+L*t])
    contact=region.boundary.intersection(line.buffer(tol,cap_style=2))
    pts=[]
    if contact.geom_type=="LineString":
        pts.extend(list(contact.coords))
    else:
        for geom in getattr(contact,"geoms",[]):
            if geom.geom_type=="LineString":
                pts.extend(list(geom.coords))
            elif geom.geom_type=="Point":
                pts.append(geom.coords[0])
    if len(pts)<2:
        raise ValueError("active constraint cannot be resolved on feasible boundary")
    arrp=np.asarray(pts,dtype=float)
    best=None; best_d=-1.0
    for i in range(len(arrp)):
        for j in range(i+1,len(arrp)):
            d=float(np.linalg.norm(arrp[i]-arrp[j]))
            if d>best_d:
                best_d=d; best=(arrp[i],arrp[j])
    return np.vstack(best)


def viability_region(cfg):
    xmin, xmax, ymin, ymax = map(float, cfg["bounds"])
    region = box(xmin, ymin, xmax, ymax)
    L = 20.0 * max(xmax - xmin, ymax - ymin)
    constraints = []
    for name, a, b, c in cfg["constraints"]:
        a, b, c = float(a), float(b), float(c)
        region = region.intersection(halfplane_polygon(a, b, c, L))
        constraints.append({"name": name, "a": a, "b": b, "c": c})
    if region.is_empty or region.geom_type != "Polygon":
        raise ValueError("viability constraints must produce one non-empty polygon")

    state = Point(tuple(map(float, cfg["state"])))
    if not region.covers(state):
        raise ValueError("configured viability state must lie inside feasible region")
    q = nearest_points(state, region.boundary)[1]
    qv = np.array([q.x, q.y], dtype=float)
    xv = np.array([state.x, state.y], dtype=float)

    names=[g["name"] for g in constraints]
    if len(names) != len(set(names)):
        raise ValueError("viability constraint names must be unique")
    active = min(
        constraints,
        key=lambda g: abs(g["a"]*q.x + g["b"]*q.y - g["c"]),
    )
    active_index = next(i for i,g in enumerate(constraints,1) if g["name"] == active["name"])
    av = np.array([active["a"], active["b"]], dtype=float)
    tangent = np.array([-av[1], av[0]], dtype=float)
    displacement = qv - xv
    active_segment = line_segment_for_constraint(active["a"],active["b"],active["c"],region)

    return {
        "state": xv,
        "boundary_point": qv,
        "rho": float(state.distance(region.boundary)),
        "area": float(region.area),
        "perimeter": float(region.length),
        "vertices": np.asarray(region.exterior.coords[:-1], dtype=float),
        "constraints": constraints,
        "active_constraint": active["name"],
        "active_constraint_index": active_index,
        "active_segment": active_segment,
        "boundary_residual": abs(active["a"]*q.x + active["b"]*q.y - active["c"]),
        "orthogonality_residual": abs(float(displacement @ tangent)),
    }


def compute():
    with SOURCE.open("rb") as f:
        cfg = tomllib.load(f)

    R = rotation_matrix(cfg["projection"]["yaw_deg"], cfg["projection"]["pitch_deg"])

    power = orthonormal_plane(**{
        "origin": cfg["hero"]["power_plane"]["origin"],
        "b1": cfg["hero"]["power_plane"]["basis1"],
        "b2": cfg["hero"]["power_plane"]["basis2"],
    })
    transport = orthonormal_plane(**{
        "origin": cfg["hero"]["transport_plane"]["origin"],
        "b1": cfg["hero"]["transport_plane"]["basis1"],
        "b2": cfg["hero"]["transport_plane"]["basis2"],
    })

    hero_proj = hyperplane_projection(
        cfg["hero"]["state_geometry"]["state"],
        cfg["hero"]["state_geometry"]["normal"],
        cfg["hero"]["state_geometry"]["b"],
    )

    # Multilayer 3D coordinates: same 2D intrinsic coordinates, separate affine layers.
    p_nodes_3d = np.vstack([plane_point(power, uv) for uv in cfg["coupled"]["power_nodes"]])
    t_nodes_3d = np.vstack([plane_point(transport, uv) for uv in cfg["coupled"]["transport_nodes"]])
    p_nodes_2d = project_3d(p_nodes_3d, R)
    t_nodes_2d = project_3d(t_nodes_3d, R)
    p_plane_2d = project_3d(plane_corners(power), R)
    t_plane_2d = project_3d(plane_corners(transport), R)

    ip = int(cfg["coupled"]["interface_power_node"])
    it = int(cfg["coupled"]["interface_transport_node"])
    interface_segment_3d = np.vstack([p_nodes_3d[ip], t_nodes_3d[it]])
    interface_segment_2d = project_3d(interface_segment_3d, R)

    viable = viability_region(cfg["viability"])

    # Research-state space: SVD/PCA projection of explicitly conceptual 4D vectors.
    X = np.asarray(cfg["research_state"]["vectors"], dtype=float)
    centered = X - X.mean(axis=0)
    _, svals, vt = svd(centered, full_matrices=False)
    basis2 = vt[:2].T
    state2 = centered @ basis2

    # SVD vector signs are mathematically arbitrary. Canonicalize orientation so
    # component 1 increases with the governed stage order, then canonicalize
    # component 2 by the sign of its largest-magnitude loading.
    order = np.arange(len(X), dtype=float)
    if float(np.dot(state2[:, 0] - state2[:, 0].mean(), order - order.mean())) < 0:
        basis2[:, 0] *= -1.0
        state2[:, 0] *= -1.0
    pivot = int(np.argmax(np.abs(basis2[:, 1])))
    if basis2[pivot, 1] < 0:
        basis2[:, 1] *= -1.0
        state2[:, 1] *= -1.0

    explained = (svals**2) / np.sum(svals**2)

    # Equal-area project signatures, independently checked by Shapely.
    target_area = float(cfg["projects"]["target_area"])
    projects = []
    for name, n in zip(cfg["projects"]["names"], cfg["projects"]["sides"]):
        n = int(n)
        r = equal_area_radius(n, target_area)
        pts = regular_polygon(n, r)
        poly = Polygon(pts)
        projects.append({
            "name": name,
            "sides": n,
            "radius": r,
            "vertices": pts,
            "area": float(poly.area),
            "bounds": list(poly.bounds),
            "centroid": [poly.centroid.x, poly.centroid.y],
        })

    # Continuous seven-stage trajectory gamma(t) through all stage anchors.
    labels = cfg["pipeline"]["labels"]
    ys = np.asarray(cfg["pipeline"]["y"], dtype=float)
    ts = np.linspace(0.0, 1.0, len(labels))
    spline = CubicSpline(ts, ys, bc_type="natural")
    sample_t = np.linspace(0.0, 1.0, 241)
    gamma = np.column_stack([sample_t, spline(sample_t)])
    anchors = np.column_stack([ts, ys])

    result = {
        "schema_version": "3.0",
        "contract_id": "SCIENTIFIC-GEOMETRY-V3",
        "source": str(SOURCE.relative_to(ROOT)),
        "projection_matrix": R,
        "hero": {
            "power_plane": {
                "origin": power["origin"],
                "basis": power["basis"],
                "Q": power["Q"],
                "rank": power["rank"],
                "condition_number": power["condition_number"],
                "corners_3d": plane_corners(power),
                "corners_2d": p_plane_2d,
            },
            "transport_plane": {
                "origin": transport["origin"],
                "basis": transport["basis"],
                "Q": transport["Q"],
                "rank": transport["rank"],
                "condition_number": transport["condition_number"],
                "corners_3d": plane_corners(transport),
                "corners_2d": t_plane_2d,
            },
            "state_geometry": hero_proj,
        },
        "coupled": {
            "power_nodes_3d": p_nodes_3d,
            "transport_nodes_3d": t_nodes_3d,
            "power_nodes_2d": p_nodes_2d,
            "transport_nodes_2d": t_nodes_2d,
            "power_plane_2d": p_plane_2d,
            "transport_plane_2d": t_plane_2d,
            "power_edges": cfg["coupled"]["power_edges"],
            "transport_edges": cfg["coupled"]["transport_edges"],
            "interface_segment_3d": interface_segment_3d,
            "interface_segment_2d": interface_segment_2d,
            "layer_separation": float(cfg["coupled"]["layer_separation"]),
        },
        "viability": viable,
        "research_state": {
            "labels": cfg["research_state"]["labels"],
            "vectors_4d": X,
            "center": X.mean(axis=0),
            "basis_2d": basis2,
            "projected_2d": state2,
            "singular_values": svals,
            "explained_variance_ratio": explained,
            "current_index": int(cfg["research_state"]["current_index"]),
            "target_index": int(cfg["research_state"]["target_index"]),
        },
        "projects": {
            "target_area": target_area,
            "items": projects,
        },
        "pipeline": {
            "labels": labels,
            "sides": cfg["pipeline"]["sides"],
            "anchors": anchors,
            "sample_t": sample_t,
            "gamma": gamma,
            "max_anchor_residual": float(np.max(np.abs(spline(ts) - ys))),
        },
    }

    def default(o):
        c = clean(o)
        if c is not o:
            return c
        raise TypeError(type(o).__name__)

    OUT.write_text(json.dumps(result, indent=2, default=default) + "\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")
    print(f"hero projection residuals: boundary={hero_proj['boundary_residual']:.3e}, orthogonality={hero_proj['orthogonality_residual']:.3e}")
    print(f"viability: vertices={len(viable['vertices'])}, rho={viable['rho']:.6f}, active={viable['active_constraint']}")
    print(f"pipeline anchor residual={result['pipeline']['max_anchor_residual']:.3e}")


if __name__ == "__main__":
    compute()
