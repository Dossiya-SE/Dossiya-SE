#!/usr/bin/env python3
"""Byte-level determinism verification for SCIENTIFIC-GEOMETRY-V3.

The first build has already passed G1-G6 before this script runs. This gate
records hashes of all release-critical V3 artifacts, rebuilds them from the
governed sources, then requires byte-identical outputs.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated"
ART = ROOT / "artifacts"
PREVIEW = ART / "geometric-readme-preview"
MANIFEST = ART / "v3-determinism-manifest.json"

SVG_FILES = [
    "research-hero-light.svg",
    "research-hero-dark.svg",
    "research-question.svg",
    "coupled-network-3d-light.svg",
    "coupled-network-3d-dark.svg",
    "graph-to-viability.svg",
    "research-state-light.svg",
    "research-state-dark.svg",
    "project-system.svg",
    "research-pipeline.svg",
]

STATIC_TARGETS = [
    ROOT / "data" / "computed-geometry-v3.json",
    ART / "julia-geometry-check.toml",
    ART / "visual-layout-v3.json",
    ROOT / "mathematical-art" / "profile-geometry" / "overleaf" / "profile_geometry_v3.tex",
    *[OUT / name for name in SVG_FILES],
]

REBUILD_COMMANDS = [
    [sys.executable, "scripts/compute_scientific_geometry.py"],
    ["julia", "mathematical-art/profile-geometry/julia/verify_geometry_v3.jl"],
    [sys.executable, "scripts/render_publication_geometry.py"],
    [sys.executable, "scripts/render_geometric_readme.py"],
    [sys.executable, "scripts/validate_geometric_readme_runtime.py"],
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def targets() -> list[Path]:
    previews = sorted(PREVIEW.glob("*.png"))
    require(len(previews) == 28, f"expected 28 runtime previews, found {len(previews)}")
    all_targets = STATIC_TARGETS + previews
    missing = [str(p.relative_to(ROOT)) for p in all_targets if not p.exists()]
    require(not missing, "missing determinism targets: " + ", ".join(missing))
    return all_targets


def manifest(paths: list[Path]) -> dict[str, str]:
    return {str(p.relative_to(ROOT)): sha256(p) for p in paths}


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    first_paths = targets()
    before = manifest(first_paths)

    for command in REBUILD_COMMANDS:
        run(command)

    second_paths = targets()
    after = manifest(second_paths)

    require(set(before) == set(after), "determinism target set changed after rebuild")
    changed = {
        name: {"before": before[name], "after": after[name]}
        for name in before
        if before[name] != after[name]
    }

    report = {
        "contract_id": "SCIENTIFIC-GEOMETRY-V3",
        "hash_algorithm": "sha256",
        "target_count": len(before),
        "rebuild_count": 2,
        "status": "PASS" if not changed else "FAIL",
        "hashes": after,
        "changed": changed,
    }
    ART.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if changed:
        print("V3 DETERMINISM: FAIL — second build changed release-critical bytes.", file=sys.stderr)
        for name, pair in changed.items():
            print(f"  {name}: {pair['before']} -> {pair['after']}", file=sys.stderr)
        return 1

    print(
        f"V3 DETERMINISM: PASS — {len(before)} release-critical artifacts are "
        "byte-identical across two consecutive builds."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"V3 DETERMINISM: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
