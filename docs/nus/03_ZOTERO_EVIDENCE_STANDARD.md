# Zotero Evidence Standard

## Governing visible annotation state

The frozen visible Zotero annotation standard is:

```text
exact highlight/region
+ unique top-level role color
+ controlled semantic descriptor
+ exact author wording after the colon
+ zero annotation tags
```

The nine scientific evidence roles remain unchanged:

```text
PURPOSE
INTERVENTION
INPUT
ENGINEERING_METHOD
ENGINEERING_OUTPUT
SUSTAINABILITY_TRANSFORMATION
SUSTAINABILITY_METHOD
SUSTAINABLE_OUTCOME
DECISION
```

The evidence architecture remains:

```text
Q → I → M_E → P → F → M_S → S → D
```

with `PURPOSE` outside the chain.

## Critical revision: nature is visible only for outputs

The previous broader proposal to expose a scientific nature for all nine roles is superseded.

Nature is now shown visibly **only** for:

1. `ENGINEERING_OUTPUT`
2. `SUSTAINABLE_OUTCOME`

The other seven roles keep concise role-only labels.

The reason is deliberate: output nature carries immediate scientific interpretive value while adding nature to every role creates unnecessary comment complexity.

## Final visible comment patterns

```text
Purpose : [exact author wording]

Intervention : [exact author wording]

Input : [exact author wording]

Engineering method : [exact author wording]

Engineering output here is [engineering nature] : [exact author wording]

Sustainability transformation : [exact author wording]

Sustainability method : [exact author wording]

Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]

Decision : [exact author wording]
```

If the nature of an output is not directly supportable from focal evidence, use the broader role-only fallback rather than guessing:

```text
Engineering output : [exact author wording]
Sustainability output : [exact author wording]
```

## Engineering-output nature ontology

Preferred pattern:

```text
Engineering output here is <nature> : <exact author wording>
```

Controlled nature values:

| Nature | Typical outputs |
|---|---|
| `mechanical` | compressive strength, splitting tensile strength, flexural strength, modulus of elasticity, shear strength |
| `fresh-state` | slump, flow, workability, consistency |
| `physical` | density, porosity, water absorption, void content |
| `durability` | chloride resistance, sulfate resistance, carbonation, freeze–thaw, abrasion |
| `transport/permeability` | permeability, sorptivity, diffusivity, penetration |
| `thermal` | thermal conductivity, heat capacity, thermal resistance |
| `structural/functional` | load capacity, deflection, serviceability, system/component performance |
| `fracture/damage` | fracture energy, toughness, ductility, brittleness, crack propagation |
| `time-dependent` | creep, shrinkage, relaxation, age-dependent performance |
| `constructability/production` | compaction, placement, production or construction performance |

Nature must be supported by the **actual focal output**, not by background discussion, hypotheses, or common disciplinary expectations.

### NUS-48 mechanical example

```text
Engineering output here is mechanical : The results from optimization were maximum CS, STS, FS and ME values of 39.71 MPa, 3.47 MPa, 5.64 MPa, and 33.36 GPa, respectively.
```

Internally, the four metrics remain distinct:

```text
CS  → COMPRESSIVE_STRENGTH
STS → SPLITTING_TENSILE_STRENGTH
FS  → FLEXURAL_STRENGTH
ME  → MODULUS_OF_ELASTICITY
```

The visible comment does not need to expose that full metric ontology.

## Sustainability-output nature ontology

Preferred pattern:

```text
Sustainability output here is <nature> : <exact author wording>
```

Controlled natures:

```text
environmental
economic
social
integrated
```

### Environmental

Examples include focal quantified/assessed outcomes involving:

```text
embodied carbon
CO₂ emissions
embodied energy
energy consumption
water
waste
resource consumption
pollution
material/resource efficiency
environmental impact indicators
```

NUS-48 example:

```text
Sustainability output here is environmental : The combined addition of JF and CCA in RCC has reduced the embodied carbon.
```

### Economic

Examples include:

```text
material cost
construction cost
life-cycle cost
cost savings
economic efficiency
affordability
payback
economic value
```

NUS-48 example:

```text
Sustainability output here is economic : The use of 5%, 10%, 15%, and 20% CCA reduced the overall cost of 1 m3 of RCC by $0.98, $2.15, $3.32, and $4.49 at 0.25% of JF.
```

### Social

Use `social` only when the focal study actually evaluates a social outcome such as health, safety, worker conditions, accessibility, equity, employment, community effects, social acceptance, or quality of life.

Mere statements about local availability, possible community benefit, or generalized social relevance are not automatically social outputs.

### Integrated

Use `integrated` only when the focal authors explicitly integrate multiple sustainability dimensions through an actual integration mechanism.

Invariant:

```text
ENV + ECO + SOC ≠ INT
```

Co-occurrence is insufficient.

## Nature, metric, result and evidence state are different fields

Maintain the hierarchy:

```text
Role
→ Nature
→ Metric
→ Result
```

Example:

```text
ENGINEERING_OUTPUT
→ MECHANICAL
→ COMPRESSIVE_STRENGTH
→ 39.71 MPa
```

Example:

```text
SUSTAINABLE_OUTCOME
→ ENVIRONMENTAL
→ EMBODIED_CARBON
→ reported focal result
```

Nature must also remain distinct from evidence state.

For example:

```text
Role           = ENGINEERING_OUTPUT
Nature         = MECHANICAL
Evidence state = OPTIMIZATION_PREDICTED
Metrics        = CS, STS, FS, ME
```

The visible comment remains:

```text
Engineering output here is mechanical : [exact author wording]
```

Evidence state remains external metadata unless a future separately justified rule explicitly exposes it.

## The other seven roles remain simple

The following forms are authoritative:

```text
Purpose : [exact author wording]
Intervention : [exact author wording]
Input : [exact author wording]
Engineering method : [exact author wording]
Sustainability transformation : [exact author wording]
Sustainability method : [exact author wording]
Decision : [exact author wording]
```

Do not use the superseded forms:

```text
Purpose here is ...
Input here is ...
Engineering method here is ...
Sustainability transformation here is ...
Sustainability method here is ...
Decision here is ...
```

## Exact-author-wording invariant

After the colon:

- no paraphrasing;
- no grammar correction;
- no terminology substitution;
- no unit normalization;
- no inferred explanation;
- no silent correction of contradictions;
- no reviewer interpretation inserted into author wording.

Changing an author abbreviation such as `ME` to `modulus of elasticity` inside the author sentence is prohibited unless that expanded phrase is the author's exact wording at the selected evidence anchor.

## Observed output vs discussion claim

Mentioned, hypothesized, or expected performance does not become an output merely because its nature can be named.

```text
Mentioned/hypothesized performance ≠ observed focal engineering output
```

Likewise:

```text
possible economic benefit ≠ focal economic sustainability output
```

unless the focal study actually evaluates that outcome.

## Evidence hierarchy and nonredundancy

Prefer:

```text
Direct focal result
>
author synthesis
>
practical implication
>
general/background discussion
```

The output-nature convention improves description only. It must not increase annotation count by itself.

```text
N_final = scientifically necessary nonredundant evidence
```

## Role-color ontology remains unchanged

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

Nature never creates a new color.

## Tags remain zero

```text
Zotero annotation tags = 0
```

Detailed ontology remains in the external ledger and is linked through annotation identity.

## External metadata becomes richer, not the visible comment

Recommended external fields include:

```text
role
nature
metric
method
result
unit
alternative
origin
evidence_state
provenance
ontology_code
annotation_key
page
geometry
```

Example:

```text
role: ENGINEERING_OUTPUT
nature: MECHANICAL
metric: COMPRESSIVE_STRENGTH
result: 39.71
unit: MPa
evidence_state: OPTIMIZATION_PREDICTED
provenance: FOCAL
```

while Zotero remains concise:

```text
Engineering output here is mechanical : [exact author wording]
```

## NUS-48 retrofit/migration rule

A later project update states that NUS-48 already has **33 native annotations** written under the then-authorized frozen schema.

Therefore this new output-nature convention must not be applied through manual comment edits.

Any retrofit requires the controlled sequence:

```text
new comment convention
→ schema revision
→ regression validation
→ explicit authorization
→ controlled comment-only migration
→ independent audit
```

Changing an existing annotation comment is a state mutation even if geometry, color, and source text remain unchanged.

The new generic convention does **not** by itself authorize migration of the 33 NUS-48 annotations.

## Machine-readable authority

The authoritative machine-readable successor is:

```text
docs/nus/machine/comment_generation_rule_v3.json
```

The earlier `comment_generation_rule_v2.json` is preserved as historical evidence of the superseded all-role-nature proposal.
