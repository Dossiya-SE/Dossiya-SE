#!/usr/bin/env python3
"""Render deterministic mathematical-art SVG assets for the living research profile.

Design grammar
--------------
Physical topology   -> charcoal/ink geometry
Causal mechanism    -> gold geometry and motion
Mathematical state  -> blue level sets, vector field and trajectory
Engineering action  -> gold decision geometry

The art layer is deterministic and explanatory. It is not infrastructure telemetry,
a calibrated system trajectory, or empirical validation. No JavaScript is embedded;
CSS motion is disabled when prefers-reduced-motion is requested.
"""

from __future__ import annotations

import json
import math
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
        return str(value)[:10]


def timestamp(value: str | None) -> float:
    if not value:
        return 0.0
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def path_from_points(points: list[tuple[float, float]], *, close: bool = False) -> str:
    if not points:
        return ""
    body = "M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return body + ("Z" if close else "")


def warped_loop(cx: float, cy: float, rx: float, ry: float, phase: float, *, n: int = 96) -> str:
    """Deterministic smooth level-set-like loop for the state-space art layer."""
    pts: list[tuple[float, float]] = []
    for k in range(n):
        t = 2.0 * math.pi * k / n
        modulation = 1.0 + 0.055 * math.sin(3 * t + phase) + 0.025 * math.cos(5 * t - 0.7 * phase)
        x = cx + rx * modulation * math.cos(t) + 0.035 * rx * math.sin(2 * t + phase)
        y = cy + ry * modulation * math.sin(t) + 0.028 * ry * math.cos(3 * t - phase)
        pts.append((x, y))
    return path_from_points(pts, close=True)


def spiral_path(cx: float, cy: float, r0: float, r1: float, *, turns: float = 1.65, n: int = 120) -> str:
    pts: list[tuple[float, float]] = []
    for k in range(n):
        s = k / (n - 1)
        theta = 0.28 + turns * 2.0 * math.pi * s
        r = r0 * (1 - s) + r1 * s
        x = cx + r * math.cos(theta)
        y = cy + 0.70 * r * math.sin(theta)
        pts.append((x, y))
    return path_from_points(pts)


def vector_field_markup(x0: float, y0: float, width: float, height: float, cols: int, rows: int) -> str:
    """Schematic stable-spiral field; visual mathematics only, not a fitted infrastructure model."""
    parts = ['<g class="vector-field" opacity=".20">']
    for j in range(rows):
        for i in range(cols):
            x = x0 + (i + 0.5) * width / cols
            y = y0 + (j + 0.5) * height / rows
            xn = (x - (x0 + width / 2)) / (width / 2)
            yn = (y - (y0 + height / 2)) / (height / 2)
            vx = -0.62 * yn - 0.18 * xn
            vy = 0.54 * xn - 0.16 * yn
            norm = max(math.hypot(vx, vy), 1e-9)
            scale = 10.5
            dx = scale * vx / norm
            dy = scale * vy / norm
            x1, y1 = x - dx, y - dy
            x2, y2 = x + dx, y + dy
            ah = 3.4
            ang = math.atan2(dy, dx)
            a1 = ang + 2.55
            a2 = ang - 2.55
            p1 = (x2 + ah * math.cos(a1), y2 + ah * math.sin(a1))
            p2 = (x2 + ah * math.cos(a2), y2 + ah * math.sin(a2))
            parts.append(f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}M{x2:.1f} {y2:.1f}L{p1[0]:.1f} {p1[1]:.1f}M{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="var(--blue)" stroke-width="1.05"/>')
    parts.append('</g>')
    return "\n".join(parts)


def svg_open(width: int, height: int, title: str, desc: str, style: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
{style}'''


def base_style(*, dark: bool | None = None) -> str:
    if dark is True:
        root = "--bg:#0b0f14;--panel:#10161e;--ink:#f3f6f8;--muted:#9aa5b1;--line:#2b3440;--gold:#d4ad4c;--blue:#78a9ff;--soft:#151d27;--ghost:#1c2632"
        media = ""
    elif dark is False:
        root = "--bg:#fbfaf7;--panel:#ffffff;--ink:#11161d;--muted:#606a76;--line:#d8d4cb;--gold:#9a6a12;--blue:#316fc7;--soft:#f3f0e8;--ghost:#eae6dc"
        media = ""
    else:
        root = "--bg:#fbfaf7;--panel:#ffffff;--ink:#11161d;--muted:#606a76;--line:#d8d4cb;--gold:#9a6a12;--blue:#316fc7;--soft:#f3f0e8;--ghost:#eae6dc"
        media = '@media(prefers-color-scheme:dark){:root{--bg:#0b0f14;--panel:#10161e;--ink:#f3f6f8;--muted:#9aa5b1;--line:#2b3440;--gold:#d4ad4c;--blue:#78a9ff;--soft:#151d27;--ghost:#1c2632}}'
    return f'''<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.k{{font-size:12px;font-weight:800;letter-spacing:.14em}} .h{{font-size:30px;font-weight:780}} .hero{{font-size:45px;font-weight:820;letter-spacing:-.025em}}
.v{{font-size:19px;font-weight:720}} .m{{font-size:15px;fill:var(--muted)}} .s{{font-size:12px;fill:var(--muted)}}
.math{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:22px}} .math-sm{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:16px}}
.flow-gold{{stroke:var(--gold);stroke-dasharray:10 13;animation:flowGold 3.1s linear infinite}}
.flow-blue{{stroke:var(--blue);stroke-dasharray:9 13;animation:flowBlue 3.8s linear infinite}}
.pulse-gold{{animation:pulseGold 2.8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.pulse-blue{{animation:pulseBlue 3.2s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.latest{{animation:latestPulse 3.4s ease-in-out infinite}}
.level-set{{fill:none;stroke:var(--blue)}}
@keyframes flowGold{{to{{stroke-dashoffset:-46}}}}
@keyframes flowBlue{{to{{stroke-dashoffset:-44}}}}
@keyframes pulseGold{{0%,100%{{opacity:.52;transform:scale(.97)}}50%{{opacity:1;transform:scale(1.04)}}}}
@keyframes pulseBlue{{0%,100%{{opacity:.60;transform:scale(.98)}}50%{{opacity:1;transform:scale(1.035)}}}}
@keyframes latestPulse{{0%,100%{{stroke-opacity:.38}}50%{{stroke-opacity:1}}}}
@media(prefers-reduced-motion:reduce){{.flow-gold,.flow-blue,.pulse-gold,.pulse-blue,.latest{{animation:none!important}}}}
</style>'''


def render_hero(state: dict, observed: dict, *, dark: bool) -> str:
    focus = state["current_focus"]
    observed_at = fmt_date(observed.get("generated_at"))
    style = base_style(dark=dark)
    parts = [svg_open(
        1600,
        690,
        "Dossiya Dakou — mathematical engineering research portrait",
        "Animated mathematical-art research portrait separating physical Power and Transportation topology, causal interfaces, and schematic state-space viability geometry. Vector field, level sets and motion are explanatory visual mathematics, not measured infrastructure telemetry.",
        style,
    )]
    parts.append('<rect x="1" y="1" width="1598" height="688" rx="30" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<path d="M42 172H1558" stroke="var(--line)" stroke-width="1"/>')
    parts.append('<text x="56" y="55" class="k" fill="var(--gold)">MATHEMATICAL ENGINEERING · LIVING RESEARCH PROFILE</text>')
    parts.append('<text x="56" y="108" class="hero">Dossiya Dakou</text>')
    parts.append('<text x="56" y="143" class="m">Physical reality → causal mechanism → mathematical structure → engineering decision</text>')
    parts.append(f'<text x="1544" y="55" text-anchor="end" class="s">public evidence · {escape(observed_at)}</text>')

    parts.append('<g transform="translate(58 215)">')
    parts.append('<text x="0" y="0" class="k">01 · PHYSICAL REALITY</text>')
    parts.append('<text x="0" y="30" class="v">Power ↔ Transportation</text>')
    parts.append('<text x="0" y="54" class="s">components · flows · constraints · timescales</text>')
    pnodes = [(24,128),(118,91),(214,126),(119,185),(229,206),(35,220)]
    pedges = [(0,1),(1,2),(1,3),(3,4),(2,4),(0,5),(5,3)]
    for a,b in pedges:
        x1,y1 = pnodes[a]; x2,y2 = pnodes[b]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="var(--ink)" stroke-width="1.8" opacity=".78"/>')
    for idx,(x,y) in enumerate(pnodes):
        r = 8 if idx not in (1,3) else 10
        parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>')
    parts.append('<path d="M24 128L118 91L214 126L229 206" fill="none" class="flow-gold" stroke-width="3.5" stroke-linecap="round"/>')
    parts.append('<text x="0" y="263" class="s">power network</text>')
    parts.append('<g transform="translate(0 298)">')
    parts.append('<path d="M8 46C64 4 134 7 190 43S287 94 347 54" fill="none" stroke="var(--ink)" stroke-width="2" opacity=".86"/>')
    parts.append('<path d="M22 91C96 120 163 92 233 111S319 137 366 103" fill="none" stroke="var(--ink)" stroke-width="1.6" opacity=".55"/>')
    parts.append('<path d="M8 46C64 4 134 7 190 43S287 94 347 54" fill="none" class="flow-gold" stroke-width="3.5" stroke-linecap="round"/>')
    for x,y in [(8,46),(103,17),(190,43),(279,82),(347,54),(366,103)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="6.5" fill="var(--bg)" stroke="var(--ink)" stroke-width="1.8"/>')
    parts.append('<text x="0" y="147" class="s">mobility network</text>')
    parts.append('</g></g>')

    parts.append('<g transform="translate(505 258)">')
    parts.append('<text x="0" y="0" class="k" fill="var(--gold)">02 · CAUSAL INTERFACE</text>')
    parts.append('<text x="0" y="34" class="math" fill="var(--gold)">𝕀<tspan baseline-shift="sub" font-size="13">PT</tspan></text>')
    parts.append('<text x="58" y="32" class="s">mechanism · magnitude · sign · delay</text>')
    parts.append('<path d="M45 86V330" fill="none" class="flow-gold" stroke-width="4"/>')
    parts.append('<path d="M27 108L45 86L63 108M27 308L45 330L63 308" fill="none" stroke="var(--gold)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>')
    parts.append('<circle cx="45" cy="208" r="18" fill="var(--gold)" class="pulse-gold"/>')
    parts.append('<path d="M80 208H182" class="flow-gold" stroke-width="3"/>')
    parts.append('<text x="87" y="190" class="s">graph → dynamics</text>')
    parts.append('</g>')

    panel_x, panel_y, panel_w, panel_h = 760, 208, 785, 422
    parts.append(f'<rect x="{panel_x}" y="{panel_y}" width="{panel_w}" height="{panel_h}" rx="24" fill="var(--panel)" stroke="var(--line)"/>')
    parts.append(f'<text x="{panel_x+32}" y="{panel_y+38}" class="k" fill="var(--blue)">03 · STATE / VIABILITY GEOMETRY</text>')
    parts.append(f'<text x="{panel_x+32}" y="{panel_y+68}" class="s">schematic phase portrait · level sets · admissible boundary · resilience margin</text>')
    parts.append(vector_field_markup(panel_x+300, panel_y+92, 430, 278, 9, 6))
    cx, cy = panel_x + 505, panel_y + 232
    for idx, scale in enumerate((1.00, .84, .69, .54, .40)):
        d = warped_loop(cx, cy, 185*scale, 123*scale, phase=0.55+idx*0.34)
        opacity = .62 if idx == 0 else .12 + idx*.055
        width = 2.4 if idx == 0 else 1.2
        parts.append(f'<path d="{d}" class="level-set" stroke-width="{width}" opacity="{opacity:.2f}"/>')
    traj = spiral_path(cx+18, cy+7, 150, 20, turns=1.20)
    parts.append(f'<path d="{traj}" fill="none" stroke="var(--blue)" stroke-width="1.7" opacity=".24"/>')
    parts.append(f'<path d="{traj}" fill="none" class="flow-blue" stroke-width="4.2" stroke-linecap="round"/>')
    state_x = cx + 18 + 20*math.cos(0.28+1.20*2*math.pi)
    state_y = cy + 7 + .70*20*math.sin(0.28+1.20*2*math.pi)
    parts.append(f'<circle cx="{state_x:.1f}" cy="{state_y:.1f}" r="9" fill="var(--blue)" class="pulse-blue"/>')
    boundary_x, boundary_y = cx - 164, cy - 38
    parts.append(f'<path d="M{state_x:.1f} {state_y:.1f}L{boundary_x:.1f} {boundary_y:.1f}" stroke="var(--gold)" stroke-width="2" stroke-dasharray="5 7" opacity=".9"/>')
    parts.append(f'<text x="{boundary_x-9:.1f}" y="{boundary_y-10:.1f}" class="math-sm" fill="var(--gold)">ρ<tspan baseline-shift="sub" font-size="10">g</tspan></text>')
    parts.append(f'<text x="{cx+152}" y="{cy-98}" class="math-sm" fill="var(--blue)">∂𝒱</text>')
    parts.append(f'<text x="{cx-65}" y="{cy+145}" class="math-sm">Y(t)</text>')
    parts.append(f'<text x="{panel_x+34}" y="{panel_y+136}" class="math-sm">Ẏ = F<tspan baseline-shift="sub" font-size="10">𝒢</tspan>(Y,u,η;θ)</text>')
    parts.append(f'<text x="{panel_x+34}" y="{panel_y+174}" class="math-sm">Y ∈ 𝒱<tspan baseline-shift="sub" font-size="10">sus</tspan></text>')
    parts.append(f'<text x="{panel_x+34}" y="{panel_y+212}" class="math-sm" fill="var(--gold)">ρ<tspan baseline-shift="sub" font-size="10">g</tspan> = d<tspan baseline-shift="sub" font-size="10">g</tspan>(Y,∂𝒱)</text>')
    parts.append(f'<path d="M{panel_x+84} {panel_y+270}H{panel_x+230}" class="flow-gold" stroke-width="3"/>')
    parts.append(f'<text x="{panel_x+34}" y="{panel_y+258}" class="k" fill="var(--gold)">04 · DECISION</text>')
    parts.append(f'<text x="{panel_x+112}" y="{panel_y+304}" class="math" fill="var(--gold)">u*</text>')
    parts.append(f'<text x="{panel_x+34}" y="{panel_y+355}" class="s">vector field + level sets are deterministic visual mathematics, not fitted data</text>')
    parts.append(f'<text x="{panel_x+34}" y="{panel_y+381}" class="s">current research transition · {escape(focus["transition"])}</text>')
    parts.append('<text x="56" y="660" class="s">Visual grammar: ink = physical system · gold = causal/decision structure · blue = mathematical state/dynamics. Motion is not a measured flow or empirical validation.</text>')
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
    parts = [svg_open(1400, 470, "Governed living research state", "Compact generated panel distinguishing declared research configuration from observed public repository evidence.", style)]
    parts.append('<rect x="1" y="1" width="1398" height="468" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="48" y="56" class="k" fill="var(--gold)">CURRENT RESEARCH STATE</text>')
    parts.append('<text x="48" y="98" class="h">Power ↔ Transportation</text>')
    parts.append('<text x="48" y="126" class="m">information + organization as supporting non-physical layers</text>')
    parts.append('<line x1="48" y1="158" x2="1352" y2="158" stroke="var(--line)"/>')
    parts.append('<text x="48" y="202" class="k" fill="var(--muted)">ACTIVE FORMAL TRANSITION</text>')
    parts.append(f'<text x="48" y="238" class="v" fill="var(--gold)">{escape(focus["transition"])}</text>')
    parts.append('<path d="M48 269H566" class="flow-gold" stroke-width="3"/>')
    parts.append(f'<text x="48" y="311" class="m">{escape(focus["label"])}</text>')
    parts.append('<text x="720" y="202" class="k" fill="var(--muted)">MATHEMATICAL SIGNATURE</text>')
    parts.append('<text x="720" y="243" class="math" fill="var(--blue)">R_phys → C → (G, I_ij) → F_G → V → ρ_g → u*</text>')
    parts.append('<path d="M720 270H1265" class="flow-blue" stroke-width="2.7"/>')
    parts.append('<text x="720" y="310" class="s">objects are governed by research-state.json; public activity cannot promote a scientific claim</text>')
    cards = [
        (48, 354, 250, "PUBLIC SYSTEMS", f"{len(active):02d}", "allowlisted", "var(--ink)"),
        (330, 354, 250, "FEATURED", f"{len(featured):02d}", "research-facing", "var(--gold)"),
        (612, 354, 350, "STATE VERIFIED", verified, "declared configuration", "var(--blue)"),
        (1002, 354, 350, "EVIDENCE OBSERVED", observed_at, "public metadata", "var(--ink)"),
    ]
    for x,y,w,label,value,sub,color in cards:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="82" rx="16" fill="var(--panel)" stroke="var(--line)"/>')
        parts.append(f'<text x="{x+18}" y="{y+27}" class="k" fill="var(--muted)">{escape(label)}</text>')
        parts.append(f'<text x="{x+18}" y="{y+56}" class="v" fill="{color}">{escape(value)}</text>')
        parts.append(f'<text x="{x+w-18}" y="{y+56}" text-anchor="end" class="s">{escape(sub)}</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_pipeline(state: dict, framework: dict) -> str:
    stages = framework["stages"]
    active = set(state["current_focus"]["active_stages"])
    style = base_style(dark=None)
    parts = [svg_open(1400, 390, "Seven-stage research architecture", "A transformation-first seven-stage research path. Only the declared active transition from causal mechanisms to coupled dynamics is animated.", style)]
    parts.append('<rect x="1" y="1" width="1398" height="388" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="48" y="55" class="k" fill="var(--gold)">FORMAL RESEARCH ARCHITECTURE</text>')
    parts.append('<text x="48" y="84" class="s">engineering reality constrains abstraction · motion appears only on the currently declared research transition</text>')
    xs = [90, 285, 480, 675, 870, 1065, 1260]
    y = 184
    parts.append(f'<path d="M{xs[0]} {y}C{xs[1]-85} {y-52},{xs[1]-50} {y-52},{xs[1]} {y}S{xs[2]-40} {y+52},{xs[2]} {y}S{xs[3]-40} {y-52},{xs[3]} {y}S{xs[4]-40} {y+52},{xs[4]} {y}S{xs[5]-40} {y-52},{xs[5]} {y}S{xs[6]-40} {y+52},{xs[6]} {y}" fill="none" stroke="var(--line)" stroke-width="2"/>')
    parts.append(f'<path d="M{xs[1]} {y}C{xs[1]+60} {y+52},{xs[2]-55} {y+52},{xs[2]} {y}" fill="none" class="flow-gold" stroke-width="4"/>')
    for idx, stage in enumerate(stages):
        sid = int(stage["id"]); x = xs[idx]
        stroke = "var(--gold)" if sid == 2 else ("var(--blue)" if sid == 3 else "var(--line)")
        fill = "var(--soft)" if sid in active else "var(--panel)"
        parts.append(f'<circle cx="{x}" cy="{y}" r="27" fill="{fill}" stroke="{stroke}" stroke-width="{2.8 if sid in active else 1.4}"/>')
        parts.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" class="k" fill="{stroke}">0{sid}</text>')
        words = stage["display_label"].split()
        if len(words) > 2:
            split = max(1, min(len(words)-1, len(words)//2)); line1 = " ".join(words[:split]); line2 = " ".join(words[split:])
        else:
            line1, line2 = stage["display_label"], ""
        parts.append(f'<text x="{x}" y="{y+61}" text-anchor="middle" class="s">{escape(line1)}</text>')
        if line2:
            parts.append(f'<text x="{x}" y="{y+79}" text-anchor="middle" class="s">{escape(line2)}</text>')
        parts.append(f'<text x="{x}" y="{y-48}" text-anchor="middle" class="math-sm" fill="{stroke}">{escape(str(stage["symbol"]))}</text>')
    parts.append('<text x="48" y="334" class="k" fill="var(--muted)">CURRENT TRANSITION</text>')
    parts.append(f'<text x="48" y="363" class="v" fill="var(--gold)">{escape(state["current_focus"]["transition"])}</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_projects(observed: dict) -> str:
    repos = sorted(observed["repositories"], key=lambda item: int(item["profile_order"]))
    most_recent = max(repos, key=lambda item: timestamp((item.get("latest_commit") or {}).get("date") or item.get("pushed_at"))) if repos else None
    style = base_style(dark=None)
    parts = [svg_open(1400, 600, "Observed public research systems", "Professional research-system panel generated from the explicit public repository allowlist. The only pulsing boundary marks the most recently observed public repository change.", style)]
    parts.append('<rect x="1" y="1" width="1398" height="598" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="48" y="54" class="k" fill="var(--gold)">SELECTED PUBLIC RESEARCH SYSTEMS</text>')
    parts.append(f'<text x="48" y="82" class="s">observed {escape(fmt_date(observed.get("generated_at")))} · explicit public allowlist only</text>')
    for idx, repo in enumerate(repos):
        col, row = idx % 3, idx // 3
        x, y = 48 + col * 442, 116 + row * 220
        featured = bool(repo.get("featured"))
        recent = most_recent is not None and repo.get("repository") == most_recent.get("repository")
        stroke = "var(--blue)" if recent else ("var(--gold)" if featured else "var(--line)")
        cls = "latest" if recent else ""
        parts.append(f'<rect x="{x}" y="{y}" width="408" height="190" rx="18" fill="var(--panel)" stroke="{stroke}" stroke-width="{3 if recent else (2 if featured else 1)}" class="{cls}"/>')
        tag = "MOST RECENT PUBLIC CHANGE" if recent else ("FEATURED" if featured else "SUPPORTING")
        parts.append(f'<text x="{x+20}" y="{y+30}" class="k" fill="{stroke}">0{int(repo["profile_order"])} · {tag}</text>')
        parts.append(f'<text x="{x+20}" y="{y+66}" font-size="20" font-weight="780">{escape(str(repo["short_name"]))}</text>')
        role = str(repo.get("research_role", "")); words = role.split()
        parts.append(f'<text x="{x+20}" y="{y+96}" class="m">{escape(" ".join(words[:7]))}</text>')
        parts.append(f'<text x="{x+20}" y="{y+118}" class="m">{escape(" ".join(words[7:14]))}</text>')
        commit = repo.get("latest_commit") or {}; latest = fmt_date(commit.get("date") or repo.get("pushed_at")); language = repo.get("language") or "mixed / unspecified"
        parts.append(f'<text x="{x+20}" y="{y+154}" class="s">{escape(str(language))} · latest public commit {escape(latest)}</text>')
        parts.append(f'<text x="{x+20}" y="{y+176}" class="s">public · {escape(str(repo.get("status")))}</text>')
    parts.append('<text x="48" y="566" class="s">Pulsing border = most recent observed repository change. Recency is not scientific importance, quality, or empirical validation.</text>')
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
    print("Rendered deterministic mathematical-art living-profile SVG assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())