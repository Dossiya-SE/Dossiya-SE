"""Verified geometry primitives for the Dossiya-SE profile visual system."""
from .surfaces import torus_point, torus_partials, torus_unit_normal, torus_metric, torus_gaussian_curvature, sample_torus
from .verification import verify_torus_geometry
from .export import torus_exchange, write_torus_exchange

__all__ = ["torus_point", "torus_partials", "torus_unit_normal", "torus_metric",
           "torus_gaussian_curvature", "sample_torus", "verify_torus_geometry",
           "torus_exchange", "write_torus_exchange"]
