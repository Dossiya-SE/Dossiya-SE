# Flat Geometry Visual System — FLAT-GEOMETRY-V1

## Purpose

This system turns elementary plane figures and advanced Euclidean/affine flats into one rigorous visual grammar for the GitHub research profile.

The bridge is **constraint geometry and state-space reasoning**. A triangle, pentagon or ellipse is **not** treated as an affine flat. Plane figures are bounded subsets or curves in a plane; an affine (k)-flat is an unbounded translated linear subspace.

## Mathematical contract

### Regular polygons

For an (n)-gon with center (c=(c_x,c_y)) and circumradius (r),

[
p_j
=
c+r
egin{bmatrix}
cos(2pi j/n)\\
sin(2pi j/n)
end{bmatrix},
qquad j=0,ldots,n-1.
]

The governed taxonomy includes triangle through decagon.

### Curved plane figures

[
	ext{circle: }(x-c_x)^2+(y-c_y)^2=r^2,
]

[
	ext{ellipse: }rac{(x-c_x)^2}{a^2}+rac{(y-c_y)^2}{b^2}=1,
]

and a semicircle is the corresponding circle restricted to one closed half-plane.

The profile uses **ellipse** as the precise mathematical term rather than treating “oval” as a unique formal object.

### Affine flats

A (k)-dimensional affine flat in (mathbb R^n) is

[
F=x_0+operatorname{span}{v_1,ldots,v_k},
]

with linearly independent (v_i). Point, line and plane correspond to (k=0,1,2).

A hyperplane is the ((n-1))-flat

[
H={xinmathbb R^n:a^	op x=b},qquad a
eq0,
]

with Euclidean point-to-hyperplane distance

[
d(x,H)=rac{|a^	op x-b|}{|a|_2}.
]

## Visual architecture

The final README figure has three fields:

1. **Plane geometry** — regular polygons and exact curved figures.
2. **Affine geometry** — point, line, plane and the general (k)-flat.
3. **Boundary geometry** — a hyperplane, signed side structure and geometric distance.

The third field connects naturally to viability and constrained engineering, but the figure itself remains mathematical and does not claim empirical calibration.

## Rendering authority

| Layer | Role |
|---|---|
| **TikZ / Overleaf** | publication-quality mathematical source |
| **Python** | deterministic GitHub SVG and validation authority |
| **Julia** | numerical geometry / vertex and distance computation |
| **React + CSS** | interactive web mirror |
| **Go** | dependency-light static renderer |
| **C#** | engineering/software integration mirror |

All implementations declare the contract ID `FLAT-GEOMETRY-V1`.

## Color discipline

The figure inherits the governed sRGB profile palette.

- neutral charcoal: geometric construction;
- violet: mathematical abstraction;
- green: admissible/viable side;
- dashed red: critical hyperplane/boundary;
- Light Sky Blue accent family: geometric projection/intervention cue; RGB(135,206,250) primary with contrast-safe light-background stroke RGB(45,143,214).

Color is redundant with labels, line pattern, shape and direction.

## Evidence boundary

This visual is a mathematical-definition figure. It is **not measured infrastructure behavior**, not live telemetry, and not evidence that a chosen metric or hyperplane is physically valid for a particular engineering system.
