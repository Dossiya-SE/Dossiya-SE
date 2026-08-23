# Release State Machine and Mutation Authorization

## Release state machine

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

## Current NUS-48 state

After V8 `58/58 PASS`:

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
```

Thus `58/58 PASS` is compatible with and requires:

```text
mutation_authorized = false
```

## Hypothetical final state before mutation

Before any Zotero write, construct the entire proposed state:

```text
Z* = Z_current ∪ A_approved
```

Validate `Z*` as a whole for:

- source identity;
- annotation count derived from approved evidence;
- unique anchors;
- role/color consistency;
- exact author-verbatim comments;
- zero annotation tags;
- ontology consistency;
- ledger links;
- no duplicate geometry;
- no unresolved critical evidence;
- provenance and transformation lineage.

## Transactional writer requirements

The writer must be transactional and idempotent.

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

After mutation and zero-delta rerun, an independent auditor must verify at least:

- expected annotation count;
- no duplicates;
- exact comment text;
- correct role/color;
- exact/approved geometry;
- zero annotation tags;
- unchanged PDF SHA-256;
- complete evidence-ledger links;
- writer/auditor report integrity.

Only then may the state become `FROZEN`.
