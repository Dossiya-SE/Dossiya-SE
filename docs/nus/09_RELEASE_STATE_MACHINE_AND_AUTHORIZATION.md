# Release State Machine and Mutation Authorization

## Generic release state machine

```text
UNVERIFIED
→ IDENTITY_VERIFIED
→ EXTRACTION_COMPLETE
→ PREMUTATION_REGRESSION_PASS
→ INDEPENDENT_CERTIFICATION_PASS
→ SCIENTIFIC_ADJUDICATION_COMPLETE
→ HUMAN_APPROVED
→ SURFACES_COMPLETE
→ GEOMETRY_PROVEN
→ SCHEMA_PASS
→ WRITER_DRYRUN_PASS
→ AUDITOR_DRYRUN_PASS
→ MUTATION_AUTHORIZED
→ MUTATED
→ WRITER_RERUN_ZERO_DELTA
→ INDEPENDENT_AUDIT_PASS
→ FROZEN
```

Any failed or unresolved gate routes to:

```text
ABSTAIN_OR_FAIL
```

rather than silently continuing.

## Mutation authorization equation

The governing mutation authorization is:

```text
W = R ∧ C ∧ A ∧ H ∧ F ∧ S ∧ G ∧ SCHEMA ∧ D_W ∧ D_A ∧ U_0
```

Where:

- `R` = historical/master regressions PASS;
- `C` = independent certification PASS;
- `A` = scientific adjudication complete;
- `H` = explicit human approval;
- `F` = focality/citation-scope closure;
- `S` = all physical surfaces resolved;
- `G` = exact geometry proven for every to-be-created annotation;
- `SCHEMA` = complete hypothetical final state validates;
- `D_W` = writer dry-run PASS;
- `D_A` = independent auditor dry-run PASS;
- `U_0` = zero unresolved critical ambiguity.

If any term is false:

```text
W = 0
```

## Historical NUS-48 premutation state

At V8 `58/58 PASS` the state was still premutation:

```text
R = true
C = true
A = false
H = false
F = false
S = false
G = false
SCHEMA = false
D_W = false
D_A = false
U_0 = false
W = false
live_annotation_count = 0
```

This remains the authoritative historical premutation state.

## Automated adjudication state

Subsequent automated scientific adjudication advanced the scientific fields, including completion of claim, focality/citation, surface and transformation adjudication at the automated level.

That automated state did not itself constitute human approval or writer authorization.

## Later declared native-annotation state

A later project update states that NUS-48 now has:

```text
33 native Zotero annotations
```

written under the then-authorized frozen schema.

The GitHub archive treats this as a **later state transition**, not as a reason to rewrite the historical premutation state.

The current update does not include the explicit human-approval, geometry, writer, zero-delta and independent-audit artifacts that led to the 33-annotation state. Therefore the archive records:

```text
current native count = 33 (user-declared)
historical write described as authorized = yes
full write/audit provenance in this archive = incomplete
```

No missing gate is silently reconstructed.

## Schema evolution creates a new authorization domain

`NUS_COMMENT_GENERATION_RULE_V3` is now frozen for generic use.

It changes visible output comments from prior role-only wording to:

```text
Engineering output here is [nature] : [exact author wording]
Sustainability output here is [nature] : [exact author wording]
```

for supported output natures.

Even if the existing 33 annotations were validly written under the prior schema, V3 retrofit is a **new mutation** and requires a new authorization path.

Define a migration authorization:

```text
W_migrate = R_m ∧ SCHEMA_m ∧ PLAN_m ∧ H_m ∧ D_Wm ∧ D_Am ∧ U_m
```

where at minimum:

- `R_m` = migration regression suite PASS;
- `SCHEMA_m` = V3 migration schema PASS;
- `PLAN_m` = exact comment-only migration plan complete;
- `H_m` = explicit migration authorization;
- `D_Wm` = migration writer dry-run PASS;
- `D_Am` = independent migration auditor dry-run PASS;
- `U_m` = zero unresolved critical migration ambiguity.

Until all terms are true:

```text
W_migrate = false
```

Therefore:

```text
existing 33 annotations ≠ authorization to edit their comments
```

## Hypothetical final state before any new mutation

Before any new write or migration, construct the proposed state:

```text
Z* = Z_current ∪ Δ_approved
```

Validate `Z*` as a whole for:

- source identity;
- annotation cardinality;
- unique anchors;
- role/color consistency;
- exact author-verbatim comment suffixes;
- output nature grounding where V3 applies;
- zero annotation tags;
- ontology consistency;
- ledger links;
- geometry stability;
- no duplicate state;
- provenance and transformation lineage.

## Transactional writer requirements

Any writer or migration writer must be transactional and idempotent.

First run:

```text
W1: Z0 → Z1
```

Second run:

```text
W2: Z1 → Z1
Δ = 0
```

If the second run changes the state, freeze is prohibited.

## Independent final audit

After any mutation and zero-delta rerun, an independent auditor must verify at least:

- expected annotation count;
- no duplicates;
- exact comment text;
- correct role/color;
- exact/approved geometry;
- zero annotation tags;
- unchanged focal PDF SHA-256;
- complete evidence-ledger links;
- writer/auditor report integrity.

For V3 comment migration, the auditor must additionally prove that:

```text
annotation count did not increase because of schema change
source wording after colon is unchanged
only supported output natures were added
non-output roles remain simple labels
```

Only then may a migrated state become frozen under V3.
