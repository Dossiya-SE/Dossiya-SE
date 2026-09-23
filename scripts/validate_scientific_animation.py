#!/usr/bin/env python3
"""Validate SCIENTIFIC-ANIMATION-V1 GIF timing, motion, palette and provenance."""

from __future__ import annotations

import colorsys
import hashlib
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageStat

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
ART=ROOT/"artifacts"
SPEC=DATA/"animation-spec.json"
PALETTE=DATA/"visual-palette.json"
GEOM=DATA/"computed-geometry-v3.json"
META=ART/"animation-metadata.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()


def hue_sat(rgb: tuple[int,int,int]) -> tuple[float,float]:
    r,g,b=(v/255 for v in rgb)
    h,s,_=colorsys.rgb_to_hsv(r,g,b)
    return 360*h,s


def image_difference(a: Image.Image, b: Image.Image) -> float:
    diff=ImageChops.difference(a.convert("RGB"),b.convert("RGB"))
    stat=ImageStat.Stat(diff)
    return sum(stat.mean)/3.0


def validate_gif(path: Path, spec: dict, mode: str) -> dict:
    require(path.exists(),f"{mode}: GIF missing")
    frame_spec=spec["frame"]
    forbidden=spec["color"]
    h0,h1=map(float,forbidden["prohibited_warm_hue_band_deg"])
    min_sat=float(forbidden["prohibited_minimum_saturation"])

    with Image.open(path) as im:
        require(bool(getattr(im,"is_animated",False)),f"{mode}: GIF must be animated")
        require(int(getattr(im,"n_frames",1))==int(frame_spec["frame_count"]),f"{mode}: frame count mismatch")
        require(im.size==(int(frame_spec["width_px"]),int(frame_spec["height_px"])),f"{mode}: GIF size mismatch")
        require(int(im.info.get("loop",-1))==int(frame_spec["loop"]),f"{mode}: loop setting mismatch")
        require(int(im.info.get("duration",-1))==int(frame_spec["frame_duration_ms"]),f"{mode}: frame duration mismatch")

        frames=[]
        max_unique=0
        max_step=0.0
        used_colors=set()
        for i in range(im.n_frames):
            im.seek(i)
            frame=im.convert("RGB").copy()
            frames.append(frame)
            colors=frame.getcolors(maxcolors=1_000_000)
            require(colors is not None,f"{mode}: frame {i} exceeds GIF palette limit")
            max_unique=max(max_unique,len(colors))
            for _,color in colors:
                used_colors.add(tuple(color))
            if i:
                max_step=max(max_step,image_difference(frames[i-1],frame))

        require(max_unique<=256,f"{mode}: GIF frame exceeds 256 colors")
        required_primary=tuple(int(v) for v in forbidden["required_primary_rgb"])
        require(required_primary in used_colors,f"{mode}: exact Light Sky Blue primary RGB{required_primary} missing from decoded GIF")
        for color in used_colors:
            hue,sat=hue_sat(color)
            if sat>=min_sat:
                require(not (h0<=hue<=h1),f"{mode}: forbidden warm-hue pixel {color} at {hue:.1f}°")

        quarter=frames[len(frames)//4]
        half=frames[len(frames)//2]
        motion_q=image_difference(frames[0],quarter)
        motion_h=image_difference(frames[0],half)
        seam=image_difference(frames[0],frames[-1])
        require(motion_q>1.0 and motion_h>1.0,f"{mode}: animation does not show meaningful viewpoint change")
        require(max_step<18.0,f"{mode}: consecutive-frame change too abrupt ({max_step:.2f})")
        require(seam<motion_q,f"{mode}: loop seam is larger than quarter-orbit motion")

    return {
        "sha256":sha256(path),
        "max_unique_colors":max_unique,
        "max_consecutive_mean_abs_difference":max_step,
        "quarter_orbit_difference":motion_q,
        "half_orbit_difference":motion_h,
        "loop_seam_difference":seam,
        "used_color_count":len(used_colors),
    }


def main() -> int:
    spec=load(SPEC)
    palette=load(PALETTE)
    meta=load(META)

    require(spec.get("contract_id")=="SCIENTIFIC-ANIMATION-V1","animation contract id mismatch")
    require(spec.get("animation_semantics")=="camera_orbit_only","animation must be viewpoint-only")
    require(spec.get("schema_version")=="1.1","animation schema must be 1.1")
    v5=spec.get("v5_alignment",{})
    require(v5.get("architecture_id")=="MATH-ART-V5","V5 animation architecture alignment missing")
    require(v5.get("figure_class")=="C_COMPUTED_CAMERA_DERIVATIVE","profile orbit must remain a computed camera derivative")
    require(v5.get("evidence_state")=="C","profile orbit evidence state must remain computed [C]")
    static=v5.get("static_authority",{})
    require(static.get("light")=="assets/generated/coupled-network-3d-light.svg","light static authority mismatch")
    require(static.get("dark")=="assets/generated/coupled-network-3d-dark.svg","dark static authority mismatch")
    motion=spec.get("motion_variable",{})
    require(motion.get("symbol")=="theta","camera motion variable must be theta")
    require(motion.get("physical_time") is False and motion.get("model_time") is False,"theta must not be interpreted as physical/model time")
    require(motion.get("mathematical_definition")=="theta=2*pi*k/N","camera parameter definition mismatch")
    accessibility=spec.get("accessibility",{})
    require(accessibility.get("static_master_complete") is True,"static scientific authority must remain complete")
    require(accessibility.get("essential_information_only_in_motion") is False,"motion may not carry exclusive scientific information")
    require(palette.get("color_model")=="RGB" and palette.get("color_space")=="sRGB","animation palette must be RGB/sRGB")
    accent=palette.get("accent_contract",{})
    require(accent.get("contract_id")=="LIGHT-SKY-BLUE-ACCENT-V1","Light Sky Blue accent contract missing")
    require(accent.get("primary",{}).get("rgb")==[135,206,250],"Light Sky Blue primary RGB mismatch")
    require(accent.get("strong",{}).get("rgb")==[0,191,255],"Deep Sky Blue strong RGB mismatch")
    require(meta.get("contract_id")==spec["contract_id"],"animation metadata contract mismatch")
    require(float(meta.get("periodic_rotation_residual",1.0))<1e-12,"camera orbit is not mathematically periodic")

    expected_sources={
        "geometry":sha256(GEOM),
        "palette":sha256(PALETTE),
        "spec":sha256(SPEC),
    }
    require(meta.get("source_sha256")==expected_sources,"animation source provenance hash mismatch")

    results={}
    for mode in ("light","dark"):
        path=ROOT/spec["outputs"][mode]
        results[mode]=validate_gif(path,spec,mode)
        require(meta["output_sha256"][mode]==results[mode]["sha256"],f"{mode}: output hash mismatch")

    # Light and dark outputs must encode the same motion but differ visually.
    require(results["light"]["sha256"]!=results["dark"]["sha256"],"light and dark GIF outputs must differ")

    report={
        "contract_id":spec["contract_id"],
        "status":"PASS",
        "results":results,
        "scientific_boundary":spec["scientific_boundary"],
    }
    (ART/"animation-validation.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("SCIENTIFIC ANIMATION VALIDATION: PASS — timing, motion, RGB palette, exact Light Sky Blue accent, loop continuity and provenance are valid.")
    return 0


if __name__=="__main__":
    try:
        raise SystemExit(main())
    except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:
        print(f"SCIENTIFIC ANIMATION VALIDATION: FAIL — {exc}",file=sys.stderr)
        raise SystemExit(1)
