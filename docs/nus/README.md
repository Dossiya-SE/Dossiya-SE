# NUS Frozen-37 Evidence Engine Archive

**Project:** Construction sustainability review / Frozen-37 evidence workflow  
**Repository snapshot date:** 2026-08-23  
**Current paper:** NUS-48 — *Combined effect of jute fiber and corn cob ash on sustainability assessment and mechanical properties of roller compacted concrete using RSM modelling*  
**Premutation state:** `PASS_PREMUTATION_READY_FOR_SCIENTIFIC_ADJUDICATION` (`58/58 PASS`)  
**Current scientific state:** `PASS_AUTOMATED_SCIENTIFIC_ADJUDICATION_READY_FOR_HUMAN_REVIEW`  
**Current gate:** `HUMAN_SCIENTIFIC_REVIEW`  
**Zotero live annotations for NUS-48:** `0`  
**Mutation authorized:** `false`

This directory is the version-controlled external evidence/governance record for the NUS Frozen-37 workflow. It preserves the development history, frozen scientific rules, regression knowledge, current authoritative state, and next gates. It does **not** replace the focal PDFs, Zotero, or human scientific approval.

## Authoritative navigation

1. [`00_PROJECT_GOVERNANCE.md`](00_PROJECT_GOVERNANCE.md) — purpose, corpus identity, evidence hierarchy, fail-closed principles.
2. [`01_FROZEN37_CORPUS.md`](01_FROZEN37_CORPUS.md) — canonical 37-paper order and calibration/production split.
3. [`02_SCIENTIFIC_ONTOLOGY_AND_ADJUDICATION.md`](02_SCIENTIFIC_ONTOLOGY_AND_ADJUDICATION.md) — Q→I→M_E→P→F→M_S→S→D architecture, focality and adjudication order.
4. [`03_ZOTERO_EVIDENCE_STANDARD.md`](03_ZOTERO_EVIDENCE_STANDARD.md) — visible annotation contract, colors, verbatim-comment rule, zero-tag rule, and permanent `ROLE here is SCIENTIFIC NATURE : EXACT AUTHOR WORDING` convention.
5. [`04_NUS172_CALIBRATION_HISTORY.md`](04_NUS172_CALIBRATION_HISTORY.md) — first calibration/reference paper and frozen lessons.
6. [`05_NUS48_FULL_DEVELOPMENT_HISTORY.md`](05_NUS48_FULL_DEVELOPMENT_HISTORY.md) — complete NUS-48 evolution from unannotated PDF through V8 `58/58 PASS`.
7. [`06_NUS48_CURRENT_58_OF_58_STATE.md`](06_NUS48_CURRENT_58_OF_58_STATE.md) — frozen authoritative NUS-48 premutation state.
8. [`07_REGRESSION_CORPUS_T001_T039.md`](07_REGRESSION_CORPUS_T001_T039.md) — permanent failure knowledge and current executable families.
9. [`08_GENERIC_ENGINE_SCALING_STRATEGY.md`](08_GENERIC_ENGINE_SCALING_STRATEGY.md) — NUS Evidence Engine scaling and generalization criteria.
10. [`09_RELEASE_STATE_MACHINE_AND_AUTHORIZATION.md`](09_RELEASE_STATE_MACHINE_AND_AUTHORIZATION.md) — release gates and mutation authorization equation.
11. [`10_ARTIFACT_HASH_LEDGER.md`](10_ARTIFACT_HASH_LEDGER.md) — known controlled artifacts and hashes.
12. [`11_NEXT_SCIENTIFIC_ADJUDICATION.md`](11_NEXT_SCIENTIFIC_ADJUDICATION.md) — scientific-adjudication work specification preserved as the pre-adjudication plan.
13. [`12_ARCHIVE_PROVENANCE_AND_COVERAGE.md`](12_ARCHIVE_PROVENANCE_AND_COVERAGE.md) — archive boundaries and external evidence objects.
14. [`13_NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.md`](13_NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.md) — current automated scientific adjudication result.
15. [`14_HUMAN_SCIENTIFIC_REVIEW_DECISION_RECORD.md`](14_HUMAN_SCIENTIFIC_REVIEW_DECISION_RECORD.md) — pending explicit human approval/revision record.
16. [`15_T040_CANDIDATE_ADMINISTRATIVE_METADATA_REGRESSION.md`](15_T040_CANDIDATE_ADMINISTRATIVE_METADATA_REGRESSION.md) — candidate generic-engine lesson discovered during adjudication.
17. [`machine/current_state.json`](machine/current_state.json) — machine-readable current NUS-48 state.
18. [`machine/frozen37_order.json`](machine/frozen37_order.json) — machine-readable canonical corpus order.
19. [`machine/comment_generation_rule_v2.json`](machine/comment_generation_rule_v2.json) — machine-readable scientific-nature visible-comment contract.

## Current governing interpretation

The frozen preprocessing result remains:

```text
33/33 Master
24/24 Independent
1/1 Orchestration
58/58 total
```

Automated scientific adjudication has now additionally resolved:

```text
426 atomic claims
11 abstract/body relationships
34 physical surfaces
3 sustainability transformations
3 preserved author inconsistencies
24 text candidates
31 region candidates
55 total generated candidates
```

The 55 candidates are not a target `N_final` and remain subject to visual verification, human review, geometry, and final redundancy analysis.

## Permanent visible-comment convention

When a scientifically important nature/subtype is directly supported by focal evidence, use:

```text
ROLE here is SCIENTIFIC NATURE : EXACT AUTHOR WORDING
```

If the nature cannot be established directly from focal evidence, fall back to:

```text
ROLE: EXACT AUTHOR WORDING
```

This convention is now frozen for the NUS evidence architecture and must be applied consistently to later papers. It does not alter the top-level role ontology and does not permit inferred subtype wording.

The current transition is:

```text
PREPROCESSING FREEZE
→ AUTOMATED SCIENTIFIC ADJUDICATION
→ HUMAN SCIENTIFIC REVIEW
```

No Zotero mutation is authorized. Human approval must be explicit and cannot be inferred from automated adjudication or from this comment-generation rule change.

## Engine-change governance

No further preprocessing change is justified by preference alone. A new permanent engine change requires:

```text
new observed failure
→ general invariant
→ implementation
→ permanent regression
→ historical retest
```

`T040` is currently a candidate lesson only and has not yet been promoted to the permanent regression corpus.
