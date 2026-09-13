#!/usr/bin/env python3
"""Refine generated profile visuals into a research-grade container hierarchy.

This post-render stage does not alter the scientific model. It governs how the
model is communicated in the profile:

1. one scientific question per primary container;
2. neutral surfaces dominate;
3. semantic color is sparse and role-specific;
4. red is reserved for genuine criticality/boundaries, never metadata;
5. graph/model space is visually separated from state/viability space;
6. public-repository recency is metadata, not scientific importance.

All geometry remains explanatory. No figure produced here is empirical
validation or live infrastructure telemetry.
"""

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


def write(name: str, text: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(text.rstrip() + "\n", encoding="utf-8")


def fmt_date(value: str | None) -> str:
    if not value:
        return "not observed"
    try:
        d = datetime.fromisoformat(value.replace("Z", "+00:00")).date() if "T" in value else date.fromisoformat(value)
        return d.strftime("%d %b %Y")
    except ValueError:
        return str(value)[:10]


def timestamp(value: str | None) -> float:
    if not value:
        return 0.0
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def css_vars(values: dict) -> str:
    order = [
        "bg", "panel", "ink", "muted", "line", "topology",
        "green", "green_soft", "red", "red_soft",
        "yellow", "yellow_soft", "yellow_ink", "ghost",
    ]
    return ";".join(f"--{k.replace('_','-')}:{values[k]}" for k in order)


def style(palette: dict, mode: str = "adaptive") -> str:
    light = css_vars(palette["light"])
    dark = css_vars(palette["dark"])
    root = dark if mode == "dark" else light
    media = "" if mode in {"light", "dark"} else f"@media(prefers-color-scheme:dark){{:root{{{dark}}}}}"
    return f'''<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:Georgia,"STIX Two Text","Times New Roman",serif}}
.eyebrow{{font-size:12px;font-weight:800;letter-spacing:.14em;fill:var(--muted)}}
.title{{font-size:31px;font-weight:800;letter-spacing:-.02em}}
.h{{font-size:20px;font-weight:760}} .m{{font-size:14px;fill:var(--muted)}} .s{{font-size:11px;fill:var(--muted)}}
.value{{font-size:18px;font-weight:720}} .math-lg{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:25px}}
.panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.2}}
.flow-yellow{{fill:none;stroke:var(--yellow);stroke-width:3.5;stroke-linecap:round;stroke-dasharray:9 11;animation:flow 3.2s linear infinite}}
.flow-green{{fill:none;stroke:var(--green);stroke-width:3;stroke-linecap:round;stroke-dasharray:10 12;animation:flow 3.8s linear infinite}}
.pulse-green{{animation:pulse 3.2s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.latest{{animation:latest 3.4s ease-in-out infinite}}
@keyframes flow{{to{{stroke-dashoffset:-42}}}}
@keyframes pulse{{0%,100%{{opacity:.65}}50%{{opacity:1}}}}
@keyframes latest{{0%,100%{{stroke-opacity:.35}}50%{{stroke-opacity:1}}}}
@media(prefers-reduced-motion:reduce){{.flow-yellow,.flow-green,.pulse-green,.latest{{animation:none!important}}}}
</style>'''


def svg_open(width: int, height: int, title: str, desc: str, css: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
{css}'''


def render_question(palette: dict) -> str:
    parts = [svg_open(
        1400, 330,
        "Current research question",
        "Research question for coupled Power and Transportation systems. Light yellow identifies the causal interface question and green identifies the viable-state objective. The visual is explanatory, not empirical evidence.",
        style(palette, "adaptive"),
    )]
    parts.append('<rect x="1" y="1" width="1398" height="328" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="48" y="49" class="eyebrow">RESEARCH QUESTION · CURRENT</text>')
    parts.append('<text x="48" y="94" class="title">How do physically supported infrastructure interfaces generate coupled dynamics?</text>')
    parts.append('<rect x="48" y="124" width="392" height="46" rx="12" fill="var(--yellow-soft)" stroke="var(--yellow)" stroke-width="1.5"/>')
    parts.append('<text x="68" y="153" class="h" fill="var(--yellow-ink)">Power ↔ Transportation interfaces</text>')
    parts.append('<path d="M458 147H590" class="flow-yellow"/>')
    parts.append('<text x="612" y="142" class="value">disturbance + control</text>')
    parts.append('<text x="612" y="165" class="m">time-dependent cross-system state evolution</text>')
    parts.append('<path d="M940 147H1040" stroke="var(--line)" stroke-width="2"/>')
    parts.append('<path d="M1026 137L1040 147L1026 157" fill="none" stroke="var(--line)" stroke-width="2"/>')
    parts.append('<rect x="1062" y="116" width="290" height="64" rx="14" fill="var(--panel)" stroke="var(--green)" stroke-width="2"/>')
    parts.append('<circle cx="1087" cy="148" r="7" fill="var(--green)" class="pulse-green"/>')
    parts.append('<text x="1106" y="143" class="m">viability objective</text>')
    parts.append('<text x="1106" y="166" class="math" font-size="19" fill="var(--green)">Y(t) ∈ 𝒱ₛᵤₛ(t)</text>')
    parts.append('<line x1="48" y1="211" x2="1352" y2="211" stroke="var(--line)"/>')
    parts.append('<text x="48" y="252" class="m">Engineering interpretation</text>')
    parts.append('<text x="48" y="282" class="value">Identify mechanisms → formalize coupled dynamics → quantify distance to critical boundaries → design admissible intervention.</text>')
    parts.append('<text x="1352" y="308" text-anchor="end" class="s">Question structure is declared research scope; it is not a validated causal law.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_state(state: dict, observed: dict, palette: dict, mode: str) -> str:
    repos = observed.get("repositories", [])
    active = [r for r in repos if r.get("status") == "active" and not r.get("archived")]
    featured = [r for r in active if r.get("featured")]
    focus = state["current_focus"]
    parts = [svg_open(
        1400, 360,
        "Governed living research state",
        "Minimal research-state panel. Neutral structure dominates, light yellow marks the active causal-to-dynamics transition, and green marks the active mathematical research state. No red is used for metadata.",
        style(palette, mode),
    )]
    parts.append('<rect x="1" y="1" width="1398" height="358" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<circle cx="55" cy="47" r="6" fill="var(--green)" class="pulse-green"/>')
    parts.append('<text x="74" y="52" class="eyebrow">CURRENT RESEARCH STATE</text>')
    parts.append('<text x="48" y="104" class="title">Power ↔ Transportation</text>')
    parts.append('<text x="48" y="132" class="m">Information + Organization enter only when they materially alter operation, coordination, inference or recovery.</text>')
    parts.append('<line x1="48" y1="158" x2="1352" y2="158" stroke="var(--line)"/>')

    parts.append('<text x="48" y="194" class="eyebrow">CURRENT SCIENTIFIC TRANSITION</text>')
    parts.append('<rect x="48" y="215" width="268" height="54" rx="13" class="panel"/>')
    parts.append('<text x="68" y="248" class="value">Causal Mechanisms</text>')
    parts.append('<path d="M334 242H535" class="flow-yellow"/>')
    parts.append('<rect x="554" y="215" width="410" height="54" rx="13" class="panel"/>')
    parts.append('<text x="574" y="248" class="value">Coupled Hybrid Multiscale Dynamics</text>')
    parts.append('<text x="48" y="296" class="m">physically supported interfaces → coupled state evolution under disturbance and control</text>')

    parts.append('<text x="1010" y="194" class="eyebrow">MATHEMATICAL STATE</text>')
    parts.append('<text x="1010" y="237" class="math-lg">R_phys → C → (G,I) → F_G → V → ρ_g → u*</text>')
    parts.append('<path d="M1010 261H1348" class="flow-green"/>')

    verified = fmt_date(state.get("last_verified"))
    observed_at = fmt_date(observed.get("generated_at"))
    parts.append('<line x1="48" y1="318" x2="1352" y2="318" stroke="var(--line)"/>')
    footer = f"{len(active):02d} public systems  ·  {len(featured):02d} featured  ·  state verified {verified}  ·  public evidence observed {observed_at}"
    parts.append(f'<text x="48" y="342" class="s">{escape(footer)}</text>')
    parts.append('<text x="1352" y="342" text-anchor="end" class="s">public activity cannot promote a scientific claim</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_viability(palette: dict) -> str:
    parts = [svg_open(
        1400, 500,
        "Graph to viability transformation",
        "Architectural separation of graph and model space from state and viability space. The causal interface is highlighted in ochre, admissible viability in green, and the critical boundary in red. Geometry is explanatory, not fitted data.",
        style(palette, "adaptive"),
    )]
    parts.append('<rect x="1" y="1" width="1398" height="498" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="48" y="48" class="eyebrow">GRAPH → DYNAMICS → VIABILITY → DECISION</text>')
    parts.append('<text x="48" y="84" class="m">The figure separates structural/model objects from the state-space viability geometry they induce.</text>')

    parts.append('<text x="48" y="126" class="eyebrow">GRAPH / MODEL SPACE</text>')
    boxes = [
        (48, "𝓖", "multilayer topology", "neutral"),
        (222, "𝕀", "causal interface", "yellow"),
        (396, "F𝓖", "coupled dynamics", "neutral"),
        (570, "Y(t)", "state trajectory", "neutral"),
    ]
    for i, (x, sym, lab, kind) in enumerate(boxes):
        fill = "var(--yellow-soft)" if kind == "yellow" else "var(--panel)"
        stroke = "var(--yellow)" if kind == "yellow" else "var(--line)"
        parts.append(f'<rect x="{x}" y="146" width="142" height="104" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="{1.8 if kind == "yellow" else 1.2}"/>')
        parts.append(f'<text x="{x+71}" y="190" text-anchor="middle" class="math-lg" fill="{("var(--yellow-ink)" if kind=="yellow" else "var(--ink)")}">{sym}</text>')
        parts.append(f'<text x="{x+71}" y="224" text-anchor="middle" class="s">{lab}</text>')
        if i < len(boxes)-1:
            x2 = boxes[i+1][0]
            cls = ' class="flow-yellow"' if i in {0,1} else ''
            stroke_attr = '' if cls else ' stroke="var(--line)" stroke-width="2"'
            parts.append(f'<path d="M{x+142} 198H{x2}"{cls}{stroke_attr}/>' )

    parts.append('<path d="M736 198H805" stroke="var(--line)" stroke-width="2"/>')
    parts.append('<path d="M791 188L805 198L791 208" fill="none" stroke="var(--line)" stroke-width="2"/>')

    # State / viability space: separate coordinate object, not another process node.
    x0, y0, w, h = 825, 112, 527, 318
    parts.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="20" class="panel"/>')
    parts.append(f'<text x="{x0+24}" y="{y0+32}" class="eyebrow">STATE / VIABILITY SPACE</text>')
    parts.append(f'<line x1="{x0+54}" y1="{y0+264}" x2="{x0+470}" y2="{y0+264}" stroke="var(--line)" stroke-width="1.2"/>')
    parts.append(f'<line x1="{x0+54}" y1="{y0+264}" x2="{x0+54}" y2="{y0+62}" stroke="var(--line)" stroke-width="1.2"/>')
    parts.append(f'<text x="{x0+476}" y="{y0+270}" class="s">x₁</text>')
    parts.append(f'<text x="{x0+42}" y="{y0+55}" class="s">x₂</text>')

    # Viability region and nested level geometry.
    region = "M900 329C907 244 965 185 1055 175C1152 164 1242 199 1289 270C1311 304 1292 355 1235 379C1166 408 1063 397 986 382C931 371 896 356 900 329Z"
    inner = "M939 320C949 260 995 219 1062 211C1132 202 1204 228 1243 277C1262 300 1245 334 1203 350C1151 370 1078 365 1022 354C979 346 935 340 939 320Z"
    parts.append(f'<path d="{region}" fill="var(--green-soft)" stroke="var(--green)" stroke-width="2.2" opacity=".9"/>')
    parts.append(f'<path d="{inner}" fill="none" stroke="var(--green)" stroke-width="1.2" opacity=".35"/>')
    parts.append(f'<path d="{region}" fill="none" stroke="var(--red)" stroke-width="3" stroke-dasharray="9 8" opacity=".9"/>')
    parts.append('<text x="1187" y="203" class="math" font-size="18" fill="var(--red)">∂𝒱</text>')
    parts.append('<text x="1120" y="338" class="math" font-size="21" fill="var(--green)">𝒱ₛᵤₛ</text>')

    # State, resilience margin and control.
    parts.append('<circle cx="1048" cy="292" r="9" fill="var(--green)" class="pulse-green"/>')
    parts.append('<text x="1064" y="297" class="math" font-size="17">Y(t)</text>')
    parts.append('<path d="M1057 286L1212 225" stroke="var(--red)" stroke-width="2.4" stroke-dasharray="6 6"/>')
    parts.append('<text x="1128" y="246" class="math" font-size="17" fill="var(--red)">ρ_g</text>')
    parts.append('<path d="M1058 301Q1105 337 1174 329" class="flow-yellow"/>')
    parts.append('<polygon points="1190,317 1195,327 1206,329 1198,337 1200,349 1190,343 1180,349 1182,337 1174,329 1185,327" fill="var(--yellow-soft)" stroke="var(--yellow)" stroke-width="2"/>')
    parts.append('<text x="1212" y="340" class="math" font-size="18" fill="var(--yellow-ink)">u*</text>')

    parts.append('<line x1="48" y1="286" x2="746" y2="286" stroke="var(--line)"/>')
    parts.append('<text x="48" y="323" class="math" font-size="18">Ẏ = F_𝒢(Y,u,η;θ)</text>')
    parts.append('<text x="48" y="359" class="math" font-size="18" fill="var(--green)">Y(t) ∈ 𝒱ₛᵤₛ(t)</text>')
    parts.append('<text x="48" y="395" class="math" font-size="18" fill="var(--red)">ρ_g(Y) = d_g(Y,∂𝒱)</text>')
    parts.append('<text x="48" y="445" class="m">Structural topology constrains dynamics; viability encodes admissible operation; the margin measures proximity to a critical boundary; control selects an admissible intervention.</text>')
    parts.append('<text x="1352" y="474" text-anchor="end" class="s">No empirical validity is implied by the geometry alone.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_projects(observed: dict, palette: dict) -> str:
    repos = [r for r in observed.get("repositories", []) if r.get("status") == "active" and not r.get("archived")]
    featured = sorted([r for r in repos if r.get("featured")], key=lambda r: int(r.get("profile_order", 99)))[:4]
    recent = max(repos, key=lambda r: timestamp((r.get("latest_commit") or {}).get("date") or r.get("pushed_at"))) if repos else None
    parts = [svg_open(
        1400, 510,
        "Featured public research systems",
        "Four featured public research systems shown in neutral research cards. Green indicates active public status. A light-yellow metadata cue identifies the most recent public repository change without implying scientific importance or validity.",
        style(palette, "adaptive"),
    )]
    parts.append('<rect x="1" y="1" width="1398" height="508" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="48" y="48" class="eyebrow">FEATURED RESEARCH SYSTEMS</text>')
    parts.append(f'<text x="48" y="79" class="m">four research-facing public systems · observed {escape(fmt_date(observed.get("generated_at")))}</text>')

    for idx, repo in enumerate(featured):
        col, row = idx % 2, idx // 2
        x, y = 48 + col * 662, 112 + row * 158
        parts.append(f'<rect x="{x}" y="{y}" width="628" height="132" rx="17" class="panel research-card"/>')
        parts.append(f'<circle cx="{x+24}" cy="{y+27}" r="5.5" fill="var(--green)"/>')
        parts.append(f'<text x="{x+42}" y="{y+32}" class="h">{escape(str(repo.get("short_name", repo.get("repository", "research system"))))}</text>')
        role = str(repo.get("research_role", ""))
        words = role.split()
        line1 = " ".join(words[:10])
        line2 = " ".join(words[10:20])
        parts.append(f'<text x="{x+24}" y="{y+65}" class="m">{escape(line1)}</text>')
        if line2:
            parts.append(f'<text x="{x+24}" y="{y+87}" class="m">{escape(line2)}</text>')
        latest = fmt_date((repo.get("latest_commit") or {}).get("date") or repo.get("pushed_at"))
        lang = repo.get("language") or "mixed / unspecified"
        parts.append(f'<text x="{x+24}" y="{y+114}" class="s">{escape(str(lang))} · latest public commit {escape(latest)}</text>')

    recent_name = str((recent or {}).get("short_name") or (recent or {}).get("repository") or "not observed")
    parts.append('<line x1="48" y1="442" x2="1352" y2="442" stroke="var(--line)"/>')
    parts.append('<rect x="48" y="459" width="206" height="28" rx="8" fill="var(--yellow-soft)" stroke="var(--yellow)" class="latest"/>')
    parts.append('<text x="61" y="478" class="eyebrow" fill="var(--yellow-ink)">MOST RECENT PUBLIC CHANGE</text>')
    parts.append(f'<text x="275" y="478" class="s">{escape(recent_name)} · recency is metadata, not scientific importance or validation.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def main() -> int:
    palette = load("visual-palette.json")
    state = load("research-state.json")
    observed = load("public-github-state.json")

    write("research-question.svg", render_question(palette))
    write("research-state-light.svg", render_state(state, observed, palette, "light"))
    write("research-state-dark.svg", render_state(state, observed, palette, "dark"))
    write("graph-to-viability.svg", render_viability(palette))
    write("project-system.svg", render_projects(observed, palette))

    print("Refined profile containers: question, research state, graph-to-viability and featured research systems.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
