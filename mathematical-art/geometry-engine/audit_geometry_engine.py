#!/usr/bin/env python3
"""Fail-closed audit of the V6 renderer registry."""

from __future__ import annotations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "mathematical-art" / "geometry-engine" / "renderer_registry_v6.json"
REQUIRED = {"profile-header","professional-trajectory","mathematics-universe","research-operating-system",
            "differential-geometry-foundations","computational-stack","formula-evidence-lattice","evidence-maturity-map"}


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    failures = []
    if data.get("schema") != "Dossiya-SE/profile-renderer-registry/v6":
        failures.append("unexpected schema")
    parts = data.get("profile_parts", [])
    ids = {p.get("id") for p in parts}
    if REQUIRED - ids:
        failures.append("missing profile parts: " + ", ".join(sorted(REQUIRED - ids)))
    for part in parts:
        asset = part.get("asset")
        if not asset or not (ROOT / asset).exists():
            failures.append(f"{part.get('id')}: missing asset {asset!r}")
        if not part.get("canonical_renderer") or not part.get("motion_policy"):
            failures.append(f"{part.get('id')}: incomplete renderer contract")
    dg = next((p for p in parts if p.get("id") == "differential-geometry-foundations"), {})
    if dg.get("promotion_target") != "P3" or not dg.get("verified_source"):
        failures.append("differential geometry P3 verified-source contract missing")
    if failures:
        for failure in failures:
            print("FAIL:", failure)
        return 1
    print(f"PASS: renderer registry covers {len(parts)} profile parts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
