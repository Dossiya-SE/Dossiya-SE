#!/usr/bin/env python3
"""Render the living research-state SVG from declared configuration + public telemetry."""

from __future__ import annotations

import json
from datetime import datetime
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA_DIR = ROOT / "data"
OUT = ROOT / "assets" / "math-art" / "research-state-v1.svg"

INK = "#111318"
MUTED = "#5F6670"
HAIR = "#D9DDE2"
SOFT = "#F7F7F5"
GOLD = "#B58A37"
GOLD2 = "#F2EAD8"
FONT = "'DejaVu Sans', Arial, Helvetica, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"


def esc(value: object) -> str:
    return escape(str(value))


def text(x: float, y: float, value: object, size: int = 18, *, anchor: str = "start", weight: str = "400", fill: str = INK, style: str = "", family: str | None = None) -> str:
    family = family or FONT
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'font-style="{style}" fill="{fill}">{esc(value)}</text>'
    )


def line(x1: float, y1: float, x2: float, y2: float, *, stroke: str = HAIR, width: float = 1.0, dash: str | None = None) -> str:
    dashed = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"{dashed}/>'


def rect(x: float, y: float, width: float, height: float, *, fill: str = "none", stroke: str = HAIR, stroke_width: float = 1.0, radius: float = 0) -> str:
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'


def circle(cx: float, cy: float, radius: float, *, fill: str = INK, stroke: str = "none", stroke_width: float = 1.0) -> str:
    return f'<circle cx="{cx}" cy="{cy}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>'


def date_label(value: object) -> str:
    if not value:
        return "—"
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00")).strftime("%d %b %Y")
    except ValueError:
        return str(value)[:10]


def load_json(name: str) -> dict[str, object]:
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))


def compact_name(value: object, limit: int = 38) -> str:
    label = str(value)
    return label if len(label) <= limit else label[: limit - 1] + "…"


def render_research_state() -> Path:
    research = load_json("research-state.json")
    framework = load_json("framework.json")
    projects = load_json("projects.json")
    github = load_json("github-state.json")

    width, height = 1920, 560
    active_stage = int(research["framework"]["active_stage"])
    stages = framework["stages"]
    physical = research["system"]["physical"]
    nonphysical = research["system"]["nonphysical"]
    telemetry = github.get("repositories", []) if github.get("status") == "live" else []

    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Living mathematical and engineering research state</title>',
        '<desc id="desc">Declared research configuration combined with an allowlisted public GitHub telemetry snapshot.</desc>',
        '<metadata>DECLARED_RESEARCH_CONFIGURATION + OBSERVED_PUBLIC_REPOSITORY_METADATA; public-only allowlist; generated deterministically from repository data.</metadata>',
        f'<style>text{{font-family:{FONT};}}</style>',
        f'<rect width="100%" height="100%" fill="#FFFFFF"/>',
        text(50, 52, "Living Research State", 38, weight="700", family=SERIF),
        text(50, 82, "mathematical configuration + public engineering telemetry", 16, style="italic", fill=MUTED),
        text(1865, 50, f"FRAMEWORK v{research['framework_version']}", 13, anchor="end", weight="700", fill=GOLD),
        text(1865, 78, str(research["research_status"]).upper(), 13, anchor="end", weight="700"),
        line(50, 105, 1870, 105),
    ]

    # System composition.
    parts += [
        text(55, 145, "SYSTEM COMPOSITION", 13, weight="700", fill=MUTED),
        text(55, 178, "Physical", 18, weight="700"),
        text(55, 207, " · ".join(str(x).title() for x in physical), 16),
        text(55, 250, "Non-physical", 18, weight="700"),
        text(55, 279, " · ".join(str(x).title() for x in nonphysical), 16),
        rect(55, 315, 490, 92, fill=SOFT, radius=10),
        text(78, 346, "Current focus", 12, weight="700", fill=MUTED),
        text(78, 378, research["current_focus"]["name"], 21, weight="700"),
        text(78, 401, research["current_focus"]["label"], 13, style="italic", fill=MUTED),
    ]

    # Seven-stage state line.
    parts += [text(610, 145, "SEVEN-STAGE RESEARCH ARCHITECTURE", 13, weight="700", fill=MUTED)]
    x_start, x_end, y = 640, 1280, 225
    parts.append(line(x_start, y, x_end, y, stroke=HAIR, width=2))
    step = (x_end - x_start) / (len(stages) - 1)
    for index, stage in enumerate(stages):
        x = x_start + index * step
        sid = int(stage["id"])
        active = sid == active_stage
        parts.append(circle(x, y, 17 if active else 12, fill=GOLD if active else "#FFFFFF", stroke=GOLD if active else INK, stroke_width=2 if active else 1.2))
        parts.append(text(x, y + 5, sid, 12, anchor="middle", weight="700", fill="#FFFFFF" if active else INK))
        parts.append(text(x, 276, compact_name(stage["name"], 21), 12, anchor="middle", weight="700" if active else "400", fill=GOLD if active else INK))
    parts += [
        rect(620, 318, 680, 88, fill=SOFT, radius=10),
        text(645, 347, "ACTIVE MATHEMATICAL OBJECT", 12, weight="700", fill=MUTED),
        text(645, 382, stages[active_stage - 1]["symbol"], 24, weight="700", fill=GOLD),
        text(710, 382, stages[active_stage - 1]["question"], 14),
    ]

    # Public GitHub telemetry.
    parts += [text(1360, 145, "PUBLIC RESEARCH TELEMETRY", 13, weight="700", fill=MUTED)]
    if telemetry:
        shown = telemetry[:4]
        for row, repo in enumerate(shown):
            yy = 183 + row * 66
            parts += [
                circle(1370, yy - 5, 4.5, fill=GOLD),
                text(1387, yy, compact_name(repo["display_name"], 37), 15, weight="700"),
                text(1387, yy + 22, f"{repo.get('language') or 'mixed'} · pushed {date_label(repo.get('pushed_at'))}", 12, fill=MUTED),
                line(1387, yy + 37, 1865, yy + 37),
            ]
    else:
        parts += [
            rect(1360, 170, 505, 180, fill=SOFT, radius=10),
            text(1385, 208, "Telemetry bootstrap", 18, weight="700"),
            text(1385, 240, "Public allowlist configured", 14),
            text(1385, 267, f"{len(projects['projects'])} research repositories", 14),
            text(1385, 302, "First live snapshot is generated by the", 13, fill=MUTED),
            text(1385, 324, "scheduled GitHub Action after release.", 13, fill=MUTED),
        ]

    generated = date_label(github.get("generated_at")) if github.get("generated_at") else "bootstrap"
    parts += [
        line(50, 455, 1870, 455),
        text(55, 490, "PROVENANCE", 12, weight="700", fill=MUTED),
        text(155, 490, "declared configuration", 13, weight="700"),
        text(330, 490, "+", 14, fill=GOLD, weight="700"),
        text(355, 490, "observed public GitHub metadata", 13, weight="700"),
        text(1865, 490, f"snapshot: {generated}", 12, anchor="end", fill=MUTED),
        text(55, 525, "Identity is stable; research state is dynamic. Private repositories are excluded by construction.", 13, style="italic", fill=MUTED),
        text(1865, 525, "fetch → validate → render → audit → publish", 13, anchor="end", weight="700", fill=GOLD),
        "</svg>\n",
    ]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"generated {OUT.relative_to(ROOT)}")
    return OUT


def main() -> int:
    render_research_state()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
