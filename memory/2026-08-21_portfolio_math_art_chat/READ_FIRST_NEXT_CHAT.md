# READ FIRST — Future Chat Bootstrap

Use this file before continuing any profile/portfolio work from the 2026-08-21 conversation.

## 1. Interpret the user’s wording correctly

When the user writes **“profit”** in this project context, they have repeatedly meant **GitHub profile / portfolio**.

Do not alter financial-profit content unless the surrounding request is actually about finance.

## 2. Distinguish the two central GitHub surfaces

These are different repositories and must never be conflated:

- `Dossiya-SE/Dossiya-SE` → controls the **GitHub profile README** displayed on `github.com/Dossiya-SE`.
- `Dossiya-SE/dossiya-se.github.io` → controls the **GitHub Pages research website** at `https://dossiya-se.github.io/`.

A prior error in the conversation changed the website while the user was looking at the profile. This mismatch was later corrected.

## 3. Always inspect current `main` before writing

The dated commit/PR hashes in this capsule are provenance, not a guarantee that they remain current HEAD.

Before changing a repository:

1. fetch repository metadata;
2. fetch the current `main` README/files involved;
3. inspect relevant recent PRs/commits;
4. create a feature branch from current `main`;
5. make only scoped changes;
6. compare branch vs `main`;
7. open a draft PR;
8. run/check CI where available;
9. merge only after verification;
10. re-fetch `main` after merge.

## 4. Keep the profile visual-first

The user explicitly requested **more mathematical visuals than text**.

Preferred order:

1. mathematical-art figure;
2. short equation/definition;
3. evidence status;
4. compact explanation;
5. source/test/validation link.

Avoid returning the profile to long prose sections or decorative badge accumulation.

## 5. GitHub profile math rendering rule

Do **not** use raw `\[ ... \]` or `\( ... \)` LaTeX delimiters in the profile README.

Use GitHub-safe Unicode/plain-text notation for small expressions, or SVG mathematical art for complex formulas.

Example profile-safe chain:

`D_obs → inference → (G_hat, theta_hat, Sigma_theta) → dynamic model → admissible set → viability/recovery → control/design`

The website and technical repositories may use GitHub-supported fenced `math` blocks or MathJax where their rendering stack supports it.

## 6. Do not collapse different mathematical chains

Keep these conceptually distinct:

### Physical forcing chain

`climate/forcing ξ → hazard η → states/interfaces/modes → coupled dynamics → service trajectory`

### Inference chain

`D_obs → observation operator → inverse problem → (G_hat, theta_hat, Sigma_theta)`

### Service/viability chain

`state trajectory → service mapping → population/equity mapping → admissible set K_R → viability/recovery geometry → control/design`

The inference chain informs uncertain model parameters; it is not the physical causal chain itself.

## 7. Mathematics-atlas edge rule

Never use one unlabeled line to imply all of the following at once:

- subject classification;
- conceptual relatedness;
- prerequisite relation;
- formal ontology relation;
- theorem implication;
- method use.

Every formalized edge should have a relation type and provenance.

Theorem-level relations such as `proves`, `implies`, or `derives` require an explicit mathematical result or formal proof dependency.

## 8. Standards/reference stack frozen by this chat

Use the following as **references**, not as unearned certification claims:

- ISO/IEC/IEEE 15288:2023 — system life-cycle process framework.
- ISO 80000-2:2019 — mathematical quantities/symbol notation reference.
- ISO 25964 — controlled vocabulary/thesaurus interoperability reference.
- MSC2020 / MSC2020-SKOS — mathematical disciplinary taxonomy.
- W3C SKOS — taxonomy/knowledge-organization relations.
- RDF/OWL 2 — ontology semantics.
- OpenMath — mathematical-object semantics.
- MathML — web mathematics representation.
- OMDoc/MMT — theories, documents, theory morphisms and formal knowledge structure.
- MaRDI MathModDB — applied mathematical model/formulation/task ontology.
- W3C PROV-O — provenance semantics.
- Lean / Isabelle / Rocq-Coq / Mathematical Components / Mizar — formal-proof ecosystems for theorem-level evidence.

## 9. Do not claim an exact 1,000-source scrape for this chat

The user asked for “1000 scraping mathematics websites and high rigor papers.” The assistant performed a broad standards-first review and produced a standards architecture, but **did not construct and validate an enumerated dataset of exactly 1,000 sources in this chat**.

Future chats must not say that a 1,000-source scrape was completed unless an actual source registry proves it.

## 10. Evidence classes

Keep the following distinctions explicit:

- observed/measured;
- published/official;
- derived;
- simulation/model output;
- synthetic experiment;
- expert judgment;
- scenario assumption;
- engineering design target;
- planned/not yet executed.

Do not relabel one class as another.

## 11. Verification is not validation

Software tests can verify:

- algorithm invariants;
- schema integrity;
- deterministic reproducibility;
- numerical implementation properties;
- build/runtime behavior.

They do **not** automatically validate a physical, financial, educational, social or infrastructure model against reality.

## 12. Current public-profile philosophy

The profile should demonstrate technical skill through:

- mathematics;
- vector mathematical art;
- source code;
- tests/CI;
- provenance;
- limitations;
- validation gates;
- mature vs prototype repository separation.

Do not imply mastery of every programming language merely because it appears in a diagram or roadmap.

## 13. Cross-project continuity

Do not duplicate or overwrite project-specific memory packages.

Relevant existing continuity artifacts include:

- thesis memory capsule(s) in `MSE-thesis`;
- NUS reusable skill/control package in `infrastructure-interface-resilience-review`;
- RGAN project documentation and manifests;
- AED governance/provenance documents.

This folder is the **profile/portfolio cross-repository memory**, not a replacement for those.
