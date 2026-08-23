"""Run native PRK-1.0 implementations against frozen conformance fixtures."""

from __future__ import annotations

import json
import math
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ["baseline", "controlled-recovery", "severe-hazard"]

COMMANDS = {
    "python-reference-prk1": lambda fixture: [
        sys.executable,
        str(ROOT / "implementations/python/kernel.py"),
        str(fixture),
    ],
    "go-native-prk1": lambda fixture: [
        "go",
        "run",
        str(ROOT / "implementations/go/main.go"),
        str(fixture),
    ],
    "javascript-native-prk1": lambda fixture: [
        "node",
        str(ROOT / "implementations/javascript/kernel.mjs"),
        str(fixture),
    ],
}

RUNTIME_EXECUTABLES = {
    "python-reference-prk1": Path(sys.executable).name,
    "go-native-prk1": "go",
    "javascript-native-prk1": "node",
}


def run_json(command: list[str]) -> dict:
    completed = subprocess.run(
        command,
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(completed.stdout)


def max_abs_error(observed: list[float], expected: list[float]) -> float:
    if len(observed) != len(expected):
        raise AssertionError("vector length mismatch")
    return max((abs(a - b) for a, b in zip(observed, expected)), default=0.0)


def main() -> None:
    expected_bundle = json.loads(
        (ROOT / "fixtures/expected-results.json").read_text(encoding="utf-8")
    )
    tolerance = float(expected_bundle["max_abs_tolerance"])

    missing_runtimes = [
        implementation_id
        for implementation_id, executable in RUNTIME_EXECUTABLES.items()
        if shutil.which(executable) is None
    ]
    if missing_runtimes:
        raise SystemExit(
            "CONFORMANCE FAIL: required runtimes unavailable: "
            + ", ".join(missing_runtimes)
        )

    global_max_error = 0.0
    records: list[dict] = []

    for fixture_name in FIXTURES:
        fixture = ROOT / "fixtures" / f"{fixture_name}.json"
        expected = expected_bundle["results"][fixture_name]

        for implementation_id, command_factory in COMMANDS.items():
            observed = run_json(command_factory(fixture))
            if observed.get("kernel_version") != "PRK-1.0":
                raise AssertionError(f"{implementation_id}: kernel_version mismatch")
            if observed.get("fixture_id") != fixture_name:
                raise AssertionError(f"{implementation_id}: fixture_id mismatch")

            dx_error = max_abs_error(observed["dx"], expected["dx"])
            x_error = max_abs_error(observed["x_next"], expected["x_next"])
            service_error = abs(
                observed["weighted_service_next"]
                - expected["weighted_service_next"]
            )
            error = max(dx_error, x_error, service_error)
            global_max_error = max(global_max_error, error)

            passed = error <= tolerance
            records.append(
                {
                    "implementation_id": implementation_id,
                    "fixture_id": fixture_name,
                    "max_abs_error_dx": dx_error,
                    "max_abs_error_x_next": x_error,
                    "weighted_service_error": service_error,
                    "pass": passed,
                }
            )
            print(
                f"{'PASS' if passed else 'FAIL'} "
                f"{implementation_id} / {fixture_name} / max_error={error:.3e}"
            )
            if not passed:
                raise AssertionError(
                    f"{implementation_id} failed {fixture_name}: "
                    f"{error:.3e} > {tolerance:.3e}"
                )

    # Pairwise equality is not required bit-for-bit, but the frozen reference target is.
    if not math.isfinite(global_max_error):
        raise AssertionError("non-finite conformance error")

    print(f"POLYGLOT CONFORMANCE PASS ({len(records)} implementation-fixture checks)")
    print(f"Global maximum absolute error: {global_max_error:.3e}")
    print(f"Acceptance tolerance: {tolerance:.3e}")


if __name__ == "__main__":
    main()
