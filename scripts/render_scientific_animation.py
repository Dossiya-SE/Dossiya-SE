#!/usr/bin/env python3
"""Render deterministic RGB GIF camera-orbit animations from SCIENTIFIC-GEOMETRY-V3.

The animation changes viewpoint only. The underlying affine planes, nodes, edges,
and interlayer interface are fixed across all frames. It is not physical time,
simulated infrastructure dynamics, measured flow, or live telemetry.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
OUT=ROOT/"assets"/"generated"
ART=ROOT/"artifacts"

GEOM=DATA/"computed-geometry-v3.json"
PALETTE=DATA/"visual-palette.json"
SPEC=DATA/"animation-spec.json"
META=ART/"animation-metadata.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()


def rgb(palette: dict, mode: str, key: str) -> tuple[int,int,int]:
    values=palette["rgb_values"][mode][key]
    return tuple(int(v) for v in values)


def rotation_matrix(azimuth_deg: float, elevation_deg: float) -> np.ndarray:
    a=math.radians(azimuth_deg)
    e=math.radians(elevation_deg)
    ca,sa=math.cos(a),math.sin(a)
    ce,se=math.cos(e),math.sin(e)
    rz=np.array([[ca,-sa,0.0],[sa,ca,0.0],[0.0,0.0,1.0]],dtype=float)
    rx=np.array([[1.0,0.0,0.0],[0.0,ce,-se],[0.0,se,ce]],dtype=float)
    return rx@rz


def project(points: np.ndarray, center: np.ndarray, R: np.ndarray, scale: float, cx: float, cy: float) -> tuple[np.ndarray,np.ndarray]:
    q=(np.asarray(points,dtype=float)-center)@R.T
    screen=np.column_stack([cx+scale*q[:,0],cy-scale*q[:,2]])
    depth=q[:,1]
    return screen,depth


def regular_polygon(cx: float, cy: float, r: float, n: int) -> list[tuple[float,float]]:
    return [
        (cx+r*math.cos(-math.pi/2+2*math.pi*j/n),
         cy+r*math.sin(-math.pi/2+2*math.pi*j/n))
        for j in range(n)
    ]


def dashed_line(draw: ImageDraw.ImageDraw, a: tuple[float,float], b: tuple[float,float], *, fill, width: int, dash: int, gap: int) -> None:
    x1,y1=a; x2,y2=b
    dx,dy=x2-x1,y2-y1
    length=math.hypot(dx,dy)
    if length<=1e-9:
        return
    ux,uy=dx/length,dy/length
    s=0.0
    while s<length:
        e=min(length,s+dash)
        draw.line((x1+ux*s,y1+uy*s,x1+ux*e,y1+uy*e),fill=fill,width=width)
        s+=dash+gap


def fixed_palette(palette: dict, mode: str) -> Image.Image:
    source=palette["rgb_values"][mode]
    bg=np.array(source["bg"],dtype=float)
    keys=[
        "ink","muted","line","topology","power","power_soft",
        "transport","transport_soft","information","information_soft",
        "organization","organization_soft","control","control_soft",
        "cyan","cyan_soft","violet","violet_soft","magenta","magenta_soft",
        "green","green_soft","red","red_soft","ghost","panel",
    ]
    colors=[]
    seen=set()
    def add(c):
        t=tuple(max(0,min(255,int(round(v)))) for v in c)
        if t not in seen:
            seen.add(t); colors.append(t)
    accent_contract=palette.get("accent_contract",{})
    for key in ("primary","strong","on_light_graphic","on_light_text","on_dark_text"):
        spec=accent_contract.get(key,{})
        if "rgb" in spec:
            add(spec["rgb"])
    for triplet in source.values():
        add(triplet)
    for key in keys:
        target=np.array(source[key],dtype=float)
        for s in np.linspace(0.0,1.0,10):
            add((1-s)*bg+s*target)
    for v in np.linspace(0,255,48):
        add((v,v,v))
    colors=colors[:256]
    while len(colors)<256:
        colors.append(colors[-1] if colors else (0,0,0))
    pal=Image.new("P",(1,1))
    pal.putpalette([v for c in colors for v in c])
    return pal


def scene_data(g: dict) -> dict:
    c=g["coupled"]
    power_nodes=np.asarray(c["power_nodes_3d"],dtype=float)
    transport_nodes=np.asarray(c["transport_nodes_3d"],dtype=float)
    power_plane=np.asarray(g["hero"]["power_plane"]["corners_3d"],dtype=float)
    transport_plane=np.asarray(g["hero"]["transport_plane"]["corners_3d"],dtype=float)
    interface=np.asarray(c["interface_segment_3d"],dtype=float)
    all_points=np.vstack([power_nodes,transport_nodes,power_plane,transport_plane,interface])
    center=all_points.mean(axis=0)
    radius=float(np.max(np.linalg.norm(all_points-center,axis=1)))
    if not math.isfinite(radius) or radius<=0:
        raise ValueError("animation scene radius must be positive and finite")
    return {
        "power_nodes":power_nodes,
        "transport_nodes":transport_nodes,
        "power_plane":power_plane,
        "transport_plane":transport_plane,
        "interface":interface,
        "power_edges":c["power_edges"],
        "transport_edges":c["transport_edges"],
        "center":center,
        "radius":radius,
    }


def render_frame(g: dict, palette: dict, spec: dict, mode: str, k: int) -> Image.Image:
    frame=spec["frame"]
    N=int(frame["frame_count"])
    ss=int(frame["supersampling"])
    W=int(frame["width_px"]); H=int(frame["height_px"])
    t=k/N

    azimuth=360.0*t
    elevation=24.0+5.0*math.sin(2.0*math.pi*t)
    R=rotation_matrix(azimuth,elevation)

    s=scene_data(g)
    scale=0.34*min(W,H)*ss/s["radius"]
    cx,cy=0.50*W*ss,0.52*H*ss

    bg=rgb(palette,mode,"bg")
    panel=rgb(palette,mode,"panel")
    ink=rgb(palette,mode,"ink")
    muted=rgb(palette,mode,"muted")
    line=rgb(palette,mode,"line")
    power=rgb(palette,mode,"power")
    power_soft=rgb(palette,mode,"power_soft")
    transport=rgb(palette,mode,"transport")
    transport_soft=rgb(palette,mode,"transport_soft")
    control=rgb(palette,mode,"control")
    control_soft=rgb(palette,mode,"control_soft")
    accent_primary=tuple(int(v) for v in palette["accent_contract"]["primary"]["rgb"])

    image=Image.new("RGB",(W*ss,H*ss),bg)
    draw=ImageDraw.Draw(image)

    projected={}
    depths={}
    for key in ("power_plane","transport_plane","power_nodes","transport_nodes","interface"):
        projected[key],depths[key]=project(s[key],s["center"],R,scale,cx,cy)

    planes=[
        (float(depths["power_plane"].mean()),"power_plane",power_soft,power),
        (float(depths["transport_plane"].mean()),"transport_plane",transport_soft,transport),
    ]
    for _,key,fill,stroke in sorted(planes,key=lambda x:x[0],reverse=True):
        poly=[tuple(p) for p in projected[key]]
        draw.polygon(poly,fill=fill)
        draw.line(poly+[poly[0]],fill=stroke,width=2*ss,joint="curve")

    def draw_edges(edge_list,node_key,color):
        pts=projected[node_key]
        for a,b in edge_list:
            draw.line((tuple(pts[a]),tuple(pts[b])),fill=color,width=3*ss)

    draw_edges(s["power_edges"],"power_nodes",power)
    draw_edges(s["transport_edges"],"transport_nodes",transport)

    power_sides=(3,4,5,6,4)
    transport_sides=(4,6,5,3,6)
    for pts2,sides,color in (
        (projected["power_nodes"],power_sides,power),
        (projected["transport_nodes"],transport_sides,transport),
    ):
        for (x,y),n in zip(pts2,sides):
            poly=regular_polygon(float(x),float(y),11*ss,int(n))
            draw.polygon(poly,fill=panel)
            draw.line(poly+[poly[0]],fill=color,width=3*ss,joint="curve")

    a,b=map(tuple,projected["interface"])
    # Contrast-safe underlay + exact Light Sky Blue overlay.
    dashed_line(draw,a,b,fill=control,width=6*ss,dash=9*ss,gap=7*ss)
    dashed_line(draw,a,b,fill=accent_primary,width=3*ss,dash=9*ss,gap=7*ss)
    mx,my=(a[0]+b[0])/2,(a[1]+b[1])/2
    h=regular_polygon(mx,my,17*ss,6)
    draw.polygon(h,fill=control_soft)
    draw.line(h+[h[0]],fill=control,width=5*ss,joint="curve")
    draw.line(h+[h[0]],fill=accent_primary,width=2*ss,joint="curve")

    # Neutral reference ring: camera/viewpoint cue only, not physical geometry.
    r=0.39*min(W,H)*ss
    draw.ellipse((cx-r,cy-r,cx+r,cy+r),outline=line,width=1*ss)

    if ss>1:
        image=image.resize((W,H),Image.Resampling.LANCZOS)

    # Text is drawn after downsampling with Pillow's bundled default font so the
    # release does not depend on system font files.
    draw=ImageDraw.Draw(image)
    font1=ImageFont.load_default(size=18)
    font2=ImageFont.load_default(size=13)
    draw.text((22,18),"COMPUTED R3 AFFINE SYSTEM",fill=ink,font=font1)
    draw.text((22,44),"RGB CAMERA ORBIT",fill=muted,font=font2)
    draw.text((22,H-42),"CAMERA MOTION ONLY · NOT PHYSICAL TIME",fill=muted,font=font2)

    y=74
    legend=(("POWER",power),("TRANSPORT",transport),("INTERFACE / CONTROL",accent_primary))
    for label,color in legend:
        draw.line((24,y+6,54,y+6),fill=color,width=4)
        draw.text((64,y),label,fill=ink,font=font2)
        y+=24

    return image


def save_mode(g: dict, palette: dict, spec: dict, mode: str, out_path: Path) -> list[str]:
    frame=spec["frame"]
    N=int(frame["frame_count"])
    duration=int(frame["frame_duration_ms"])
    master=fixed_palette(palette,mode)

    frames=[]
    hashes=[]
    for k in range(N):
        rgb_frame=render_frame(g,palette,spec,mode,k)
        p=rgb_frame.quantize(palette=master,dither=Image.Dither.NONE)
        frames.append(p)
        hashes.append(hashlib.sha256(p.tobytes()).hexdigest())

    out_path.parent.mkdir(parents=True,exist_ok=True)
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=int(frame["loop"]),
        disposal=2,
        optimize=False,
    )
    return hashes


def main() -> int:
    g=load(GEOM)
    palette=load(PALETTE)
    spec=load(SPEC)

    if g.get("contract_id")!=spec["source_geometry_contract"]:
        raise ValueError("animation source geometry contract mismatch")
    if palette.get("color_model")!="RGB" or palette.get("color_space")!="sRGB":
        raise ValueError("animation requires governed RGB/sRGB palette")

    ART.mkdir(parents=True,exist_ok=True)
    output_hashes={}
    frame_hashes={}
    for mode in ("light","dark"):
        out=ROOT/spec["outputs"][mode]
        frame_hashes[mode]=save_mode(g,palette,spec,mode,out)
        output_hashes[mode]=sha256(out)

    R0=rotation_matrix(0.0,24.0)
    R1=rotation_matrix(360.0,24.0)
    periodic_residual=float(np.linalg.norm(R0-R1))

    metadata={
        "contract_id":spec["contract_id"],
        "source_geometry_contract":g["contract_id"],
        "animation_semantics":spec["animation_semantics"],
        "color_model":palette["color_model"],
        "color_space":palette["color_space"],
        "frame_count":int(spec["frame"]["frame_count"]),
        "frame_duration_ms":int(spec["frame"]["frame_duration_ms"]),
        "effective_fps":float(spec["frame"]["effective_fps"]),
        "size_px":[int(spec["frame"]["width_px"]),int(spec["frame"]["height_px"])],
        "periodic_rotation_residual":periodic_residual,
        "source_sha256":{
            "geometry":sha256(GEOM),
            "palette":sha256(PALETTE),
            "spec":sha256(SPEC),
        },
        "output_sha256":output_hashes,
        "frame_pixel_sha256":frame_hashes,
        "scientific_boundary":spec["scientific_boundary"],
    }
    META.write_text(json.dumps(metadata,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("SCIENTIFIC ANIMATION RENDER: PASS — deterministic RGB camera-orbit GIFs generated.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
