#!/usr/bin/env python3
"""Validate README information architecture and refined profile containers."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated"
README = ROOT / "README.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def svg(name: str) -> str:
    path = OUT / name
    require(path.exists(), f"missing refined profile visual: {name}")
    text = path.read_text(encoding="utf-8")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"invalid SVG XML: {name}: {exc}") from exc
    require(root.tag.endswith("svg"), f"{name}: root must be SVG")
    require(root.attrib.get("viewBox"), f"{name}: viewBox missing")
    require("<title" in text and "<desc" in text, f"{name}: accessibility metadata missing")
    require("prefers-reduced-motion:reduce" in text, f"{name}: reduced-motion fallback missing")
    return text


def validate_readme() -> None:
    text = README.read_text(encoding="utf-8")
    lower = text.lower()

    # Seven visible primary containers in a fixed narrative order.
    headings = [
        "## 01 · Research problem",
        "## 02 · Coupled physical system",
        "## 03 · Graph → dynamics → viability",
        "## 04 · Current research state",
        "## 05 · Mathematical foundations for the physical problem",
        "## 06 · Research systems",
        "## 07 · Experience and education",
    ]
    positions = []
    for heading in headings:
        require(heading in text, f"README missing primary container: {heading}")
        positions.append(text.index(heading))
    require(positions == sorted(positions), "README primary containers are not in governed order")

    require("assets/generated/research-question.svg" in text, "README must surface the current research question visually")
    require("assets/generated/graph-to-viability.svg" in text, "README must surface graph-to-viability transformation")
    require("assets/generated/research-state-light.svg" in text, "README must surface living research state")
    require("assets/generated/project-system.svg" in text, "README must surface featured research systems")
    require("assets/generated/flat-geometry.svg" in text, "README must surface the governed flat-geometry visual")
    require("mathematical-art/flat-geometry/overleaf/flat_geometry.tex" in text, "README must expose the publication-quality TikZ source")
    require("plane figures" in lower and "affine flats" in lower, "README must distinguish bounded plane figures from affine flats")

    # Full framework, design manual and automation are secondary, not primary sections.
    for forbidden_heading in ("## Research architecture", "## Scientific visual constitution", "## Living-profile engine"):
        require(forbidden_heading not in text, f"secondary material leaked into primary reading path: {forbidden_heading}")
    require("<summary><b>Full seven-stage research architecture</b></summary>" in text, "full research architecture must be collapsed")
    require("<summary><b>Scientific visual and accessibility standard</b></summary>" in text, "visual standard must be collapsed")
    require("<summary><b>Living-profile engine</b></summary>" in text, "living-profile engine must be collapsed")

    # Project prose must not duplicate the project figure as repeated mini-sections.
    repeated_project_headings = [
        "### Mathematics for Sustainable Resilience",
        "### Optimization for Sustainability and Resilience",
        "### Africa Energy Dignity",
        "### Engineering Computation",
    ]
    require(not any(h in text for h in repeated_project_headings), "project figure must not be duplicated by repeated project mini-sections")

    # Key scientific boundaries stay visible.
    require("claim strength" in lower and "evidence strength" in lower, "claim/evidence invariant missing")
    require("not measured infrastructure behavior" in lower or "not live infrastructure telemetry" in lower, "motion/measurement boundary missing")
    require("topology first" in lower and "mechanism before model" in lower, "physics-first research logic missing")


def validate_question() -> None:
    text = svg("research-question.svg")
    require("RESEARCH QUESTION" in text, "research-question figure missing title")
    require("Power ↔ Transportation interfaces" in text, "research-question figure missing physical interface scope")
    require("Y(t) ∈ 𝒱" in text, "research-question figure missing viability objective")
    require("var(--yellow" in text and "var(--green" in text, "research-question figure missing semantic causal/viability cues")
    body = text.split("</style>", 1)[-1]
    for token in ("var(--power)", "var(--transport)", "var(--information)"):
        require(token in body, f"research-question figure missing RGB sector/dynamics token: {token}")


def validate_state() -> None:
    for name in ("research-state-light.svg", "research-state-dark.svg"):
        text = svg(name)
        body = text.split("</style>", 1)[-1]
        require("CURRENT SCIENTIFIC TRANSITION" in body, f"{name}: active transition missing")
        require("Causal Mechanisms" in body and "Coupled Hybrid Multiscale Dynamics" in body, f"{name}: transition endpoints missing")
        require("MATHEMATICAL STATE" in body, f"{name}: mathematical signature missing")
        require("var(--power)" in body and "var(--transport)" in body and "var(--information)" in body, f"{name}: RGB sector channels missing")
        require("var(--red)" not in body and "var(--red-soft)" not in body, f"{name}: red must not encode metadata or normal research state")
        require("EVIDENCE OBSERVED" not in body, f"{name}: metadata must not be presented as a critical-status card")
        require(body.count("<rect") <= 4, f"{name}: excessive container/card count reintroduced")


def validate_viability() -> None:
    text = svg("graph-to-viability.svg")
    require("GRAPH / MODEL SPACE" in text, "graph-to-viability must identify graph/model space")
    require("STATE / VIABILITY SPACE" in text, "graph-to-viability must identify state/viability space")
    require("∂𝒱" in text and "ρ_g" in text and "u*" in text, "graph-to-viability core objects missing")
    require("var(--red)" in text and "var(--green)" in text and "var(--yellow)" in text, "graph-to-viability semantic colors missing")
    require("No empirical validity is implied" in text, "graph-to-viability evidence boundary missing")


def validate_projects() -> None:
    text = svg("project-system.svg")
    require("FEATURED RESEARCH SYSTEMS" in text, "project system must emphasize research-facing systems")
    require(text.count('class="panel research-card"') == 4, "project system must show exactly four featured research cards")
    require("MOST RECENT PUBLIC CHANGE" in text, "project system must retain public recency metadata")
    require("recency is metadata, not scientific importance or validation" in text, "project recency boundary missing")
    body = text.split("</style>", 1)[-1]
    require("var(--violet)" in body and "var(--information)" in body and "var(--transport)" in body and "var(--cyan)" in body, "project index must retain restrained RGB navigation accents")


def main() -> int:
    validate_readme()
    validate_question()
    validate_state()
    validate_viability()
    validate_projects()
    print("PROFILE LAYOUT VALIDATION: PASS — information hierarchy, container economy, semantic color discipline and scientific boundaries are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"PROFILE LAYOUT VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
