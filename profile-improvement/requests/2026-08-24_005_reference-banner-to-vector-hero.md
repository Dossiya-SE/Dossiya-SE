# DD-PROFILE-REQ-20260824-005 — Reference banner to vector hero

## User request

Use the supplied wide mathematics-art banner as the design reference for the public GitHub profile at `https://github.com/Dossiya-SE`.

## Intended public surface

- `README.md` hero image through the existing stable path `assets/math-art/profile-header-v5.svg`.

## Design interpretation

The supplied reference establishes the desired composition:

- white/light mathematical canvas;
- high-green identity language;
- electrical engineering and renewable-energy foundations on the left;
- centered identity and 2016→2026 professional trajectory;
- sustainable engineering and financial engineering as intermediate stages;
- deeper mathematics/mathematical physics as forward research direction;
- networks, stochastic systems, optimization and differential geometry on the right;
- scientific-computing/systems/sustainability capability rail at the bottom;
- mathematics art rather than a conventional résumé infographic.

## Evidence and claim controls

The implementation must not use decorative formulas that imply unsupported expertise. Equations and structures are limited to mathematics connected to the public research trajectory, including:

- electrical/control state-space structure `ẋ = Ax + Bu`;
- energy balance;
- Markov/network structure;
- stochastic differential equations;
- constrained optimization;
- differential-geometric metric/geodesic structure.

The trajectory is explicitly conceptual. It is not a proficiency score, empirical embedding or fitted manifold. The final SVG contains the visible micro-label `conceptual trajectory · no proficiency scoring · adaptive SVG`.

The deeper-mathematics region is a forward research direction, not a completed credential or universal-theory claim.

## Rendering contract

- keep the existing public path `assets/math-art/profile-header-v5.svg` to avoid README/path drift;
- use a 2048×640 vector canvas;
- use adaptive SVG theme tokens with `prefers-color-scheme`;
- preserve geometry, equations, labels and evidence meaning across themes;
- no raster dependency is required for the public master;
- the user-supplied 2047×639 raster is treated as a visual composition reference, not the canonical scientific artifact.

## Files changed

- `assets/math-art/profile-header-v5.svg`
- this request record

## Validation required before merge

1. SVG/XML structural validation.
2. Profile governance check.
3. Mathematical-presentation audit.
4. Adaptive-visual audit.
5. PR must be conflict-free on the exact final head.

## Status

IMPLEMENTED_ON_REVIEW_BRANCH — pending CI and merge.
