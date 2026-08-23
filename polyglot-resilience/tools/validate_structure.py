"""Validate the Polyglot Resilience Atlas structure and PRK-1.0 contracts.

Uses only the Python standard library so it can run as an early CI gate.
"""

from __future__ import annotations

import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "KERNEL_SPECIFICATION.md",
    "SEMANTIC_CONTRACT.md",
    "MODEL_ASSUMPTIONS.md",
    "VALIDATION_STANDARD.md",
    "BENCHMARK_PROTOCOL.md",
    "schemas/resilience-kernel-v1.schema.json",
    "fixtures/baseline.json",
    "fixtures/controlled-recovery.json",
    "fixtures/severe-hazard.json",
    "fixtures/expected-results.json",
    "registry/implementation-registry.json",
    "implementations/python/kernel.py",
    "implementations/go/main.go",
    "implementations/javascript/kernel.mjs",
    "architecture/polyglot-resilience-architecture.svg",
]

FIXTURE_NAMES = ("baseline", "controlled-recovery", "severe-hazard")


def fail(message: str) -> None:
    raise SystemExit(f"POLYGLOT STRUCTURE FAIL: {message}")


def finite(values: list[float]) -> bool:
    return all(math.isfinite(float(value)) for value in values)


def validate_fixture(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("kernel_version") != "PRK-1.0":
        fail(f"{path.name}: wrong kernel version")

    required = {"fixture_id", "dt", "x", "D", "A", "r", "h", "B", "u", "weights"}
    missing = required.difference(payload)
    if missing:
        fail(f"{path.name}: missing fields {sorted(missing)}")

    x = payload["x"]
    n = len(x)
    m = len(payload["u"])
    if n == 0 or m == 0:
        fail(f"{path.name}: empty state/control vector")
    if not math.isfinite(float(payload["dt"])) or payload["dt"] <= 0:
        fail(f"{path.name}: invalid dt")
    if any(len(payload[key]) != n for key in ("r", "h", "weights")):
        fail(f"{path.name}: vector dimension mismatch")
    for key in ("D", "A"):
        if len(payload[key]) != n or any(len(row) != n for row in payload[key]):
            fail(f"{path.name}: {key} must be n x n")
    if len(payload["B"]) != n or any(len(row) != m for row in payload["B"]):
        fail(f"{path.name}: B must be n x m")

    numeric = (
        list(x)
        + payload["r"]
        + payload["h"]
        + payload["u"]
        + payload["weights"]
        + [v for row in payload["D"] for v in row]
        + [v for row in payload["A"] for v in row]
        + [v for row in payload["B"] for v in row]
    )
    if not finite(numeric):
        fail(f"{path.name}: non-finite numerical input")
    if any(value < 0 or value > 1 for value in x):
        fail(f"{path.name}: x outside [0,1]")
    if any(value < 0 for value in payload["r"]):
        fail(f"{path.name}: negative recovery")
    if any(value < 0 for value in payload["weights"]):
        fail(f"{path.name}: negative weight")
    if abs(sum(payload["weights"]) - 1.0) > 1e-12:
        fail(f"{path.name}: weights do not sum to one")
    return payload


def main() -> None:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    if missing:
        fail(f"missing required paths: {missing}")

    # Parse all machine-readable contracts before deeper checks.
    json.loads((ROOT / "schemas/resilience-kernel-v1.schema.json").read_text(encoding="utf-8"))
    registry = json.loads((ROOT / "registry/implementation-registry.json").read_text(encoding="utf-8"))
    expected = json.loads((ROOT / "fixtures/expected-results.json").read_text(encoding="utf-8"))

    if registry.get("kernel_version") != "PRK-1.0":
        fail("registry kernel version mismatch")
    if expected.get("kernel_version") != "PRK-1.0":
        fail("expected-results kernel version mismatch")

    ids = [item["implementation_id"] for item in registry.get("implementations", [])]
    if len(ids) != len(set(ids)):
        fail("implementation IDs must be unique")

    valid_statuses = set(registry.get("maturity_scale", []))
    for item in registry.get("implementations", []):
        if item.get("maturity") not in valid_statuses:
            fail(f"invalid maturity for {item.get('implementation_id')}")
        path = item.get("path")
        if path and item.get("maturity") in {"IMPLEMENTED", "TESTED", "VALIDATED", "BENCHMARKED"}:
            if not (ROOT / path).exists():
                fail(f"implemented path missing: {path}")

    fixtures = {}
    for name in FIXTURE_NAMES:
        payload = validate_fixture(ROOT / "fixtures" / f"{name}.json")
        if payload["fixture_id"] != name:
            fail(f"fixture ID mismatch for {name}")
        fixtures[name] = payload

    expected_names = set(expected.get("results", {}))
    if expected_names != set(FIXTURE_NAMES):
        fail(f"expected-results fixture set mismatch: {sorted(expected_names)}")

    # Baseline deliberately activates terms that reduced legacy snippets omitted.
    baseline = fixtures["baseline"]
    if not any(abs(v) > 0 for row in baseline["B"] for v in row) or not any(abs(v) > 0 for v in baseline["u"]):
        fail("baseline must activate the Bu control term")
    off_diagonal_d = [
        abs(baseline["D"][i][j])
        for i in range(len(baseline["D"]))
        for j in range(len(baseline["D"]))
        if i != j
    ]
    if not any(value > 0 for value in off_diagonal_d):
        fail("baseline must contain non-diagonal D entries")

    # SVG validity is a repository invariant because GitHub must render the architecture.
    try:
        ET.parse(ROOT / "architecture/polyglot-resilience-architecture.svg")
    except ET.ParseError as exc:
        fail(f"architecture SVG is invalid XML: {exc}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "architecture/polyglot-resilience-architecture.svg" not in readme:
        fail("README does not reference the canonical architecture SVG")

    print("POLYGLOT STRUCTURE PASS")
    print(f"Fixtures validated: {len(fixtures)}")
    print(f"Implementation IDs validated: {len(ids)}")
    print("Control-term activation: PASS")
    print("Full-D fixture coverage: PASS")
    print("Architecture SVG XML: PASS")


if __name__ == "__main__":
    main()
