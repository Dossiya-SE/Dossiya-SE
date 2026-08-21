# Sources, Provenance and Authenticity Boundaries

This file states what kinds of evidence support this memory capsule and what must **not** be inferred from it.

## 1. Evidence used to build this capsule

The capsule was reconstructed from:

- visible user requests in the conversation;
- GitHub repository reads;
- GitHub merged-PR search;
- GitHub commit/tree verification for the central profile repository;
- PR-head workflow results observed during the conversation;
- files/READMEs that were directly fetched from GitHub during the work;
- merge commit results returned by GitHub operations.

## 2. What this capsule does not contain

It does not contain:

- hidden assistant chain-of-thought;
- private passwords, API keys or secrets;
- unrelated sensitive personal information;
- licensed paper full text;
- unverified claims presented as fact;
- a complete byte-for-byte transcript of every assistant message;
- an exact 1,000-source mathematics scraping dataset.

## 3. Repository source-of-truth rule

For technical facts, the hierarchy is:

```text
current repository main
> repository-specific rigor/control docs
> machine-readable manifests/tests
> merged PR provenance
> this memory capsule
> conversational memory
```

If a current file disagrees with this capsule, inspect the newer commit history before deciding which state is authoritative.

## 4. Public vs private repositories

A private repository may support internal research continuity, but an outside visitor cannot inspect it.

Therefore public-profile evidence should prioritize:

- public code;
- public tests/CI;
- public generated figures;
- public methods/rigor documents;
- public reproducibility instructions.

Private projects may be described by scope/status without pretending their source is publicly available.

## 5. Standards provenance boundary

The conversation identified a standards/reference stack for the mathematics atlas. Those references justify **architecture and terminology**, not certification.

The portfolio should never say, without a separate audit, that it is:

- ISO certified;
- ISO/IEC/IEEE 15288 compliant;
- formally complete under MSC;
- a complete OWL ontology;
- formally verified merely because MMT/OpenMath/proof systems are referenced.

## 6. Mathematics-atlas authenticity boundary

Current visual atlas edges are not automatically formal dependencies.

The future formal version must store:

- relation type;
- source/provenance;
- vocabulary/version;
- evidence/authority level;
- node class;
- formal-proof reference for theorem-level relations.

Until then, stronger formal-ontology language should be avoided.

## 7. Scientific-model authenticity boundary

The public P–W–T–SW browser model is an **illustrative reduced demonstrator**.

Do not infer:

- city-specific calibration;
- field validation;
- empirically estimated infrastructure coupling;
- validated failure probability;
- computed full thesis viability kernel;
- production digital-twin status.

The code/tests establish implementation behavior under declared assumptions, not empirical truth.

## 8. Visual-art authenticity boundary

Mathematical-art SVGs demonstrate:

- mathematical communication;
- vector design;
- systems representation;
- programmatic/version-controlled visual skill.

They do not by themselves prove:

- data provenance;
- calibration;
- causality;
- statistical significance;
- theorem correctness;
- field performance.

Those claims require independent evidence.

## 9. Programming-language authenticity boundary

The portfolio uses role-based language categories.

A language may appear as:

- primary workflow;
- implemented repository language;
- interoperability target;
- numerical/HPC exploration;
- learning example;
- future roadmap.

Do not convert presence in a visual/table into an expert-proficiency claim without substantial implementation evidence.

## 10. 1,000-source request boundary

The user requested an exact 1,000-source scraping/review operation for mathematics standards.

The actual conversation outcome was a standards-first synthesis, not a retained 1,000-record source registry.

Correct language:

> “A broad standards-first review identified a layered mathematics-knowledge architecture.”

Incorrect language:

> “Exactly 1,000 mathematics websites and papers were scraped and validated.”

The latter requires an auditable source registry that does not exist in this chat state.

## 11. CI evidence boundary

A workflow PASS is tied to a specific commit/head.

Do not reuse old PASS statements for future commits without checking current runs.

Where no PR-triggered CI existed, this capsule says so explicitly.

## 12. User-intent authenticity

The user repeatedly emphasized:

- high rigor;
- professionalism;
- mathematical art;
- programming evidence;
- more visuals than text;
- explicit error correction;
- GitHub implementation;
- future-chat memory/reproducibility.

Future assistants should preserve these goals where relevant, but newer explicit user instructions always take priority.
