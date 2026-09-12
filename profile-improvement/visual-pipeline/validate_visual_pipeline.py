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
RESEARCH_STATE = ROOT / "data" / "research-state.json"
FRAMEWORK_STATE = ROOT / "data" / "framework.json"
PROJECTS_STATE = ROOT / "data" / "projects.json"
GITHUB_STATE = ROOT / "data" / "github-state.json"
DYNAMIC_ASSET = ROOT / "assets" / "math-art" / "research-state-v1.svg"


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


def svg_text_sizes(root: ET.Element) -> list[float]:
    sizes: list[float] = []
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
    return sizes


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

    minimum = float(cfg.get("minimum_label_px", 0))
    sizes = svg_text_sizes(root)
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


def validate_declared_research_state() -> None:
    research = json.loads(RESEARCH_STATE.read_text(encoding="utf-8"))
    framework = json.loads(FRAMEWORK_STATE.read_text(encoding="utf-8"))
    projects_doc = json.loads(PROJECTS_STATE.read_text(encoding="utf-8"))

    stages = framework.get("stages", [])
    if len(stages) != 7:
        fail("framework.json must contain exactly seven stages")
    if [stage.get("id") for stage in stages] != list(range(1, 8)):
        fail("framework stage IDs must be the ordered integers 1..7")

    declared_count = research.get("framework", {}).get("stages")
    active_stage = research.get("framework", {}).get("active_stage")
    if declared_count != 7:
        fail("research-state framework stage count must be 7")
    if active_stage not in range(1, 8):
        fail("research-state active stage must lie in 1..7")
    if research.get("current_focus", {}).get("stage") != active_stage:
        fail("current_focus.stage must equal framework.active_stage")

    physical = set(research.get("system", {}).get("physical", []))
    nonphysical = set(research.get("system", {}).get("nonphysical", []))
    if not {"power", "transportation"}.issubset(physical):
        fail("physical system must retain power and transportation")
    if not {"information", "organization"}.issubset(nonphysical):
        fail("nonphysical system must retain information and organization")

    if projects_doc.get("public_only") is not True:
        fail("projects.json must enforce public_only=true")
    required = {"name", "repository", "research_role", "status"}
    repositories: list[str] = []
    for project in projects_doc.get("projects", []):
        if not required.issubset(project):
            fail(f"project record missing required fields: {project}")
        repository = str(project["repository"])
        if "/" in repository or repository.startswith("http"):
            fail(f"project repository must be an allowlisted repository name only: {repository}")
        repositories.append(repository)
    if len(repositories) != len(set(repositories)):
        fail("projects.json contains duplicate repositories")
    if not repositories:
        fail("projects.json must contain at least one public research repository")


def validate_github_state() -> None:
    github = json.loads(GITHUB_STATE.read_text(encoding="utf-8"))
    projects = json.loads(PROJECTS_STATE.read_text(encoding="utf-8"))
    configured = {str(project["repository"]) for project in projects["projects"]}

    if github.get("evidence_state") != "OBSERVED_PUBLIC_REPOSITORY_METADATA":
        fail("GitHub state evidence label is missing or changed")
    if github.get("source") != "GitHub REST API":
        fail("GitHub telemetry source must be GitHub REST API")
    if github.get("status") not in {"bootstrap_pending_refresh", "live"}:
        fail("GitHub telemetry status must be bootstrap_pending_refresh or live")

    telemetry = github.get("repositories", [])
    if github.get("status") == "live":
        observed = {str(repo.get("repository")) for repo in telemetry}
        if observed != configured:
            fail("live GitHub telemetry must match the explicit public project allowlist exactly")
        for repo in telemetry:
            name = str(repo.get("repository"))
            url = str(repo.get("url") or "")
            if not url.startswith("https://github.com/Dossiya-SE/"):
                fail(f"unexpected repository URL in public telemetry: {name}")
            if repo.get("archived") not in {True, False}:
                fail(f"archived flag missing for repository: {name}")
            commit = repo.get("latest_commit")
            if commit is not None and not {"sha", "date", "message"}.issubset(commit):
                fail(f"latest_commit malformed for repository: {name}")


def validate_dynamic_asset() -> None:
    if not DYNAMIC_ASSET.is_file():
        fail("missing dynamic visual: assets/math-art/research-state-v1.svg")
    source, root = read_svg(DYNAMIC_ASSET)
    if root.attrib.get("viewBox") != "0 0 1920 560":
        fail("research-state-v1.svg must retain viewBox 0 0 1920 560")
    lowered = source.lower()
    if "<image" in lowered or "data:image/" in lowered:
        fail("dynamic research-state visual must remain native SVG without raster embedding")
    if "□" in source or "�" in source:
        fail("dynamic research-state visual contains a missing-glyph marker")

    visible = visible_svg_text(root)
    required_tokens = [
        "Living Research State",
        "SYSTEM COMPOSITION",
        "SEVEN-STAGE RESEARCH ARCHITECTURE",
        "PUBLIC RESEARCH TELEMETRY",
        "PROVENANCE",
        "Private repositories are excluded by construction.",
    ]
    for token in required_tokens:
        if token not in visible:
            fail(f"dynamic research-state visual missing semantic token: {token}")
    sizes = svg_text_sizes(root)
    if sizes and min(sizes) < 12:
        fail(f"dynamic research-state visual contains text below 12px; found {min(sizes)}px")


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    if spec.get("spec_id") != "DD-VISUAL-PIPELINE-001":
        fail("unexpected visual-pipeline specification")

    validate_synthetic_source()
    for name, cfg in spec["canonical_assets"].items():
        validate_asset(name, cfg)
    validate_declared_research_state()
    validate_github_state()
    validate_dynamic_asset()

    print("PROFESSIONAL MATHEMATICAL VISUAL PIPELINE: PASS")
    print("Synthetic-source provenance: PASS")
    print("Canonical V5 assets frozen and valid: PASS")
    print("Declared research-state schema: PASS")
    print("Public-only project allowlist: PASS")
    print("GitHub telemetry evidence boundary: PASS")
    print("Dynamic native SVG contract: PASS")
    print("Renderer-safe glyph markers: PASS")
    print("Canvas contracts: PASS")
    print("Minimum label-size gate: PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, KeyError, TypeError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"PROFESSIONAL MATHEMATICAL VISUAL PIPELINE: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
