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
SVG = WORKSPACE / "assets" / "engineering-to-mathematics-resilience-trajectory.svg"

REQUIRED = [
    README,
    REGISTRY,
    MASTER,
    PUBLIC,
    WORKSPACE / "PROFILE_CREDENTIAL_VERIFICATION_CHECKLIST.md",
    WORKSPACE / "PROFILE_RELEASE_GATE.md",
    WORKSPACE / "REQUEST_PROTOCOL.md",
    SVG,
]


def fail(message: str) -> None:
    raise AssertionError(message)


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
        "profile-improvement/assets/engineering-to-mathematics-resilience-trajectory.svg",
        "Profile Improvement Workspace",
        "MSE Sustainable Engineering — Arizona State University, ongoing",
        "MS Financial Engineering — WorldQuant University, ongoing",
    ]
    for token in required_readme_tokens:
        if token not in readme:
            fail(f"Public README missing required governed token: {token}")

    credentials = {item["credential_id"]: item for item in registry["credentials"]}

    # Fail closed while unresolved titles are explicitly on hold.
    for credential_id in ("DD-EDU-001", "DD-EDU-002", "DD-EDU-003"):
        item = credentials[credential_id]
        if item.get("public_change_status") == "HOLD_UNTIL_TITLE_VERIFIED":
            title = item.get("user_stated_title", "")
            if title and title in readme:
                fail(
                    f"Unverified technical credential title was published in root README: {title}"
                )

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

    # XML parser is sufficient to catch malformed SVG entities/structure.
    ET.parse(SVG)

    print("PROFILE GOVERNANCE VALIDATION: PASS")
    print(f"Credentials checked: {len(credentials)}")
    print("Unverified technical titles remain unpublished in root README: PASS")
    print("Ongoing graduate status preserved: PASS")
    print("Research-ambition boundary preserved: PASS")
    print("Trajectory SVG XML parse: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, ET.ParseError) as exc:
        print(f"PROFILE GOVERNANCE VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
