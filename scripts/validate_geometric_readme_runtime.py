#!/usr/bin/env python3
"""Raster-test GEOMETRIC-README-V2 final SVGs at GitHub widths."""
from __future__ import annotations
import re,sys
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

def require(ok,msg):
    if not ok: raise ValueError(msg)

def materialize_css_vars(text: str) -> str:
    m=re.search(r":root\\{([^}]*)\\}",text)
    require(m is not None,"missing :root CSS variables")
    values={}
    for item in m.group(1).split(";"):
        if ":" not in item: continue
        k,v=item.split(":",1)
        k=k.strip()
        if k.startswith("--"): values[k[2:]]=v.strip()
    def repl(match):
        key=match.group(1)
        require(key in values,f"unresolved CSS variable --{key}")
        return values[key]
    out=re.sub(r"var\\(--([a-z0-9-]+)\\)",repl,text,flags=re.I)
    require("var(--" not in out,"unresolved CSS variable remains")
    return out

def main():
    PRE.mkdir(parents=True,exist_ok=True)
    for name in FILES:
        text=(OUT/name).read_text(encoding="utf-8")
        raster_text=materialize_css_vars(text,name)
        vb=re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"',text)
        require(vb is not None,f"{name}: simple viewBox required")
        w0,h0=map(float,vb.groups())
        for width in WIDTHS:
            height=max(1,round(width*h0/w0))
            out=PRE/f"{name[:-4]}-{width}px.png"
            cairosvg.svg2png(bytestring=raster_text.encode(),write_to=str(out),output_width=width,output_height=height)
            with Image.open(out) as im:
                require(im.size==(width,height),f"{name}: raster size mismatch at {width}")
                rgb=im.convert("RGB")
                extrema=rgb.getextrema()
                spread=sum(hi-lo for lo,hi in extrema)
                require(spread>45,f"{name}: raster appears visually empty/flat at {width}")
    print("GEOMETRIC README RUNTIME VALIDATION: PASS — all final visuals rasterize at 980 px and 640 px.")
    return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except (OSError,ValueError) as e:
        print(f"GEOMETRIC README RUNTIME VALIDATION: FAIL — {e}",file=sys.stderr); raise SystemExit(1)
