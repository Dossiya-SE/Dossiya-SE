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
