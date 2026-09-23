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
3. **The computed cyan control/resilience vector is the Euclidean L2 margin `ρ₂`; it must be mathematically normal to the active critical boundary. A general `ρ_g` requires a separately justified metric.**
4. **Power/Transportation layer separation is a visual coordinate, not geographic elevation.**
5. **Research-system shapes have equal computed area. Shape/color are navigation only.**
6. **The seven-stage architecture is a continuous `γ:[0,1]→R²` satisfying `γ(t_i)=S_i`.**
7. **A release must pass G1–G6:** mathematics, numerical verification, computational geometry, semantics, quantitative visual quality, and deterministic rendering.
8. **Hero and graph→viability share one viability object.** The hero state, active constraint, nearest-boundary point and Euclidean `ρ₂` are derived from the same governed viability source used by graph→viability and the generated TikZ representation; Python, Shapely and Julia must agree numerically.
9. **GitHub-width readability is release-critical.** At 640 px, governed typography must remain above minimum effective sizes, project signatures must occupy identical layout cells, and project labels must remain non-overlapping; 980 px and 640 px raster previews are both inspected before release; adaptive single-file SVGs are additionally rasterized with their explicit dark-mode CSS variables.
10. **Computed numerical artifacts are canonically serialized.** Computation uses double precision; release artifacts are emitted at the governed 12-significant-digit representation with values below \(10^{-14}\) canonicalized to zero. The conceptual-state SVD uses the explicit LAPACK `gesvd` driver, and CI runs BLAS/LAPACK single-threaded. Numerically equivalent runs must therefore produce byte-identical computed JSON, TikZ and SVG artifacts.
11. **G6 is a true double-build byte test.** The release hashes the computed JSON, Julia audit, layout metadata, TikZ source, all 10 final SVGs, both governed GIFs, animation metadata/validation, and all 28 runtime PNG previews, rebuilds the complete geometry+animation chain, and requires all 46 SHA-256 hashes to remain identical.
12. **Adaptive dark mode is explicitly rendered.** The research-question, graph→viability, project-system and research-pipeline SVGs are raster-tested with both their light root and their dark CSS variable branch at 640 px and 980 px.

## SCIENTIFIC-ANIMATION-V1

The supplementary GIF is generated from the same fixed `SCIENTIFIC-GEOMETRY-V3` affine scene. Only the camera changes with frame index:

```text
computed-geometry-v3.json + visual-palette.json + animation-spec.json
        ↓
fixed RGB/sRGB frame renderer
        ↓
60 deterministic frames · 100 ms/frame · 10 fps
        ↓
fixed 256-color GIF palette
        ↓
light + dark GIF
        ↓
timing · motion · loop · hue · provenance validation
        ↓
G6 byte-identical rebuild
```

The reference repository `ronikbhaskar/math-art` informed the general workflow principles—fixed frame cadence, deterministic mathematical input, explicit camera rotation and a separate GIF-writing stage. No source code, visual identity, equations, palette or exact animation formula is copied. The governed animation is **camera orbit only**: it does not represent physical time, infrastructure dynamics, measured flow or telemetry.

The static SVG remains the primary scientific figure and accessibility fallback.

### Animation release QA

A release is not accepted from metadata alone. Representative frames **0, 15, 30, 45 and 59** are inspected in both light and dark GIFs. The release requires: no canvas clipping, no label collision, preserved Power/Transportation layer distinction, a visible cyan interlayer/control cue, smooth viewpoint progression, and a visually small loop seam. The decoded GIF palette is independently checked against the governed RGB hue exclusion before release.

## Rhino / Grasshopper policy

Rhino/Grasshopper remains an optional parametric exploration laboratory for future CAD/surface investigations. It is intentionally **not** a GitHub release dependency because none of the current README figures requires Rhino-specific geometry. If a future figure depends on Rhino/Grasshopper, its numerical parameters must be exported into the governed source contract before the deterministic SVG release step.

## Evidence boundary

The visual system distinguishes mathematical consistency, numerical verification, computational geometry validity, empirical validation and engineering usefulness. Passing the visual pipeline does not establish physical calibration or empirical validity.
