#!/usr/bin/env python3
"""Fail-closed validation for LIGHT-SKY-BLUE-ACCENT-V1 across governed profile surfaces."""

from __future__ import annotations

import colorsys
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE = ROOT / "data" / "visual-palette.json"
CONTRACT = ROOT / "ACCENT_CONTRACT_V1.md"

TEXT_SUFFIXES = {
    ".css", ".html", ".js", ".mjs", ".ts", ".tsx", ".jsx", ".json",
    ".md", ".py", ".svg", ".tex", ".toml", ".yml", ".yaml",
}
SCAN_ROOTS = (
    ROOT / "README.md",
    ROOT / "data",
    ROOT / "scripts",
    ROOT / "assets",
    ROOT / "mathematical-art",
)
EXCLUDED = {
    Path("scripts/validate_accent_contract.py"),
}

FORBIDDEN_EXACT = {
    "#ffd700", "#ffc107", "#ffb300", "#e0a800", "#d4af37", "#c99700",
    "#f4c430", "#daa520", "#b8860b", "#ffc94a", "#f59e0b", "#eab308",
    "#9a6700", "#d5ad47", "#d2a63c", "#d29922", "#b45309", "#a16207",
    "#f4c95d", "#fbbf24", "#facc15", "#fde68a",
}

HEX_RE = re.compile(r"(?<![0-9A-Za-z])#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})(?![0-9A-Fa-f])")
RGB_RE = re.compile(
    r"rgba?\(\s*(\d{1,3})\s*(?:,|\s)\s*(\d{1,3})\s*(?:,|\s)\s*(\d{1,3})",
    re.IGNORECASE,
)
TIKZ_RGB_RE = re.compile(
    r"\\definecolor\{[^}]+\}\{RGB\}\{\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\}",
    re.IGNORECASE,
)
SEMANTIC_RE = re.compile(
    r"--(?:gold|amber|ochre|yellow-gold|warm-accent|warning-gold|accent-gold)\b"
    r"|\b(?:accent[_-]?gold|warning[_-]?gold|warm[_-]?accent)\b"
    r"|(?:fill|stroke)\s*=\s*[\"'](?:gold|goldenrod|darkgoldenrod|amber|ochre)[\"']",
    re.IGNORECASE,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    rf, gf, bf = r / 255, g / 255, b / 255
    h, l, s = colorsys.rgb_to_hls(rf, gf, bf)
    return h * 360.0, s, l


def warm_family(r: int, g: int, b: int) -> bool:
    h, s, l = hsl(r, g, b)
    return 32.0 <= h <= 72.0 and s >= 0.45 and 0.18 <= l <= 0.90


def expand_hex(value: str) -> str:
    value = value.lower()
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    return "#" + value


def iter_files() -> list[Path]:
    files: set[Path] = set()
    for root in SCAN_ROOTS:
        if root.is_file():
            files.add(root)
            continue
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                files.add(path)
    return sorted(files)


def validate_contract() -> None:
    require(CONTRACT.exists(), "ACCENT_CONTRACT_V1.md is missing")
    contract = CONTRACT.read_text(encoding="utf-8")
    for marker in (
        "LIGHT-SKY-BLUE-ACCENT-V1",
        "RGB(135, 206, 250)",
        "RGB(0, 191, 255)",
        "#2D8FD6",
        "#2878CD",
        "#BFE8FF",
    ):
        require(marker in contract, f"accent contract missing marker: {marker}")

    palette = json.loads(PALETTE.read_text(encoding="utf-8"))
    accent = palette.get("accent_contract", {})
    require(accent.get("contract_id") == "LIGHT-SKY-BLUE-ACCENT-V1", "palette contract id mismatch")
    require(accent.get("primary", {}).get("rgb") == [135, 206, 250], "primary accent RGB mismatch")
    require(accent.get("primary", {}).get("hex") == "#87CEFA", "primary accent hex mismatch")
    require(accent.get("strong", {}).get("rgb") == [0, 191, 255], "strong accent RGB mismatch")
    require(accent.get("strong", {}).get("hex") == "#00BFFF", "strong accent hex mismatch")
    require(accent.get("glow") == "rgba(0,191,255,0.28)", "glow token mismatch")
    require(accent.get("border") == "rgba(135,206,250,0.55)", "border token mismatch")


def scan_file(path: Path) -> list[str]:
    rel = path.relative_to(ROOT)
    if rel in EXCLUDED:
        return []
    text = path.read_text(encoding="utf-8")
    failures: list[str] = []

    semantic = SEMANTIC_RE.search(text)
    if semantic:
        failures.append(f"legacy semantic token {semantic.group(0)!r}")

    for match in HEX_RE.finditer(text):
        literal = expand_hex(match.group(1))
        if literal.lower() in FORBIDDEN_EXACT:
            failures.append(f"forbidden literal {literal}")
            continue
        r, g, b = (int(literal[i:i+2], 16) for i in (1, 3, 5))
        if warm_family(r, g, b):
            failures.append(f"warm hue literal {literal} -> RGB({r},{g},{b})")

    for regex in (RGB_RE, TIKZ_RGB_RE):
        for match in regex.finditer(text):
            r, g, b = map(int, match.groups()[:3])
            if any(v > 255 for v in (r, g, b)):
                continue
            if warm_family(r, g, b):
                failures.append(f"warm RGB literal RGB({r},{g},{b})")

    return sorted(set(failures))


def main() -> int:
    validate_contract()
    failures: list[str] = []
    files = iter_files()
    for path in files:
        issues = scan_file(path)
        for issue in issues:
            failures.append(f"{path.relative_to(ROOT)}: {issue}")

    if failures:
        raise ValueError(
            "LIGHT-SKY-BLUE-ACCENT-V1 violations:\n  - " + "\n  - ".join(failures)
        )

    print(
        "ACCENT CONTRACT VALIDATION: PASS — "
        f"{len(files)} governed text surfaces scanned; "
        "Light Sky Blue / Deep Sky Blue contract is canonical and no gold-family hue or semantic token is present."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ACCENT CONTRACT VALIDATION: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
