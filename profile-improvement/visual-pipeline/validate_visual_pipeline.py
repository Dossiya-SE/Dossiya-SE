#!/usr/bin/env python3
"""Fail-closed checks for the profile mathematical-visual pipeline."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC_PATH = HERE / "visual_spec.json"
GENERATOR = HERE / "generate_synthetic_math.py"
DATA = HERE / "synthetic_profile_data.json"


def fail(message: str) -> None:
    raise AssertionError(message)


def read_svg(path: Path) -> tuple[str, ET.Element]:
    source = path.read_text(encoding="utf-8")
    try:
        root = ET.fromstring(source)
    except ET.ParseError as exc:
        fail(f"invalid SVG/XML: {path.relative_to(ROOT)} — {exc}")
    return source, root


def visible_svg_text(root: ET.Element) -> str:
    return " ".join(x.strip() for x in root.itertext() if x.strip())


def validate_asset(name: str, cfg: dict[str, object]) -> None:
    path = ROOT / str(cfg["path"])
    if not path.is_file():
        fail(f"missing canonical visual: {path.relative_to(ROOT)}")

    source, root = read_svg(path)
    if root.attrib.get("viewBox") != cfg["viewBox"]:
        fail(f"{name}: expected viewBox {cfg['viewBox']}, found {root.attrib.get('viewBox')}")

    lowered = source.lower()
    if "<image" in lowered or "data:image/" in lowered:
        fail(f"{name}: embedded raster is prohibited")

    if "□" in source or "�" in source:
        fail(f"{name}: replacement/missing-glyph marker detected")

    if name == "hero" and "@media(prefers-color-scheme:dark)" not in source:
        fail("hero: adaptive-theme declaration missing")

    text = visible_svg_text(root)
    for token in cfg.get("required_tokens", []):
        if token not in text:
            fail(f"{name}: missing required semantic token: {token}")

    # Fail on text smaller than the public-spec minimum, except metadata/title/desc.
    minimum = float(cfg.get("minimum_label_px", 0))
    sizes = []
    for element in root.iter():
        if not element.tag.endswith("text"):
            continue
        style = element.attrib.get("style", "")
        match = re.search(r"font-size:\s*([0-9.]+)px", style)
        if match:
            sizes.append(float(match.group(1)))
        elif "font-size" in element.attrib:
            value = element.attrib["font-size"].replace("px", "")
            try:
                sizes.append(float(value))
            except ValueError:
                pass
    if sizes and min(sizes) < minimum:
        fail(f"{name}: text below minimum label size {minimum}px; found {min(sizes)}px")


def validate_synthetic_source() -> None:
    subprocess.run([sys.executable, str(GENERATOR)], cwd=ROOT, check=True)
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    if payload.get("evidence_state") != "SYNTHETIC_ILLUSTRATIVE_NOT_EMPIRICAL":
        fail("synthetic data evidence label missing or changed")
    if payload.get("random_seed") != 20260912:
        fail("deterministic synthetic seed changed unexpectedly")

    models = payload["models"]
    if len(models["potential"]["data"]) != 3:
        fail("potential family must contain three controlled parameter cases")
    if len(models["manifold_centerline"]["data"]) != 181:
        fail("manifold source sampling changed unexpectedly")
    if len(models["viability_boundary"]["data"]) != 241:
        fail("viability source sampling changed unexpectedly")
    if len(models["multilayer_graph"]["nodes"]) != 20:
        fail("multilayer graph must retain 4 layers × 5 nodes")


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    if spec.get("spec_id") != "DD-VISUAL-PIPELINE-001":
        fail("unexpected visual-pipeline specification")

    validate_synthetic_source()
    for name, cfg in spec["canonical_assets"].items():
        validate_asset(name, cfg)

    print("PROFESSIONAL MATHEMATICAL VISUAL PIPELINE: PASS")
    print("Synthetic-source provenance: PASS")
    print("Native SVG / no raster: PASS")
    print("Renderer-safe glyph markers: PASS")
    print("Canvas contracts: PASS")
    print("Minimum label-size gate: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"PROFESSIONAL MATHEMATICAL VISUAL PIPELINE: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
