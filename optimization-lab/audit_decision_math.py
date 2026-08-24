#!/usr/bin/env python3
"""Fail-closed profile audit for executable OR/Bayesian decision benchmarks."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

from decision_math import (
    equality_qp_certificate,
    lp_primal_dual_certificate,
    min_cost_flow_certificate,
)

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "knowledge-graphs" / "iee574_bayesian_knowledge_graph_v1.json"
ANCHORS = ROOT / "docs" / "knowledge-graphs" / "OR_SOURCE_ANCHORS_V1.md"
SVG = ROOT / "assets" / "math-art" / "optimization-decision-system-v6.svg"

REQUIRED_ANCHORS = {
    "LP-STANDARD-001",
    "CVX-SET-002",
    "LP-BFS-004",
    "LP-REDUCEDCOST-005",
    "LP-WEAKDUAL-010",
    "LP-STRONGDUAL-011",
    "LP-CS-012",
    "LP-SENS-013",
    "IP-RELAX-002",
    "IP-BOUND-003",
    "NF-BALANCE-001",
    "NF-MINCOST-002",
    "NLP-LAGRANGE-002",
    "NLP-KKT-003",
    "NLP-QP-004",
}

SEMANTIC_COLOR_TOKENS = {
    "--source",
    "--state",
    "--interface",
    "--uncertainty",
    "--viability",
    "--decision",
    "--computed",
}

MIN_SOURCE_FONT_SIZE = 30.0  # 30 * 768 / 1920 = 12 px at the target README width.


def main() -> int:
    failures: list[str] = []

    graph = json.loads(GRAPH.read_text())
    ids = [node["id"] for node in graph["nodes"]]
    if len(ids) != len(set(ids)):
        failures.append("duplicate knowledge-graph node IDs")
    known = set(ids)
    dangling = [edge for edge in graph["edges"] if edge["source"] not in known or edge["target"] not in known]
    if dangling:
        failures.append(f"dangling graph edges: {dangling}")
    if len([x for x in ids if x.startswith("IEE574-")]) != 17:
        failures.append("IEE 574 inventory is not 17/17")

    anchor_text = ANCHORS.read_text()
    missing = sorted(REQUIRED_ANCHORS - {x for x in REQUIRED_ANCHORS if x in anchor_text})
    if missing:
        failures.append(f"missing P0 anchors: {missing}")

    svg = SVG.read_text()
    for token in ("<title", "<desc", "viewBox=\"0 0 1920 600\"", "prefers-color-scheme:dark"):
        if token not in svg:
            failures.append(f"professional decision SVG missing {token}")

    missing_colors = sorted(token for token in SEMANTIC_COLOR_TOKENS if token not in svg)
    if missing_colors:
        failures.append(f"professional decision SVG missing semantic color tokens: {missing_colors}")

    font_sizes = [float(x) for x in re.findall(r'font-size="([0-9]+(?:\.[0-9]+)?)"', svg)]
    if not font_sizes:
        failures.append("professional decision SVG has no explicit font sizes")
    elif min(font_sizes) < MIN_SOURCE_FONT_SIZE:
        failures.append(
            f"professional decision SVG minimum font size {min(font_sizes):g} "
            f"is below {MIN_SOURCE_FONT_SIZE:g} source units"
        )

    for name, certificate in (
        ("LP primal/dual", lp_primal_dual_certificate()),
        ("min-cost flow", min_cost_flow_certificate()),
        ("equality QP", equality_qp_certificate()),
    ):
        if not certificate.passed:
            failures.append(f"{name} failed: {certificate.residuals}")
        else:
            print(f"PASS {name}: {certificate.residuals}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(
        "PASS: professional optimization/decision architecture is source-anchored, "
        "legible, semantically encoded, and numerically closed."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
