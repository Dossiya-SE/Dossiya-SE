#!/usr/bin/env python3
"""Fail-closed audit for profile-wide mathematical presentation artifacts.

The audit separates the complete mathematical-art inventory from the smaller
set deliberately published on the GitHub profile. Passing this audit verifies
structure and provenance metadata; it does not prove mathematics or empirical validity.
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
PUBLIC_INTEGRITY = ROOT / "docs" / "RESEARCH_INTEGRITY.md"

VISUAL_GENERATION = "v5"
V5_SVGS = [
    ASSET_DIR / f"profile-mathematics-universe-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"research-operating-system-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"differential-geometry-foundations-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"formula-evidence-lattice-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"evidence-maturity-map-{VISUAL_GENERATION}.svg",
    ASSET_DIR / f"computational-stack-{VISUAL_GENERATION}.svg",
]
PUBLISHED_PROFILE_SVGS = [
    ASSET_DIR / "profile-header-v5.svg",
    ASSET_DIR / "research-operating-system-v5.svg",
    ASSET_DIR / "differential-geometry-foundations-v5.svg",
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


def audit_svg(path: Path, *, native_vector: bool = False) -> None:
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

    if native_vector:
        source = path.read_text(encoding="utf-8").lower()
        if "<image" in source or "data:image/" in source:
            fail(f"published profile SVG embeds raster content: {path.relative_to(ROOT)}")

    print(f"PASS: accessible SVG {path.relative_to(ROOT)}")


def audit_docs() -> None:
    for path in (STANDARD, ATLAS, PROFILE, PUBLIC_INTEGRITY):
        if not path.exists() or path.stat().st_size < 500:
            fail(f"missing or unexpectedly small documentation file: {path.relative_to(ROOT)}")

    profile = PROFILE.read_text(encoding="utf-8")

    required_profile_refs = [
        "profile-header-v5.svg",
        "research-operating-system-v5.svg",
        "differential-geometry-foundations-v5.svg",
        "docs/RESEARCH_INTEGRITY.md",
    ]
    for ref in required_profile_refs:
        if ref not in profile:
            fail(f"profile README does not reference required public artifact: {ref}")

    intentionally_unpublished_refs = [
        "profile-mathematics-universe-v5.svg",
        "formula-evidence-lattice-v5.svg",
        "evidence-maturity-map-v5.svg",
        "computational-stack-v5.svg",
        "optimization-decision-system-v6.svg",
    ]
    for ref in intentionally_unpublished_refs:
        if ref in profile:
            fail(f"profile README exceeds the selected visual budget with: {ref}")

    standard = STANDARD.read_text(encoding="utf-8")
    for state in sorted(ALLOWED_STATES):
        if f"[{state}]" not in standard:
            fail(f"presentation standard does not define evidence state [{state}]")

    print("PASS: deep mathematical inventory is separated from concise public profile publication")


def main() -> None:
    count = audit_registry()

    for svg in V5_SVGS:
        audit_svg(svg)

    for svg in PUBLISHED_PROFILE_SVGS:
        audit_svg(svg, native_vector=True)

    audit_docs()
    print(
        f"PASS: mathematical presentation inventory remains intact while the public profile "
        f"uses a bounded three-visual interface ({count} formula records)"
    )


if __name__ == "__main__":
    main()
