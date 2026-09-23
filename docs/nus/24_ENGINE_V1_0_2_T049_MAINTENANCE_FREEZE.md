# Generic NUS Evidence Engine V1.0.2 — T049 Maintenance Freeze

## Status

```text
FROZEN_ENGINE_V1_0_2_T049
```

The NUS-18 generalization test exposed one legitimate generic ontology gap after Engine V1.0.1: focal whole-building operational energy/EUI outputs could not be represented exactly by the existing engineering-output nature vocabulary without unsafe coercion.

## T049 invariant

```text
Never force a legitimate focal engineering output into the nearest existing nature.
```

If no controlled nature fits exactly:

```text
fail closed
→ adjudicate the new nature
→ version the ontology
→ add a permanent regression
→ rerun maintenance/static controls
```

The controlled nature added by this maintenance release is:

```text
energy
```

for operational/whole-building energy demand, EUI, energy-use breakdown, and related focal energy-performance outputs.

## Why `thermal` is not acceptable here

NUS-18 reports EUI and whole-building energy use including lighting, equipment, conditioning, and other loads. Therefore:

```text
whole-building energy/EUI ≠ thermal by default
```

The engine must represent the actual output rather than coercing it into the nearest prior category.

## Release authority

```text
Engine version              1.0.2
Regression range            T001–T049
Static validation           20/20 PASS
Regression corpus SHA-256   415ff08df8b33afa2abac631c16e01453221356ea1b07603a476538a691ea3ee
Freeze manifest SHA-256     a4ce6742cd7f1c73737f8ee5b7564d4dbdb499bb628111a310df14e2587277b2
Package SHA-256             5f96b510fa286b2008a7e84063fd1c7b1acb5994de1c1ebc8a69c14bddc4e8b1
```

## Genericity interpretation

This is a generic maintenance extension, not a bespoke NUS-18 pipeline redesign. The nine roles, focality-before-role order, provenance architecture, colors, zero-tag rule, exact-author-wording rule, output-only nature visibility, writer authorization, and audit architecture remain unchanged.

## Current engine state

```text
NUS_EVIDENCE_ENGINE_V1.0.2
= FROZEN_FOR_NUS18_POST_ADJUDICATION_GATES
```

Unknown future engineering-output natures remain fail-closed.
