# Standards and Mathematical Knowledge-Graph Architecture

This file preserves the standards-first conclusion reached in the conversation about how to formalize the mathematics atlas.

## 1. No single ISO-like master standard exists for all mathematics

The conversation compared the desired mathematics framework with systems engineering and ISO/IEC/IEEE 15288.

Conclusion:

- systems engineering has a recognized life-cycle process framework such as **ISO/IEC/IEEE 15288:2023**;
- mathematics does **not** have one equivalent international standard that defines the complete hierarchy, dependency graph, theory structure, methods, proofs and workflows of all mathematics.

Therefore the mathematics atlas should use a **layered standards/reference stack** rather than inventing one universal standard.

## 2. Recommended layered stack

### Systems life-cycle process reference

**ISO/IEC/IEEE 15288:2023**

Use for systems-engineering process structure where relevant.

Do not claim certification/compliance unless actually audited.

### Mathematical notation

**ISO 80000-2:2019 — Quantities and units — Part 2: Mathematics**

Use as a notation/symbol reference, especially for scientific/engineering communication.

### Mathematical disciplinary taxonomy

**MSC2020 — Mathematics Subject Classification**

Primary role:

- subject taxonomy;
- disciplinary classification;
- literature organization.

Preferred machine-readable reference:

**MSC2020-SKOS** where available/appropriate.

MSC does not by itself prove that one mathematical field formally implies another.

### Controlled vocabulary / taxonomy semantics

**ISO 25964** and **W3C SKOS**

Useful standardized relation family:

- `skos:broader`
- `skos:narrower`
- `skos:related`

Use these for knowledge-organization relations, not theorem implication.

### Formal ontology layer

**RDF / RDFS / OWL 2**

Examples:

- `rdfs:subClassOf`
- `owl:equivalentClass`

Ontology semantics are stronger/different from SKOS subject relatedness.

Do not treat `skos:broader` and `rdfs:subClassOf` as automatically equivalent.

### Mathematical-object semantics

**OpenMath**

Use conceptually for machine-readable semantics of mathematical symbols/objects rather than purely visual notation.

### Web mathematics representation

**MathML**

Use for structured mathematical representation on the web when appropriate.

This is a representation/markup layer, not the entire mathematical knowledge graph.

### Formal mathematical theories/documents

**OMDoc / MMT**

Useful concepts:

- documents;
- theories;
- symbols;
- theory inclusion;
- theory morphisms;
- formal statement/proof structure.

This layer is important for actual formal dependency architecture.

### Applied mathematical models/workflows

**MaRDI MathModDB**

Useful conceptual classes include:

- Mathematical Model;
- Mathematical Formulation;
- Research Problem;
- Quantity;
- Computational Task;
- Publication.

This is especially relevant to the infrastructure/energy/system-modeling portfolio.

### Provenance

**W3C PROV-O**

Use as the future machine-readable provenance model reference.

Every nontrivial atlas edge should eventually be able to carry source/provenance metadata.

### Theorem-level proof/dependency

Use formal proof ecosystems or explicit theorem references, for example:

- Lean;
- Isabelle / Archive of Formal Proofs;
- Rocq/Coq;
- Mathematical Components;
- Mizar;
- other machine-checked formal libraries.

Do not infer `proves` or `implies` from co-occurrence, subject classification or an unlabeled visual connection.

## 3. Formal graph architecture

A stronger mathematical atlas can be represented as a typed directed multigraph:

```text
G_M = (V, E, tau_V, tau_E, pi, alpha, nu)
```

where:

- `V` = mathematical knowledge entities;
- `E` = typed directed relations;
- `tau_V` = node-type map;
- `tau_E` = edge/relation-type map;
- `pi` = provenance map;
- `alpha` = authority/evidence level;
- `nu` = vocabulary/source/version metadata.

An edge can be represented as:

```text
e_ij = (v_i, r_ij, v_j, provenance, evidence_level)
```

## 4. Suggested node classes

```text
MSCSubject
MathematicalObject
Definition
Theory
Theorem
Proof
Method
Algorithm
NumericalScheme
MathematicalModel
MathematicalFormulation
ComputationalTask
Dataset / EvidenceObject
ApplicationDomain
```

Examples:

- Functional analysis → `MSCSubject` / theory domain.
- Banach space → `MathematicalObject`.
- Banach fixed-point theorem → `Theorem`.
- finite element method → `Method` / `NumericalScheme`.
- Navier–Stokes equations → `MathematicalFormulation`.
- P–W–T–SW infrastructure model → `MathematicalModel`.

## 5. Suggested relation hierarchy

### Level A — standardized taxonomy

```text
broader
narrower
related
```

Prefer SKOS-compatible semantics when aligned to a controlled taxonomy.

### Level B — ontology

```text
subClassOf
equivalentClass
hasProperty
hasPart
```

Only use where ontology semantics are actually defined.

### Level C — formal theory structure

```text
includes
theoryMorphism
imports
instantiates
```

Use OMDoc/MMT or formal-library semantics where available.

### Level D — applied mathematics/model workflow

```text
formulates
uses
discretizes
estimates
calibrates
simulates
optimizes
controls
validates
```

Each relation should have provenance and a declared evidence class.

### Level E — literature-supported conceptual relation

Examples:

```text
provides_foundation_for
frequently_used_in
supports_method_for
related_to_application
```

These are weaker than formal theorem dependencies and should be visibly distinguished.

### Level F — theorem-level relation

```text
proves
implies
derives
is_corollary_of
is_equivalent_to
```

Require an explicit theorem/proof dependency or formal source.

## 6. Evidence/authority levels for atlas edges

A useful working scale discussed in the conversation is:

- **S0** — official standard/taxonomy/controlled classification;
- **S1** — formal ontology relation;
- **S2** — formal theory/proof dependency;
- **S3** — peer-reviewed literature-supported relation;
- **S4** — exploratory/project hypothesis.

The exact labels are project-internal unless formally standardized. Their purpose is to prevent visual edges of different epistemic strength from being treated as equal.

## 7. Recommended atlas legend

Possible visual encoding:

- solid line → taxonomy/ontology relation;
- double/formal arrow → theorem/theory dependency;
- dashed line → literature-supported method/concept relation;
- dotted line → exploratory/project hypothesis;
- color/marker → node class;
- tooltip/panel → provenance, version, evidence level, source.

Do not let color alone carry critical meaning; maintain accessible labels.

## 8. Replacement for the weak interpretation sentence

Weak/original form:

> The graph encodes conceptual dependence, not a formal ontology. Links mean “mathematically informative for” rather than theorem-level implication.

Preferred future form after formalization:

> **Standards basis.** The atlas uses MSC2020 as its primary disciplinary classification and represents taxonomic relationships with explicitly typed knowledge-organization relations. Formal semantic relations are kept distinct from subject relatedness; mathematical-object semantics may be aligned with OpenMath, formal theory relations with OMDoc/MMT, applied-model relations with MaRDI MathModDB, and provenance with PROV-O. Every non-taxonomic dependency carries a relation type, evidence status and source. Theorem-level implication is asserted only when supported by an explicit mathematical result or formal proof dependency.

Do not use this stronger wording until the underlying graph data actually carries the claimed typed relations/provenance.

## 9. Standards integrity rule

A standards reference can justify architecture or terminology. It does not automatically prove:

- certification;
- compliance;
- completeness;
- formal correctness;
- theorem validity;
- empirical validation.

Always state the actual role of the standard/reference.

## 10. Authenticity boundary from the conversation

The user requested a 1,000-source scraping exercise. The conversation produced this standards architecture from a broad standards-first research pass, but did **not** preserve an enumerated 1,000-source dataset.

Therefore this file documents the resulting architecture, not a claim that the architecture was statistically derived from 1,000 independently audited sources.
