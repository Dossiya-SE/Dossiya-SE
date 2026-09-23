# Mathematical Art V5 Specification

**Architecture ID:** MATH-ART-V5

```text
DEFINITION
→ SYMBOLIC / ANALYTIC REPRESENTATION
→ NUMERICAL REALIZATION
→ GEOMETRIC PRIMITIVES
→ VISUAL ENCODING
→ MOTION ENCODING
→ VERIFICATION
→ EXPORT
```

## Figure classes

A source/definition; B derived; C computed; D empirical; E hybrid.

## Required manifest

Stable figure ID, scientific role, evidence state, mathematical definition, domain/assumptions, units, coordinate system, generator/master, semantic encoding, motion variable, verification oracle/tolerance, export targets, provenance hashes and limitations.

## Priority V5 animations

1. Frenet frame traversal (`s`).
2. Geodesic integration (`s`).
3. Laplace–Beltrami heat flow (`t_model`).
4. Graph → dynamics → viability structural reveal (`tau_ui`).
5. Viability margin/control intervention (`lambda` or `t_model`).
6. Fixed-geometry 3D orbit (`theta`, camera only).

## Acceptance

Computed figures require independent oracles where practical and deterministic regeneration. Animation may not create a stronger claim than the static master.

V4 is replaced only when V5 mathematical verification, accessibility, deterministic reproduction and semantic documentation are at least as strong.
