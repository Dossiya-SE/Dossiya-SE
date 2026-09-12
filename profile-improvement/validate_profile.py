#!/usr/bin/env python3
"""Fail-closed validation for the professional public profile interface."""

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
CREDENTIAL_CHECKLIST = WORKSPACE / "PROFILE_CREDENTIAL_VERIFICATION_CHECKLIST.md"
RELEASE_GATE = WORKSPACE / "PROFILE_RELEASE_GATE.md"
WORKSPACE_README = WORKSPACE / "README.md"

HEADER = ROOT / "assets" / "math-art" / "profile-header-v5.svg"
PRIMARY_VISUALS = [
    ROOT / "assets" / "math-art" / "research-operating-system-v5.svg",
    ROOT / "assets" / "math-art" / "differential-geometry-foundations-v5.svg",
]
PUBLIC_INTEGRITY = ROOT / "docs" / "RESEARCH_INTEGRITY.md"

REQUIRED = [
    README,
    REGISTRY,
    MASTER,
    PUBLIC,
    CREDENTIAL_CHECKLIST,
    RELEASE_GATE,
    WORKSPACE_README,
    HEADER,
    PUBLIC_INTEGRITY,
    *PRIMARY_VISUALS,
]

UNDERGRAD_PUBLIC_TITLE = "Licence, Énergies Renouvelables et Systèmes Énergétiques"
STALE_UNDERGRAD_TITLE = "Licence Professionnelle"
CANONICAL_PROFILE_IDENTITY = "Mathematical Sustainable Engineering for Sustainable Resilience"
CANONICAL_PROFILE_IDENTITY_TOKEN = "MATHEMATICAL SUSTAINABLE ENGINEERING"
STALE_PROFILE_IDENTITY = "Mathematical Systems Engineering for Sustainable Resilience"
STALE_PROFILE_IDENTITY_TOKEN = "MATHEMATICAL SYSTEMS ENGINEERING"


def fail(message: str) -> None:
    raise AssertionError(message)


def svg_text(path: Path) -> str:
    tree = ET.parse(path)
    return " ".join(part.strip() for part in tree.getroot().itertext() if part.strip())


def assert_native_vector(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    ET.fromstring(source)
    lowered = source.lower()
    if "<image" in lowered:
        fail(f"Raster/image wrapper is prohibited in public vector visual: {path.relative_to(ROOT)}")
    if "data:image/" in lowered:
        fail(f"Embedded raster data URI is prohibited in public vector visual: {path.relative_to(ROOT)}")


def main() -> int:
    for path in REQUIRED:
        if not path.is_file():
            fail(f"Required profile artifact missing: {path.relative_to(ROOT)}")

    readme = README.read_text(encoding="utf-8")
    master = MASTER.read_text(encoding="utf-8")
    public = PUBLIC.read_text(encoding="utf-8")
    checklist = CREDENTIAL_CHECKLIST.read_text(encoding="utf-8")
    release_gate = RELEASE_GATE.read_text(encoding="utf-8")
    workspace_readme = WORKSPACE_README.read_text(encoding="utf-8")
    registry_source = REGISTRY.read_text(encoding="utf-8")
    registry = json.loads(registry_source)

    if "ACTIVE_GOVERNING_PROFILE_ARCHITECTURE" not in master:
        fail("Profile master specification is not marked active.")

    required_sections = [
        "## About",
        "## Featured research",
        "## Research framework",
        "## Mathematical focus",
        "## Computational toolkit",
        "## Education",
        "## Research integrity",
        "## Connect",
    ]
    positions = []
    for section in required_sections:
        if section not in readme:
            fail(f"Public README missing required professional section: {section}")
        positions.append(readme.index(section))
    if positions != sorted(positions):
        fail("Professional public sections are not in the governed order.")

    required_readme_tokens = [
        CANONICAL_PROFILE_IDENTITY,
        "assets/math-art/profile-header-v5.svg",
        "assets/math-art/research-operating-system-v5.svg",
        "assets/math-art/differential-geometry-foundations-v5.svg",
        "docs/RESEARCH_INTEGRITY.md",
        "MSE Sustainable Engineering — Arizona State University, ongoing",
        "MS Financial Engineering — WorldQuant University, ongoing",
        UNDERGRAD_PUBLIC_TITLE,
        "not a claim of an already validated universal theory",
    ]
    for token in required_readme_tokens:
        if token not in readme:
            fail(f"Public README missing required governed token: {token}")

    prohibited_public_tokens = [
        "Profile Improvement Workspace",
        "Profile Credential Verification Checklist",
        "Repository evidence-maturity map",
        "Full repository matrix",
        "Core mathematical objects across the profile",
        "<details>",
        STALE_UNDERGRAD_TITLE,
        STALE_PROFILE_IDENTITY,
    ]
    for token in prohibited_public_tokens:
        if token in readme:
            fail(f"Prohibited or stale content leaked into public interface: {token}")

    active_credential_surfaces = {
        "PROFILE_CREDENTIALS_REGISTRY.json": registry_source,
        "PROFILE_MASTER_SPEC.md": master,
        "PUBLIC_PROFILE_TRAJECTORY.md": public,
        "PROFILE_CREDENTIAL_VERIFICATION_CHECKLIST.md": checklist,
        "PROFILE_RELEASE_GATE.md": release_gate,
        "profile-improvement/README.md": workspace_readme,
    }
    for name, text in active_credential_surfaces.items():
        if STALE_UNDERGRAD_TITLE in text:
            fail(f"Stale undergraduate credential wording remains in active governance surface: {name}")

    readme_bytes = len(readme.encode("utf-8"))
    if not 5_000 <= readme_bytes <= 14_000:
        fail(f"Public README must remain concise (5–14 KB); found {readme_bytes} bytes.")

    local_image_refs = readme.count("<img src=\"assets/")
    if local_image_refs != 3:
        fail(f"Professional profile must use exactly three local visuals; found {local_image_refs}.")

    credentials = {item["credential_id"]: item for item in registry["credentials"]}

    for credential_id in ("DD-EDU-001", "DD-EDU-002", "DD-EDU-003"):
        item = credentials[credential_id]
        if item.get("public_change_status") == "HOLD_UNTIL_TITLE_VERIFIED":
            title = item.get("user_stated_title", "")
            if title and title in readme:
                fail(f"Unverified technical credential title was published: {title}")

    undergrad = credentials["DD-EDU-004"]
    if undergrad.get("user_stated_title") != UNDERGRAD_PUBLIC_TITLE:
        fail("Credential registry does not preserve the user-confirmed undergraduate title.")
    if undergrad.get("current_public_profile_title") != UNDERGRAD_PUBLIC_TITLE:
        fail("Credential registry public undergraduate title is inconsistent with the correction.")
    if undergrad.get("public_change_status") != "USER_CONFIRMED_PUBLIC_TITLE":
        fail("Undergraduate credential correction is not marked USER_CONFIRMED_PUBLIC_TITLE.")
    if "USER_CONFIRMED" not in undergrad.get("evidence_state", []):
        fail("Undergraduate credential correction is missing USER_CONFIRMED evidence state.")
    if undergrad.get("translation_status") != "NO_ENGLISH_TITLE_ASSERTED":
        fail("Undergraduate translation boundary is not explicitly controlled.")
    if undergrad.get("institution") != "Université d’Abomey-Calavi":
        fail("Undergraduate institution changed unexpectedly.")

    for credential_id in ("DD-EDU-005", "DD-EDU-006"):
        item = credentials[credential_id]
        if item.get("programme_status") != "ONGOING":
            fail(f"Graduate programme status changed unexpectedly for {credential_id}.")

    if "RELEASABLE_WITH_CREDENTIAL_TITLE_RECONCILIATION_PENDING" not in public:
        fail("Public-safe trajectory is missing its controlled release status.")

    assert_native_vector(HEADER)
    for visual in PRIMARY_VISUALS:
        assert_native_vector(visual)

    header_source = HEADER.read_text(encoding="utf-8")
    if "@media(prefers-color-scheme:dark)" not in header_source:
        fail("Profile hero must adapt to light/dark rendering.")
    if 'viewBox="0 0 2048 640"' not in header_source:
        fail("Profile hero must use the governed 2048×640 canvas.")
    if STALE_PROFILE_IDENTITY in header_source or STALE_PROFILE_IDENTITY_TOKEN in header_source:
        fail("Stale profile identity wording remains in the public hero source.")

    header_text = svg_text(HEADER)
    for token in (
        "Dossiya Dakou",
        CANONICAL_PROFILE_IDENTITY_TOKEN,
        "SUSTAINABILITY · RESILIENCE · OPTIMIZATION",
        "ẋ = f(x,u,η)",
        "ρ(x)=d(x,∂V)",
        "EVIDENCE → MODEL → COMPUTE → VERIFY → VALIDATE → DECIDE",
    ):
        if token not in header_text:
            fail(f"Profile hero missing required semantic token: {token}")

    integrity = PUBLIC_INTEGRITY.read_text(encoding="utf-8")
    for token in (
        "Simulation is not relabeled as observation.",
        "Passing tests is not relabeled as empirical validation.",
        "claim strength",
    ):
        if token not in integrity:
            fail(f"Public research-integrity standard missing token: {token}")

    print("PROFESSIONAL PROFILE VALIDATION: PASS")
    print(f"README size: {readme_bytes} bytes")
    print("Public sections: 8/8")
    print("Local visuals: 3/3")
    print("Native vector hero: PASS")
    print("Credential safeguards: PASS")
    print("Licence-title regression guard: PASS")
    print("Canonical identity regression guard: PASS")
    print("Research-integrity boundary: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, ET.ParseError, json.JSONDecodeError) as exc:
        print(f"PROFESSIONAL PROFILE VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
