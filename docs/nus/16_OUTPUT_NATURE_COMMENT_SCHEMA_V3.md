# Output-Nature Comment Schema V3

## Decision

The nine-role evidence ontology remains unchanged. The visible Zotero comment schema is refined narrowly so that scientific **nature** is exposed only for outputs.

Authoritative patterns:

```text
Engineering output here is [engineering nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

All other roles retain concise role-only descriptors.

## Why the revision is narrow

The purpose of visible nature is to let a human reader immediately answer two questions for output evidence:

```text
What evidence role is this?
What scientific kind of output is it?
```

Extending `here is [nature]` to every role was judged unnecessarily complex. The superseded V2 proposal is preserved in Git history and in `machine/comment_generation_rule_v2.json`, but it is no longer authoritative.

## Engineering output

Controlled natures:

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

Use nature only when the focal result itself supports it.

Example:

```text
Engineering output here is mechanical : The results from optimization were maximum CS, STS, FS and ME values of 39.71 MPa, 3.47 MPa, 5.64 MPa, and 33.36 GPa, respectively.
```

Do not convert a discussion statement such as possible enhanced ductility/fracture resistance into a `fracture/damage` output unless that performance was actually evaluated as a focal result.

## Sustainability output

Controlled natures:

```text
environmental
economic
social
integrated
```

Environmental example:

```text
Sustainability output here is environmental : The combined addition of JF and CCA in RCC has reduced the embodied carbon.
```

Economic example:

```text
Sustainability output here is economic : The use of 5%, 10%, 15%, and 20% CCA reduced the overall cost of 1 m3 of RCC by $0.98, $2.15, $3.32, and $4.49 at 0.25% of JF.
```

Social is used only for actually evaluated focal social outcomes.

Integrated is used only when focal authors explicitly integrate multiple sustainability dimensions.

Invariant:

```text
ENV + ECO + SOC ≠ INT
```

## The other seven roles

Authoritative simple labels:

```text
Purpose : [exact author wording]
Intervention : [exact author wording]
Input : [exact author wording]
Engineering method : [exact author wording]
Sustainability transformation : [exact author wording]
Sustainability method : [exact author wording]
Decision : [exact author wording]
```

## Role → Nature → Metric → Result

Nature is an intermediate classification level, not the metric itself.

```text
ENGINEERING_OUTPUT
→ MECHANICAL
→ COMPRESSIVE_STRENGTH
→ 39.71 MPa
```

```text
SUSTAINABLE_OUTCOME
→ ECONOMIC
→ COST_REDUCTION
→ $4.49
```

Only Role + Nature + exact author wording need be visible. Metric, result, unit, alternative, provenance, evidence state, and geometry remain in the external ledger.

## Nature is not evidence state

Example:

```text
Role           = ENGINEERING_OUTPUT
Nature         = MECHANICAL
Metric         = COMPRESSIVE_STRENGTH
Evidence state = OPTIMIZATION_PREDICTED
```

The visible comment is still only:

```text
Engineering output here is mechanical : [exact author wording]
```

## Exact wording remains immutable

After the colon:

```text
no paraphrase
no grammar correction
no terminology substitution
no unit normalization
no inferred explanation
no silent contradiction repair
```

## Evidence quantity unchanged

The schema changes annotation description only.

```text
new label convention ≠ new evidence
```

No annotation is added merely because an output nature can now be named.

## Color and tag invariants

Colors remain role-based and unchanged. Nature creates no new colors.

Annotation tags remain:

```text
[]
```

## NUS-48 migration boundary

The current project update states that NUS-48 already has **33 native annotations** under its then-authorized frozen schema.

The new V3 label convention does not authorize editing those comments.

Any retrofit must follow:

```text
schema revision
→ regression validation
→ explicit authorization
→ controlled comment-only migration
→ independent audit
```

A comment edit is a Zotero state mutation even when the source highlight geometry and role color do not change.

## Generic-engine authority

This rule should govern new papers from generalization onward unless a later demonstrated failure creates a controlled successor schema.

Machine-readable authority:

```text
docs/nus/machine/comment_generation_rule_v3.json
```
