# Scientific profile geometry

## SCIENTIFIC-GEOMETRY-V3

The primary README figures are generated from a governed computational geometry pipeline. Scientific coordinates are not hand-positioned in SVG.

```text
scientific-geometry-v3.toml
        ↓
SymPy
exact symbolic projection / equations
        ↓
NumPy + SciPy
rank · QR · SVD · conditioning · spline geometry
        ↓
Shapely
constraint intersections · feasible region · nearest boundary · area / centroid
        ↓
Julia / LinearAlgebra
independent rank · QR · projection · equal-area verification
        ↓
PyVista + Trimesh
3D multilayer scene / mesh validation where 3D is scientifically relevant
        ↓
computed-geometry-v3.json
        ├── TikZ / Overleaf publication representation
        └── Python deterministic SVG
                ↓
semantic + quantitative-layout + palette + raster gates
                ↓
README
```

## Tool allocation

| Existing README visual | Governing computation | Release representation |
|---|---|---|
| Research hero | affine rank/QR + Shapely viability + exact nearest-boundary projection | Python SVG; TikZ counterpart where mathematical construction is publication-relevant |
| Research question | minimal symbolic logic; geometric spacing checks | TikZ logic + Python SVG |
| Coupled physical system | R³ affine embedding, orthographic projection, PyVista/Trimesh scene validation | Python SVG |
| Graph → dynamics → viability | symbolic constraints + Shapely intersection + exact nearest-boundary distance | TikZ + Python SVG |
| Current research state | SVD projection of explicitly conceptual 4D state vectors | Python SVG |
| Research systems | equal-area regular polygons + Shapely area/centroid validation | Python SVG |
| Seven-stage architecture | SciPy continuous cubic spline `γ(t)` through seven anchors | TikZ + Python SVG |

## Non-negotiable invariants

1. **Scientific coordinates come from computation.** Manual coordinates may control framing, typography and panel placement, but not the mathematical state, boundary, projection, affine plane, 3D layer embedding, project area, research-state projection or continuous stage trajectory.
2. **Computed does not mean empirically validated.** Viability constraints and research-state vectors remain schematic until case-specific evidence supports calibration.
3. **The gold resilience-margin vector must be mathematically normal to the active critical boundary.**
4. **Power/Transportation layer separation is a visual coordinate, not geographic elevation.**
5. **Research-system shapes have equal computed area. Shape/color are navigation only.**
6. **The seven-stage architecture is a continuous `γ:[0,1]→R²` satisfying `γ(t_i)=S_i`.**
7. **A release must pass G1–G6:** mathematics, numerical verification, computational geometry, semantics, quantitative visual quality, and deterministic rendering.
8. **Hero and graph→viability share one viability object.** The hero state, active constraint, nearest-boundary point and `ρ_g` are derived from the same governed viability source used by graph→viability and the generated TikZ representation; Python, Shapely and Julia must agree numerically.
9. **GitHub-width readability is release-critical.** At 640 px, governed typography must remain above minimum effective sizes, project signatures must occupy identical layout cells, and project labels must remain non-overlapping; 980 px and 640 px raster previews are both inspected before release.

## Rhino / Grasshopper policy

Rhino/Grasshopper remains an optional parametric exploration laboratory for future CAD/surface investigations. It is intentionally **not** a GitHub release dependency because none of the current README figures requires Rhino-specific geometry. If a future figure depends on Rhino/Grasshopper, its numerical parameters must be exported into the governed source contract before the deterministic SVG release step.

## Evidence boundary

The visual system distinguishes mathematical consistency, numerical verification, computational geometry validity, empirical validation and engineering usefulness. Passing the visual pipeline does not establish physical calibration or empirical validity.
