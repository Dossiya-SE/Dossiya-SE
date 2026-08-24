from __future__ import annotations

import numpy as np

from decision_math import (
    equality_qp_certificate,
    expected_improvement,
    lp_primal_dual_certificate,
    min_cost_flow_certificate,
    upper_confidence_bound,
)


def test_lp_primal_dual_certificate() -> None:
    cert = lp_primal_dual_certificate()
    assert cert.passed, cert.residuals


def test_min_cost_flow_certificate() -> None:
    cert = min_cost_flow_certificate()
    assert cert.passed, cert.residuals


def test_equality_qp_certificate() -> None:
    cert = equality_qp_certificate()
    assert cert.passed, cert.residuals


def test_ei_increases_with_predictive_uncertainty_at_incumbent() -> None:
    low = expected_improvement(mu=1.0, sigma=0.1, incumbent=1.0)
    high = expected_improvement(mu=1.0, sigma=1.0, incumbent=1.0)
    assert high > low > 0.0


def test_ei_zero_variance_reduces_to_positive_improvement() -> None:
    assert expected_improvement(2.0, 0.0, 1.5) == 0.5
    assert expected_improvement(1.0, 0.0, 1.5) == 0.0


def test_ucb_exploration_parameter_changes_uncertainty_weight() -> None:
    assert np.isclose(upper_confidence_bound(2.0, 3.0, 0.0), 2.0)
    assert upper_confidence_bound(2.0, 3.0, 2.0) > upper_confidence_bound(2.0, 3.0, 1.0)
