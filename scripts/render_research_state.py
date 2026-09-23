#!/usr/bin/env python3
"""Render deterministic mathematical-art SVG assets for the living research profile.

Publication sRGB system
-----------------------
Power          -> red channel
Transportation -> green channel
Information    -> blue channel
Organization   -> magenta
viability      -> green state semantics
criticality    -> dashed red state semantics
causal/control -> cyan/control
mathematics    -> violet when a distinct model channel is needed

The visual mathematics is explanatory and deterministic. It is not measured
infrastructure telemetry, a calibrated trajectory, or empirical validation.
No JavaScript is embedded. CSS motion is disabled for reduced-motion users.
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


def path_from_points(points: list[tuple[float, float]], close: bool = False) -> str:
    if not points:
        return ""
    path = "M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return path + ("Z" if close else "")


def warped_loop(cx: float, cy: float, rx: float, ry: float, phase: float, n: int = 100) -> str:
    pts: list[tuple[float, float]] = []
    for k in range(n):
        t = 2 * math.pi * k / n
        mod = 1 + 0.052 * math.sin(3 * t + phase) + 0.024 * math.cos(5 * t - 0.7 * phase)
        x = cx + rx * mod * math.cos(t) + 0.034 * rx * math.sin(2 * t + phase)
        y = cy + ry * mod * math.sin(t) + 0.028 * ry * math.cos(3 * t - phase)
        pts.append((x, y))
    return path_from_points(pts, close=True)


def spiral_path(cx: float, cy: float, r0: float, r1: float, turns: float = 1.18, n: int = 120) -> str:
    pts: list[tuple[float, float]] = []
    for k in range(n):
        s = k / (n - 1)
        theta = 0.28 + turns * 2 * math.pi * s
        r = r0 * (1 - s) + r1 * s
        pts.append((cx + r * math.cos(theta), cy + 0.70 * r * math.sin(theta)))
    return path_from_points(pts)


def vector_field_markup(x0: float, y0: float, width: float, height: float, cols: int, rows: int) -> str:
    parts = ['<g class="vector-field" opacity=".25">']
    for j in range(rows):
        for i in range(cols):
            x = x0 + (i + 0.5) * width / cols
            y = y0 + (j + 0.5) * height / rows
            xn = (x - (x0 + width / 2)) / (width / 2)
            yn = (y - (y0 + height / 2)) / (height / 2)
            vx, vy = -0.62 * yn - 0.18 * xn, 0.54 * xn - 0.16 * yn
            norm = max(math.hypot(vx, vy), 1e-9)
            dx, dy = 10.5 * vx / norm, 10.5 * vy / norm
            x1, y1, x2, y2 = x - dx, y - dy, x + dx, y + dy
            ang = math.atan2(dy, dx)
            p1 = (x2 + 3.4 * math.cos(ang + 2.55), y2 + 3.4 * math.sin(ang + 2.55))
            p2 = (x2 + 3.4 * math.cos(ang - 2.55), y2 + 3.4 * math.sin(ang - 2.55))
            parts.append(
                f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}M{x2:.1f} {y2:.1f}L{p1[0]:.1f} {p1[1]:.1f}M{x2:.1f} {y2:.1f}L{p2[0]:.1f} {p2[1]:.1f}" '
                'fill="none" stroke="var(--violet)" stroke-width="1.05"/>'
            )
    parts.append('</g>')
    return "\n".join(parts)


def svg_open(width: int, height: int, title: str, desc: str, style: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(desc)}</desc>
{style}'''


def base_style(dark: bool | None = None) -> str:
    palette = load("visual-palette.json")
    keys = [
        "bg","panel","ink","muted","line","topology",
        "green","green_soft","red","red_soft","control","control_soft","control_ink","ghost",
        "power","power_soft","transport","transport_soft","information","information_soft",
        "organization","organization_ink","organization_soft","cyan","cyan_soft",
        "violet","violet_soft","magenta","magenta_soft",
    ]
    def vars_for(values: dict) -> str:
        return ";".join(f"--{k.replace('_','-')}:{values[k]}" for k in keys)
    light = vars_for(palette["light"])
    dark_vars = vars_for(palette["dark"])
    root = dark_vars if dark is True else light
    media = "" if dark is not None else f'@media(prefers-color-scheme:dark){{:root{{{dark_vars}}}}}'
    return f'''<style>
:root{{{root}}}
{media}
text{{font-family:Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:var(--ink)}}
.k{{font-size:12px;font-weight:800;letter-spacing:.14em}} .h{{font-size:30px;font-weight:780}} .hero{{font-size:45px;font-weight:820;letter-spacing:-.025em}}
.v{{font-size:19px;font-weight:720}} .m{{font-size:15px;fill:var(--muted)}} .s{{font-size:12px;fill:var(--muted)}}
.math{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:22px}} .math-sm{{font-family:Georgia,"STIX Two Text","Times New Roman",serif;font-size:16px}}
.label-control{{fill:var(--control-soft);stroke:var(--control)}} .label-green{{fill:var(--green-soft);stroke:var(--green)}} .label-red{{fill:var(--red-soft);stroke:var(--red)}}
.flow-control{{stroke:var(--control);stroke-dasharray:10 13;animation:flowControl 3.1s linear infinite}}
.flow-green{{stroke:var(--green);stroke-dasharray:9 13;animation:flowGreen 3.8s linear infinite}}
.flow-red{{stroke:var(--red);stroke-dasharray:7 11;animation:flowRed 3.3s linear infinite}}
.flow-power{{stroke:var(--power);stroke-dasharray:11 9;animation:flowPower 3.6s linear infinite}}
.flow-transport{{stroke:var(--transport);stroke-dasharray:10 10;animation:flowTransport 3.9s linear infinite}}
.flow-blue{{stroke:var(--information);stroke-dasharray:8 11;animation:flowBlue 4.1s linear infinite}}
.pulse-control{{animation:pulseControl 2.8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.pulse-green{{animation:pulseGreen 3.2s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.pulse-red{{animation:pulseRed 2.7s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
.latest{{animation:latestPulse 3.4s ease-in-out infinite}}
.level-set{{fill:none;stroke:var(--green)}} .critical-boundary{{fill:none;stroke:var(--red)}}
@keyframes flowControl{{to{{stroke-dashoffset:-46}}}} @keyframes flowGreen{{to{{stroke-dashoffset:-44}}}} @keyframes flowRed{{to{{stroke-dashoffset:-38}}}}
@keyframes flowPower{{to{{stroke-dashoffset:-40}}}} @keyframes flowTransport{{to{{stroke-dashoffset:-40}}}} @keyframes flowBlue{{to{{stroke-dashoffset:-40}}}}
@keyframes pulseControl{{0%,100%{{opacity:.58;transform:scale(.97)}}50%{{opacity:1;transform:scale(1.04)}}}}
@keyframes pulseGreen{{0%,100%{{opacity:.62;transform:scale(.98)}}50%{{opacity:1;transform:scale(1.035)}}}}
@keyframes pulseRed{{0%,100%{{opacity:.55;transform:scale(.97)}}50%{{opacity:1;transform:scale(1.04)}}}}
@keyframes latestPulse{{0%,100%{{stroke-opacity:.40}}50%{{stroke-opacity:1}}}}
@media(prefers-reduced-motion:reduce){{.flow-control,.flow-green,.flow-red,.flow-power,.flow-transport,.flow-blue,.pulse-control,.pulse-green,.pulse-red,.latest{{animation:none!important}}}}
</style>'''

def label(parts: list[str], x: float, y: float, w: float, text: str, kind: str = "control") -> None:
    cls = f"label-{kind}"
    color = {"control":"var(--control-ink)","green":"var(--green)","red":"var(--red)"}[kind]
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="31" rx="9" class="{cls}" stroke-width="1"/>')
    parts.append(f'<text x="{x+14}" y="{y+21}" class="k" fill="{color}">{escape(text)}</text>')


def render_hero(state: dict, observed: dict, dark: bool) -> str:
    focus = state["current_focus"]
    observed_at = fmt_date(observed.get("generated_at"))
    parts = [svg_open(
        1600, 700,
        "Dossiya Dakou — physics-grounded mathematical engineering",
        "Publication-style research portrait. Power uses red, Transportation green, Information blue and Organization sky blue. Causal mechanisms use light sky blue, model geometry uses violet, viability uses green, and critical boundaries use dashed red. Color is never the sole encoding.",
        base_style(dark),
    )]
    parts.append('<rect x="1" y="1" width="1598" height="698" rx="18" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<path d="M48 20H235" stroke="var(--power)" stroke-width="3"/><path d="M235 20H422" stroke="var(--transport)" stroke-width="3"/><path d="M422 20H609" stroke="var(--information)" stroke-width="3"/>')
    parts.append('<text x="56" y="72" class="hero">Dossiya Dakou</text>')
    parts.append('<text x="56" y="108" class="m">Physics-grounded mathematical engineering for sustainable infrastructure</text>')
    parts.append(f'<text x="1544" y="55" text-anchor="end" class="s">public evidence · {escape(observed_at)}</text>')
    parts.append('<line x1="48" y1="138" x2="1552" y2="138" stroke="var(--line)"/>')

    # Left: physical and supporting system channels.
    parts.append('<g transform="translate(58 178)">')
    parts.append('<text x="0" y="0" class="k">SYSTEM CHANNELS</text>')
    parts.append('<text x="0" y="42" class="v" fill="var(--power)">POWER</text>')
    parts.append('<text x="116" y="42" class="v" fill="var(--transport)">TRANSPORTATION</text>')
    parts.append('<text x="0" y="74" class="s" fill="var(--information)">INFORMATION · sensing / estimation</text>')
    parts.append('<text x="0" y="98" class="s" fill="var(--organization-ink)">ORGANIZATION · coordination / recovery</text>')

    pnodes=[(24,175),(115,138),(212,173),(118,230),(230,250),(36,262)]
    pedges=[(0,1),(1,2),(1,3),(3,4),(2,4),(0,5),(5,3)]
    for a,b in pedges:
        x1,y1=pnodes[a]; x2,y2=pnodes[b]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="var(--topology)" stroke-width="1.5" opacity=".55"/>')
    for i,(x,y) in enumerate(pnodes):
        parts.append(f'<circle cx="{x}" cy="{y}" r="{9 if i in (1,3) else 7}" fill="var(--bg)" stroke="var(--power)" stroke-width="2"/>')
    parts.append('<path d="M24 175L115 138L212 173L230 250" fill="none" class="flow-power" stroke-width="3.3" stroke-linecap="round"/>')
    parts.append('<text x="0" y="292" class="s">solid carmine path · electrical service</text>')

    parts.append('<g transform="translate(0 325)">')
    parts.append('<path d="M8 46C64 4 134 7 190 43S287 94 347 54" fill="none" stroke="var(--topology)" stroke-width="1.6" opacity=".55"/>')
    parts.append('<path d="M22 91C96 120 163 92 233 111S319 137 366 103" fill="none" stroke="var(--topology)" stroke-width="1.3" opacity=".38"/>')
    parts.append('<path d="M8 46C64 4 134 7 190 43S287 94 347 54" fill="none" class="flow-transport" stroke-width="3.3" stroke-linecap="round"/>')
    for x,y in [(8,46),(103,17),(190,43),(279,82),(347,54),(366,103)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="6.5" fill="var(--bg)" stroke="var(--transport)" stroke-width="1.8"/>')
    parts.append('<path d="M103 17V108M279 82V140" class="flow-blue" stroke-width="2.2" fill="none"/>')
    parts.append('<text x="0" y="147" class="s">green physical path · blue dashed information relation</text>')
    parts.append('</g></g>')

    # Center: causal interface.
    parts.append('<g transform="translate(475 200)">')
    parts.append('<text x="0" y="0" class="k" fill="var(--control-ink)">CAUSAL INTERFACE</text>')
    parts.append('<text x="0" y="48" class="math" fill="var(--control-ink)">𝕀<tspan baseline-shift="sub" font-size="13">PT</tspan></text>')
    parts.append('<text x="58" y="46" class="s">mechanism · magnitude · sign · delay</text>')
    parts.append('<path d="M58 86V337" fill="none" class="flow-control" stroke-width="3.6"/>')
    parts.append('<path d="M38 108L58 86L78 108M38 315L58 337L78 315" fill="none" stroke="var(--control)" stroke-width="2.3"/>')
    parts.append('<circle cx="58" cy="211" r="15" fill="var(--control-soft)" stroke="var(--control)" stroke-width="2.2" class="pulse-control"/>')
    parts.append('<path d="M93 211H205" class="flow-control" stroke-width="2.8"/>')
    parts.append('<text x="100" y="191" class="s">graph → dynamics</text>')
    parts.append('<text x="0" y="380" class="s">cyan = interface / intervention; labels + dashed geometry remain authoritative</text>')
    parts.append('</g>')

    # Right: model and viability geometry.
    px,py,pw,ph=735,178,810,455
    parts.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18" fill="var(--panel)" stroke="var(--line)"/>')
    parts.append(f'<text x="{px+28}" y="{py+38}" class="k" fill="var(--violet)">MATHEMATICAL STATE / VIABILITY GEOMETRY</text>')
    parts.append(f'<text x="{px+28}" y="{py+68}" class="s">vector field · level sets · critical boundary · resilience margin · admissible control</text>')
    parts.append(vector_field_markup(px+300,py+102,450,275,9,6))
    cx,cy=px+520,py+245
    for idx,scale in enumerate((1.00,.84,.69,.54,.40)):
        d=warped_loop(cx,cy,190*scale,126*scale,0.55+idx*0.34)
        parts.append(f'<path d="{d}" class="level-set" stroke-width="{2.4 if idx==0 else 1.2}" opacity="{0.74 if idx==0 else 0.18+idx*0.05:.2f}"/>')
    boundary=warped_loop(cx,cy,198,134,0.48)
    parts.append(f'<path d="{boundary}" class="critical-boundary flow-red" stroke-width="2.6" opacity=".92"/>')
    traj=spiral_path(cx+15,cy+6,154,22)
    parts.append(f'<path d="{traj}" fill="none" class="flow-green" stroke-width="3.7" stroke-linecap="round"/>')
    state_x=cx+15+22*math.cos(0.28+1.18*2*math.pi)
    state_y=cy+6+.70*22*math.sin(0.28+1.18*2*math.pi)
    parts.append(f'<circle cx="{state_x:.1f}" cy="{state_y:.1f}" r="9" fill="var(--control)" stroke="var(--panel)" stroke-width="3"/>')
    bx,by=cx-174,cy-46
    parts.append(f'<path d="M{state_x:.1f} {state_y:.1f}L{bx:.1f} {by:.1f}" stroke="var(--red)" stroke-width="2.1" stroke-dasharray="5 7"/>')
    parts.append(f'<text x="{bx-7:.1f}" y="{by-10:.1f}" class="math-sm" fill="var(--red)">ρ<tspan baseline-shift="sub" font-size="10">g</tspan></text>')
    parts.append(f'<text x="{cx+155}" y="{cy-106}" class="math-sm" fill="var(--red)">∂𝒱</text>')
    parts.append(f'<text x="{cx-75}" y="{cy+149}" class="math-sm" fill="var(--green)">Y(t)</text>')
    parts.append(f'<text x="{px+30}" y="{py+142}" class="math-sm" fill="var(--information)">Ẏ = F<tspan baseline-shift="sub" font-size="10">𝒢</tspan>(Y,u,η;θ)</text>')
    parts.append(f'<text x="{px+30}" y="{py+182}" class="math-sm" fill="var(--green)">Y ∈ 𝒱<tspan baseline-shift="sub" font-size="10">sus</tspan></text>')
    parts.append(f'<text x="{px+30}" y="{py+222}" class="math-sm" fill="var(--red)">ρ<tspan baseline-shift="sub" font-size="10">g</tspan> = d<tspan baseline-shift="sub" font-size="10">g</tspan>(Y,∂𝒱)</text>')
    parts.append(f'<path d="M{px+30} {py+270}H{px+230}" class="flow-control" stroke-width="2.8"/>')
    parts.append(f'<text x="{px+248}" y="{py+276}" class="math-sm" fill="var(--control)">u*</text>')
    parts.append(f'<text x="{px+30}" y="{py+350}" class="s">violet = mathematical model · cyan = state/inference · green = viable · dashed red = critical · light sky blue = intervention</text>')
    parts.append(f'<text x="{px+30}" y="{py+382}" class="s">current research transition · {escape(focus["transition"])}</text>')
    parts.append('<text x="56" y="675" class="s">Mathematical art is explanatory: motion is not a measured flow, level sets are not fitted telemetry, and RGB does not increase evidence strength.</text>')
    parts.append('</svg>')
    return "\n".join(parts)

def render_state(state: dict, observed: dict, dark: bool) -> str:
    repos = observed.get("repositories", [])
    active = [r for r in repos if r.get("status") == "active" and not r.get("archived")]
    featured = [r for r in active if r.get("featured")]
    focus = state["current_focus"]
    parts = [svg_open(1400, 480, "Governed living research state", "Research-state panel using green for viable/sustainable state, red for boundaries or criticality, and cyan control for causal transitions.", base_style(dark))]
    parts.append('<rect x="1" y="1" width="1398" height="478" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    label(parts, 48, 35, 230, "CURRENT RESEARCH STATE", "green")
    parts.append('<text x="48" y="108" class="h" fill="var(--green)">Power ↔ Transportation</text>')
    parts.append('<text x="48" y="137" class="m">Information + Organization as supporting non-physical layers</text>')
    parts.append('<line x1="48" y1="165" x2="1352" y2="165" stroke="var(--line)"/>')
    label(parts, 48, 190, 255, "ACTIVE FORMAL TRANSITION", "control")
    parts.append(f'<text x="48" y="260" class="v" fill="var(--control-ink)">{escape(focus["transition"])}</text>')
    parts.append('<path d="M48 286H555" class="flow-control" stroke-width="3"/>')
    parts.append(f'<text x="48" y="320" class="m">{escape(focus["label"])}</text>')
    label(parts, 720, 190, 230, "MATHEMATICAL SIGNATURE", "green")
    parts.append('<text x="720" y="260" class="math" fill="var(--green)">R_phys → C → (G, I_ij) → F_G → V → ρ_g → u*</text>')
    parts.append('<path d="M720 286H1265" class="flow-green" stroke-width="2.7"/>')
    parts.append('<text x="720" y="320" class="s">public activity cannot promote a scientific claim</text>')
    cards = [
        (48,355,250,"PUBLIC SYSTEMS",f"{len(active):02d}","allowlisted","green"),
        (330,355,250,"FEATURED",f"{len(featured):02d}","research-facing","control"),
        (612,355,350,"STATE VERIFIED",fmt_date(state.get("last_verified")),"declared configuration","green"),
        (1002,355,350,"EVIDENCE OBSERVED",fmt_date(observed.get("generated_at")),"public metadata","red"),
    ]
    for x,y,w,t,v,sub,kind in cards:
        cls=f"label-{kind}"; color={"green":"var(--green)","red":"var(--red)","control":"var(--control-ink)"}[kind]
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="86" rx="16" class="{cls}" stroke-width="1"/>')
        parts.append(f'<text x="{x+18}" y="{y+28}" class="k" fill="{color}">{escape(t)}</text>')
        parts.append(f'<text x="{x+18}" y="{y+60}" class="v" fill="{color}">{escape(v)}</text>')
        parts.append(f'<text x="{x+w-18}" y="{y+60}" text-anchor="end" class="s">{escape(sub)}</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def render_pipeline(state: dict, framework: dict) -> str:
    stages=framework["stages"]
    active=set(state["current_focus"]["active_stages"])
    parts=[svg_open(
        1400,400,
        "Seven-stage research architecture",
        "Seven-stage RGB-derived research progression. Stage colors progress red, magenta, green, cyan, blue, magenta and neutral white; active causal-to-dynamics transition remains explicitly marked.",
        base_style(None),
    )]
    parts.append('<rect x="1" y="1" width="1398" height="398" rx="18" fill="var(--bg)" stroke="var(--line)"/>')
    parts.append('<text x="48" y="51" class="k">FORMAL RESEARCH ARCHITECTURE</text>')
    parts.append('<text x="48" y="82" class="s">RGB progression is a visual navigation system, not a scientific ontology or evidence scale.</text>')
    xs=[90,285,480,675,870,1065,1260]; y=190
    parts.append(f'<path d="M{xs[0]} {y}H{xs[-1]}" fill="none" stroke="var(--line)" stroke-width="2"/>')
    parts.append(f'<path d="M{xs[1]} {y}H{xs[2]}" fill="none" class="flow-control" stroke-width="4"/>')
    colors=["var(--power)","var(--organization)","var(--transport)","var(--control)","var(--information)","var(--magenta)","var(--topology)"]
    fills=["var(--power-soft)","var(--organization-soft)","var(--transport-soft)","var(--control-soft)","var(--information-soft)","var(--magenta-soft)","var(--panel)"]
    text_colors=["var(--power)","var(--organization-ink)","var(--transport)","var(--control)","var(--information)","var(--magenta)","var(--ink)"]
    for idx,stage in enumerate(stages):
        sid=int(stage["id"]); x=xs[idx]
        sw=3.2 if sid in active else 1.8
        parts.append(f'<circle cx="{x}" cy="{y}" r="27" fill="{fills[idx]}" stroke="{colors[idx]}" stroke-width="{sw}"/>')
        parts.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" class="k" fill="{text_colors[idx]}">0{sid}</text>')
        words=stage["display_label"].split()
        split=max(1,min(len(words)-1,len(words)//2)) if len(words)>2 else len(words)
        line1=" ".join(words[:split]); line2=" ".join(words[split:]) if split<len(words) else ""
        parts.append(f'<text x="{x}" y="{y+61}" text-anchor="middle" class="s">{escape(line1)}</text>')
        if line2:
            parts.append(f'<text x="{x}" y="{y+79}" text-anchor="middle" class="s">{escape(line2)}</text>')
        parts.append(f'<text x="{x}" y="{y-48}" text-anchor="middle" class="math-sm" fill="{text_colors[idx]}">{escape(str(stage["symbol"]))}</text>')
    parts.append('<line x1="48" y1="326" x2="1352" y2="326" stroke="var(--line)"/>')
    parts.append('<text x="48" y="359" class="k" fill="var(--control-ink)">CURRENT TRANSITION</text>')
    parts.append(f'<text x="255" y="360" class="v">{escape(state["current_focus"]["transition"])}</text>')
    parts.append('</svg>')
    return "\n".join(parts)

def render_projects(observed: dict) -> str:
    repos=sorted(observed["repositories"],key=lambda x:int(x["profile_order"]))
    recent=max(repos,key=lambda x:timestamp((x.get("latest_commit") or {}).get("date") or x.get("pushed_at"))) if repos else None
    parts=[svg_open(1400,610,"Observed public research systems","Public research systems using green for active featured work, cyan control for the most recent public change, and red only for inactive or critical status.",base_style(None))]
    parts.append('<rect x="1" y="1" width="1398" height="608" rx="28" fill="var(--bg)" stroke="var(--line)"/>')
    label(parts,48,28,310,"SELECTED PUBLIC RESEARCH SYSTEMS","green")
    parts.append(f'<text x="48" y="84" class="s">observed {escape(fmt_date(observed.get("generated_at")))} · explicit public allowlist only</text>')
    for idx,repo in enumerate(repos):
        col,row=idx%3,idx//3; x,y=48+col*442,116+row*220
        is_recent=recent is not None and repo.get("repository")==recent.get("repository")
        is_featured=bool(repo.get("featured")); active=str(repo.get("status"))=="active"
        if not active: kind,color="red","var(--red)"
        elif is_recent: kind,color="control","var(--control)"
        elif is_featured: kind,color="green","var(--green)"
        else: kind,color="green","var(--line)"
        cls="latest" if is_recent else ""
        fill={"red":"var(--red-soft)","control":"var(--control-soft)","green":"var(--panel)"}[kind]
        parts.append(f'<rect x="{x}" y="{y}" width="408" height="190" rx="18" fill="{fill}" stroke="{color}" stroke-width="{3 if is_recent else (2 if is_featured else 1)}" class="{cls}"/>')
        tag="MOST RECENT PUBLIC CHANGE" if is_recent else ("FEATURED" if is_featured else "SUPPORTING")
        parts.append(f'<text x="{x+20}" y="{y+30}" class="k" fill="{color}">0{int(repo["profile_order"])} · {tag}</text>')
        parts.append(f'<text x="{x+20}" y="{y+66}" font-size="20" font-weight="780">{escape(str(repo["short_name"]))}</text>')
        words=str(repo.get("research_role","")).split()
        parts.append(f'<text x="{x+20}" y="{y+96}" class="m">{escape(" ".join(words[:7]))}</text>')
        parts.append(f'<text x="{x+20}" y="{y+118}" class="m">{escape(" ".join(words[7:14]))}</text>')
        commit=repo.get("latest_commit") or {}; latest=fmt_date(commit.get("date") or repo.get("pushed_at")); lang=repo.get("language") or "mixed / unspecified"
        parts.append(f'<text x="{x+20}" y="{y+154}" class="s">{escape(str(lang))} · latest public commit {escape(latest)}</text>')
        parts.append(f'<text x="{x+20}" y="{y+176}" class="s">public · {escape(str(repo.get("status")))}</text>')
    parts.append('<text x="48" y="582" class="s">Cyan-control pulse = most recent public change. Recency is not scientific importance, quality, or empirical validation.</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def main() -> int:
    state=load("research-state.json"); framework=load("framework.json"); observed=load("public-github-state.json")
    write("research-hero-light.svg",render_hero(state,observed,False))
    write("research-hero-dark.svg",render_hero(state,observed,True))
    write("research-state-light.svg",render_state(state,observed,False))
    write("research-state-dark.svg",render_state(state,observed,True))
    write("research-pipeline.svg",render_pipeline(state,framework))
    write("project-system.svg",render_projects(observed))
    print("Rendered publication-style sRGB mathematical-art profile assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
