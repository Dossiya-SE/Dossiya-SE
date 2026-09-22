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

def main():
    PRE.mkdir(parents=True,exist_ok=True)
    for name in FILES:
        text=(OUT/name).read_text(encoding="utf-8")
        vb=re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"',text)
        require(vb is not None,f"{name}: simple viewBox required")
        w0,h0=map(float,vb.groups())
        for width in WIDTHS:
            height=max(1,round(width*h0/w0))
            out=PRE/f"{name[:-4]}-{width}px.png"
            cairosvg.svg2png(bytestring=text.encode(),write_to=str(out),output_width=width,output_height=height)
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
