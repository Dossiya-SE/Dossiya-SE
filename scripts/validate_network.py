#!/usr/bin/env python3
"""Validate the governed coupled Power–Transportation network and generated SVGs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"
README = ROOT / "README.md"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_layer(layer: dict, expected_id: str, required_types: set[str]) -> set[str]:
    require(layer.get("schema_version") == "1.0", f"{expected_id}: schema must be 1.0")
    require(layer.get("evidence_state") == "DECLARED_EXPLANATORY_NETWORK_MODEL", f"{expected_id}: invalid evidence state")
    require(layer.get("network_id") == expected_id, f"{expected_id}: network_id mismatch")
    nodes = layer.get("nodes", [])
    edges = layer.get("edges", [])
    require(nodes and edges, f"{expected_id}: empty nodes or edges")
    ids = [str(n["id"]) for n in nodes]
    require(len(ids) == len(set(ids)), f"{expected_id}: duplicate node ids")
    node_types = {str(n["type"]) for n in nodes}
    require(required_types.issubset(node_types), f"{expected_id}: required node type missing")
    for n in nodes:
        require(isinstance(n.get("x"), (int,float)) and isinstance(n.get("y"), (int,float)), f"{expected_id}: node coordinate missing")
    edge_ids = [str(e["id"]) for e in edges]
    require(len(edge_ids) == len(set(edge_ids)), f"{expected_id}: duplicate edge ids")
    for e in edges:
        require(e.get("source") in ids and e.get("target") in ids, f"{expected_id}: edge endpoint absent from node set")
        require(e.get("state") == "operational", f"{expected_id}: declared baseline edge must be operational")
        require(e.get("direction") in {"forward","bidirectional"}, f"{expected_id}: invalid edge direction")
    require("explanatory" in str(layer.get("scientific_boundary", "")).lower(), f"{expected_id}: scientific boundary missing")
    return set(ids)


def validate_interface(interfaces: dict, pids: set[str], tids: set[str]) -> None:
    require(interfaces.get("schema_version") == "1.0", "interfaces: schema must be 1.0")
    require(interfaces.get("evidence_state") == "DECLARED_EXPLANATORY_INTERFACE_MODEL", "interfaces: invalid evidence state")
    items = interfaces.get("interfaces", [])
    require(len(items) == 1, "exactly one governed profile interface is required")
    item = items[0]
    require(item.get("shared_asset") == "C1", "shared asset must be C1")
    require("C1" in pids and "C1" in tids, "C1 must exist in both physical layers")
    require(item.get("power_entity") == "C1" and item.get("transport_entity") == "C1", "interface entities must reference shared C1")
    mechanisms = item.get("mechanisms", [])
    dirs = {m.get("direction") for m in mechanisms}
    require({"P_to_T","T_to_P"}.issubset(dirs), "interface must contain bidirectional causal mechanisms")
    mids = {m.get("id") for m in mechanisms}
    require("M_PT_electricity_supply" in mids and "M_TP_charging_demand" in mids, "required power-transport mechanisms missing")
    for m in mechanisms:
        require(isinstance(m.get("delay"), str) and m.get("delay", "").startswith("tau_"), "delays must remain symbolic in the profile model")
        require(isinstance(m.get("magnitude"), str) and m.get("magnitude", "").startswith("w_"), "magnitudes must remain symbolic in the profile model")
        require("no calibrated magnitude claimed" in str(m.get("evidence_status", "")) or "conditional mechanism declaration" in str(m.get("evidence_status", "")), "mechanism evidence boundary missing")
    require("symbolic" in str(item.get("scientific_boundary", "")).lower(), "interface scientific boundary must protect uncalibrated parameters")


def validate_dynamics(dyn: dict, power: dict, transport: dict) -> None:
    require(dyn.get("schema_version") == "1.0", "network dynamics schema must be 1.0")
    require(dyn.get("evidence_state") == "DECLARED_EXPLANATORY_DYNAMIC_CYCLE", "dynamic cycle evidence state invalid")
    require(float(dyn.get("cycle_seconds", 0)) > 0, "dynamic cycle duration must be positive")
    states = dyn.get("states", [])
    expected = ["nominal","disturbance","propagation","control","recovery"]
    require([s.get("id") for s in states] == expected, "dynamic cycle order must be nominal→disturbance→propagation→control→recovery")
    previous = 0.0
    for s in states:
        fr = s.get("fraction")
        require(isinstance(fr,list) and len(fr)==2, "state fraction must be [start,end]")
        start,end = map(float,fr)
        require(0 <= start < end <= 1, "state fraction outside [0,1]")
        require(abs(start-previous) < 1e-9, "dynamic state fractions must be contiguous")
        previous = end
    require(abs(previous-1.0) < 1e-9, "dynamic cycle must end at 1.0")
    p_edges = {e["id"] for e in power["edges"]}; t_edges = {e["id"] for e in transport["edges"]}
    sp = dyn.get("scenario_path", {})
    require(sp.get("disturbance_origin") in p_edges, "disturbance origin edge missing from power layer")
    require(sp.get("transport_propagation_edge") in t_edges, "propagation edge missing from transport layer")
    require(sp.get("interface") == "C1" and sp.get("transport_receiver") == "H1", "scenario path must propagate through C1 to H1")
    require("not measured" in str(dyn.get("scientific_boundary", "")).lower(), "dynamic cycle must state non-measurement boundary")


def validate_svg(name: str) -> str:
    path = OUT / name
    require(path.exists(), f"missing generated SVG: {name}")
    text = path.read_text(encoding="utf-8")
    lower = text.lower()
    require("<script" not in lower, f"{name}: scripts are prohibited")
    require(re.search(r"\b(?:href|src)=[\"']http://", text, flags=re.I) is None, f"{name}: insecure external reference")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise ValueError(f"{name}: invalid SVG XML: {exc}") from exc
    require(root.tag.endswith("svg"), f"{name}: root is not SVG")
    require(root.attrib.get("viewBox"), f"{name}: viewBox missing")
    require("<title" in text and "<desc" in text, f"{name}: accessible title/desc missing")
    require("prefers-reduced-motion:reduce" in text, f"{name}: reduced-motion fallback missing")
    return text


def validate_generated() -> None:
    light = validate_svg("coupled-network-light.svg")
    dark = validate_svg("coupled-network-dark.svg")
    transform = validate_svg("graph-to-viability.svg")
    for text,name in ((light,"light network"),(dark,"dark network")):
        require("POWER NETWORK" in text and "TRANSPORTATION NETWORK" in text, f"{name}: both physical layers required")
        require("shared physical asset · C1" in text, f"{name}: shared interface annotation missing")
        require("interface-flow" in text and "critical-demo" in text and "control-demo" in text and "recovery-demo" in text, f"{name}: semantic motion classes missing")
        require("not measured infrastructure telemetry" in text.lower(), f"{name}: animation/data boundary missing")
        require("--green:" in text and "--red:" in text and "--yellow:" in text, f"{name}: permanent semantic palette missing")
    require("∂𝒱" in transform and "ρ" in transform and "Y(t)" in transform and "u*" in transform, "graph-to-viability figure missing core mathematical objects")
    require("No empirical validity is implied" in transform, "graph-to-viability evidence boundary missing")


def validate_readme() -> None:
    text = README.read_text(encoding="utf-8")
    lower = text.lower()
    hero_2d = "assets/generated/coupled-network-light.svg" in text and "assets/generated/coupled-network-dark.svg" in text
    hero_3d = "assets/generated/coupled-network-3d-light.svg" in text and "assets/generated/coupled-network-3d-dark.svg" in text
    require(hero_2d or hero_3d, "README must use a governed coupled network as primary hero")
    require("assets/generated/graph-to-viability.svg" in text, "README must include graph-to-viability transformation")
    require("same physical object" in lower and "c_1" in lower, "README must explain shared-interface semantics")
    require("not measured infrastructure behavior" in lower or "not live infrastructure telemetry" in lower, "README must state visualization/measurement boundary")
    require("topology first" in lower, "README must preserve topology-first principle")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-only", action="store_true")
    args = parser.parse_args()
    power = load("power-network.json")
    transport = load("transport-network.json")
    interfaces = load("interfaces.json")
    dyn = load("network-dynamics.json")
    pids = validate_layer(power,"G_P",{"generator","substation","load","interface"})
    tids = validate_layer(transport,"G_T",{"origin","destination","intersection","hub","terminal","interface"})
    validate_interface(interfaces,pids,tids)
    validate_dynamics(dyn,power,transport)
    if not args.input_only:
        validate_generated()
        validate_readme()
    print("NETWORK VALIDATION: PASS — topology, shared interface, dynamic semantics, SVGs and scientific boundaries are consistent.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"NETWORK VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
