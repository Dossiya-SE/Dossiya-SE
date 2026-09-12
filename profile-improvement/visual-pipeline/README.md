# Professional Mathematical Visual Pipeline

**Status:** experimental production pipeline for the GitHub profile visual system.  
**Scope:** profile hero, research operating system, differential-geometry foundations, and future repository visual assets.

## Governing method

```text
SEARCH
→ VERIFY
→ DEFINE
→ DERIVE
→ IMPLEMENT
→ INDEPENDENT CHECK
→ TEST
→ STRESS
→ VISUALIZE
→ REPRODUCE
→ RED-TEAM
→ DOCUMENT
→ CI
→ REVIEW
→ MERGE
→ RELEASE
```

The design is not beautified first. Mathematical meaning and evidence status are defined before visual composition.

## Production architecture

```text
SCIENTIFIC / MATHEMATICAL SOURCE
        │
        ├── Python / Julia / Mathematica
        │
        ▼
DETERMINISTIC SYNTHETIC OR EMPIRICAL DATA
        │
        ├── explicit equations
        ├── explicit parameters
        ├── fixed random seed when stochastic
        └── evidence label
        │
        ▼
SCIENTIFIC VISUALIZATION
        │
        ├── Matplotlib / Makie / PyVista
        ├── TikZ / PGFPlots / Asymptote
        └── native vector geometry
        │
        ▼
PROFESSIONAL COMPOSITION
        │
        ├── Figma / Illustrator when edit access is available
        └── repository-native SVG composition otherwise
        │
        ▼
SVG CANONICAL ASSET
        │
        ├── SVGO-style simplification / XML checks
        ├── GitHub-scale downsampling test
        ├── overlap / clipping / glyph checks
        └── accessibility metadata
        │
        ▼
GITHUB README
        │
        ▼
AUTOMATED GOVERNANCE + MATHEMATICAL PRESENTATION CHECKS
```

## Evidence rule

Synthetic visualization is permitted only when it is explicitly identified as synthetic or illustrative. A synthetic curve, manifold, phase portrait, network, uncertainty envelope, or viability set must never be presented as observed infrastructure data.

```text
SYNTHETIC ≠ OBSERVED
MODEL ≠ MECHANISM
VERIFIED ≠ EMPIRICALLY VALIDATED
```

## Canonical mathematical visual sources

### Multilayer system

```math
\mathcal G=(G_P,G_T,G_I,G_O,E_{PT},E_{PI},E_{PO},\ldots)
```

The profile uses four visual layers:

- Power
- Transportation
- Information
- Organization

### Canonical interdependency object

```math
\mathfrak I_{ij}^{\alpha\beta}
=
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t)
```

### Synthetic nonlinear potential family

The illustrative stability landscape is generated from

```math
V(x;\mu)=\frac14x^4-\frac12x^2-\mu x,
```

for a controlled set of values of `mu`. This is a conceptual bifurcation/stability visualization, not measured data.

### Synthetic manifold

The illustrative state-space surface uses a deterministic smooth function such as

```math
z=f(x,y)=0.40\sin(1.25x)+0.12\sin(2.7x)+\text{controlled transverse variation}.
```

The tangent and trajectory elements are derived from the same surface geometry rather than drawn independently.

### Viability geometry

```math
\rho_g(x)=d_g(x,\partial\mathcal V_{\mathrm{sus}}).
```

The profile visual treats this first as a geometric margin. It is not labeled an empirical resilience metric without a separately validated mapping to engineering performance.

## Visual release gates

A public visual must satisfy all of the following:

1. white scientific canvas unless a repository-specific design contract overrides it;
2. native vector geometry for canonical static visuals;
3. no embedded raster in governed SVG assets;
4. no clipped or overlapping text at GitHub profile scale;
5. no unsupported-glyph boxes;
6. minimum practical label size specified in `visual_spec.json`;
7. explicit hierarchy between identity, mathematics, annotation and evidence status;
8. renderer-safe mathematical notation;
9. synthetic-data provenance recorded;
10. XML/SVG parsing passes;
11. profile governance passes;
12. mathematical-presentation audit passes;
13. visual review occurs before merge to `main`.

## Figma integration state

The connected Figma account currently exposes a **View** seat. Therefore Figma is treated as a future professional composition stage, not falsely reported as an executed edit stage. When edit access is available, the SVG design system can be imported as editable vector layers and used as the canonical composition workspace.
