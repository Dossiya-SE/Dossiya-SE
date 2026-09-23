# Polyglot Flat Geometry

Contract: **FLAT-GEOMETRY-V1**

This directory contains reproducible implementations of the same mathematical primitives used by the GitHub profile figure.

- `overleaf/flat_geometry.tex` — canonical publication composition in TikZ.
- `julia/flat_geometry.jl` — numerical geometry primitives.
- `react/FlatGeometry.tsx` + `flat-geometry.css` — interactive SVG mirror.
- `go/main.go` — dependency-light static SVG generation.
- `csharp/FlatGeometry.cs` — C# geometry/integration mirror.
- `../../scripts/render_flat_geometry.py` — authoritative GitHub SVG renderer.

The shared mathematical definitions live in `../../data/flat-geometry.json`.

## Invariant

All implementations must preserve:

[
p_j=c+r(cos(2pi j/n),sin(2pi j/n)),
]

[
F=x_0+operatorname{span}{v_1,ldots,v_k},
]

and

[
d(x,H)=rac{|a^	op x-b|}{|a|_2}.
]

Visual differences are allowed; mathematical definitions are not.

## Runtime release gate

GitHub CI rasterizes the governed SVG at **980 px** and **640 px** in both **light** and **dark** palettes. The release gate checks that all three visual fields remain non-empty and that violet mathematical structure, green admissibility, dashed red criticality, and the Light Sky Blue orthogonal-projection cue survives rasterization, using a contrast-safe light-background stroke where required.

The projection shown in the hyperplane panel is an actual orthogonal projection onto the displayed line, not a decorative connector.

