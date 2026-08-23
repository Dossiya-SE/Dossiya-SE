#!/usr/bin/env python3
"""Fail-closed validation for the governed public profile architecture."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT / "profile-improvement"
README = ROOT / "README.md"
REGISTRY = WORKSPACE / "PROFILE_CREDENTIALS_REGISTRY.json"
MASTER = WORKSPACE / "PROFILE_MASTER_SPEC.md"
PUBLIC = WORKSPACE / "PUBLIC_PROFILE_TRAJECTORY.md"

VISUAL_GENERATION = "v5"
HEADER = ROOT / "assets" / "math-art" / f"profile-header-{VISUAL_GENERATION}.svg"
TRAJECTORY_SVG = WORKSPACE / "assets" / f"engineering-to-mathematics-resilience-trajectory-{VISUAL_GENERATION}.svg"
TECHNICAL_SVGS = [
    ROOT / "assets" / "math-art" / f"profile-mathematics-universe-{VISUAL_GENERATION}.svg",
    ROOT / "assets" / "math-art" / f"research-operating-system-{VISUAL_GENERATION}.svg",
    ROOT / "assets" / "math-art" / f"differential-geometry-foundations-{VISUAL_GENERATION}.svg",
    ROOT / "assets" / "math-art" / f"formula-evidence-lattice-{VISUAL_GENERATION}.svg",
    ROOT / "assets" / "math-art" / f"evidence-maturity-map-{VISUAL_GENERATION}.svg",
    ROOT / "assets" / "math-art" / f"computational-stack-{VISUAL_GENERATION}.svg",
]

REQUIRED = [
    README,
    REGISTRY,
    MASTER,
    PUBLIC,
    WORKSPACE / "PROFILE_CREDENTIAL_VERIFICATION_CHECKLIST.md",
    WORKSPACE / "PROFILE_RELEASE_GATE.md",
    WORKSPACE / "REQUEST_PROTOCOL.md",
    WORKSPACE / "MATHEMATICS_ART_IDENTITY_V1.md",
    WORKSPACE / "PROFILE_PAGE_COMPOSITION_V1.md",
    HEADER,
    TRAJECTORY_SVG,
    *TECHNICAL_SVGS,
]


def fail(message: str) -> None:
    raise AssertionError(message)


def svg_text(path: Path) -> str:
    """Parse SVG as XML and return all visible/accessible text for semantic checks."""
    tree = ET.parse(path)
    return " ".join(part.strip() for part in tree.getroot().itertext() if part.strip())


def main() -> int:
    for path in REQUIRED:
        if not path.is_file():
            fail(f"Required profile-control artifact missing: {path.relative_to(ROOT)}")

    readme = README.read_text(encoding="utf-8")
    master = MASTER.read_text(encoding="utf-8")
    public = PUBLIC.read_text(encoding="utf-8")
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    if "ACTIVE_GOVERNING_PROFILE_ARCHITECTURE" not in master:
        fail("Profile master specification is not marked active.")

    required_readme_tokens = [
        "## Professional and research trajectory",
        "## Research programmes",
        "## Mathematics as a research operating system",
        "## Scientific computing and mathematical art",
        "## Evidence and validation",
        "assets/math-art/profile-header-v5.svg",
        "profile-improvement/assets/engineering-to-mathematics-resilience-trajectory-v5.svg",
        "assets/math-art/profile-mathematics-universe-v5.svg",
        "assets/math-art/research-operating-system-v5.svg",
        "assets/math-art/differential-geometry-foundations-v5.svg",
        "assets/math-art/formula-evidence-lattice-v5.svg",
        "assets/math-art/evidence-maturity-map-v5.svg",
        "assets/math-art/computational-stack-v5.svg",
        "Profile Improvement Workspace",
        "MSE Sustainable Engineering — Arizona State University, ongoing",
        "MS Financial Engineering — WorldQuant University, ongoing",
    ]
    for token in required_readme_tokens:
        if token not in readme:
            fail(f"Public README missing required governed token: {token}")

    legacy_primary_paths = [
        "assets/math-art/profile-header-v4.svg",
        "profile-improvement/assets/engineering-to-mathematics-resilience-trajectory.svg",
        "assets/math-art/profile-mathematics-universe-v4.svg",
        "assets/math-art/research-operating-system-v4.svg",
        "assets/math-art/differential-geometry-foundations-v4.svg",
        "assets/math-art/formula-evidence-lattice-v4.svg",
        "assets/math-art/evidence-maturity-map-v4.svg",
        "assets/math-art/computational-stack-v4.svg",
        "assets/math-art/profile-mathematics-universe-v3.svg",
        "assets/math-art/research-operating-system.svg",
        "assets/math-art/differential-geometry-viability-v3.svg",
        "assets/math-art/formula-evidence-lattice-v3.svg",
        "assets/math-art/evidence-maturity-map.svg",
        "assets/math-art/computational-stack.svg",
    ]
    for token in legacy_primary_paths:
        if token in readme:
            fail(f"README still uses legacy primary visual path despite V5 master: {token}")

    evidence_index = readme.index("## Evidence and validation")
    for workflow_token in (
        "actions/workflows/verify.yml",
        "actions/workflows/production-audit.yml",
        "africa-energy-dignity/actions/workflows/python-app.yml",
    ):
        position = readme.find(workflow_token)
        if 0 <= position < evidence_index:
            fail(f"Workflow badge appears before Evidence and validation: {workflow_token}")

    if "Electrical engineering practice\n→ renewable-energy + physical systems" in readme:
        fail("README still contains redundant text-only trajectory chain.")

    credentials = {item["credential_id"]: item for item in registry["credentials"]}

    for credential_id in ("DD-EDU-001", "DD-EDU-002", "DD-EDU-003"):
        item = credentials[credential_id]
        if item.get("public_change_status") == "HOLD_UNTIL_TITLE_VERIFIED":
            title = item.get("user_stated_title", "")
            if title and title in readme:
                fail(f"Unverified technical credential title was published in root README: {title}")

    undergrad = credentials["DD-EDU-004"]
    if undergrad.get("public_change_status") == "RECONCILE_BEFORE_PUBLIC_CHANGE":
        unresolved_title = undergrad.get("user_stated_title", "")
        if unresolved_title and unresolved_title in readme:
            fail(
                "Unreconciled undergraduate English title was published in root README: "
                f"{unresolved_title}"
            )
        current_title = undergrad.get("current_public_profile_title", "")
        if current_title and current_title not in readme:
            fail("Current public undergraduate title disappeared before reconciliation.")

    for credential_id in ("DD-EDU-005", "DD-EDU-006"):
        item = credentials[credential_id]
        if item.get("programme_status") != "ONGOING":
            fail(f"Graduate programme status changed unexpectedly for {credential_id}.")

    if "RELEASABLE_WITH_CREDENTIAL_TITLE_RECONCILIATION_PENDING" not in public:
        fail("Public-safe trajectory is missing its controlled release status.")

    if "not a claim of an already validated universal theory" not in readme:
        fail("Cross-sector research-ambition boundary is missing from root README.")

    header_text = svg_text(HEADER)
    trajectory_text = svg_text(TRAJECTORY_SVG)
    for svg in TECHNICAL_SVGS:
        svg_text(svg)

    required_header_tokens = [
        "Dossiya Dakou",
        "γ : [2016,2026] → 𝓜",
        "ẋ = Ax + Bu",
        "Pgen + Pimport + Pdis = Pload + Ploss + Pch + Pexport",
        "Pᵢⱼ = Pr(Sₜ₊₁=j | Sₜ=i)",
        "L = D − A",
        "dXₜ=b(Xₜ,t)dt+σ(Xₜ,t)dWₜ",
        "u* = arg min J(u)",
        "gᵢⱼ = ⟨∂ᵢr,∂ⱼr⟩",
        "conceptual trajectory · no proficiency scoring · adaptive SVG",
    ]
    for token in required_header_tokens:
        if token not in header_text:
            fail(f"Mathematics-art header missing governed mathematical token: {token}")

    header_source = HEADER.read_text(encoding="utf-8")
    if "@media(prefers-color-scheme:dark)" not in header_source:
        fail("V5 hero is not adaptive to light/dark rendering.")
    if 'viewBox="0 0 2048 640"' not in header_source:
        fail("V5 hero does not use the governed 2048×640 wide vector canvas.")

    required_trajectory_tokens = [
        "PROFESSIONAL TRAJECTORY: ENGINEERING → MATHEMATICS → RESILIENCE",
        "2016",
        "2026 →",
        "PROFESSIONAL",
        "ELECTRICAL ENGINEERING",
        "RENEWABLE ENERGY",
        "SUSTAINABLE",
        "FINANCIAL",
        "DEEPER MATHEMATICS",
        "SUSTAINABLE RESILIENT",
    ]
    for token in required_trajectory_tokens:
        if token not in trajectory_text:
            fail(f"Mathematics-art trajectory missing governed token: {token}")

    prohibited_art_tokens = [
        "Schrödinger",
        "quantum",
        "universal resilience theory",
    ]
    combined_art = f"{header_text} {trajectory_text}".lower()
    for token in prohibited_art_tokens:
        if token.lower() in combined_art:
            fail(f"Profile mathematical art contains prohibited/decorative claim token: {token}")

    print("PROFILE GOVERNANCE VALIDATION: PASS")
    print(f"Credentials checked: {len(credentials)}")
    print("Unverified technical titles remain unpublished in root README: PASS")
    print("Ongoing graduate status preserved: PASS")
    print("Research-ambition boundary preserved: PASS")
    print("Header + trajectory + six V5 technical SVG XML parses: PASS")
    print("Professional page composition and V5 binding: PASS")
    print("Verification badges remain below Evidence and validation: PASS")
    print("Mathematics-art semantic token audit: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, ET.ParseError) as exc:
        print(f"PROFILE GOVERNANCE VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
