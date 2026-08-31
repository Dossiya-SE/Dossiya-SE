# NUS-48 Human Scientific Review Decision / Provenance Record

## Current archive status

```text
HUMAN_APPROVAL_PROVENANCE_NOT_EXPLICITLY_RECORDED_IN_THIS_ARCHIVE
```

This file originally existed to prevent automated adjudication from being silently promoted to human approval.

A later project update now states that NUS-48 has **33 native Zotero annotations written under the then-authorized frozen schema**. That later source-state event means the earlier statement `Live Zotero annotations = 0` is historical premutation information, not the current native-annotation state.

The GitHub archive therefore preserves both facts:

```text
Premutation stage: live annotations = 0
Later declared native state: 33 annotations
```

However, the explicit human-approval decision event and complete writer/auditor provenance that led from the first state to the second were not supplied in the current update. The archive must not invent them.

## Scientific review items preserved from automated adjudication

The following scientific issues remain part of the adjudication history and must not be silently erased merely because native annotations later exist.

### HR001 — IC001 abstract/body mechanical contradiction

Abstract for `0.50% JF + 10% CCA`:

```text
FS = 5.3 MPa
STS = 3.8 MPa
CS = 32.88 MPa
```

Body/conclusion:

```text
FS = 5.60 MPa
STS = 3.50 MPa
CS = 39.42 MPa
```

Required scientific treatment:

```text
Preserve as unresolved author inconsistency.
Do not average, silently correct, or substitute values.
```

### HR002 — IC002 modulus-of-elasticity composition inconsistency

```text
33.11 GPa at 0.50% JF + 0% CCA
vs
33.11 GPa at 0.50% JF + 10% CCA
```

Required treatment:

```text
Preserve both source states unless focal-source inspection explicitly resolves the inconsistency.
```

### HR003 — IC003 R² assignment inconsistency

Table 7 approximately:

```text
CS 0.9913
STS 0.9699
FS 0.9913
ME 0.9913
```

Conclusion approximately:

```text
CS 99.13%
STS 99%
FS 97%
ME 99%
```

Required treatment:

```text
Preserve both; do not silently reassign the lower value.
```

### HR004 — Equation 2 exactness

Automated adjudication supports:

```text
Exists(Eq.2) = true
semantic role = sustainability transformation
link_status = COUPLED
```

while focal-PDF text extraction did not author-exactly recover the displayed formula:

```text
ExactFormula(Eq.2) = not text-layer verified
visual_review_required = true
```

This distinction remains valid unless a later focal-PDF visual record explicitly closes it.

### HR005 — Table 1 provenance uncertainty

Any unresolved provenance must remain explicit rather than being forced into `FG`, `FA`, `LD`, or `HY` without evidence.

### HR006 — Optimization-scope separation

Keep distinct:

```text
local FS response condition = 14% CCA + 0.70% JF
numerical RSM optimum = 10.24% CCA + 0.52% JF
practical recommendation = 10% CCA + 0.50% JF
```

### HR007 — Sustainability integration interpretation

Current scientific interpretation remains:

```text
Environmental outcomes = yes
Economic outcomes = yes
Social quantified focal outcome = no
Integrated sustainability = not established
Eq. 2 = COUPLED engineering/environmental transformation
```

### HR008 — Candidate annotation set was not N_final

Automated adjudication previously generated:

```text
24 text candidates
31 region candidates
55 total candidates
```

The later declared native state contains:

```text
33 native annotations
```

This confirms why `55` was never to be treated as a preset target count. The archive does not infer the exact visual/redundancy decisions that reduced 55 candidates to 33 native annotations unless those migration/review artifacts are later supplied.

### HR009 — T040 remains candidate

Six administrative/non-scientific records survived preprocessing and were excluded during adjudication.

T040 remains:

```text
CANDIDATE_REGRESSION
```

until deliberately promoted and independently validated.

## New V3 comment-schema decision

The current generic visible-comment rule is now `NUS_COMMENT_GENERATION_RULE_V3`:

```text
Engineering output here is [engineering nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

The other seven roles remain simple role-only labels.

This schema freeze is **not** equivalent to authorization to alter the existing 33 NUS-48 annotations.

## Human-approval provenance rule

If the historical human approval / writer / auditor artifacts that produced the 33 native annotations are later supplied, record them here as a dated state transition without rewriting prior evidence.

Until then:

```text
33 annotations = accepted as user-declared current source state
human approval event = not explicitly documented in this GitHub archive
V3 comment migration = not authorized
```

## Future V3 migration approval

Any retrofit of the 33 annotations to V3 requires its own explicit authorization after a validated migration package.

Valid future migration decision states:

```text
PRESERVE_NUS48_PRIOR_SCHEMA
AUTHORIZE_CONTROLLED_V3_COMMENT_MIGRATION
REVISE_MIGRATION_PACKAGE
REJECT_V3_RETROFIT
```

The generic V3 convention can still govern NUS-18 and later papers without retrofitting NUS-48.
