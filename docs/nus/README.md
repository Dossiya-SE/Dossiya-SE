# NUS Frozen-37 Evidence Engine Archive

**Project:** Construction sustainability review / Frozen-37 evidence workflow  
**Repository snapshot date:** 2026-08-24  
**Current paper:** NUS-48 — *Combined effect of jute fiber and corn cob ash on sustainability assessment and mechanical properties of roller compacted concrete using RSM modelling*  
**Frozen premutation state:** `PASS_PREMUTATION_READY_FOR_SCIENTIFIC_ADJUDICATION` (`58/58 PASS`)  
**Automated scientific state:** `PASS_AUTOMATED_SCIENTIFIC_ADJUDICATION_READY_FOR_HUMAN_REVIEW`  
**Latest declared native NUS-48 annotation count:** `33`  
**Current generic comment schema:** `NUS_COMMENT_GENERATION_RULE_V3`  
**V3 retrofit to existing NUS-48 comments:** `NOT AUTHORIZED`

This directory is the version-controlled external evidence/governance record for the NUS Frozen-37 workflow. It preserves development history, frozen scientific rules, regression knowledge, annotation-schema evolution, current state transitions, and next gates. It does **not** replace the focal PDFs, Zotero database, writer/auditor artifacts, or explicit human decisions.

## Authoritative navigation

1. [`00_PROJECT_GOVERNANCE.md`](00_PROJECT_GOVERNANCE.md) — purpose, corpus identity, evidence hierarchy, fail-closed principles.
2. [`01_FROZEN37_CORPUS.md`](01_FROZEN37_CORPUS.md) — canonical 37-paper order and calibration/production split.
3. [`02_SCIENTIFIC_ONTOLOGY_AND_ADJUDICATION.md`](02_SCIENTIFIC_ONTOLOGY_AND_ADJUDICATION.md) — Q→I→M_E→P→F→M_S→S→D architecture, focality and adjudication order.
4. [`03_ZOTERO_EVIDENCE_STANDARD.md`](03_ZOTERO_EVIDENCE_STANDARD.md) — authoritative visible annotation contract: nature is visible only for engineering and sustainability outputs.
5. [`04_NUS172_CALIBRATION_HISTORY.md`](04_NUS172_CALIBRATION_HISTORY.md) — first calibration/reference paper and frozen lessons.
6. [`05_NUS48_FULL_DEVELOPMENT_HISTORY.md`](05_NUS48_FULL_DEVELOPMENT_HISTORY.md) — complete NUS-48 evolution from unannotated PDF through V8 `58/58 PASS`.
7. [`06_NUS48_CURRENT_58_OF_58_STATE.md`](06_NUS48_CURRENT_58_OF_58_STATE.md) — frozen historical premutation state.
8. [`07_REGRESSION_CORPUS_T001_T039.md`](07_REGRESSION_CORPUS_T001_T039.md) — permanent failure knowledge and current executable families.
9. [`08_GENERIC_ENGINE_SCALING_STRATEGY.md`](08_GENERIC_ENGINE_SCALING_STRATEGY.md) — NUS Evidence Engine scaling and generalization criteria.
10. [`09_RELEASE_STATE_MACHINE_AND_AUTHORIZATION.md`](09_RELEASE_STATE_MACHINE_AND_AUTHORIZATION.md) — release gates and mutation authorization equation.
11. [`10_ARTIFACT_HASH_LEDGER.md`](10_ARTIFACT_HASH_LEDGER.md) — known controlled artifacts and hashes.
12. [`11_NEXT_SCIENTIFIC_ADJUDICATION.md`](11_NEXT_SCIENTIFIC_ADJUDICATION.md) — preserved pre-adjudication scientific-work specification.
13. [`12_ARCHIVE_PROVENANCE_AND_COVERAGE.md`](12_ARCHIVE_PROVENANCE_AND_COVERAGE.md) — archive boundaries and external evidence objects.
14. [`13_NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.md`](13_NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.md) — automated scientific adjudication result.
15. [`14_HUMAN_SCIENTIFIC_REVIEW_DECISION_RECORD.md`](14_HUMAN_SCIENTIFIC_REVIEW_DECISION_RECORD.md) — explicit human-review decision record; approval must not be inferred.
16. [`15_T040_CANDIDATE_ADMINISTRATIVE_METADATA_REGRESSION.md`](15_T040_CANDIDATE_ADMINISTRATIVE_METADATA_REGRESSION.md) — candidate generic-engine lesson discovered during adjudication.
17. [`16_OUTPUT_NATURE_COMMENT_SCHEMA_V3.md`](16_OUTPUT_NATURE_COMMENT_SCHEMA_V3.md) — frozen narrow output-only nature convention.
18. [`17_NUS48_NATIVE_ANNOTATION_STATE_AND_V3_MIGRATION_BOUNDARY.md`](17_NUS48_NATIVE_ANNOTATION_STATE_AND_V3_MIGRATION_BOUNDARY.md) — declared 33 native annotations and controlled migration boundary.
19. [`machine/current_state.json`](machine/current_state.json) — machine-readable current NUS-48 state transition.
20. [`machine/frozen37_order.json`](machine/frozen37_order.json) — machine-readable canonical corpus order.
21. [`machine/comment_generation_rule_v3.json`](machine/comment_generation_rule_v3.json) — current machine-readable comment-generation authority.
22. [`machine/comment_generation_rule_v2.json`](machine/comment_generation_rule_v2.json) — superseded historical all-role-nature proposal.

## Frozen preprocessing result

```text
33/33 Master
24/24 Independent
1/1 Orchestration
58/58 total
```

This remains the historical premutation readiness state and originally had:

```text
live_annotation_count = 0
```

That zero-annotation state is preserved as premutation history.

## Automated scientific adjudication result

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

The `55` candidate set was not a target `N_final`.

## Latest native-annotation state update

A subsequent project update states that NUS-48 now has:

```text
33 native Zotero annotations
```

under the then-authorized frozen schema.

The repository records this as a later state transition rather than rewriting the earlier zero-annotation premutation record.

The count of 33 is currently provenance-labelled:

```text
USER_DECLARED_NOT_MACHINE_REVERIFIED_IN_THIS_UPDATE
```

because this GitHub update did not independently query the Zotero database.

## Authoritative visible-comment convention V3

Nature is visible only for output roles.

### Engineering output

```text
Engineering output here is [engineering nature] : [exact author wording]
```

Controlled engineering-output natures:

```text
mechanical
fresh-state
physical
durability
transport/permeability
thermal
structural/functional
fracture/damage
time-dependent
constructability/production
```

### Sustainability output

```text
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

Invariant:

```text
ENV + ECO + SOC ≠ INT
```

### Other seven roles

```text
Purpose : [exact author wording]
Intervention : [exact author wording]
Input : [exact author wording]
Engineering method : [exact author wording]
Sustainability transformation : [exact author wording]
Sustainability method : [exact author wording]
Decision : [exact author wording]
```

The earlier all-role-nature convention is superseded.

## Exactness and nonredundancy invariants

After the colon, author wording remains verbatim. No paraphrase, grammar correction, terminology substitution, unit normalization, inferred explanation, or silent contradiction repair is allowed.

The new V3 schema improves **description**, not evidence quantity:

```text
new output label ≠ new annotation
```

Role colors remain unchanged and annotation tags remain zero.

## Existing NUS-48 annotations are not automatically retrofitted

Changing an existing comment from:

```text
Engineering output : ...
```

to:

```text
Engineering output here is mechanical : ...
```

is a schema/comment mutation.

Any NUS-48 retrofit requires:

```text
schema revision
→ regression validation
→ explicit authorization
→ controlled comment-only migration
→ zero-delta rerun
→ independent audit
```

Manual edits are prohibited.

## Current legitimate branch point

Two scientifically legitimate paths exist:

### Preserve calibration history

```text
NUS-48 remains under its existing authorized schema
NUS-18 onward uses V3
```

### Controlled retrofit

```text
NUS-48 existing 33 annotations
→ validated V3 migration package
→ explicit authorization
→ comment-only migration
→ independent audit
```

Freezing V3 alone does not select either path.

## Engine-change governance

No further preprocessing change is justified by preference alone. A new permanent engine change requires:

```text
new observed failure
→ general invariant
→ implementation
→ permanent regression
→ historical retest
```

`T040` remains a candidate lesson and has not yet been promoted to the permanent regression corpus.
