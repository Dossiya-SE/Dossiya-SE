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

The implementation does not use decorative formulas that imply unsupported expertise. Equations and structures are limited to mathematics connected to the public research trajectory, including:

- electrical/control state-space structure `ẋ = Ax + Bu`;
- energy balance;
- Markov/network structure;
- stochastic differential equations;
- constrained optimization;
- differential-geometric metric/geodesic structure.

The trajectory is explicitly conceptual. It is not a proficiency score, empirical embedding or fitted manifold. The final SVG contains the visible micro-label `conceptual trajectory · no proficiency scoring · adaptive SVG`.

The deeper-mathematics region is a forward research direction, not a completed credential or universal-theory claim.

## Rendering contract

- existing public path retained: `assets/math-art/profile-header-v5.svg`;
- 2048×640 vector canvas;
- adaptive SVG theme tokens with `prefers-color-scheme`;
- geometry, equations, labels and evidence meaning invariant across themes;
- no raster dependency for the public master;
- the user-supplied 2047×639 raster is treated as a visual composition reference, not the canonical scientific artifact.

## Files changed

- `assets/math-art/profile-header-v5.svg`
- `profile-improvement/validate_profile.py`
- `mathematical-art/audit_profile_math.py`
- this request record

The two validators were migrated from stale V4 filename requirements to the already-public V5 visual generation. Their evidence, accessibility and fail-closed behavior were preserved.

## Validation evidence

Exact implementation head before documentation synchronization: `4c874a0c4dd8c65b267ea01fd500f34a77cfb977`.

- profile-governance run `32660039077` — PASS;
- mathematical-presentation-audit run `32660039068` — PASS;
- adaptive-visual-audit run `32660039087` — PASS;
- PR #23 reported mergeable/conflict-free at that head.

A final exact-head CI pass is required after this record synchronization before merge.

## Status

VALIDATED_PRE_MERGE — final exact-head CI pending.
