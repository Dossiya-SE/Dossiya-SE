#!/usr/bin/env python3
"""Raster-test all PROFILE-GEOMETRY-V3 README visuals at GitHub widths."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

import cairosvg
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"assets"/"generated"
DATA=ROOT/"data"
PREVIEW=ROOT/"artifacts"/"geometry-v3-preview"
WIDTHS=(980,640)

CASES={
    "research-hero-light.svg":("light",("power","transport","violet","green","red","control")),
    "research-hero-dark.svg":("dark",("power","transport","violet","green","red","control")),
    "research-question.svg":("light",("power","transport","information","green","control")),
    "coupled-network-3d-light.svg":("light",("power","transport","green","red","control")),
    "coupled-network-3d-dark.svg":("dark",("power","transport","green","red","control")),
    "graph-to-viability.svg":("light",("violet","green","red","control")),
    "research-state-light.svg":("light",("power","transport","information","cyan","control")),
    "research-state-dark.svg":("dark",("power","transport","information","cyan","control")),
    "project-system.svg":("light",("violet","information","transport","cyan")),
    "research-pipeline.svg":("light",("power","organization","transport","cyan","information","magenta")),
}

def require(ok:bool,msg:str)->None:
    if not ok:
        raise ValueError(msg)

def rgb(value:str)->tuple[int,int,int]:
    h=value.lstrip("#")
    return tuple(int(h[i:i+2],16) for i in (0,2,4))

def materialize(svg:str,values:dict)->str:
    def repl(m:re.Match[str])->str:
        key=m.group(1).replace("-","_")
        require(key in values,f"unknown palette token --{m.group(1)}")
        return values[key]
    return re.sub(r"var\(--([a-z0-9-]+)\)",repl,svg,flags=re.I)

def color_pixels(im:Image.Image,target:tuple[int,int,int],tol:int=26)->int:
    total=0
    for px in im.convert("RGB").getdata():
        if max(abs(px[i]-target[i]) for i in range(3))<=tol:
            total+=1
    return total

def density(im:Image.Image,bg:tuple[int,int,int])->float:
    changed=0
    pix=list(im.convert("RGB").getdata())
    for px in pix:
        if math.sqrt(sum((px[i]-bg[i])**2 for i in range(3)))>18:
            changed+=1
    return changed/max(1,len(pix))

def viewbox(text:str)->tuple[float,float]:
    root=ET.fromstring(text)
    vb=root.attrib.get("viewBox","").split()
    require(len(vb)==4,"invalid viewBox")
    return float(vb[2]),float(vb[3])

def validate_asset(name:str,mode:str,roles:tuple[str,...],palette:dict)->None:
    path=OUT/name
    require(path.exists(),f"missing asset {name}")
    text=path.read_text(encoding="utf-8")
    vw,vh=viewbox(text)
    values=palette[mode]
    source=materialize(text,values).encode("utf-8")
    PREVIEW.mkdir(parents=True,exist_ok=True)

    for width in WIDTHS:
        height=max(1,round(width*vh/vw))
        out=PREVIEW/f"{path.stem}-{mode}-{width}px.png"
        cairosvg.svg2png(bytestring=source,write_to=str(out),output_width=width,output_height=height)
        with Image.open(out) as im:
            require(im.size==(width,height),f"{name}: raster size mismatch at {width}px")
            require(im.getbbox() is not None,f"{name}: blank raster at {width}px")
            bg=rgb(values["bg"])
            require(density(im,bg)>.018,f"{name}: visual density too low at {width}px")
            threshold=max(5,int(width*height*0.000006))
            for role in roles:
                require(color_pixels(im,rgb(values[role]))>=threshold,f"{name}: {role} cue lost at {width}px")

def main()->int:
    palette=json.loads((DATA/"visual-palette.json").read_text(encoding="utf-8"))
    for name,(mode,roles) in CASES.items():
        validate_asset(name,mode,roles,palette)
    print("PROFILE GEOMETRY V3 RUNTIME: PASS — all README visuals survive 980/640 px rasterization with governed semantic cues.")
    return 0

if __name__=="__main__":
    try:
        raise SystemExit(main())
    except (OSError,ValueError,ET.ParseError) as exc:
        print(f"PROFILE GEOMETRY V3 RUNTIME: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
