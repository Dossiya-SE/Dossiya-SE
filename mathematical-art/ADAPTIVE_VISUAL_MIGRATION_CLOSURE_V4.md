# Adaptive Mathematical Visual Migration V4 — Closure Record

Date: 2026-08-22
Scope: the 14 repositories inventoried in `visual_migration_manifest_v4.json`.

## Final rule

Every active semantic mathematical SVG follows

```math
\boxed{\mathcal I(F_{light})=\mathcal I(F_{dark})}
```

where `I` includes equations, values, geometry, topology, arrow direction, evidence state, uncertainty meaning and scientific conclusions.

Theme changes may alter background, foreground, contrast and semantic palette values only.

## Closure status

All 14 inventoried repositories now have their primary active mathematical visual system merged to V4. The MSE thesis also had its two remaining secondary active mathematical SVGs migrated, so its current `assets/math-art/` visual set is fully adaptive.

Repositories whose Actions execution worked were merged only after their declared checks passed. Repositories showing zero-step Actions execution failures were handled through new, explicit, file-scoped exceptions after direct native-SVG invariant inspection. Those exceptions expire with the associated merge and do not apply to future scientific/software changes.

## Validation classes used

### Executable CI pass

Used where Actions exposed and executed the repository checks, including the central profile, live portfolio, Mathematics Research Ecosystem, Africa Energy Dignity, Rapid Engineering/EDA, Data Science/ML, Solar+STEM and Chatbot migrations.

### Direct invariant audit + scoped infrastructure exception

Used only where GitHub Actions returned failed jobs with no exposed executable steps and no retrievable scientific assertion failure: MSE thesis, Interface Resilience, RGAN, Quantitative Finance and Kudos IA.

This classification is deliberately different from a passing CI run.

## Raster evidence policy

Raster evidence is **not** made adaptive by inversion. If a PNG/JPEG encodes data by color, reversing or filtering colors can change scientific meaning.

Therefore the EDA correlation/covariance heatmaps and pairplot remain fixed evidence artifacts until their generating analysis is fully reproducible. The same rule applies to archived presentation screenshots and historical design renders in other repositories: archive fidelity has priority over theme adaptation.

## Current production hierarchy

```text
formula / source / data
→ symbolic or numerical object
→ verified geometry / field
→ semantic native SVG / MathJax / TikZ
→ light | dark | publication-white render
→ CI or explicit invariant audit
→ merge
```

A raster export is a derivative output, not the canonical mathematical source.

## Scientific boundaries retained

- source differential geometry != geometric metaphor != formally defined research manifold;
- simulation != observation;
- passing software tests != empirical validation;
- calibration != truth;
- visual strength != evidence strength;
- prototype UI != validated intervention;
- a theme change cannot upgrade evidence maturity.

## Remaining maintenance rule

There is no remaining V4 primary-visual migration backlog in the 14-repository inventory. Future work is maintenance: any newly added semantic scientific visual must satisfy the adaptive/native contract at creation time rather than requiring a later retrofit.
