#!/usr/bin/env python3
"""Render deterministic, self-contained animated SVG assets for the living research profile.

Motion is semantic rather than decorative:
- gold moving dashes = causal/interface transfer;
- blue moving dashes = mathematical state evolution;
- stage 2 -> 3 motion = declared active research transition;
- pulsing project border = most recently observed public repository change.

No JavaScript is embedded. CSS animations are disabled for prefers-reduced-motion.
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


def timestamp(value: str | None) -> float:
    if not value:
        return 0.0
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def svg_open(width: int, height: int, title: str, desc: str, style: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
{style}'''


def base_style(*, dark: bool | None = None) -> str:
    if dark is True:
        root = "--bg:#0d1117;--panel:#111820;--ink:#f0f3f6;--muted:#9ba5b0;--line:#30363d;--gold:#d2a63c;--blue:#72a7ff;--soft:#161d26"
        media = ""
    elif dark is False:
        root = "--bg:#fffdfa;--panel:#ffffff;--ink:#0d1117;--muted:#57606a;--line:#d8d3c8;--gold:#9a6700;--blue:#2f6fda;--soft:#f4f1e8"
        media = ""
    else:
        root = "--bg:#fffdfa;--panel:#ffffff;--ink:#0d1117;--muted:#57606a;--line:#d8d3c8;--gold:#9a6700;--blue:#2f6fda;--soft:#f4f1e8"
        media = '@media(prefers-color-scheme:dark){:root{--bg:#0d1117;--panel:#111820;--ink:#f0f3f6;--muted:#9ba5b0;--line:#30363d;--gold:#d2a63c;--blue:#72a7ff;--soft:#161d26}}'
    return f'''<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.k{{font-size:13px;font-weight:800;letter-spacing:.11em}} .h{{font-size:28px;font-weight:800}} .v{{font-size:20px;font-weight:750}}
.m{{font-size:15px;fill:var(--muted)}} .s{{font-size:12px;fill:var(--muted)}} .math{{font-family:Georgia,"Times New Roman",serif;font-size:21px}}
.flow-gold{{stroke:var(--gold);stroke-dasharray:10 12;animation:flowGold 2.8s linear infinite}}
.flow-blue{{stroke:var(--blue);stroke-dasharray:9 12;animation:flowBlue 3.4s linear infinite}}
.pulse-gold{{animation:pulseGold 2.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.pulse-blue{{animation:pulseBlue 2.8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.latest{{animation:latestPulse 3.2s ease-in-out infinite}}
@keyframes flowGold{{to{{stroke-dashoffset:-44}}}}
@keyframes flowBlue{{to{{stroke-dashoffset:-42}}}}
@keyframes pulseGold{{0%,100%{{opacity:.48;transform:scale(.96)}}50%{{opacity:1;transform:scale(1.04)}}}}
@keyframes pulseBlue{{0%,100%{{opacity:.58;transform:scale(.97)}}50%{{opacity:1;transform:scale(1.03)}}}}
@keyframes latestPulse{{0%,100%{{stroke-opacity:.42}}50%{{stroke-opacity:1}}}}
@media(prefers-reduced-motion:reduce){{.flow-gold,.flow-blue,.pulse-gold,.pulse-blue,.latest{{animation:none!important}}}}
</style>'''


def render_hero(state: dict, observed: dict, *, dark: bool) -> str:
    focus = state["current_focus"]
    observed_at = fmt_date(observed.get("generated_at"))
    style = base_style(dark=dark)
    parts = [svg_open(
        1400,
        570,
        "Dossiya Dakou — animated physics-to-mathematics research system",
        "Semantic animated SVG showing coupled Power and Transportation infrastructure, causal-interface transfer, mathematical state evolution, viability geometry, and engineering decision. Motion is schematic and not an empirical measurement.",
        style,
    )]
    parts.append('<rect x="1" y="1" width="1398" height="568" rx="30" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="58" y="62" class="k" fill="var(--gold)">PHYSICS-GROUNDED MATHEMATICAL ENGINEERING</text>')
    parts.append('<text x="58" y="108" class="h">Physical reality → causality → mathematical structure → engineering decision</text>')
    parts.append(f'<text x="58" y="140" class="m">Current formal transition: {escape(focus["transition"])} · public evidence observed {escape(observed_at)}</text>')

    # Physical system: power network.
    parts.append('<g transform="translate(70 205)">')
    parts.append('<text x="0" y="0" class="k">POWER</text>')
    lines = [(10,55,116,22),(116,22,222,58),(116,22,128,120),(128,120,235,128),(222,58,235,128)]
    for x1,y1,x2,y2 in lines:
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="var(--ink)" stroke-width="2"/>')
    for x,y in [(10,55),(116,22),(222,58),(128,120),(235,128)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="8" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>')
    parts.append('<path d="M11 55L116 22L222 58" fill="none" class="flow-gold" stroke-width="4" stroke-linecap="round"/>')
    parts.append('<text x="0" y="168" class="s">generation · grid · charging supply</text>')
    parts.append('</g>')

    # Physical system: transport network.
    parts.append('<g transform="translate(70 405)">')
    parts.append('<text x="0" y="0" class="k">TRANSPORTATION</text>')
    parts.append('<path d="M8 56C78 2 164 14 238 58S350 111 430 64" fill="none" stroke="var(--ink)" stroke-width="2"/>')
    parts.append('<path d="M18 102C118 142 207 105 298 129S394 154 440 118" fill="none" stroke="var(--ink)" stroke-width="2"/>')
    parts.append('<path d="M8 56C78 2 164 14 238 58S350 111 430 64" fill="none" class="flow-gold" stroke-width="4" stroke-linecap="round"/>')
    for x,y in [(8,56),(135,26),(238,58),(298,129),(430,64),(440,118)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>')
    parts.append('</g>')

    # Bidirectional causal interface, motion means possible transfer, not measured magnitude.
    parts.append('<g transform="translate(420 224)">')
    parts.append('<text x="0" y="0" class="k" fill="var(--gold)">CAUSAL INTERFACE</text>')
    parts.append('<path d="M70 34V216" fill="none" class="flow-gold" stroke-width="4"/>')
    parts.append('<path d="M47 58L70 34L93 58M47 192L70 216L93 192" fill="none" stroke="var(--gold)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    parts.append('<circle cx="70" cy="125" r="15" fill="var(--gold)" class="pulse-gold"/>')
    parts.append('<text x="106" y="111" class="math" fill="var(--gold)">I<tspan baseline-shift="sub" font-size="12">PT</tspan></text>')
    parts.append('<text x="106" y="140" class="s">mechanism · sign · delay</text>')
    parts.append('</g>')

    # Mathematical state-space geometry.
    parts.append('<line x1="624" y1="182" x2="624" y2="524" stroke="var(--line)"/>')
    parts.append('<g transform="translate(690 205)">')
    parts.append('<text x="0" y="0" class="k" fill="var(--blue)">MATHEMATICAL STATE</text>')
    parts.append('<text x="0" y="29" class="s">schematic state-space trajectory constrained by engineering admissibility</text>')
    parts.append('<path d="M35 112C120 37 284 45 369 128C438 195 422 305 330 346C233 390 96 360 42 271C4 208 7 144 35 112Z" fill="var(--soft)" stroke="var(--blue)" stroke-width="2"/>')
    parts.append('<path d="M86 302C132 254 160 213 202 194C247 174 286 193 296 231C307 272 266 294 225 278C197 267 187 239 200 215" fill="none" stroke="var(--blue)" stroke-width="2.4" opacity=".30"/>')
    parts.append('<path d="M86 302C132 254 160 213 202 194C247 174 286 193 296 231C307 272 266 294 225 278C197 267 187 239 200 215" fill="none" class="flow-blue" stroke-width="4" stroke-linecap="round"/>')
    parts.append('<circle cx="200" cy="215" r="9" fill="var(--blue)" class="pulse-blue"/>')
    parts.append('<line x1="200" y1="215" x2="88" y2="176" stroke="var(--gold)" stroke-width="2" stroke-dasharray="5 7"/>')
    parts.append('<text x="42" y="169" class="math" fill="var(--gold)">ρ<tspan baseline-shift="sub" font-size="12">g</tspan></text>')
    parts.append('<text x="334" y="116" class="math" fill="var(--blue)">∂V</text>')
    parts.append('<text x="105" y="332" class="math">Y(t)</text>')
    parts.append('<text x="298" y="338" class="s">viable region</text>')
    parts.append('<path d="M438 226H554" class="flow-gold" stroke-width="3"/>')
    parts.append('<text x="456" y="211" class="k" fill="var(--gold)">DECISION</text>')
    parts.append('<text x="474" y="263" class="math" fill="var(--gold)">u*</text>')
    parts.append('</g>')

    parts.append('<text x="58" y="548" class="s">Motion encodes schematic causal transfer and state evolution; it is not a measured flow, calibrated trajectory, or empirical validation claim.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_state(state: dict, observed: dict, *, dark: bool) -> str:
    repos = observed.get("repositories", [])
    active = [r for r in repos if r.get("status") == "active" and not r.get("archived")]
    featured = [r for r in active if r.get("featured")]
    verified = fmt_date(state.get("last_verified"))
    observed_at = fmt_date(observed.get("generated_at"))
    focus = state["current_focus"]
    style = base_style(dark=dark)
    parts = [svg_open(
        1400,
        560,
        "Current animated research state",
        "Generated panel showing Power–Transportation research configuration, active formal transition, mathematical objects, and observed public research evidence. The live indicator is visual status only.",
        style,
    )]
    parts.append('<rect x="1" y="1" width="1398" height="558" rx="30" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<rect x="34" y="34" width="1332" height="492" rx="24" fill="var(--panel)" stroke="var(--line)"/>')
    parts.append('<circle cx="1315" cy="72" r="7" fill="var(--gold)" class="pulse-gold"/>')
    parts.append('<text x="1288" y="77" text-anchor="end" class="k" fill="var(--gold)">LIVING STATE</text>')
    parts.append('<text x="70" y="80" class="k" fill="var(--gold)">CURRENT RESEARCH STATE</text>')
    parts.append('<text x="70" y="122" class="h">Governed scientific state</text>')
    parts.append('<text x="70" y="153" class="m">Declared research configuration + observed public repository evidence</text>')

    y = 208
    entries = [
        ("PRIMARY PHYSICAL SYSTEM", "POWER  ⇄  TRANSPORTATION", "var(--gold)"),
        ("SUPPORTING NON-PHYSICAL LAYERS", "INFORMATION  ·  ORGANIZATION", "var(--ink)"),
        ("CURRENT FORMAL TRANSITION", focus["transition"], "var(--blue)"),
        ("CURRENT QUESTION", focus["question"], "var(--ink)"),
    ]
    for label, value, color in entries:
        parts.append(f'<text x="70" y="{y}" class="k" fill="var(--muted)">{escape(label)}</text>')
        if label == "PRIMARY PHYSICAL SYSTEM":
            parts.append(f'<text x="70" y="{y+31}" class="v" fill="{color}">POWER</text>')
            parts.append(f'<line x1="168" y1="{y+24}" x2="304" y2="{y+24}" class="flow-gold" stroke-width="3"/>')
            parts.append(f'<text x="329" y="{y+31}" class="v" fill="{color}">TRANSPORTATION</text>')
            y += 76
        elif label == "CURRENT QUESTION":
            words = value.split()
            line1 = " ".join(words[:11])
            line2 = " ".join(words[11:])
            parts.append(f'<text x="70" y="{y+30}" class="v" fill="{color}">{escape(line1)}</text>')
            parts.append(f'<text x="70" y="{y+57}" class="v" fill="{color}">{escape(line2)}</text>')
            y += 100
        else:
            parts.append(f'<text x="70" y="{y+31}" class="v" fill="{color}">{escape(value)}</text>')
            y += 76

    parts.append('<line x1="820" y1="184" x2="820" y2="486" stroke="var(--line)"/>')
    parts.append('<text x="870" y="208" class="k" fill="var(--muted)">MATHEMATICAL OBJECTS</text>')
    parts.append('<text x="870" y="248" class="math" fill="var(--blue)">R_phys · C · G · I_ij · F_G · V · rho_g · u*</text>')
    parts.append('<path d="M872 265H1260" class="flow-blue" stroke-width="2"/>')

    parts.append('<rect x="870" y="282" width="216" height="96" rx="18" fill="var(--soft)" stroke="var(--line)"/>')
    parts.append('<text x="892" y="315" class="k" fill="var(--muted)">PUBLIC SYSTEMS</text>')
    parts.append(f'<text x="892" y="356" class="h">{len(active):02d}</text>')
    parts.append('<text x="948" y="354" class="s">active allowlisted</text>')
    parts.append('<rect x="1104" y="282" width="216" height="96" rx="18" fill="var(--soft)" stroke="var(--line)"/>')
    parts.append('<text x="1126" y="315" class="k" fill="var(--muted)">FEATURED SYSTEMS</text>')
    parts.append(f'<text x="1126" y="356" class="h" fill="var(--gold)">{len(featured):02d}</text>')
    parts.append('<text x="1182" y="354" class="s">research-facing</text>')
    parts.append('<text x="870" y="426" class="k" fill="var(--muted)">STATE LAST VERIFIED</text>')
    parts.append(f'<text x="870" y="456" class="v">{escape(verified)}</text>')
    parts.append('<text x="1104" y="426" class="k" fill="var(--muted)">PUBLIC EVIDENCE OBSERVED</text>')
    parts.append(f'<text x="1104" y="456" class="v">{escape(observed_at)}</text>')
    parts.append('<text x="870" y="500" class="s">DECLARED ≠ OBSERVED ≠ VERIFIED COMPUTATION ≠ EMPIRICALLY VALIDATED</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_pipeline(state: dict, framework: dict) -> str:
    stages = framework["stages"]
    active = set(state["current_focus"]["active_stages"])
    style = base_style(dark=None)
    parts = [svg_open(
        1400,
        430,
        "Animated seven-stage research pipeline",
        "Formal seven-stage research architecture with semantic motion only on the declared active transition from causal mechanisms to coupled hybrid multiscale dynamics.",
        style,
    )]
    parts.append('<rect x="1" y="1" width="1398" height="428" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="54" y="58" class="k" fill="var(--gold)">FORMAL RESEARCH PIPELINE</text>')
    parts.append('<text x="54" y="88" class="s">Only the declared active transition moves; inactive stages remain static context.</text>')
    x0, y0, w, gap = 54, 132, 174, 18
    for index, stage in enumerate(stages):
        x = x0 + index * (w + gap)
        sid = int(stage["id"])
        if sid == 2:
            stroke, fill, cls = "var(--gold)", "var(--soft)", "pulse-gold"
        elif sid == 3:
            stroke, fill, cls = "var(--blue)", "var(--soft)", "pulse-blue"
        else:
            stroke, fill, cls = "var(--line)", "var(--bg)", ""
        parts.append(f'<rect x="{x}" y="{y0}" width="{w}" height="162" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="{2.5 if sid in active else 1.2}" class="{cls}"/>')
        parts.append(f'<text x="{x+18}" y="{y0+30}" class="k" fill="{stroke}">0{sid}</text>')
        label = stage["display_label"]
        words = label.split()
        if len(words) <= 2:
            line1, line2 = label, ""
        else:
            split = max(1, len(words) // 2)
            line1, line2 = " ".join(words[:split]), " ".join(words[split:])
        parts.append(f'<text x="{x+18}" y="{y0+69}" class="v" font-size="15">{escape(line1)}</text>')
        if line2:
            parts.append(f'<text x="{x+18}" y="{y0+91}" class="v" font-size="15">{escape(line2)}</text>')
        parts.append(f'<text x="{x+18}" y="{y0+132}" class="s">{escape(stage["symbol"])}</text>')
        if index < len(stages) - 1:
            edge_class = 'class="flow-gold"' if sid == 2 and (sid + 1) == 3 else ''
            edge_stroke = 'var(--gold)' if edge_class else 'var(--muted)'
            edge_width = 3 if edge_class else 1.4
            parts.append(f'<path d="M{x+w+4} {y0+81}H{x+w+gap-4}" {edge_class} stroke="{edge_stroke}" stroke-width="{edge_width}"/>')
    parts.append('<text x="54" y="346" class="k" fill="var(--muted)">CURRENT TRANSITION</text>')
    parts.append(f'<text x="54" y="380" class="v" font-size="15" fill="var(--gold)">{escape(state["current_focus"]["transition"])}</text>')
    parts.append('<text x="54" y="406" class="s">Motion represents declared research focus, not stage completion or empirical validation.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_projects(observed: dict) -> str:
    repos = sorted(observed["repositories"], key=lambda item: int(item["profile_order"]))
    most_recent = max(
        repos,
        key=lambda item: timestamp((item.get("latest_commit") or {}).get("date") or item.get("pushed_at")),
    )["repository"] if repos else None
    style = base_style(dark=None)
    parts = [svg_open(
        1400,
        650,
        "Animated observed public research systems",
        "Evidence panel listing explicitly allowlisted public research repositories. The pulsing border marks the repository with the most recently observed public commit; it does not indicate scientific importance or validation.",
        style,
    )]
    parts.append('<rect x="1" y="1" width="1398" height="648" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="54" y="58" class="k" fill="var(--gold)">OBSERVED PUBLIC RESEARCH SYSTEMS</text>')
    parts.append(f'<text x="54" y="88" class="m">GitHub REST API · allowlist only · observed {escape(fmt_date(observed.get("generated_at")))}</text>')
    for idx, repo in enumerate(repos):
        col, row = idx % 3, idx // 3
        x, y = 54 + col * 438, 126 + row * 238
        featured = bool(repo.get("featured"))
        latest = repo.get("repository") == most_recent
        stroke = "var(--blue)" if latest else ("var(--gold)" if featured else "var(--line)")
        cls = "latest" if latest else ""
        parts.append(f'<rect x="{x}" y="{y}" width="408" height="206" rx="20" fill="var(--soft)" stroke="{stroke}" stroke-width="{3 if latest else (2 if featured else 1)}" class="{cls}"/>')
        label = "MOST RECENT PUBLIC CHANGE" if latest else ("FEATURED" if featured else "SUPPORTING")
        parts.append(f'<text x="{x+22}" y="{y+33}" class="k" fill="{stroke}">0{int(repo["profile_order"])} · {label}</text>')
        parts.append(f'<text x="{x+22}" y="{y+70}" font-size="20" font-weight="800">{escape(str(repo["short_name"]))}</text>')
        role = str(repo.get("research_role", ""))
        words = role.split()
        parts.append(f'<text x="{x+22}" y="{y+101}" class="m">{escape(" ".join(words[:7]))}</text>')
        parts.append(f'<text x="{x+22}" y="{y+124}" class="m">{escape(" ".join(words[7:14]))}</text>')
        language = repo.get("language") or "mixed / unspecified"
        commit = repo.get("latest_commit") or {}
        latest_date = fmt_date(commit.get("date") or repo.get("pushed_at"))
        parts.append(f'<text x="{x+22}" y="{y+164}" class="s">{escape(str(language))} · latest public commit {escape(latest_date)}</text>')
        parts.append(f'<text x="{x+22}" y="{y+188}" class="s">visibility: public · status: {escape(str(repo.get("status")))}</text>')
    parts.append('<text x="54" y="620" class="s">Pulsing border = most recent observed public repository change; public activity is not empirical validation.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def main() -> int:
    state = load("research-state.json")
    framework = load("framework.json")
    observed = load("public-github-state.json")
    write("research-hero-light.svg", render_hero(state, observed, dark=False))
    write("research-hero-dark.svg", render_hero(state, observed, dark=True))
    write("research-state-light.svg", render_state(state, observed, dark=False))
    write("research-state-dark.svg", render_state(state, observed, dark=True))
    write("research-pipeline.svg", render_pipeline(state, framework))
    write("project-system.svg", render_projects(observed))
    print("Rendered deterministic animated living-profile SVG assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
