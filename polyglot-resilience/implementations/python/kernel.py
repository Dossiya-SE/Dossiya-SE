"""Reference implementation of the Polyglot Resilience Kernel PRK-1.0.

This module intentionally uses only the Python standard library so that the
reference semantics remain easy to inspect and reproduce.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


def _all_finite(values: list[float]) -> bool:
    return all(math.isfinite(float(value)) for value in values)


def validate_payload(payload: dict[str, Any]) -> None:
    """Validate cross-field PRK-1.0 semantic invariants."""
    if payload.get("kernel_version") != "PRK-1.0":
        raise ValueError("kernel_version must equal PRK-1.0")

    x = payload["x"]
    d_matrix = payload["D"]
    a_matrix = payload["A"]
    recovery = payload["r"]
    hazard = payload["h"]
    b_matrix = payload["B"]
    control = payload["u"]
    weights = payload["weights"]
    dt = float(payload["dt"])

    n = len(x)
    m = len(control)

    if n == 0 or m == 0:
        raise ValueError("non-empty state and control vectors are required")
    if not math.isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and strictly positive")

    if any(len(vector) != n for vector in (recovery, hazard, weights)):
        raise ValueError("x, r, h and weights must have the same length n")
    if len(d_matrix) != n or any(len(row) != n for row in d_matrix):
        raise ValueError("D must have shape n x n")
    if len(a_matrix) != n or any(len(row) != n for row in a_matrix):
        raise ValueError("A must have shape n x n")
    if len(b_matrix) != n or any(len(row) != m for row in b_matrix):
        raise ValueError("B must have shape n x m")

    flattened = (
        list(x)
        + list(recovery)
        + list(hazard)
        + list(weights)
        + list(control)
        + [value for row in d_matrix for value in row]
        + [value for row in a_matrix for value in row]
        + [value for row in b_matrix for value in row]
    )
    if not _all_finite(flattened):
        raise ValueError("all numerical inputs must be finite")

    if any(value < 0.0 or value > 1.0 for value in x):
        raise ValueError("input state x must lie in [0,1]^n")
    if any(value < 0.0 for value in recovery):
        raise ValueError("recovery vector r must be componentwise non-negative")
    if any(value < 0.0 for value in weights):
        raise ValueError("weights must be componentwise non-negative")
    if abs(sum(weights) - 1.0) > 1e-12:
        raise ValueError("weights must sum to one within 1e-12")


def step(payload: dict[str, Any]) -> dict[str, Any]:
    """Evaluate one deterministic PRK-1.0 explicit-Euler step."""
    validate_payload(payload)

    x = payload["x"]
    d_matrix = payload["D"]
    a_matrix = payload["A"]
    recovery = payload["r"]
    hazard = payload["h"]
    b_matrix = payload["B"]
    control = payload["u"]
    weights = payload["weights"]
    dt = float(payload["dt"])
    n = len(x)

    phi = [math.tanh(value) for value in x]
    dx: list[float] = []

    for i in range(n):
        degradation = sum(d_matrix[i][j] * x[j] for j in range(n))
        coupling = sum(a_matrix[i][j] * phi[j] for j in range(n))
        control_effect = sum(
            b_matrix[i][q] * control[q] for q in range(len(control))
        )
        derivative = (
            -degradation
            + coupling
            + recovery[i] * (1.0 - x[i])
            - hazard[i]
            + control_effect
        )
        dx.append(derivative)

    x_next = [
        min(1.0, max(0.0, x[i] + dt * dx[i]))
        for i in range(n)
    ]
    weighted_service_next = sum(
        weights[i] * x_next[i] for i in range(n)
    )

    return {
        "kernel_version": payload["kernel_version"],
        "fixture_id": payload["fixture_id"],
        "dx": dx,
        "x_next": x_next,
        "weighted_service_next": weighted_service_next,
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: python kernel.py <fixture.json>")

    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    result = step(payload)
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
