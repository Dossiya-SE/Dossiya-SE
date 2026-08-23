"""Scientific invariant checks for the PRK-1.0 Python reference kernel.

Run directly with Python; no third-party test framework is required.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
KERNEL_PATH = ROOT / "implementations/python/kernel.py"

spec = importlib.util.spec_from_file_location("prk_reference", KERNEL_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("could not load reference kernel")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def load_fixture(name: str) -> dict:
    return json.loads((ROOT / "fixtures" / f"{name}.json").read_text(encoding="utf-8"))


def assert_close(a: float, b: float, tol: float = 1e-12) -> None:
    if not math.isclose(a, b, rel_tol=0.0, abs_tol=tol):
        raise AssertionError(f"{a} != {b} within {tol}")


def assert_raises(payload: dict, expected_fragment: str) -> None:
    try:
        module.step(payload)
    except ValueError as exc:
        if expected_fragment.lower() not in str(exc).lower():
            raise AssertionError(f"unexpected error: {exc}") from exc
    else:
        raise AssertionError(f"expected ValueError containing {expected_fragment!r}")


def test_frozen_expected_results() -> None:
    expected = json.loads((ROOT / "fixtures/expected-results.json").read_text(encoding="utf-8"))
    tol = float(expected["max_abs_tolerance"])

    for name, target in expected["results"].items():
        result = module.step(load_fixture(name))
        for observed, wanted in zip(result["dx"], target["dx"]):
            assert_close(observed, wanted, tol)
        for observed, wanted in zip(result["x_next"], target["x_next"]):
            assert_close(observed, wanted, tol)
        assert_close(result["weighted_service_next"], target["weighted_service_next"], tol)


def test_projection_bounds() -> None:
    payload = load_fixture("baseline")
    extreme = copy.deepcopy(payload)
    extreme["h"] = [100.0, 100.0, 100.0]
    result = module.step(extreme)
    if not all(0.0 <= value <= 1.0 for value in result["x_next"]):
        raise AssertionError("projected next state escaped [0,1]^n")


def test_determinism() -> None:
    payload = load_fixture("baseline")
    if module.step(payload) != module.step(payload):
        raise AssertionError("deterministic reference kernel returned different repeated outputs")


def test_control_term_is_active() -> None:
    payload = load_fixture("baseline")
    with_control = module.step(payload)
    without_control_payload = copy.deepcopy(payload)
    without_control_payload["u"] = [0.0 for _ in payload["u"]]
    without_control = module.step(without_control_payload)

    if max(
        abs(a - b)
        for a, b in zip(with_control["dx"], without_control["dx"])
    ) <= 0.0:
        raise AssertionError("control term Bu has no observable effect in baseline fixture")


def test_non_diagonal_d_is_active() -> None:
    payload = load_fixture("baseline")
    full_d = module.step(payload)
    diagonal_payload = copy.deepcopy(payload)
    diagonal_payload["D"] = [
        [payload["D"][i][j] if i == j else 0.0 for j in range(len(payload["D"]))]
        for i in range(len(payload["D"]))
    ]
    diagonal_d = module.step(diagonal_payload)

    if max(abs(a - b) for a, b in zip(full_d["dx"], diagonal_d["dx"])) <= 0.0:
        raise AssertionError("off-diagonal D entries have no observable effect")


def test_controlled_fixture_ordering() -> None:
    baseline = module.step(load_fixture("baseline"))
    recovery = module.step(load_fixture("controlled-recovery"))
    severe = module.step(load_fixture("severe-hazard"))

    if recovery["weighted_service_next"] <= baseline["weighted_service_next"]:
        raise AssertionError("controlled-recovery fixture did not increase next-step weighted service")
    if severe["weighted_service_next"] >= baseline["weighted_service_next"]:
        raise AssertionError("severe-hazard fixture did not reduce next-step weighted service")


def test_invalid_inputs_fail_explicitly() -> None:
    baseline = load_fixture("baseline")

    bad_dt = copy.deepcopy(baseline)
    bad_dt["dt"] = 0.0
    assert_raises(bad_dt, "dt")

    bad_state = copy.deepcopy(baseline)
    bad_state["x"][0] = 1.1
    assert_raises(bad_state, "state")

    bad_recovery = copy.deepcopy(baseline)
    bad_recovery["r"][0] = -0.1
    assert_raises(bad_recovery, "recovery")

    bad_weights = copy.deepcopy(baseline)
    bad_weights["weights"] = [0.5, 0.5, 0.5]
    assert_raises(bad_weights, "sum to one")

    bad_d = copy.deepcopy(baseline)
    bad_d["D"][0] = [0.1]
    assert_raises(bad_d, "D must")


def main() -> None:
    tests = [
        test_frozen_expected_results,
        test_projection_bounds,
        test_determinism,
        test_control_term_is_active,
        test_non_diagonal_d_is_active,
        test_controlled_fixture_ordering,
        test_invalid_inputs_fail_explicitly,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"REFERENCE INVARIANT SUITE PASS ({len(tests)} tests)")


if __name__ == "__main__":
    main()
