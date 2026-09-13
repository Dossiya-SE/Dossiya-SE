#!/usr/bin/env python3
"""Validate the living research-profile data and generated mathematical-art assets."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
GENERATED = ROOT / "assets" / "generated"
README = ROOT / "README.md"

REQUIRED_MATH_OBJECTS = {"R_phys", "C", "G", "I", "F_G", "V", "rho_g", "u_star"}
REQUIRED_GENERATED = {
    "research-hero-light.svg",
    "research-hero-dark.svg",
    "research-state-light.svg",
    "research-state-dark.svg",
    "project-system.svg",
    "research-pipeline.svg",
}
ANIMATED_GENERATED = REQUIRED_GENERATED.copy()


def load_json(name: str) -> dict:
    path = DATA / name
    if not path.exists():
        raise ValueError(f"missing required data file: {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_declared_state(state: dict, framework: dict) -> None:
    require(state.get("schema_version") == "2.0", "research-state schema must be 2.0")
    require(state.get("evidence_state") == "DECLARED_RESEARCH_CONFIGURATION", "research state evidence class is invalid")

    physical = {item.get("name") for item in state.get("system", {}).get("physical", [])}
    nonphysical = {item.get("name") for item in state.get("system", {}).get("nonphysical", [])}
    require(physical == {"power", "transportation"}, "physical system must be exactly power + transportation")
    require(nonphysical == {"information", "organization"}, "nonphysical layers must be information + organization")

    stage_ids = {int(item["id"]) for item in framework.get("stages", [])}
    active = [int(x) for x in state.get("current_focus", {}).get("active_stages", [])]
    require(active == [2, 3], "current active transition must be stages 2 -> 3")
    require(set(active).issubset(stage_ids), "active stage is absent from framework")
    require(state.get("framework", {}).get("formal_stages") == len(stage_ids) == 7, "formal framework must contain seven stages")

    object_ids = {item.get("id") for item in state.get("mathematical_objects", [])}
    require(object_ids == REQUIRED_MATH_OBJECTS, "mathematical object registry is incomplete or contains ungoverned objects")
    require(state.get("scientific_integrity", {}).get("invariant") == "claim strength <= evidence strength", "scientific-integrity invariant missing")

    verified = str(state.get("last_verified", ""))
    try:
        verified_date = date.fromisoformat(verified)
    except ValueError as exc:
        raise ValueError("last_verified must be ISO YYYY-MM-DD") from exc
    require(verified_date <= date.today(), "last_verified cannot be in the future")


def validate_projects(projects: dict, observed: dict) -> None:
    require(projects.get("schema_version") == "2.0", "projects schema must be 2.0")
    require(projects.get("public_only") is True, "projects.json must enforce public_only=true")
    require(projects.get("owner") == "Dossiya-SE", "unexpected project owner")

    allowlist = projects.get("projects", [])
    require(isinstance(allowlist, list) and allowlist, "project allowlist is empty")
    slugs = [str(item.get("repository")) for item in allowlist]
    require(len(slugs) == len(set(slugs)), "duplicate repository in public allowlist")
    orders = [int(item.get("profile_order")) for item in allowlist]
    require(len(orders) == len(set(orders)), "duplicate profile_order in public allowlist")

    require(observed.get("schema_version") == "2.0", "public evidence schema must be 2.0")
    require(observed.get("evidence_state") == "OBSERVED_PUBLIC_REPOSITORY_METADATA", "public evidence class is invalid")
    observed_repos = observed.get("repositories", [])
    observed_slugs = [str(item.get("repository")) for item in observed_repos]
    require(set(observed_slugs) == set(slugs), "observed repository set must exactly match the public allowlist")

    for item in observed_repos:
        repository = str(item.get("repository"))
        require(item.get("visibility") == "public", f"non-public evidence detected: {repository}")
        require(str(item.get("url", "")).startswith("https://github.com/Dossiya-SE/"), f"unexpected repository URL: {repository}")
        require(not bool(item.get("archived")) or item.get("status") != "active", f"active project is archived: {repository}")


def validate_readme() -> None:
    text = README.read_text(encoding="utf-8")
    lower = text.lower()
    for asset in REQUIRED_GENERATED:
        require(f"assets/generated/{asset}" in text, f"README does not reference generated asset: {asset}")
    for forbidden in ("visitor counter", "github streak", "typing animation", "language percentage"):
        require(forbidden not in lower, f"README contains prohibited vanity-profile concept: {forbidden}")
    require("semantic motion" in lower, "README must explain the meaning of animation")
    require("not a measured flow" in lower, "README must preserve the motion/measurement scientific boundary")
    require("deterministic mathematical visual constructions" in lower, "README must distinguish mathematical art from fitted data")
    require("claim strength" in lower and "evidence strength" in lower, "README must state the claim/evidence invariant")


def validate_generated() -> None:
    for name in REQUIRED_GENERATED:
        path = GENERATED / name
        require(path.exists(), f"missing generated visual: {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        require("<script" not in lower, f"generated SVG contains script: {name}")
        require(re.search(r"\b(?:href|src)=[\"']http://", text, flags=re.IGNORECASE) is None, f"generated SVG contains insecure external reference: {name}")
        try:
            root = ET.fromstring(text)
        except ET.ParseError as exc:
            raise ValueError(f"invalid SVG XML: {name}: {exc}") from exc
        require(root.tag.endswith("svg"), f"generated file is not an SVG: {name}")
        require(root.attrib.get("viewBox") is not None, f"generated SVG lacks viewBox: {name}")
        require("<title" in text and "<desc" in text, f"generated SVG lacks accessible title/description: {name}")
        if name in ANIMATED_GENERATED:
            require("@keyframes" in text, f"generated SVG lacks self-contained animation: {name}")
            require("prefers-reduced-motion:reduce" in text, f"generated SVG lacks reduced-motion fallback: {name}")

    hero_light = (GENERATED / "research-hero-light.svg").read_text(encoding="utf-8")
    pipeline = (GENERATED / "research-pipeline.svg").read_text(encoding="utf-8")
    projects = (GENERATED / "project-system.svg").read_text(encoding="utf-8")

    require("flow-gold" in hero_light and "flow-blue" in hero_light, "hero must encode causal transfer and state evolution separately")
    require('class="vector-field"' in hero_light, "hero must include a deterministic state-space vector field")
    require('class="level-set"' in hero_light, "hero must include deterministic level-set geometry")
    require("not measured infrastructure telemetry" in hero_light.lower(), "hero description must preserve the mathematical-art/data boundary")
    require("flow-gold" in pipeline, "pipeline must animate only the active transition")
    require("MOST RECENT PUBLIC CHANGE" in projects, "project panel must identify the most recent observed public change")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-only", action="store_true", help="validate source data without requiring rendered SVG assets")
    args = parser.parse_args()

    state = load_json("research-state.json")
    framework = load_json("framework.json")
    projects = load_json("projects.json")
    observed = load_json("public-github-state.json")

    require(framework.get("schema_version") == "2.0", "framework schema must be 2.0")
    validate_declared_state(state, framework)
    validate_projects(projects, observed)

    if not args.input_only:
        validate_generated()
        validate_readme()

    print("PROFILE VALIDATION: PASS — research state, evidence, mathematical art, semantic motion, and scientific boundaries are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"PROFILE VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)