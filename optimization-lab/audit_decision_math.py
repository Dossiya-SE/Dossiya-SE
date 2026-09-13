#!/usr/bin/env python3
"""Fail-closed audit for executable OR/Bayesian decision benchmarks.

This audit verifies source anchoring, graph integrity, and numerical certificates.
Profile visuals are governed independently by the living-profile validator.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

from decision_math import (
    equality_qp_certificate,
    lp_primal_dual_certificate,
    min_cost_flow_certificate,
)

ROOT = Path(__file__).resolve().parents[1]
GRAPH = ROOT / "docs" / "knowledge-graphs" / "iee574_bayesian_knowledge_graph_v1.json"
ANCHORS = ROOT / "docs" / "knowledge-graphs" / "OR_SOURCE_ANCHORS_V1.md"

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


def main() -> int:
    failures: list[str] = []

    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    ids = [node["id"] for node in graph["nodes"]]
    if len(ids) != len(set(ids)):
        failures.append("duplicate knowledge-graph node IDs")
    known = set(ids)
    dangling = [edge for edge in graph["edges"] if edge["source"] not in known or edge["target"] not in known]
    if dangling:
        failures.append(f"dangling graph edges: {dangling}")
    if len([item for item in ids if item.startswith("IEE574-")]) != 17:
        failures.append("IEE 574 inventory is not 17/17")

    anchor_text = ANCHORS.read_text(encoding="utf-8")
    missing = sorted(anchor for anchor in REQUIRED_ANCHORS if anchor not in anchor_text)
    if missing:
        failures.append(f"missing P0 anchors: {missing}")

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

    print("PASS: optimization/decision architecture is source-anchored, graph-consistent, and numerically closed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
