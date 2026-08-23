# NUS Frozen-37 Evidence Engine Archive

**Project:** Construction sustainability review / Frozen-37 evidence workflow  
**Repository snapshot date:** 2026-08-24  
**Final calibration paper:** NUS-48  
**NUS-48 state:** `FROZEN OUTPUT-NATURE V2`  
**NUS-48 annotations:** `33` (`20` highlights + `13` regions)  
**Tags:** `0`  
**Migration second-pass Δ:** `0`  
**Regression authority:** `T001–T047` / `NUS_MASTER_FAILURE_REGRESSION_CORPUS_V17`  
**Generic engine:** `NUS_EVIDENCE_ENGINE_V1 = FROZEN_FOR_GENERALIZATION_TESTING`  
**Next paper:** `NUS-18 = GENERALIZATION_TEST_1`

This directory is the version-controlled external evidence/governance archive for the NUS Frozen-37 workflow. It preserves calibration history, scientific contracts, failure-learning regressions, Zotero annotation rules, final NUS-48 freeze authorities, Generic NUS Evidence Engine V1, and the NUS-18 generalization-test contract.

## Authoritative navigation

1. [`00_PROJECT_GOVERNANCE.md`](00_PROJECT_GOVERNANCE.md)
2. [`01_FROZEN37_CORPUS.md`](01_FROZEN37_CORPUS.md)
3. [`02_SCIENTIFIC_ONTOLOGY_AND_ADJUDICATION.md`](02_SCIENTIFIC_ONTOLOGY_AND_ADJUDICATION.md)
4. [`03_ZOTERO_EVIDENCE_STANDARD.md`](03_ZOTERO_EVIDENCE_STANDARD.md)
5. [`04_NUS172_CALIBRATION_HISTORY.md`](04_NUS172_CALIBRATION_HISTORY.md)
6. [`05_NUS48_FULL_DEVELOPMENT_HISTORY.md`](05_NUS48_FULL_DEVELOPMENT_HISTORY.md)
7. [`06_NUS48_CURRENT_58_OF_58_STATE.md`](06_NUS48_CURRENT_58_OF_58_STATE.md) — historical premutation freeze
8. [`07_REGRESSION_CORPUS_T001_T039.md`](07_REGRESSION_CORPUS_T001_T039.md) — historical predecessor
9. [`08_GENERIC_ENGINE_SCALING_STRATEGY.md`](08_GENERIC_ENGINE_SCALING_STRATEGY.md)
10. [`09_RELEASE_STATE_MACHINE_AND_AUTHORIZATION.md`](09_RELEASE_STATE_MACHINE_AND_AUTHORIZATION.md)
11. [`10_ARTIFACT_HASH_LEDGER.md`](10_ARTIFACT_HASH_LEDGER.md)
12. [`11_NEXT_SCIENTIFIC_ADJUDICATION.md`](11_NEXT_SCIENTIFIC_ADJUDICATION.md) — preserved historical plan
13. [`12_ARCHIVE_PROVENANCE_AND_COVERAGE.md`](12_ARCHIVE_PROVENANCE_AND_COVERAGE.md)
14. [`13_NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.md`](13_NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.md)
15. [`14_HUMAN_SCIENTIFIC_REVIEW_DECISION_RECORD.md`](14_HUMAN_SCIENTIFIC_REVIEW_DECISION_RECORD.md) — historical review/provenance record
16. [`15_T040_CANDIDATE_ADMINISTRATIVE_METADATA_REGRESSION.md`](15_T040_CANDIDATE_ADMINISTRATIVE_METADATA_REGRESSION.md) — historical candidate record; T040 is now permanent in V17
17. [`16_OUTPUT_NATURE_COMMENT_SCHEMA_V3.md`](16_OUTPUT_NATURE_COMMENT_SCHEMA_V3.md) — pre-final documentation naming; final NUS-48 certified paper schema is Output-Nature V2
18. [`17_NUS48_NATIVE_ANNOTATION_STATE_AND_V3_MIGRATION_BOUNDARY.md`](17_NUS48_NATIVE_ANNOTATION_STATE_AND_V3_MIGRATION_BOUNDARY.md) — historical migration boundary
19. [`18_COMMENT_SCHEMA_V2_TO_V3_CHANGELOG.md`](18_COMMENT_SCHEMA_V2_TO_V3_CHANGELOG.md) — historical schema-design evolution
20. [`19_NUS48_FINAL_FREEZE_OUTPUT_NATURE_V2.md`](19_NUS48_FINAL_FREEZE_OUTPUT_NATURE_V2.md) — **final NUS-48 authority**
21. [`20_GENERIC_NUS_EVIDENCE_ENGINE_V1_FREEZE.md`](20_GENERIC_NUS_EVIDENCE_ENGINE_V1_FREEZE.md) — **generic engine freeze**
22. [`21_NUS18_GENERALIZATION_TEST_1_CONTRACT.md`](21_NUS18_GENERALIZATION_TEST_1_CONTRACT.md) — **next execution contract**
23. [`22_REGRESSION_CORPUS_T001_T047.md`](22_REGRESSION_CORPUS_T001_T047.md) — **current permanent regression boundary**
24. [`machine/current_state.json`](machine/current_state.json)
25. [`machine/generic_engine_v1_freeze_manifest.json`](machine/generic_engine_v1_freeze_manifest.json)
26. [`machine/nus18_generalization_test_1_manifest.json`](machine/nus18_generalization_test_1_manifest.json)
27. [`machine/frozen37_order.json`](machine/frozen37_order.json)

## Final NUS-48 authority

```text
NUS-48 = FROZEN OUTPUT-NATURE V2

Annotations               33
Highlights                20
Regions                   13
Tags                       0
Comment migrations         13
Engineering mechanical     6
Environmental outputs      4
Economic outputs           3
Social outputs             0
Integrated outputs         0
Second-pass Δ              0
Idempotency                PASS
Unauthorized changes       0
PDF mutation               false
Other Zotero mutation      false
```

### Frozen hashes

```text
PDF
bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609

Output-Nature Schema V2
ec29431fd42469679e6442314bca0b97ad22c77bb2a1c226fd29f0ebdb3688e4

Migration report
c5eb4caa289342d6fe2f9aa8703fe5476507f208584b0dadd69f186d0e1272f0

Post-write audit
bab0e14ee3a49b3b0c878f8f0dc997882119097c25976ba712c5e260610d930c

Freeze manifest
e5a798f1099a76835ba964ecf1376bd69b8d5cd504c7029f08378cfd0ea90009

Regression corpus V17
8595d33856aba1228a4aaeb512505241b3a8c88011a251d92ecbed16183ed77a
```

## Frozen visible-comment rule

Nature is visible only for output roles:

```text
Engineering output here is [engineering nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

The other seven evidence roles retain simple labels.

No output nature may be guessed. No social or integrated sustainability output may be introduced without focal evidence. Role colors remain unchanged and annotation tags remain zero.

## Regression authority

The permanent generic failure-learning corpus now spans:

```text
T001 → T047
```

Current authority:

```text
NUS_MASTER_FAILURE_REGRESSION_CORPUS_V17
version 17.0.0
47 tests
```

T047 captures delta-set migration-state classification. T040–T046 are also permanent and no longer candidate-only controls.

## Generic engine freeze

```text
NUS_EVIDENCE_ENGINE_V1
= FROZEN_FOR_GENERALIZATION_TESTING
```

The engine absorbs the NUS-172/NUS-48 lessons without carrying paper-specific scientific conclusions.

A new engine change requires:

```text
new observed failure
→ new paper-independent invariant
→ permanent regression
→ historical calibration retest
→ controlled engine successor
```

## Next decisive test

```text
NUS-18
GENERALIZATION TEST #1
```

Preferred result:

```text
PASS_GENERALIZATION_NO_ENGINE_CHANGE
```

NUS-18 should primarily change paper identity/configuration and source-derived scientific data. It should not trigger another long bespoke pipeline redesign.

## NUS-48 closure rule

Do not modify NUS-48 further unless a genuinely new scientific requirement is formally introduced through controlled change management.
