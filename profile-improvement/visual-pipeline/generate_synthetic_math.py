#!/usr/bin/env python3
"""Generate deterministic mathematical source data for profile visuals.

The generated objects are illustrative / synthetic. They are not empirical
infrastructure observations and must not be presented as such.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "synthetic_profile_data.json"
SEED = 20260912


def potential_family() -> dict[str, list[list[float]]]:
    xs = [(-2.0 + 4.0 * i / 160.0) for i in range(161)]
    data: dict[str, list[list[float]]] = {}
    for mu in (-0.3, 0.0, 0.3):
        pts = []
        for x in xs:
            v = 0.25 * x**4 - 0.5 * x**2 - mu * x
            pts.append([round(x, 8), round(v, 8)])
        data[f"mu={mu:+.1f}"] = pts
    return data


def manifold_centerline() -> list[list[float]]:
    pts = []
    for i in range(181):
        x = -3.0 + 6.0 * i / 180.0
        y = 0.40 * math.sin(1.25 * x) + 0.12 * math.sin(2.7 * x)
        pts.append([round(x, 8), round(y, 8)])
    return pts


def viability_boundary() -> list[list[float]]:
    pts = []
    for i in range(241):
        t = 2.0 * math.pi * i / 240.0
        r = 1.0 + 0.12 * math.sin(3.0 * t) - 0.08 * math.cos(2.0 * t)
        x = 0.95 * r * math.cos(t)
        y = 0.70 * r * math.sin(t)
        pts.append([round(x, 8), round(y, 8)])
    return pts


def multilayer_graph() -> dict[str, object]:
    layers = ["Power", "Transportation", "Information", "Organization"]
    x = [0.0, 1.0, 2.0, 3.0, 4.0]
    offsets = [0.00, 0.03, -0.015, 0.025, -0.005]
    layer_y = [3.0, 2.0, 1.0, 0.0]
    nodes = []
    intralayer_edges = []
    interlayer_edges = []
    for li, (layer, base_y) in enumerate(zip(layers, layer_y)):
        for j, (xx, off) in enumerate(zip(x, offsets)):
            nodes.append({"id": f"{layer}:{j}", "layer": layer, "x": xx, "y": base_y + off})
            if j > 0:
                intralayer_edges.append([f"{layer}:{j-1}", f"{layer}:{j}"])
        if li > 0:
            prev = layers[li - 1]
            for j in range(len(x)):
                interlayer_edges.append([f"{prev}:{j}", f"{layer}:{j}"])
    return {
        "layers": layers,
        "nodes": nodes,
        "intralayer_edges": intralayer_edges,
        "interlayer_edges": interlayer_edges,
    }


def main() -> None:
    payload = {
        "schema": "DD-SYNTHETIC-PROFILE-MATH-001",
        "evidence_state": "SYNTHETIC_ILLUSTRATIVE_NOT_EMPIRICAL",
        "random_seed": SEED,
        "models": {
            "potential": {
                "equation": "V(x;mu)=0.25*x^4-0.5*x^2-mu*x",
                "data": potential_family(),
            },
            "manifold_centerline": {
                "equation": "y(x)=0.40*sin(1.25*x)+0.12*sin(2.7*x)",
                "data": manifold_centerline(),
            },
            "viability_boundary": {
                "equation": "r(t)=1+0.12*sin(3*t)-0.08*cos(2*t)",
                "data": viability_boundary(),
            },
            "multilayer_graph": multilayer_graph(),
        },
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
