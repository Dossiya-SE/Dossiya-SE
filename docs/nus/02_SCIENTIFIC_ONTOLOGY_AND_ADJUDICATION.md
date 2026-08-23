# Scientific Ontology and Adjudication Contract

## Core analytical chain

The frozen evidence architecture is:

```text
Q → I → M_E → P → F → M_S → S → D
```

Where:

- `Q` = intervention/design choice/alternative or focal research question context;
- `I` = actual inputs consumed by the focal study;
- `M_E` = engineering method;
- `P` = engineering output/performance;
- `F` = explicit transformation/integration mechanism;
- `M_S` = sustainability assessment method;
- `S` = sustainability outcome;
- `D` = decision/recommendation.

`PURPOSE` is tracked separately and does not occupy a node in the chain.

## Core anti-overinterpretation rules

```text
P + S ≠ P → S
```

Engineering and sustainability results appearing in the same paper do not prove coupling.

```text
P → S ≤ explicit transformation
```

A direct engineering-to-sustainability link is recognized only when an explicit method/procedure/equation actually consumes an engineering output.

A transformation may instead be:

```text
I → F → S
```

with no engineering output involved.

## Scientific adjudication order

Every candidate must be adjudicated in this order:

```text
WritingMode
→ ClaimOwner
→ Focality
→ CitationScope
→ EvidenceEligibility
→ Role
→ Ontology
```

Role classification is invalid if claim ownership/focality/citation scope has not first been resolved.

## Focality states

```text
FOCAL
FOCAL_ADOPTED
EXTERNAL
MIXED
UNCLEAR
```

Decision rules:

```text
EXTERNAL → REJECT
MIXED → SPLIT
UNCLEAR → ABSTAIN
FOCAL / FOCAL_ADOPTED → continue
```

Citation presence does not itself determine citation scope. A focal sentence may use adopted external values/methods; a cited sentence may be mixed; an uncited sentence can still be non-focal.

## Provenance states

- `FG` = focal-generated.
- `FA` = focal-adopted external value/method actually consumed by the focal method.
- `LD` = literature-derived/background/comparison/support only.
- `HY` = focal calculation using adopted/external inputs.
- `UNRESOLVED` = not defensibly classifiable.

## Sustainability subtype ontology

At minimum:

```text
ENVIRONMENTAL
ECONOMIC
SOCIAL
INTEGRATED
```

Important rule:

```text
ENV + ECO + SOC ≠ INTEGRATED
```

unless the authors explicitly integrate the dimensions through a composite score, ranking, Pareto/trade-off procedure, weighted aggregation, or equivalent integration mechanism.

## Transformation ledger contract

Every sustainability transformation should eventually record:

```text
TransformationID
exact equation/procedure or exactness state
physical source object
input variables
input provenance
engineering outputs used
transformation family
target sustainability outcome
link_status
```

Minimum `link_status` vocabulary:

```text
PARALLEL_ONLY
COUPLED
UNRESOLVED
```

## Physical-source adjudication

Every physical object discovered in a focal PDF must receive exactly one final disposition:

```text
INCLUDE
EXCLUDE
REDUNDANT
ABSTAIN
```

with a scientific reason. Surface discovery is not itself scientific inclusion.

## Abstract-body crosscheck states

Each abstract claim must receive one explicit relationship to body evidence:

```text
BODY_CONFIRMED
BODY_MORE_SPECIFIC
ABSTRACT_ONLY
BODY_CONTRADICTS
NONCOMPARABLE
UNRESOLVED
```

Contradictions are preserved; they are never silently reconciled.
