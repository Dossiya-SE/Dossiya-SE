"""Analytic and sampled differential-geometry primitives."""

from __future__ import annotations
import numpy as np


def _validate_radii(major_radius: float, minor_radius: float) -> tuple[float, float]:
    R, r = float(major_radius), float(minor_radius)
    if not (R > r > 0.0):
        raise ValueError("require major_radius > minor_radius > 0")
    return R, r


def torus_point(u: float, v: float, major_radius: float = 2.0, minor_radius: float = 0.75) -> np.ndarray:
    R, r = _validate_radii(major_radius, minor_radius)
    cu, su, cv, sv = np.cos(u), np.sin(u), np.cos(v), np.sin(v)
    return np.array([(R + r * cv) * cu, (R + r * cv) * su, r * sv], dtype=float)


def torus_partials(u: float, v: float, major_radius: float = 2.0, minor_radius: float = 0.75) -> tuple[np.ndarray, np.ndarray]:
    R, r = _validate_radii(major_radius, minor_radius)
    cu, su, cv, sv = np.cos(u), np.sin(u), np.cos(v), np.sin(v)
    e_u = np.array([-(R + r * cv) * su, (R + r * cv) * cu, 0.0], dtype=float)
    e_v = np.array([-r * sv * cu, -r * sv * su, r * cv], dtype=float)
    return e_u, e_v


def torus_unit_normal(u: float, v: float, major_radius: float = 2.0, minor_radius: float = 0.75) -> np.ndarray:
    e_u, e_v = torus_partials(u, v, major_radius, minor_radius)
    cross = np.cross(e_u, e_v)
    norm = np.linalg.norm(cross)
    if norm == 0.0:
        raise ValueError("degenerate parameter point")
    return cross / norm


def torus_metric(u: float, v: float, major_radius: float = 2.0, minor_radius: float = 0.75) -> np.ndarray:
    e_u, e_v = torus_partials(u, v, major_radius, minor_radius)
    return np.array([[float(e_u @ e_u), float(e_u @ e_v)],
                     [float(e_v @ e_u), float(e_v @ e_v)]], dtype=float)


def torus_gaussian_curvature(v: float, major_radius: float = 2.0, minor_radius: float = 0.75) -> float:
    R, r = _validate_radii(major_radius, minor_radius)
    cv = float(np.cos(v))
    return cv / (r * (R + r * cv))


def sample_torus(nu: int = 96, nv: int = 64, major_radius: float = 2.0, minor_radius: float = 0.75) -> dict[str, np.ndarray]:
    if nu < 8 or nv < 8:
        raise ValueError("nu and nv must each be >= 8")
    R, r = _validate_radii(major_radius, minor_radius)
    us = np.linspace(0.0, 2.0 * np.pi, nu, endpoint=False)
    vs = np.linspace(0.0, 2.0 * np.pi, nv, endpoint=False)
    vertices = np.empty((nu, nv, 3), dtype=float)
    normals = np.empty_like(vertices)
    curvature = np.empty((nu, nv), dtype=float)
    for i, u in enumerate(us):
        for j, v in enumerate(vs):
            vertices[i, j] = torus_point(u, v, R, r)
            normals[i, j] = torus_unit_normal(u, v, R, r)
            curvature[i, j] = torus_gaussian_curvature(v, R, r)
    return {"u": us, "v": vs, "vertices": vertices, "normals": normals, "gaussian_curvature": curvature}
