#!/usr/bin/env python3
"""G6 raster-test SCIENTIFIC-GEOMETRY-V3 final SVGs at GitHub widths.

Explicit light/dark SVG files are rendered in their governed root mode.
Adaptive single-file SVGs are rendered twice: once with the light :root and
once with the prefers-color-scheme:dark variable set materialized.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import cairosvg
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"assets"/"generated"
PRE=ROOT/"artifacts"/"geometric-readme-preview"

FILES=[
    "research-hero-light.svg","research-hero-dark.svg","research-question.svg",
    "coupled-network-3d-light.svg","coupled-network-3d-dark.svg","graph-to-viability.svg",
    "research-state-light.svg","research-state-dark.svg","project-system.svg","research-pipeline.svg"
]
WIDTHS=(980,640)

DARK_MEDIA_RE=re.compile(
    r"@media\(prefers-color-scheme:dark\)\{:root\{([^}]*)\}\}",
    flags=re.I,
)
ROOT_RE=re.compile(r":root\{([^}]*)\}",flags=re.I)


def require(ok,msg):
    if not ok:
        raise ValueError(msg)


def parse_vars(block: str) -> dict[str,str]:
    values={}
    for item in block.split(";"):
        if ":" not in item:
            continue
        k,v=item.split(":",1)
        k=k.strip()
        if k.startswith("--"):
            values[k[2:]]=v.strip()
    return values


def variable_sets(text: str, name: str) -> tuple[dict[str,str],dict[str,str]|None]:
    root=ROOT_RE.search(text)
    require(root is not None,f"{name}: missing :root CSS variables")
    light=parse_vars(root.group(1))
    dark_match=DARK_MEDIA_RE.search(text)
    dark=parse_vars(dark_match.group(1)) if dark_match else None
    return light,dark


def materialize_css_vars(text: str, name: str, values: dict[str,str]) -> str:
    def repl(match):
        key=match.group(1)
        require(key in values,f"{name}: unresolved CSS variable --{key}")
        return values[key]

    out=re.sub(r"var\(--([a-z0-9-]+)\)",repl,text,flags=re.I)
    require("var(--" not in out,f"{name}: unresolved CSS variable remains")
    return out


def render_checked(name: str, text: str, values: dict[str,str], width: int, suffix: str="") -> None:
    raster_text=materialize_css_vars(text,name,values)
    vb=re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"',text)
    require(vb is not None,f"{name}: simple viewBox required")
    w0,h0=map(float,vb.groups())
    height=max(1,round(width*h0/w0))
    stem=name[:-4]
    out=PRE/f"{stem}{suffix}-{width}px.png"
    cairosvg.svg2png(
        bytestring=raster_text.encode(),
        write_to=str(out),
        output_width=width,
        output_height=height,
    )
    with Image.open(out) as im:
        require(im.size==(width,height),f"{name}{suffix}: raster size mismatch at {width}")
        rgb=im.convert("RGB")
        extrema=rgb.getextrema()
        spread=sum(hi-lo for lo,hi in extrema)
        require(spread>45,f"{name}{suffix}: raster appears visually empty/flat at {width}")


def main():
    PRE.mkdir(parents=True,exist_ok=True)
    for stale in PRE.glob("*.png"):
        stale.unlink()

    adaptive_dark_count=0
    for name in FILES:
        text=(OUT/name).read_text(encoding="utf-8")
        light,dark=variable_sets(text,name)
        for width in WIDTHS:
            render_checked(name,text,light,width)
        if dark is not None:
            adaptive_dark_count += 1
            for width in WIDTHS:
                render_checked(name,text,dark,width,suffix="-adaptive-dark")

    generated=sorted(PRE.glob("*.png"))
    expected=len(FILES)*len(WIDTHS)+adaptive_dark_count*len(WIDTHS)
    require(len(generated)==expected,
            f"runtime preview count mismatch: expected {expected}, found {len(generated)}")
    require(adaptive_dark_count==4,
            f"expected four adaptive dark-mode SVGs, found {adaptive_dark_count}")

    print(
        "SCIENTIFIC GEOMETRY V3 RUNTIME: PASS — final visuals rasterize at "
        f"980 px and 640 px; {adaptive_dark_count} adaptive SVGs also pass explicit dark-mode rendering."
    )
    return 0


if __name__=="__main__":
    try:
        raise SystemExit(main())
    except (OSError,ValueError) as e:
        print(f"SCIENTIFIC GEOMETRY V3 RUNTIME: FAIL — {e}",file=sys.stderr)
        raise SystemExit(1)
