# Research Integrity Standard

This document is the concise public standard used by the Dossiya-SE research profile.

## Evidence hierarchy

The profile distinguishes:

1. **Source-grounded statement** — supported by a traceable scholarly, technical, or primary source.
2. **Mathematical derivation** — follows from declared assumptions and definitions.
3. **Model** — a formal representation of a system, not automatically an observed mechanism.
4. **Computation** — a numerical or symbolic result produced from a declared model and inputs.
5. **Software verification** — evidence that an implementation satisfies specified tests or invariants.
6. **Empirical validation** — comparison with observations or experiments appropriate to the claim.
7. **Decision claim** — an engineering or policy implication bounded by the validity of the preceding layers.

The governing inequality is

```math
\boxed{\text{claim strength}\le\text{strength of the weakest required support}}
```

## Non-conflation rules

- Simulation is not relabeled as observation.
- Association is not relabeled as causation without an identification argument.
- Passing tests is not relabeled as empirical validation.
- Optimization is not relabeled as implementability or real-world benefit.
- A mathematical analogy is not relabeled as an engineering mechanism.
- Differential-geometric language for an application requires an explicitly defined geometric structure.
- A visual representation may improve explanation, but it may not change the evidence status of the object being visualized.
- Tool or programming-language presence does not imply equal proficiency.

## Reproducibility

Where a repository makes computational claims, it should expose the governing equations or model contract, inputs or configuration, implementation, tests, provenance, limitations, and a reproducible execution path appropriate to the project stage.

## Public communication

The profile is an interface to deeper repositories. Detailed assumptions, evidence records, model contracts, validation results, and limitations belong with the project that generates them.
