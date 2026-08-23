# Zotero Evidence Standard

## Visible annotation state

The frozen visible Zotero annotation standard is now:

```text
exact highlight/region
+ unique top-level role color
+ role/nature semantic prefix
+ exact author wording
+ zero annotation tags
```

The strongest generic visible-comment convention is:

```text
ROLE here is SCIENTIFIC NATURE : EXACT AUTHOR WORDING
```

The scientific nature/subtype is included **only when it is directly defensible from focal evidence**. If the subtype/nature cannot be established without inference, use the broader role label only.

The text after the colon must remain author-verbatim. Do not paraphrase, summarize, grammar-correct, normalize terminology, normalize units, infer missing words, or silently repair contradictions.

## Top-level roles and colors

| Role | Color |
|---|---|
| PURPOSE | `#6b7280` |
| INTERVENTION | `#2ea8e5` |
| INPUT | `#0072b2` |
| ENGINEERING_METHOD | `#a28ae5` |
| ENGINEERING_OUTPUT | `#5fb236` |
| SUSTAINABILITY_TRANSFORMATION | `#f19837` |
| SUSTAINABILITY_METHOD | `#e56eee` |
| SUSTAINABLE_OUTCOME | `#ff6666` |
| DECISION | `#ffd400` |

## Permanent role/nature comment-generation rule

### Engineering output

Preferred form:

```text
Engineering output here is <nature> : <exact author wording>
```

Typical directly supported nature values include:

```text
mechanical
physical
durability
thermal
fresh-state
transport
structural
damage/failure
```

If nature is not directly supportable:

```text
Engineering output: <exact author wording>
```

### Sustainability output

Canonical machine role remains `SUSTAINABLE_OUTCOME`, but the preferred visible phrase is:

```text
Sustainability output here is <nature> : <exact author wording>
```

Nature values:

```text
environmental
economic
social
integrated
```

Fallback:

```text
Sustainability output: <exact author wording>
```

Do not use `integrated` merely because multiple sustainability dimensions co-occur. Explicit integration must be demonstrated by the focal study.

### Engineering method

Preferred form:

```text
Engineering method here is <nature> : <exact author wording>
```

Typical nature values:

```text
experimental testing
characterization
statistical modelling
optimization
numerical modelling
```

Fallback:

```text
Engineering method: <exact author wording>
```

### Sustainability method

Preferred form:

```text
Sustainability method here is <nature> : <exact author wording>
```

Typical nature values:

```text
embodied carbon assessment
cost assessment
LCA
life-cycle cost
eco-efficiency
multi-criteria assessment
```

Fallback:

```text
Sustainability method: <exact author wording>
```

### Sustainability transformation

Preferred form:

```text
Sustainability transformation here is <nature> : <exact author wording>
```

Typical nature values:

```text
environmental
economic
social
integrated
engineering–sustainability coupled
```

Fallback:

```text
Sustainability transformation: <exact author wording>
```

The visible nature does not replace the external transformation ledger or `PARALLEL_ONLY / COUPLED / UNRESOLVED` link status.

### Input

Preferred form:

```text
Input here is <nature> : <exact author wording>
```

Typical nature values:

```text
material
mixture proportion
energy
transport
emission factor
cost factor
operational parameter
```

Fallback:

```text
Input: <exact author wording>
```

### Intervention

Preferred form:

```text
Intervention here is <nature> : <exact author wording>
```

Typical nature values:

```text
material substitution
material addition
design modification
process modification
treatment
```

Fallback:

```text
Intervention: <exact author wording>
```

For comparative/selected alternatives, levels, configurations, geometries, strategies, or design variables, `Design choice` remains available as a visible semantic label under the same `INTERVENTION` top-level role.

### Decision

Preferred form:

```text
Decision here is <nature> : <exact author wording>
```

Typical nature values:

```text
optimum mixture selection
optimum selection
recommended alternative
practical recommendation
practical application
ranking
threshold decision
```

Fallback:

```text
Decision: <exact author wording>
```

### Purpose

Preferred form:

```text
Purpose here is <nature> : <exact author wording>
```

Typical nature values:

```text
engineering
environmental
economic
social
integrated
engineering and sustainability assessment
engineering+sustainability
```

Fallback:

```text
Purpose: <exact author wording>
```

## NUS-48 examples

Examples of the new visible convention include:

```text
Engineering output here is mechanical : The results from optimization were maximum CS, STS, FS and ME values of 39.71 MPa, 3.47 MPa, 5.64 MPa, and 33.36 GPa, respectively.
```

```text
Sustainability output here is environmental : The combined addition of JF and CCA in RCC has reduced the embodied carbon.
```

```text
Sustainability output here is economic : The use of 5%, 10%, 15%, and 20% CCA reduced the overall cost of 1 m3 of RCC by $0.98, $2.15, $3.32, and $4.49 at 0.25% of JF.
```

For other NUS-48 evidence, use the same structure only after the scientific nature is directly established from the focal evidence, for example:

```text
Sustainability method here is embodied carbon assessment : <exact author wording>
Engineering method here is statistical modelling : <exact author wording>
Input here is material : <exact author wording>
Intervention here is material substitution : <exact author wording>
Decision here is practical recommendation : <exact author wording>
```

## Scientific-nature guardrail

The comment generator must not guess a nature merely because it is common for the role.

Formally:

```text
if NatureSupportedByFocalEvidence = true:
    visible_comment = "ROLE here is NATURE : EXACT AUTHOR WORDING"
else:
    visible_comment = "ROLE: EXACT AUTHOR WORDING"
```

A machine-inferred or reviewer-inferred nature that cannot be directly defended from the focal paper must remain external metadata and must not appear in the visible comment.

## Machine metadata

Detailed machine/reviewer metadata does **not** belong in the visible Zotero comment. It belongs in the external evidence ledger/repository, including:

- paper ID;
- source hash;
- claim IDs;
- source-object IDs;
- focality;
- citation scope;
- provenance;
- ontology codes;
- scientific nature/subtype evidence;
- adjudication history;
- transformation lineage;
- geometry proof;
- writer/auditor state;
- freeze hashes.

## Mutation rule

No annotation may be created merely because preprocessing, regression, certification, or automated scientific adjudication passes. Mutation is authorized only after the complete scientific/human/geometry/schema/dry-run authorization equation is true.

## Idempotence requirement

The eventual transactional writer must satisfy:

```text
Z0 → Z1
Z1 → Z1
```

on a second run. Any non-zero delta on the second writer run blocks freeze.
