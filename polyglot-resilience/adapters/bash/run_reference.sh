#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

python3 "$ROOT/tools/validate_structure.py"
python3 "$ROOT/tests/invariants/test_reference_kernel.py"
python3 "$ROOT/tests/conformance/compare_outputs.py"

printf '%s\n' "POLYGLOT RESILIENCE VALIDATION PIPELINE: PASS"
