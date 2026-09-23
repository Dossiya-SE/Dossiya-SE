#!/usr/bin/env python3
"""Render publication-style README visuals using a governed sRGB semantic system.

The figures are intentionally sparse: neutral canvas dominates, sector/state colors are
used only where they carry declared meaning, and every color channel is backed by text,
geometry, line pattern, or direction. No figure is empirical validation or telemetry.
"""

from __future__ import annotations

import json
from datetime import date, datetime
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "generated"

TOKENS = [
    "bg","panel","ink","muted","line","topology",
    "green","green_soft","red","red_soft","control","control_soft","control_ink","ghost",
    "power","power_soft","transport","transport_soft","information","information_soft",
    "organization","organization_ink","organization_soft","cyan","cyan_soft",
    "violet","violet_soft","magenta","magenta_soft","control","control_soft",
]

def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def write(name: str, text: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(text.rstrip() + "\n", encoding="utf-8")

def fmt_date(value: str | None) -> str:
    if not value:
        return "not observed"
    try:
        d = datetime.fromisoformat(value.replace("Z","+00:00")).date() if "T" in value else date.fromisoformat(value)
        return d.strftime("%d %b %Y")
    except ValueError:
        return str(value)[:10]

def timestamp(value: str | None) -> float:
    if not value:
        return 0.0
    try:
        return datetime.fromisoformat(value.replace("Z","+00:00")).timestamp()
    except ValueError:
        return 0.0

def css_vars(values: dict) -> str:
    return ";".join(f"--{k.replace('_','-')}:{values[k]}" for k in TOKENS)

def style(palette: dict, mode: str = "adaptive") -> str:
    light, dark = css_vars(palette["light"]), css_vars(palette["dark"])
    root = dark if mode == "dark" else light
    media = "" if mode in {"light","dark"} else f"@media(prefers-color-scheme:dark){{:root{{{dark}}}}}"
    return f"""<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.math{{font-family:Georgia,"STIX Two Text","Times New Roman",serif}}
.eyebrow{{font-size:12px;font-weight:800;letter-spacing:.14em;fill:var(--muted)}}
.title{{font-size:31px;font-weight:800;letter-spacing:-.02em}}
.h{{font-size:20px;font-weight:760}} .m{{font-size:14px;fill:var(--muted)}} .s{{font-size:11px;fill:var(--muted)}}
.value{{font-size:18px;font-weight:720}} .math-lg{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:25px}}
.panel{{fill:var(--panel);stroke:var(--line);stroke-width:1.1}}
.flow-control{{fill:none;stroke:var(--control);stroke-width:3.2;stroke-linecap:round;stroke-dasharray:9 11;animation:flow 3.2s linear infinite}}
.flow-green{{fill:none;stroke:var(--green);stroke-width:3;stroke-linecap:round;stroke-dasharray:10 12;animation:flow 3.8s linear infinite}}
.flow-blue{{fill:none;stroke:var(--information);stroke-width:2.8;stroke-linecap:round;stroke-dasharray:8 10;animation:flow 4.1s linear infinite}}
.pulse-green{{animation:pulse 3.2s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.latest{{animation:latest 3.4s ease-in-out infinite}}
@keyframes flow{{to{{stroke-dashoffset:-42}}}}
@keyframes pulse{{0%,100%{{opacity:.65}}50%{{opacity:1}}}}
@keyframes latest{{0%,100%{{stroke-opacity:.35}}50%{{stroke-opacity:1}}}}
@media(prefers-reduced-motion:reduce){{.flow-control,.flow-green,.flow-blue,.pulse-green,.latest{{animation:none!important}}}}
</style>"""

def svg_open(width: int, height: int, title: str, desc: str, css: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
{css}"""

def render_question(palette: dict) -> str:
    p=[svg_open(1400,315,"Current research question",
        "Publication-style research question. Power is red, Transportation green, the causal interface cyan, coupled dynamics blue, and viability green. Labels and geometry duplicate all color meaning.",
        style(palette))]
    p += [
      '<rect x="1" y="1" width="1398" height="313" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
      '<path d="M48 22H238" stroke="var(--power)" stroke-width="3"/><path d="M238 22H428" stroke="var(--transport)" stroke-width="3"/><path d="M428 22H618" stroke="var(--information)" stroke-width="3"/>',
      '<text x="48" y="52" class="eyebrow">RESEARCH QUESTION · CURRENT</text>',
      '<text x="48" y="94" class="title">How do physically supported infrastructure interfaces generate coupled dynamics?</text>',
      '<text x="48" y="143" class="h" fill="var(--power)">POWER</text>',
      '<text x="126" y="143" class="h">↔</text>',
      '<text x="160" y="143" class="h" fill="var(--transport)">TRANSPORTATION</text>',
      '<text x="48" y="169" class="m">Power ↔ Transportation interfaces</text>',
      '<path d="M365 139H510" class="flow-control"/><text x="382" y="126" class="s">typed causal mechanism</text>',
      '<text x="545" y="143" class="h" fill="var(--information)">COUPLED DYNAMICS</text>',
      '<text x="545" y="169" class="m">disturbance · delay · feedback · control</text>',
      '<path d="M785 139H955" class="flow-blue"/>',
      '<text x="990" y="143" class="h" fill="var(--green)">VIABILITY</text>',
      '<text x="990" y="169" class="math" font-size="19" fill="var(--green)">Y(t) ∈ 𝒱ₛᵤₛ(t)</text>',
      '<line x1="48" y1="211" x2="1352" y2="211" stroke="var(--line)"/>',
      '<text x="48" y="251" class="m">Engineering interpretation</text>',
      '<text x="48" y="280" class="value">Mechanism → coupled state evolution → critical-boundary margin → admissible intervention.</text>',
      '<text x="1352" y="294" text-anchor="end" class="s">Question structure is declared research scope; it is not a validated causal law.</text>',
      '</svg>'
    ]
    return "\n".join(p)

def render_state(state: dict, observed: dict, palette: dict, mode: str) -> str:
    repos=[r for r in observed.get("repositories",[]) if r.get("status")=="active" and not r.get("archived")]
    featured=[r for r in repos if r.get("featured")]
    focus=state["current_focus"]
    p=[svg_open(1400,348,"Governed living research state",
      "Publication-style current research state. Power, Transportation, Information and Organization use separate RGB-derived semantic channels; active transition and mathematical state remain explicitly labeled.",
      style(palette,mode))]
    p += [
      '<rect x="1" y="1" width="1398" height="346" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
      '<text x="48" y="49" class="eyebrow">CURRENT RESEARCH STATE</text>',
      '<text x="48" y="94" class="title"><tspan fill="var(--power)">Power</tspan><tspan> ↔ </tspan><tspan fill="var(--transport)">Transportation</tspan></text>',
      '<text x="48" y="124" class="m">Information and Organization enter only when they materially alter sensing, coordination, inference, operation or recovery.</text>',
      '<line x1="48" y1="154" x2="1352" y2="154" stroke="var(--line)"/>',
      '<text x="48" y="190" class="eyebrow">CURRENT SCIENTIFIC TRANSITION</text>',
      '<text x="48" y="230" class="value">Causal Mechanisms</text>',
      '<path d="M235 223H485" class="flow-control"/>',
      '<text x="515" y="230" class="value" fill="var(--information)">Coupled Hybrid Multiscale Dynamics</text>',
      '<text x="48" y="265" class="m">physically supported interfaces → coupled state evolution under disturbance and control</text>',
      '<text x="965" y="190" class="eyebrow">MATHEMATICAL STATE</text>',
      '<text x="965" y="232" class="math-lg">R_phys → C → (G,I) → F_G → V → ρ_g → u*</text>',
      '<path d="M965 256H1348" class="flow-green"/>',
      '<line x1="48" y1="297" x2="1352" y2="297" stroke="var(--line)"/>',
      f'<text x="48" y="325" class="s">{len(repos):02d} public systems · {len(featured):02d} featured · state verified {escape(fmt_date(state.get("last_verified")))} · evidence observed {escape(fmt_date(observed.get("generated_at")))}</text>',
      '<text x="1352" y="325" text-anchor="end" class="s">public activity cannot promote a scientific claim</text>',
      '</svg>'
    ]
    return "\n".join(p)

def render_viability(palette: dict) -> str:
    p=[svg_open(1400,500,"Graph to viability transformation",
      "Graph/model space is separated from state/viability space. Causal interface is cyan, dynamics blue, viability green, critical boundary red and intervention control; all meanings also use labels and line styles.",
      style(palette))]
    p += [
      '<rect x="1" y="1" width="1398" height="498" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
      '<text x="48" y="48" class="eyebrow">GRAPH → DYNAMICS → VIABILITY → DECISION</text>',
      '<text x="48" y="80" class="m">Structure and model objects remain distinct from the state-space geometry they induce.</text>',
      '<text x="48" y="124" class="eyebrow">GRAPH / MODEL SPACE</text>',
      '<text x="80" y="190" text-anchor="middle" class="math-lg">𝓖</text><text x="80" y="220" text-anchor="middle" class="s">topology</text>',
      '<path d="M122 184H225" stroke="var(--line)" stroke-width="2"/>',
      '<text x="275" y="190" text-anchor="middle" class="math-lg" fill="var(--control-ink)">𝕀</text><text x="275" y="220" text-anchor="middle" class="s">causal interface</text>',
      '<path d="M325 184H420" class="flow-control"/>',
      '<text x="475" y="190" text-anchor="middle" class="math-lg" fill="var(--information)">F𝓖</text><text x="475" y="220" text-anchor="middle" class="s">coupled dynamics</text>',
      '<path d="M525 184H620" class="flow-blue"/>',
      '<text x="675" y="190" text-anchor="middle" class="math-lg" fill="var(--cyan)">Y(t)</text><text x="675" y="220" text-anchor="middle" class="s">state trajectory</text>',
      '<path d="M730 184H805" stroke="var(--line)" stroke-width="2"/><path d="M791 174L805 184L791 194" fill="none" stroke="var(--line)" stroke-width="2"/>',
      '<rect x="825" y="108" width="527" height="322" rx="16" class="panel"/>',
      '<text x="850" y="141" class="eyebrow">STATE / VIABILITY SPACE</text>',
      '<line x1="880" y1="372" x2="1298" y2="372" stroke="var(--line)" stroke-width="1.2"/><line x1="880" y1="372" x2="880" y2="171" stroke="var(--line)" stroke-width="1.2"/>',
      '<path d="M915 330C925 246 985 190 1068 181C1162 171 1242 208 1285 276C1305 310 1286 350 1230 374C1160 401 1063 392 991 378C944 369 911 354 915 330Z" fill="var(--green-soft)" stroke="var(--green)" stroke-width="2.2"/>',
      '<path d="M915 330C925 246 985 190 1068 181C1162 171 1242 208 1285 276C1305 310 1286 350 1230 374C1160 401 1063 392 991 378C944 369 911 354 915 330Z" fill="none" stroke="var(--red)" stroke-width="3" stroke-dasharray="9 8"/>',
      '<text x="1188" y="205" class="math" font-size="18" fill="var(--red)">∂𝒱</text><text x="1128" y="338" class="math" font-size="21" fill="var(--green)">𝒱ₛᵤₛ</text>',
      '<circle cx="1048" cy="292" r="9" fill="var(--cyan)" stroke="var(--panel)" stroke-width="3"/><text x="1064" y="297" class="math" font-size="17">Y(t)</text>',
      '<path d="M1058 286L1212 225" stroke="var(--red)" stroke-width="2.4" stroke-dasharray="6 6"/><text x="1128" y="246" class="math" font-size="17" fill="var(--red)">ρ_g</text>',
      '<path d="M1058 301Q1105 337 1174 329" class="flow-control"/><text x="1198" y="339" class="math" font-size="18" fill="var(--control)">u*</text>',
      '<line x1="48" y1="276" x2="746" y2="276" stroke="var(--line)"/>',
      '<text x="48" y="318" class="math" font-size="18" fill="var(--information)">Ẏ = F_𝒢(Y,u,η;θ)</text>',
      '<text x="48" y="356" class="math" font-size="18" fill="var(--green)">Y(t) ∈ 𝒱ₛᵤₛ(t)</text>',
      '<text x="48" y="394" class="math" font-size="18" fill="var(--red)">ρ_g(Y) = d_g(Y,∂𝒱)</text>',
      '<text x="48" y="447" class="m">Topology constrains dynamics; viability encodes admissible operation; the margin measures proximity to a critical boundary; control selects an admissible intervention.</text>',
      '<text x="1352" y="475" text-anchor="end" class="s">No empirical validity is implied by the geometry alone.</text>',
      '</svg>'
    ]
    return "\n".join(p)

def render_projects(observed: dict, palette: dict) -> str:
    repos=[r for r in observed.get("repositories",[]) if r.get("status")=="active" and not r.get("archived")]
    featured=sorted([r for r in repos if r.get("featured")],key=lambda r:int(r.get("profile_order",99)))[:4]
    recent=max(repos,key=lambda r:timestamp((r.get("latest_commit") or {}).get("date") or r.get("pushed_at"))) if repos else None
    accents=["violet","information","transport","cyan"]
    p=[svg_open(1400,510,"Featured public research systems",
      "Four featured public research systems shown as a restrained publication index. Accent colors aid navigation only and do not encode scientific quality, importance or evidence strength.",
      style(palette))]
    p += ['<rect x="1" y="1" width="1398" height="508" rx="18" fill="var(--bg)" stroke="var(--line)"/>',
          '<text x="48" y="48" class="eyebrow">FEATURED RESEARCH SYSTEMS</text>',
          f'<text x="48" y="79" class="m">four research-facing public systems · observed {escape(fmt_date(observed.get("generated_at")))}</text>']
    for idx,repo in enumerate(featured):
        x,y,w,h=48,108+idx*82,1304,68
        accent=accents[idx%len(accents)]
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" class="panel research-card"/>')
        p.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+h}" stroke="var(--{accent})" stroke-width="5"/>')
        p.append(f'<text x="{x+24}" y="{y+29}" class="h">{escape(str(repo.get("short_name",repo.get("repository","research system"))))}</text>')
        role=" ".join(str(repo.get("research_role","")).split()[:16])
        p.append(f'<text x="{x+430}" y="{y+28}" class="m">{escape(role)}</text>')
        latest=fmt_date((repo.get("latest_commit") or {}).get("date") or repo.get("pushed_at"))
        lang=repo.get("language") or "mixed / unspecified"
        p.append(f'<text x="{x+24}" y="{y+52}" class="s">{escape(str(lang))} · latest public commit {escape(latest)}</text>')
    recent_name=str((recent or {}).get("short_name") or (recent or {}).get("repository") or "not observed")
    p += ['<line x1="48" y1="447" x2="1352" y2="447" stroke="var(--line)"/>',
          '<text x="48" y="478" class="eyebrow" fill="var(--control-ink)">MOST RECENT PUBLIC CHANGE</text>',
          f'<text x="285" y="478" class="s">{escape(recent_name)} · recency is metadata, not scientific importance or validation; row accent is navigation, not evidence status.</text>',
          '</svg>']
    return "\n".join(p)

def main() -> int:
    palette=load("visual-palette.json")
    state=load("research-state.json")
    observed=load("public-github-state.json")
    write("research-question.svg",render_question(palette))
    write("research-state-light.svg",render_state(state,observed,palette,"light"))
    write("research-state-dark.svg",render_state(state,observed,palette,"dark"))
    write("graph-to-viability.svg",render_viability(palette))
    write("project-system.svg",render_projects(observed,palette))
    print("Refined publication-style RGB profile visuals.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
