import numpy as np
from profile_geometry import sample_torus, torus_gaussian_curvature, torus_metric, torus_point, verify_torus_geometry, torus_exchange


def test_torus_known_points():
    assert np.allclose(torus_point(0.0, 0.0), [2.75, 0.0, 0.0])
    assert np.allclose(torus_point(np.pi/2.0, 0.0), [0.0, 2.75, 0.0], atol=1e-12)


def test_metric_positive_definite():
    g = torus_metric(0.7, 1.1)
    assert np.allclose(g, g.T)
    assert np.all(np.linalg.eigvalsh(g) > 0.0)


def test_curvature_changes_sign():
    assert torus_gaussian_curvature(0.0) > 0.0
    assert torus_gaussian_curvature(np.pi) < 0.0


def test_sample_shapes_and_unit_normals():
    sampled = sample_torus(16, 12)
    assert sampled["vertices"].shape == (16, 12, 3)
    assert np.allclose(np.linalg.norm(sampled["normals"], axis=2), 1.0)


def test_fail_closed_verification():
    report = verify_torus_geometry()
    assert report["passed"], report


def test_renderer_exchange():
    payload = torus_exchange(12, 10)
    assert payload["schema"] == "Dossiya-SE/verified-geometry-exchange/v1"
    assert payload["verification"]["passed"] is True
    assert payload["renderer_contract"]["renderers_may_transform_values"] is False
