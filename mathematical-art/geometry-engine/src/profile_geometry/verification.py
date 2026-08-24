"""Fail-closed numerical verification for profile geometry."""

from __future__ import annotations
import numpy as np
from .surfaces import torus_metric, torus_partials, torus_point, torus_unit_normal


def _central_difference(u: float, v: float, axis: int, h: float, R: float, r: float) -> np.ndarray:
    if axis == 0:
        return (torus_point(u + h, v, R, r) - torus_point(u - h, v, R, r)) / (2.0 * h)
    if axis == 1:
        return (torus_point(u, v + h, R, r) - torus_point(u, v - h, R, r)) / (2.0 * h)
    raise ValueError("axis must be 0 or 1")


def verify_torus_geometry(major_radius: float = 2.0, minor_radius: float = 0.75,
                          grid: int = 11, tolerance: float = 2e-6,
                          finite_difference_step: float = 1e-6) -> dict[str, float | bool]:
    if grid < 5:
        raise ValueError("grid must be >= 5")
    if tolerance <= 0.0 or finite_difference_step <= 0.0:
        raise ValueError("tolerances must be positive")
    us = np.linspace(0.11, 2.0 * np.pi - 0.11, grid)
    vs = np.linspace(0.17, 2.0 * np.pi - 0.17, grid)
    max_normal_error = max_ortho = max_sym = max_deriv = 0.0
    min_det = float("inf")
    for u in us:
        for v in vs:
            e_u, e_v = torus_partials(u, v, major_radius, minor_radius)
            n = torus_unit_normal(u, v, major_radius, minor_radius)
            g = torus_metric(u, v, major_radius, minor_radius)
            max_normal_error = max(max_normal_error, abs(float(np.linalg.norm(n)) - 1.0))
            max_ortho = max(max_ortho, abs(float(n @ e_u)), abs(float(n @ e_v)))
            max_sym = max(max_sym, float(np.max(np.abs(g - g.T))))
            min_det = min(min_det, float(np.linalg.det(g)))
            fd_u = _central_difference(u, v, 0, finite_difference_step, major_radius, minor_radius)
            fd_v = _central_difference(u, v, 1, finite_difference_step, major_radius, minor_radius)
            max_deriv = max(max_deriv, float(np.linalg.norm(fd_u - e_u)), float(np.linalg.norm(fd_v - e_v)))
    passed = max_normal_error <= tolerance and max_ortho <= tolerance and max_sym <= tolerance and min_det > 0.0 and max_deriv <= tolerance
    return {"passed": passed, "max_normal_error": max_normal_error, "max_orthogonality_error": max_ortho,
            "max_metric_symmetry_error": max_sym, "min_metric_determinant": min_det,
            "max_derivative_residual": max_deriv, "tolerance": tolerance}
