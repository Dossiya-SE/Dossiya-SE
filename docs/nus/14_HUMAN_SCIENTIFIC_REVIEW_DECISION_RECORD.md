# NUS-48 Human Scientific Review Decision Record

## Status

```text
PENDING_HUMAN_SCIENTIFIC_REVIEW
```

This file exists to prevent automated adjudication from being silently promoted to human approval.

## Preconditions already satisfied

```text
Premutation automated readiness = 58/58 PASS
Automated scientific adjudication = PASS
Claim adjudication complete = yes
Abstract/body adjudication complete = yes
Physical-surface scientific disposition complete = yes
Transformation ledger scientifically resolved = yes
Live Zotero annotations = 0
Mutation authorized = false
```

## Human decisions required

A human reviewer must explicitly accept, reject, or require revision for each of the following.

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

Recommended scientific treatment:

```text
ACCEPT contradiction as unresolved author inconsistency.
Do not average, silently correct, or substitute values.
Use source-specific evidence records and preserve BODY_CONTRADICTS.
```

Human decision: `PENDING`

### HR002 — IC002 modulus-of-elasticity composition inconsistency

Conflicting body/conclusion attribution:

```text
33.11 GPa at 0.50% JF + 0% CCA
vs
33.11 GPa at 0.50% JF + 10% CCA
```

Recommended scientific treatment:

```text
ACCEPT as unresolved author inconsistency unless visual/source inspection proves a transcription or table-link resolution.
Do not silently select one composition.
```

Human decision: `PENDING`

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

Recommended scientific treatment:

```text
ACCEPT both source states and preserve inconsistency.
Do not reassign the lower value without explicit source evidence.
```

Human decision: `PENDING`

### HR004 — Eq. 2 exactness

Automated evidence supports:

```text
Exists(Eq.2) = true
semantic role = sustainability transformation
link_status = COUPLED
```

but:

```text
ExactFormula(Eq.2) = not verified from focal-PDF text layer
visual_review_required = true
```

Recommended scientific treatment:

```text
ACCEPT semantic classification but require focal-PDF visual verification before exact formula/geometry approval.
```

Human decision: `PENDING`

### HR005 — Table 1 provenance uncertainty

Table 1 remains scientifically relevant, but any unresolved provenance attribution must remain explicit.

Recommended scientific treatment:

```text
Do not force FG/FA/LD/HY if the source provenance is not demonstrable.
Retain UNRESOLVED where necessary until the source is inspected.
```

Human decision: `PENDING`

### HR006 — Optimization-scope separation

Current adjudication distinguishes:

```text
local FS response condition = 14% CCA + 0.70% JF
numerical RSM optimum = 10.24% CCA + 0.52% JF
practical recommendation = 10% CCA + 0.50% JF
```

Recommended scientific treatment:

```text
ACCEPT these as different scopes; do not collapse into one optimum.
```

Human decision: `PENDING`

### HR007 — Sustainability integration interpretation

Current adjudication supports:

```text
Environmental outcomes = yes
Economic outcomes = yes
Social quantified focal outcome = no
Integrated sustainability = not established
Eq. 2 = COUPLED engineering/environmental transformation
```

Recommended scientific treatment:

```text
ACCEPT ENV + ECO without coding INTEGRATED sustainability.
```

Human decision: `PENDING`

### HR008 — Candidate annotation set

Current generated set:

```text
24 text candidates
31 region candidates
55 total candidate annotations
```

Recommended scientific treatment:

```text
Do not approve 55 as a target count.
Allow visual review, geometry validation, and final redundancy analysis to merge/remove candidates.
```

Human decision: `PENDING`

### HR009 — T040 candidate lesson

Six administrative/non-scientific records survived preprocessing and were excluded safely during scientific adjudication.

Recommended governance treatment:

```text
Accept the observed issue as a genuine generic-engine lesson.
Keep T040 as CANDIDATE until deliberately promoted and independently regression-tested before NUS-18 generalization.
Do not reopen NUS-48 scientific adjudication solely because these records were safely excluded.
```

Human decision: `PENDING`

## Approval rule

Human approval may be granted only by an explicit user/reviewer statement. Automated tools must never set this file to approved on their own.

A valid approval statement should clearly indicate one of:

```text
APPROVE_AS_ADJUDICATED
APPROVE_WITH_RECORDED_EXCEPTIONS
REVISE_BEFORE_APPROVAL
REJECT_ADJUDICATION
```

If approved, record the date, reviewer identity/role if desired, and any exceptions without rewriting the underlying evidence history.

## State after approval

Only after explicit approval may the release state advance to:

```text
HUMAN_APPROVED
→ VISUAL_EXACTNESS
→ GEOMETRY_PROVEN
→ SCHEMA_PASS
→ WRITER_DRYRUN_PASS
→ AUDITOR_DRYRUN_PASS
```

Mutation remains prohibited until the full authorization equation evaluates to `W=true`.
