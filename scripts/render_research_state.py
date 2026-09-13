#!/usr/bin/env python3
"""Render deterministic SVG assets for the living research profile."""

from __future__ import annotations

import json
from datetime import date, datetime
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def write(name: str, content: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(content.rstrip() + "\n", encoding="utf-8")


def fmt_date(value: str | None) -> str:
    if not value:
        return "not observed"
    try:
        if "T" in value:
            d = datetime.fromisoformat(value.replace("Z", "+00:00")).date()
        else:
            d = date.fromisoformat(value)
        return d.strftime("%d %b %Y")
    except ValueError:
        return value[:10]


def svg_open(width: int, height: int, title: str, desc: str, style: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
{style}'''


def render_state(state: dict, observed: dict, *, dark: bool) -> str:
    if dark:
        bg, panel, ink, muted, line, gold, blue, soft = "#0d1117", "#111820", "#f0f3f6", "#9ba5b0", "#30363d", "#d2a63c", "#72a7ff", "#161d26"
    else:
        bg, panel, ink, muted, line, gold, blue, soft = "#fffdfa", "#ffffff", "#0d1117", "#57606a", "#d8d3c8", "#9a6700", "#2f6fda", "#f4f1e8"

    repos = observed.get("repositories", [])
    active = [r for r in repos if r.get("status") == "active" and not r.get("archived")]
    featured = [r for r in active if r.get("featured")]
    verified = fmt_date(state.get("last_verified"))
    observed_at = fmt_date(observed.get("generated_at"))
    focus = state["current_focus"]

    style = f'''<style>
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:{ink}}}
.k{{font-size:14px;font-weight:800;letter-spacing:.12em}} .h{{font-size:30px;font-weight:800}}
.m{{font-size:17px;fill:{muted}}} .v{{font-size:21px;font-weight:750}} .s{{font-size:14px;fill:{muted}}}
.math{{font-family:Georgia,"Times New Roman",serif;font-size:22px}}
</style>'''
    parts = [svg_open(1400, 560, "Current research state", "Generated profile panel showing the current Power–Transportation research configuration, active formal stages, mathematical objects, and observed public research evidence.", style)]
    parts.append(f'<rect x="1" y="1" width="1398" height="558" rx="30" fill="{bg}" stroke="{line}"/>')
    parts.append(f'<rect x="34" y="34" width="1332" height="492" rx="24" fill="{panel}" stroke="{line}"/>')
    parts.append(f'<text x="70" y="80" class="k" fill="{gold}">CURRENT RESEARCH STATE</text>')
    parts.append('<text x="70" y="122" class="h">Living profile · governed scientific state</text>')
    parts.append(f'<text x="70" y="153" class="m">Declared research configuration + observed public repository evidence</text>')

    # left column
    y = 208
    entries = [
        ("PRIMARY PHYSICAL SYSTEM", "POWER  ⇄  TRANSPORTATION", gold),
        ("SUPPORTING NON-PHYSICAL LAYERS", "INFORMATION  ·  ORGANIZATION", ink),
        ("CURRENT FORMAL TRANSITION", focus["transition"], blue),
        ("CURRENT QUESTION", focus["question"], ink),
    ]
    for label, value, color in entries:
        parts.append(f'<text x="70" y="{y}" class="k" fill="{muted}">{escape(label)}</text>')
        if label == "CURRENT QUESTION":
            words = value.split()
            line1 = " ".join(words[:11])
            line2 = " ".join(words[11:])
            parts.append(f'<text x="70" y="{y+30}" class="v" fill="{color}">{escape(line1)}</text>')
            parts.append(f'<text x="70" y="{y+57}" class="v" fill="{color}">{escape(line2)}</text>')
            y += 100
        else:
            parts.append(f'<text x="70" y="{y+31}" class="v" fill="{color}">{escape(value)}</text>')
            y += 76

    # divider and right column
    parts.append(f'<line x1="820" y1="184" x2="820" y2="486" stroke="{line}"/>')
    parts.append(f'<text x="870" y="208" class="k" fill="{muted}">MATHEMATICAL OBJECTS</text>')
    parts.append(f'<text x="870" y="248" class="math" fill="{blue}">R_phys · C · G · I_ij · F_G · V · rho_g · u*</text>')

    parts.append(f'<rect x="870" y="282" width="216" height="96" rx="18" fill="{soft}" stroke="{line}"/>')
    parts.append(f'<text x="892" y="315" class="k" fill="{muted}">PUBLIC SYSTEMS</text>')
    parts.append(f'<text x="892" y="356" class="h" fill="{ink}">{len(active):02d}</text>')
    parts.append(f'<text x="948" y="354" class="s">active allowlisted</text>')

    parts.append(f'<rect x="1104" y="282" width="216" height="96" rx="18" fill="{soft}" stroke="{line}"/>')
    parts.append(f'<text x="1126" y="315" class="k" fill="{muted}">FEATURED SYSTEMS</text>')
    parts.append(f'<text x="1126" y="356" class="h" fill="{gold}">{len(featured):02d}</text>')
    parts.append(f'<text x="1182" y="354" class="s">research-facing</text>')

    parts.append(f'<text x="870" y="426" class="k" fill="{muted}">STATE LAST VERIFIED</text>')
    parts.append(f'<text x="870" y="456" class="v">{escape(verified)}</text>')
    parts.append(f'<text x="1104" y="426" class="k" fill="{muted}">PUBLIC EVIDENCE OBSERVED</text>')
    parts.append(f'<text x="1104" y="456" class="v">{escape(observed_at)}</text>')
    parts.append(f'<text x="870" y="500" class="s">DECLARED ≠ OBSERVED ≠ VERIFIED COMPUTATION ≠ EMPIRICALLY VALIDATED</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_pipeline(state: dict, framework: dict) -> str:
    stages = framework["stages"]
    active = set(state["current_focus"]["active_stages"])
    style = '''<style>
:root{--bg:#fffdfa;--ink:#0d1117;--muted:#57606a;--line:#d8d3c8;--gold:#9a6700;--blue:#2f6fda;--soft:#f4f1e8}
@media(prefers-color-scheme:dark){:root{--bg:#0d1117;--ink:#f0f3f6;--muted:#9ba5b0;--line:#30363d;--gold:#d2a63c;--blue:#72a7ff;--soft:#161d26}}
text{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}
.k{font-size:13px;font-weight:800;letter-spacing:.1em}.n{font-size:15px;font-weight:750}.s{font-size:12px;fill:var(--muted)}
</style>'''
    parts = [svg_open(1400, 430, "Dynamic seven-stage research pipeline", "Formal seven-stage research architecture with the currently active transition highlighted from causal mechanisms to coupled dynamics.", style)]
    parts.append('<rect x="1" y="1" width="1398" height="428" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="54" y="58" class="k" fill="var(--gold)">FORMAL RESEARCH PIPELINE</text>')
    parts.append('<text x="54" y="88" class="s">Physical grounding constrains the formal architecture; highlighted stages are the current research transition.</text>')
    x0, y0, w, gap = 54, 132, 174, 18
    for index, stage in enumerate(stages):
        x = x0 + index * (w + gap)
        sid = int(stage["id"])
        if sid == 2:
            stroke, fill = "var(--gold)", "var(--soft)"
        elif sid == 3:
            stroke, fill = "var(--blue)", "var(--soft)"
        else:
            stroke, fill = "var(--line)", "var(--bg)"
        parts.append(f'<rect x="{x}" y="{y0}" width="{w}" height="162" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="{2.5 if sid in active else 1.2}"/>')
        parts.append(f'<text x="{x+18}" y="{y0+30}" class="k" fill="{stroke}">0{sid}</text>')
        label = stage["display_label"]
        words = label.split()
        if len(words) <= 2:
            line1, line2 = label, ""
        else:
            split = max(1, len(words)//2)
            line1, line2 = " ".join(words[:split]), " ".join(words[split:])
        parts.append(f'<text x="{x+18}" y="{y0+69}" class="n">{escape(line1)}</text>')
        if line2:
            parts.append(f'<text x="{x+18}" y="{y0+91}" class="n">{escape(line2)}</text>')
        parts.append(f'<text x="{x+18}" y="{y0+132}" class="s">{escape(stage["symbol"])}</text>')
        if index < len(stages)-1:
            parts.append(f'<path d="M{x+w+4} {y0+81}H{x+w+gap-4}" stroke="var(--muted)" stroke-width="1.4"/>')
    parts.append('<text x="54" y="346" class="k" fill="var(--muted)">CURRENT TRANSITION</text>')
    parts.append(f'<text x="54" y="380" class="n" fill="var(--gold)">{escape(state["current_focus"]["transition"])}</text>')
    parts.append('<text x="54" y="406" class="s">Stage highlight reports research configuration only; it is not a claim of completion or empirical validation.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_projects(observed: dict) -> str:
    repos = sorted(observed["repositories"], key=lambda item: int(item["profile_order"]))
    style = '''<style>
:root{--bg:#fffdfa;--ink:#0d1117;--muted:#57606a;--line:#d8d3c8;--gold:#9a6700;--blue:#2f6fda;--soft:#f4f1e8}
@media(prefers-color-scheme:dark){:root{--bg:#0d1117;--ink:#f0f3f6;--muted:#9ba5b0;--line:#30363d;--gold:#d2a63c;--blue:#72a7ff;--soft:#161d26}}
text{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}
.k{font-size:13px;font-weight:800;letter-spacing:.1em}.h{font-size:20px;font-weight:800}.m{font-size:14px;fill:var(--muted)}.s{font-size:12px;fill:var(--muted)}
</style>'''
    parts = [svg_open(1400, 650, "Observed public research systems", "Dynamic evidence panel listing the explicitly allowlisted public research repositories and their latest observed public activity.", style)]
    parts.append('<rect x="1" y="1" width="1398" height="648" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="54" y="58" class="k" fill="var(--gold)">OBSERVED PUBLIC RESEARCH SYSTEMS</text>')
    parts.append(f'<text x="54" y="88" class="m">GitHub REST API · allowlist only · observed {escape(fmt_date(observed.get("generated_at")))}</text>')
    for idx, repo in enumerate(repos):
        col, row = idx % 3, idx // 3
        x, y = 54 + col * 438, 126 + row * 238
        featured = bool(repo.get("featured"))
        stroke = "var(--gold)" if featured else "var(--line)"
        parts.append(f'<rect x="{x}" y="{y}" width="408" height="206" rx="20" fill="var(--soft)" stroke="{stroke}" stroke-width="{2 if featured else 1}"/>')
        parts.append(f'<text x="{x+22}" y="{y+33}" class="k" fill="{stroke}">0{int(repo["profile_order"])} · {"FEATURED" if featured else "SUPPORTING"}</text>')
        parts.append(f'<text x="{x+22}" y="{y+70}" class="h">{escape(str(repo["short_name"]))}</text>')
        role = str(repo.get("research_role", ""))
        words = role.split()
        parts.append(f'<text x="{x+22}" y="{y+101}" class="m">{escape(" ".join(words[:7]))}</text>')
        parts.append(f'<text x="{x+22}" y="{y+124}" class="m">{escape(" ".join(words[7:14]))}</text>')
        language = repo.get("language") or "mixed / unspecified"
        commit = repo.get("latest_commit") or {}
        latest = fmt_date(commit.get("date") or repo.get("pushed_at"))
        parts.append(f'<text x="{x+22}" y="{y+164}" class="s">{escape(str(language))} · latest public commit {escape(latest)}</text>')
        parts.append(f'<text x="{x+22}" y="{y+188}" class="s">visibility: public · status: {escape(str(repo.get("status")))}</text>')
    parts.append('<text x="54" y="620" class="s">Public activity is evidence of repository state, not evidence that a scientific mechanism is empirically validated.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def main() -> int:
    state = load("research-state.json")
    framework = load("framework.json")
    observed = load("public-github-state.json")
    write("research-state-light.svg", render_state(state, observed, dark=False))
    write("research-state-dark.svg", render_state(state, observed, dark=True))
    write("research-pipeline.svg", render_pipeline(state, framework))
    write("project-system.svg", render_projects(observed))
    print("Rendered deterministic living-profile SVG assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
