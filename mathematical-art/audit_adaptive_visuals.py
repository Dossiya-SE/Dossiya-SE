#!/usr/bin/env python3
"""Fail-closed audit for adaptive mathematical SVG masters.

The audit checks structural/theming requirements only. It does not claim to prove
mathematical correctness or empirical validity.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets" / "math-art"

# V4 established the adaptive contract; V5 is the current public profile set;
# V6+ assets must satisfy the same structural contract before promotion.
ADAPTIVE_ASSETS = sorted(
    list(ASSET_DIR.glob("*-v4.svg"))
    + list(ASSET_DIR.glob("*-v5.svg"))
    + list(ASSET_DIR.glob("*-v6.svg"))
)

REQUIRED = {
    "title": re.compile(r"<title(?:\s|>)", re.I),
    "desc": re.compile(r"<desc(?:\s|>)", re.I),
    "viewBox": re.compile(r"viewBox\s*=", re.I),
    "theme query": re.compile(r"prefers-color-scheme\s*:\s*dark", re.I),
    "background token": re.compile(r"--bg\s*:", re.I),
    "foreground token": re.compile(r"--fg\s*:", re.I),
}

FORBIDDEN = {
    "AI-canonical wording": re.compile(r"AI[- ]generated equation.*canonical", re.I),
    "scientific invert filter": re.compile(r"filter\s*:\s*invert\(", re.I),
}


def audit_svg(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    for label, pattern in REQUIRED.items():
        if not pattern.search(text):
            failures.append(f"missing {label}")
    for label, pattern in FORBIDDEN.items():
        if pattern.search(text):
            failures.append(f"contains forbidden {label}")
    if "<svg" not in text or "</svg>" not in text:
        failures.append("invalid SVG root")
    return failures


def main() -> int:
    if not ADAPTIVE_ASSETS:
        print("FAIL: no adaptive V4+ SVG assets found")
        return 1

    failed = False
    for asset in ADAPTIVE_ASSETS:
        issues = audit_svg(asset)
        if issues:
            failed = True
            print(f"FAIL {asset.relative_to(ROOT)}: " + "; ".join(issues))
        else:
            print(f"PASS {asset.relative_to(ROOT)}")

    if failed:
        return 1

    print(f"PASS: {len(ADAPTIVE_ASSETS)} adaptive V4+ SVG asset(s) satisfy structural theme requirements.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
