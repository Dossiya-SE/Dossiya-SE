# Frozen-37 High-Fidelity Inventory V2

## Status

This record archives the corpus-wide NUS Frozen-37 inventory checkpoint produced on 2026-08-24.

The inventory preserves the frozen canonical 37-paper order and extends the earlier paper-level Q→I→M_E→P→F→M_S→S→D architecture with explicit source-map, EvidenceAnchor, Observation, Transformation, Surface/Geometry, Validation, Decision, QA, and Assurance layers.

## Archived artifacts

- `docs/nus/artifacts/NUS_FROZEN37_HIGH_FIDELITY_INVENTORY_V2.xlsx`
  - SHA-256: `55fc37bebb7c370a670bce3ae56b9f3d78d689d8ac67ac93a3fb238105569ad3`
- `docs/nus/machine/NUS_FROZEN37_HIGH_FIDELITY_INVENTORY_V2.json`
  - SHA-256: `15320e1b80efb9810fe7da54d94bfeb2124735b5db961da66e85a0954dc37b70`

## Authority rules

1. Current frozen / human-verified paper evidence outranks historical extraction.
2. Historical exact/full-text evidence is retained as a high-value recall and provenance layer but is not silently promoted to current gold.
3. Co-occurrence never proves engineering→sustainability coupling; `P→S` requires an explicit transformation consuming an engineering output.
4. Physical page, page index, and authoritative page label are separate metadata fields.
5. Scientific human approval and exact final-schema approval are separate assurance gates.
6. Raw surface signals are not equivalent to reconciled physical-object counts.
7. Unsupported values remain unresolved/abstained rather than inferred.

## Current paper-state boundary

- NUS-172: closed gold reference.
- NUS-48: current frozen calibration paper.
- NUS-18: scientific content human-approved; geometry/page-label authority still not closed.
- Remaining 34 papers: historical/provisional evidence retained; current-engine re-extraction remains required before final field-level synthesis.

## Regression precedence

The archived V1.0.0 engine and V17 corpus remain historical baselines through T047. The controlling project state is later than that baseline: T048 and T049 are permanent current controls; T050 and T051 remain candidate learnings unless separately promoted by a controlled release.

## Mutation status

This inventory archive is documentation/data only. It does not itself authorize Zotero annotation creation, deletion, comment mutation, geometry mutation, or PDF mutation.
