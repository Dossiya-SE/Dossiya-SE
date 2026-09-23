#!/usr/bin/env python3
"""Validate the governed living profile and its mathematical-art assets."""

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
README_GENERATED = {
    "research-state-light.svg",
    "research-state-dark.svg",
    "project-system.svg",
    "research-pipeline.svg",
}


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
    require(state.get("evidence_state") == "DECLARED_RESEARCH_CONFIGURATION", "invalid research evidence class")
    physical = {x.get("name") for x in state.get("system", {}).get("physical", [])}
    nonphysical = {x.get("name") for x in state.get("system", {}).get("nonphysical", [])}
    require(physical == {"power", "transportation"}, "physical system must be power + transportation")
    require(nonphysical == {"information", "organization"}, "supporting layers must be information + organization")
    stage_ids = {int(x["id"]) for x in framework.get("stages", [])}
    active = [int(x) for x in state.get("current_focus", {}).get("active_stages", [])]
    require(active == [2, 3], "current transition must remain stages 2 -> 3")
    require(set(active).issubset(stage_ids), "active stage absent from framework")
    require(state.get("framework", {}).get("formal_stages") == len(stage_ids) == 7, "framework must contain seven stages")
    require({x.get("id") for x in state.get("mathematical_objects", [])} == REQUIRED_MATH_OBJECTS, "mathematical object registry mismatch")
    require(state.get("scientific_integrity", {}).get("invariant") == "claim strength <= evidence strength", "claim/evidence invariant missing")
    try:
        verified = date.fromisoformat(str(state.get("last_verified", "")))
    except ValueError as exc:
        raise ValueError("last_verified must be ISO YYYY-MM-DD") from exc
    require(verified <= date.today(), "last_verified cannot be in the future")


def validate_projects(projects: dict, observed: dict) -> None:
    require(projects.get("schema_version") == "2.0", "projects schema must be 2.0")
    require(projects.get("public_only") is True, "projects.json must enforce public_only=true")
    require(projects.get("owner") == "Dossiya-SE", "unexpected project owner")
    allowlist = projects.get("projects", [])
    require(bool(allowlist), "project allowlist is empty")
    slugs = [str(x.get("repository")) for x in allowlist]
    require(len(slugs) == len(set(slugs)), "duplicate repository in allowlist")
    require(observed.get("schema_version") == "2.0", "public evidence schema must be 2.0")
    require(observed.get("evidence_state") == "OBSERVED_PUBLIC_REPOSITORY_METADATA", "invalid public evidence class")
    observed_repos = observed.get("repositories", [])
    require({str(x.get("repository")) for x in observed_repos} == set(slugs), "observed repositories must exactly match allowlist")
    for item in observed_repos:
        repo = str(item.get("repository"))
        require(item.get("visibility") == "public", f"non-public evidence detected: {repo}")
        require(str(item.get("url", "")).startswith("https://github.com/Dossiya-SE/"), f"unexpected repository URL: {repo}")


def validate_readme() -> None:
    text = README.read_text(encoding="utf-8")
    lower = text.lower()
    for asset in README_GENERATED:
        require(f"assets/generated/{asset}" in text, f"README does not reference {asset}")
    for forbidden in ("visitor counter", "github streak", "typing animation", "language percentage"):
        require(forbidden not in lower, f"README contains prohibited vanity concept: {forbidden}")
    for triplet in ("rgb(22, 130, 58)", "rgb(207, 34, 46)", "rgb(0, 122, 136)"):
        require(triplet in lower, f"README missing governed RGB semantic triplet: {triplet}")
    require("not measured infrastructure behavior" in lower or "not a measured flow" in lower, "README must preserve the motion/measurement boundary")
    require("claim strength" in lower and "evidence strength" in lower, "README must state the claim/evidence invariant")


def validate_svg(name: str) -> str:
    path = GENERATED / name
    require(path.exists(), f"missing generated visual: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    require("<script" not in lower, f"generated SVG contains script: {name}")
    require(re.search(r"\b(?:href|src)=[\"']http://", text, flags=re.IGNORECASE) is None, f"insecure external reference: {name}")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"invalid SVG XML: {name}: {exc}") from exc
    require(root.tag.endswith("svg"), f"generated file is not SVG: {name}")
    require(root.attrib.get("viewBox") is not None, f"generated SVG lacks viewBox: {name}")
    require("<title" in text and "<desc" in text, f"generated SVG lacks accessibility metadata: {name}")
    require("@keyframes" in text, f"generated SVG lacks self-contained animation: {name}")
    require("prefers-reduced-motion:reduce" in text, f"generated SVG lacks reduced-motion fallback: {name}")
    require("--green:" in text and "--red:" in text and "--control:" in text and "--control-soft:" in text, f"generated SVG lacks governed green/red/cyan-control palette: {name}")
    return text


def validate_generated() -> None:
    rendered = {name: validate_svg(name) for name in REQUIRED_GENERATED}
    hero = rendered["research-hero-light.svg"]
    pipeline = rendered["research-pipeline.svg"]
    projects = rendered["project-system.svg"]
    require('class="vector-field"' in hero, "legacy mathematical portrait must retain deterministic state-space vector field")
    require('class="level-set"' in hero, "legacy mathematical portrait must retain deterministic level sets")
    require("critical-boundary" in hero and "flow-red" in hero, "legacy portrait must encode critical boundary in red")
    require("flow-green" in hero, "legacy portrait must encode viable/sustainable state evolution in green")
    require("flow-control" in hero, "legacy portrait must encode causal/decision pathway in cyan control")
    require("not a measured flow" in hero.lower(), "legacy portrait must preserve mathematical-art/data boundary")
    hero_body = hero.split("</style>", 1)[-1]
    for token in ("var(--power)", "var(--transport)", "var(--information)", "var(--organization-ink)"):
        require(token in hero_body, f"RGB research portrait missing semantic sector token: {token}")
    require("SYSTEM CHANNELS" in hero_body, "RGB research portrait must label the system-channel ontology")
    pipeline_body = pipeline.split("</style>", 1)[-1]
    for token in ("var(--power)", "var(--organization)", "var(--transport)", "var(--cyan)", "var(--information)", "var(--magenta)"):
        require(token in pipeline_body, f"RGB pipeline missing stage-navigation token: {token}")
    require("RGB progression is a visual navigation system" in pipeline_body, "pipeline must state RGB is not scientific ontology")
    require("flow-control" in pipeline and "var(--red)" in pipeline and "var(--green)" in pipeline, "pipeline must retain governed RGB state semantics")
    require("MOST RECENT PUBLIC CHANGE" in projects, "project system must identify most recent public change")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-only", action="store_true")
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
    print("PROFILE VALIDATION: PASS — research state, public evidence, palette, mathematical art, motion, and scientific boundaries are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"PROFILE VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
