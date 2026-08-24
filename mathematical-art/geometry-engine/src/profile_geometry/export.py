"""Renderer-neutral verified geometry exchange."""

from __future__ import annotations
import json
from pathlib import Path
from typing import Any
import numpy as np
from .surfaces import sample_torus
from .verification import verify_torus_geometry

SCHEMA_ID = "Dossiya-SE/verified-geometry-exchange/v1"


def torus_exchange(nu: int = 96, nv: int = 64, major_radius: float = 2.0, minor_radius: float = 0.75) -> dict[str, Any]:
    verification = verify_torus_geometry(major_radius, minor_radius)
    if not verification["passed"]:
        raise RuntimeError(f"geometry verification failed: {verification}")
    sampled = sample_torus(nu, nv, major_radius, minor_radius)
    return {
        "schema": SCHEMA_ID,
        "object_id": "DG-TORUS-001",
        "evidence_state": "[C/V]",
        "geometry_type": "parametric_surface",
        "parameter_domain": {"u": [0.0, float(2.0*np.pi)], "v": [0.0, float(2.0*np.pi)], "periodic": {"u": True, "v": True}},
        "parameters": {"major_radius": float(major_radius), "minor_radius": float(minor_radius)},
        "shape": {"nu": int(nu), "nv": int(nv)},
        "fields": {"vertices": sampled["vertices"].tolist(), "normals": sampled["normals"].tolist(), "gaussian_curvature": sampled["gaussian_curvature"].tolist()},
        "verification": verification,
        "renderer_contract": {"mathematics_source": "profile_geometry", "renderers_may_transform_values": False, "renderers_may_change_presentation_only": True},
    }


def write_torus_exchange(path: str | Path, **kwargs: Any) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(torus_exchange(**kwargs), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target
