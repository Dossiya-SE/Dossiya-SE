# Frozen-37 Canonical Corpus

The authoritative corpus contains **37 papers** in the following permanent order:

```text
172, 48, 18, 191, 67, 15, 53, 150, 59, 187, 169, 88, 213, 127, 132, 204, 114,
152, 124, 120, 52, 50, 66, 123, 210, 156, 25, 153, 45, 94, 9, 183, 200, 74, 180, 2, 95
```

## Layer 1 — first 17

```text
172, 48, 18, 191, 67, 15, 53, 150, 59, 187, 169, 88, 213, 127, 132, 204, 114
```

## Layer 2 — remaining 20

```text
152, 124, 120, 52, 50, 66, 123, 210, 156, 25, 153, 45, 94, 9, 183, 200, 74, 180, 2, 95
```

## Calibration sequence

| Order | Paper | Role |
|---:|---|---|
| 1 | NUS-172 | Reference architecture / first rigorous calibration |
| 2 | NUS-48 | Major engine hardening / final heavy stress-test |
| 3 | NUS-18 | Generalization test 1 |
| 4 | NUS-191 | Generalization test 2 |
| 5 | NUS-67 | Final generalization test |
| 6 onward | NUS-15 onward | Production operation unless a genuinely new failure class appears |

## Known first-five titles

1. **NUS-172** — *Age dependent properties of concrete incorporating mechanically processed ultra-fine sugarcane bagasse ash* — DOI `10.1016/j.conbuildmat.2025.143509`
2. **NUS-48** — *Combined effect of jute fiber and corn cob ash on sustainability assessment and mechanical properties of roller compacted concrete using RSM modelling* — DOI `10.1038/s41598-024-81345-7`
3. **NUS-18** — *An integrated energy-emergy approach to building form optimization: Use of EnergyPlus, emergy analysis and Taguchi-regression method* — DOI `10.1016/j.buildenv.2014.10.013`
4. **NUS-191** — *Linking seismic resilience into sustainability assessment of limited-ductility RC buildings* — DOI `10.1016/j.engstruct.2019.03.021`
5. **NUS-67** — *Limestone Calcined Clay Cement-based High-Strength Engineered Cementitious Composites (LC3-HS-ECC): Material design and bond performance* — DOI `10.1016/j.jobe.2026.115960`

## Identity rules

- `NUS-<ID>` is permanent.
- Paper-specific scripts/configuration may change, but the native paper ID must not.
- A new PDF/attachment must be treated as a new source-state event and revalidated against the expected identity and SHA-256.
- The corpus order is not a ranking; it is the canonical processing sequence.
