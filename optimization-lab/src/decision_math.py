"""Small verified OR/Bayesian benchmarks used by the public profile."""

from __future__ import annotations

from dataclasses import dataclass
import math

import numpy as np
from scipy.optimize import linprog
from scipy.stats import norm

TOL = 1e-9


@dataclass(frozen=True)
class Certificate:
    passed: bool
    residuals: dict[str, float]


def lp_primal_dual_certificate() -> Certificate:
    """IEE 574 duality example: max c^T x, Ax<=b, x>=0."""
    A = np.array([[3.0, 3.0], [2.0, 5.0], [6.0, 2.0]])
    b = np.array([36.0, 50.0, 60.0])
    c = np.array([30.0, 20.0])
    x = np.array([9.0, 3.0])
    w = np.array([5.0, 0.0, 2.5])

    primal_slack = b - A @ x
    dual_slack = A.T @ w - c
    gap = float(b @ w - c @ x)
    comp_primal = float(np.max(np.abs(w * primal_slack)))
    comp_dual = float(np.max(np.abs(x * dual_slack)))

    residuals = {
        "primal_violation": float(max(0.0, -primal_slack.min(), -x.min())),
        "dual_violation": float(max(0.0, -dual_slack.min(), -w.min())),
        "duality_gap": abs(gap),
        "complementary_slackness_primal": comp_primal,
        "complementary_slackness_dual": comp_dual,
    }
    return Certificate(max(residuals.values()) <= TOL, residuals)


def min_cost_flow_certificate() -> Certificate:
    """Solve and independently check a four-node min-cost flow benchmark."""
    # arcs: s->a, s->b, a->t, b->t, a->b
    costs = np.array([2.0, 4.0, 2.0, 1.0, 0.5])
    capacities = np.array([4.0, 4.0, 4.0, 4.0, 2.0])
    # incidence convention: outflow - inflow = supply b_i
    A = np.array([
        [1, 1, 0, 0, 0],
        [-1, 0, 1, 0, 1],
        [0, -1, 0, 1, -1],
        [0, 0, -1, -1, 0],
    ], dtype=float)
    supply = np.array([5.0, 0.0, 0.0, -5.0])

    result = linprog(
        costs,
        A_eq=A,
        b_eq=supply,
        bounds=[(0.0, u) for u in capacities],
        method="highs",
    )
    if not result.success:
        return Certificate(False, {"solver_failure": math.inf})

    x = result.x
    balance = A @ x - supply
    residuals = {
        "node_balance": float(np.max(np.abs(balance))),
        "lower_bound_violation": float(max(0.0, -x.min())),
        "upper_bound_violation": float(max(0.0, np.max(x - capacities))),
        "objective_recompute": abs(float(costs @ x) - float(result.fun)),
    }
    return Certificate(max(residuals.values()) <= TOL, residuals)


def equality_qp_certificate() -> Certificate:
    """Solve a positive-definite equality QP through its KKT system."""
    D = np.array([[4.0, 1.0], [1.0, 2.0]])
    c = np.array([-1.0, -1.0])
    A = np.array([[1.0, 1.0]])
    b = np.array([1.0])

    K = np.block([[D, A.T], [A, np.zeros((1, 1))]])
    rhs = np.concatenate([-c, b])
    sol = np.linalg.solve(K, rhs)
    x, w = sol[:2], sol[2:]

    stationarity = D @ x + c + A.T @ w
    feasibility = A @ x - b
    eig_min = float(np.linalg.eigvalsh(D).min())
    residuals = {
        "stationarity": float(np.max(np.abs(stationarity))),
        "equality_feasibility": float(np.max(np.abs(feasibility))),
        "positive_definiteness_margin": max(0.0, TOL - eig_min),
    }
    return Certificate(max(residuals.values()) <= TOL, residuals)


def expected_improvement(mu: float, sigma: float, incumbent: float) -> float:
    """EI for maximization under a Gaussian predictive distribution."""
    if sigma <= 0.0:
        return max(mu - incumbent, 0.0)
    z = (mu - incumbent) / sigma
    return float((mu - incumbent) * norm.cdf(z) + sigma * norm.pdf(z))


def upper_confidence_bound(mu: float, sigma: float, kappa: float) -> float:
    return float(mu + kappa * sigma)
