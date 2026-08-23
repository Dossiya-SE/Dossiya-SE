#!/usr/bin/env python3
"""Fail-closed audit for profile-wide mathematical presentation artifacts.

This audit validates structure and provenance metadata. It does not prove the
mathematics or empirically validate any model.
"""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATH_DIR = ROOT / "mathematical-art"
ASSET_DIR = ROOT / "assets" / "math-art"

REGISTRY = MATH_DIR / "formula_registry.json"
STANDARD = MATH_DIR / "MATHEMATICAL_PRESENTATION_STANDARD.md"
ATLAS = MATH_DIR / "PROFILE_FORMULA_ATLAS.md"
PROFILE = ROOT / "README.md"

VISUAL_GENERATION = "v5"
V5_SVGS = [
    ASSET_DIR / f"profile-mathematics-universe-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"research-operating-system-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"differential-geometry-foundations-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"formula-evidence-lattice-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"evidence-maturity-map-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"computational-stack-{VISUAL_GENERATION}.svg",
]

ALLOWED_STATES = {"S", "D", "M", "C", "V", "E", "H", "T"}
REQUIRED_FORMULA_FIELDS = {
    "id",
    "domain",
    "name",
    "latex",
    "state",
    "source",
    "role",
    "primary_repository",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def audit_registry() -> int:
    try:
        data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        fail(f"cannot parse {REGISTRY}: {exc}")

    if data.get("schema_version") != "3.0.0":
        fail("formula registry schema_version must be 3.0.0")

    formulas = data.get("formulas")
    if not isinstance(formulas, list) or not formulas:
        fail("formula registry must contain a non-empty formulas list")

    seen: set[str] = set()
    for index, item in enumerate(formulas, start=1):
        if not isinstance(item, dict):
            fail(f"formula entry {index} is not an object")
        missing = REQUIRED_FORMULA_FIELDS - set(item)
        if missing:
            fail(f"formula {index} missing fields: {sorted(missing)}")
        formula_id = item["id"]
        if formula_id in seen:
            fail(f"duplicate formula id: {formula_id}")
        seen.add(formula_id)
        if item["state"] not in ALLOWED_STATES:
            fail(f"invalid evidence state {item['state']} for {formula_id}")
        for field in REQUIRED_FORMULA_FIELDS:
            if not isinstance(item[field], str) or not item[field].strip():
                fail(f"empty/non-string {field} for {formula_id}")

    print(f"PASS: registry contains {len(formulas)} unique formula records")
    return len(formulas)


def audit_svg(path: Path) -> None:
    if not path.exists():
        fail(f"missing SVG: {path.relative_to(ROOT)}")
    try:
        root = ET.parse(path).getroot()
    except Exception as exc:  # pragma: no cover
        fail(f"invalid XML in {path.relative_to(ROOT)}: {exc}")

    if "viewBox" not in root.attrib:
        fail(f"SVG lacks viewBox: {path.relative_to(ROOT)}")

    ns = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", ns)
    desc = root.find("svg:desc", ns)
    if title is None or not (title.text or "").strip():
        fail(f"SVG lacks non-empty title: {path.relative_to(ROOT)}")
    if desc is None or not (desc.text or "").strip():
        fail(f"SVG lacks non-empty desc: {path.relative_to(ROOT)}")

    print(f"PASS: accessible SVG {path.relative_to(ROOT)}")


def audit_docs() -> None:
    for path in (STANDARD, ATLAS, PROFILE):
        if not path.exists() or path.stat().st_size < 500:
            fail(f"missing or unexpectedly small documentation file: {path.relative_to(ROOT)}")

    profile = PROFILE.read_text(encoding="utf-8")
    required_profile_refs = [
        "profile-header-v5.svg",
        "profile-mathematics-universe-v5.svg",
        "research-operating-system-v5.svg",
        "differential-geometry-foundations-v5.svg",
        "formula-evidence-lattice-v5.svg",
        "evidence-maturity-map-v5.svg",
        "computational-stack-v5.svg",
        "MATHEMATICAL_PRESENTATION_STANDARD.md",
        "PROFILE_FORMULA_ATLAS.md",
        "formula_registry.json",
    ]
    for ref in required_profile_refs:
        if ref not in profile:
            fail(f"profile README does not reference required artifact: {ref}")

    legacy_primary_refs = [
        "profile-header-v4.svg",
        "profile-mathematics-universe-v4.svg",
        "research-operating-system-v4.svg",
        "differential-geometry-foundations-v4.svg",
        "formula-evidence-lattice-v4.svg",
        "evidence-maturity-map-v4.svg",
        "computational-stack-v4.svg",
        "profile-mathematics-universe-v3.svg",
        "differential-geometry-viability-v3.svg",
        "formula-evidence-lattice-v3.svg",
        "assets/math-art/research-operating-system.svg",
        "assets/math-art/evidence-maturity-map.svg",
        "assets/math-art/computational-stack.svg",
    ]
    for ref in legacy_primary_refs:
        if ref in profile:
            fail(f"profile README still references legacy primary artifact: {ref}")

    standard = STANDARD.read_text(encoding="utf-8")
    for state in sorted(ALLOWED_STATES):
        if f"[{state}]" not in standard:
            fail(f"presentation standard does not define evidence state [{state}]")

    print("PASS: profile and mathematical presentation documentation references are complete")


def main() -> None:
    count = audit_registry()
    for svg in V5_SVGS:
        audit_svg(svg)
    audit_svg(ASSET_DIR / "profile-header-v5.svg")
    audit_docs()
    print(f"PASS: profile mathematical presentation V5 audit complete ({count} formula records)")


if __name__ == "__main__":
    main()
