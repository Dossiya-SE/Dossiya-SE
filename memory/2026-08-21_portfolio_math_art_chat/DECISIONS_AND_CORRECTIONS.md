# Decisions and Corrections

This file records the decisions that should survive into future chats, including errors discovered during the conversation and the corrected state.

## D1 — Website repository vs profile repository

### Error

Changes to `Dossiya-SE/dossiya-se.github.io` were initially treated as if they would visibly change `github.com/Dossiya-SE`.

### Correction

These are distinct public surfaces:

- `Dossiya-SE/Dossiya-SE` → GitHub profile README.
- `Dossiya-SE/dossiya-se.github.io` → GitHub Pages research website.

Both must be synchronized deliberately.

---

## D2 — GitHub profile raw LaTeX rendering

### Error

The profile README used raw LaTeX-style delimiters, producing visible text such as `\mathcal`, `\rightarrow`, `\widehat`, etc.

### Correction

For the profile README:

- use Unicode/plain-text notation for small chains;
- use SVG mathematical art for complex equations;
- avoid unsupported raw delimiters.

Technical repositories may use GitHub-supported fenced `math` blocks where appropriate.

---

## D3 — The central “chain” is not one undifferentiated causal chain

### Error risk

A compact chain such as

`D_obs → (G_hat, theta_hat, Sigma_theta) → V_sus,eq`

can be misread as if observation data physically cause viability.

### Correction

Separate at least three mappings:

1. **forcing/physics** — forcing and hazard drive state/interface dynamics;
2. **inference** — observations identify uncertain parameters/interfaces;
3. **service/viability** — state trajectories are mapped to service, population/equity constraints, admissibility, viability/recovery, control/design.

Use the compact chain only as an explanatory inference-to-decision map, not as a literal physical causal law.

---

## D4 — “Viable time” must be a time measure, not a sample-count fraction

### Error

The first browser implementation counted stored RK4 states satisfying thresholds and displayed that ratio as “Viable time.”

### Correction

Define a scalar viability margin, for example

`m_V(t) = min_i[x_i(t) - x_i,min]`,

then approximate the time measure

`T_V = μ{t in [0,T] : m_V(t) >= 0}`

by interpolating threshold crossings between consecutive output states.

The same correction applies to service-floor violation duration.

---

## D5 — RK4 terminal-time handling

### Error

A fixed timestep could numerically advance beyond a requested horizon when `T/dt` was not an integer.

### Correction

Use a shortened final step:

`dt_k = min(dt, T - t_k)`.

Verify the terminal time equals the declared horizon.

---

## D6 — Seeded inverse problem wording

### Error

The UI language could imply that repeated inverse runs produced new random observations, even though the experiment used a fixed seed.

### Correction

Label it a **seeded inverse experiment**. With unchanged controls/seed, the synthetic noise realization should reproduce exactly.

---

## D7 — Private repository links on a public portfolio

### Error

Public-facing pages linked directly to private repositories, creating inaccessible destinations for outside visitors.

### Correction

Describe private research publicly but do not present inaccessible repository URLs as public evidence links. Link public repositories directly.

---

## D8 — WebGL/D3 runtime robustness

### Error

A shader or visualization dependency failure could leave an unexplained empty region.

### Correction

- check WebGL shader compile/link status;
- provide controlled fallback states;
- keep numerical logic separated from visualization dependencies;
- do not let D3/WebGL failure silently invalidate the rest of the page.

---

## D9 — Production audit false positive

### Error

A production smoke test initially expected `assets/model.js` to be referenced directly from `index.html`.

### Correct architecture

`index.html → assets/app.js → assets/model.js`

The audit was corrected to verify the actual module structure. The live homepage was reachable from GitHub-hosted CI.

---

## D10 — Python coursework repository automation mismatch

### Error

The Python EDA repository had automation expecting a Django project and generic PyPI publishing even though the repository did not contain the corresponding Django/package structure.

### Correction

Replace misleading automation with an **Evidence integrity** workflow checking what the repository actually contains:

- dataset/report/figures;
- source compilation;
- declared target column;
- scientific-integrity markers.

The replacement gate passed before merge.

---

## D11 — No “all programming languages” proficiency inflation

### User goal

Show broad programming/mathematical skill.

### Decision

Organize languages by role:

- primary scientific workflow;
- statistics/symbolics;
- numerical/HPC targets;
- systems/services;
- interactive scientific web;
- formal/functional exploration;
- automation.

Do **not** claim equal mastery of every language simply because a syntax example or visual badge exists.

---

## D12 — Mathematics atlas must not invent theorem dependencies

### Error risk

Unlabeled edges between broad mathematical domains can imply a rigor that does not exist.

### Correction

Use a typed, provenance-bearing graph.

Examples of distinct relation families:

- taxonomy: `broader`, `narrower`, `related`;
- ontology: `subClassOf`, `equivalentClass`;
- theory structure: `includes`, `theoryMorphism`;
- applied method: `uses`, `discretizes`, `estimates`, `optimizes`;
- formal theorem: `proves`, `implies`, `derives` only with theorem/proof evidence.

---

## D13 — Correct systems-engineering standard number

### Correction

The relevant systems life-cycle standard is **ISO/IEC/IEEE 15288:2023**, not “ISO 1528.”

Use it as a process-framework reference unless an actual compliance/certification audit exists.

---

## D14 — Mathematics does not have one ISO-15288-equivalent master standard

### Decision

Use a layered standards/reference architecture instead of claiming one universal standard for all mathematics.

See [`STANDARDS_AND_KNOWLEDGE_GRAPH.md`](STANDARDS_AND_KNOWLEDGE_GRAPH.md).

---

## D15 — Exact 1,000-source scraping was not completed in this chat

### User request

The user requested “1000 scraping mathematics websites and high rigor papers.”

### Correction / authenticity boundary

A broad standards-first review was performed to identify authoritative knowledge-organization and formal-mathematics frameworks. However, this conversation did **not** create, enumerate and validate a 1,000-record source corpus.

Do not later say “1,000 mathematics websites/papers were scraped” unless a source manifest with exactly 1,000 verified records exists.

---

## D16 — Evidence-first README architecture

The portfolio was deliberately changed from generic capability claims to the chain:

`claim → evidence → provenance → assumptions → method → implementation → verification → uncertainty/sensitivity → validation → bounded conclusion`.

This is a continuing design requirement.

---

## D17 — Visual-first mathematical-art architecture

The user then requested more visuals than text.

Decision:

- show the mathematical object visually where possible;
- keep explanatory prose short;
- preserve evidence-status labels;
- use SVG/vector code so visuals are version-controlled and inspectable;
- do not use decorative complexity to imply empirical validity.

---

## D18 — Mature technical READMEs should not be rewritten only for style

Where a research repository already contains rigorous equations, methods, controls and limitations, preserve the technical detail and improve the visual layer rather than deleting substantive scientific content.

This rule was applied to the thesis master architecture.

---

## D19 — Profile evidence-maturity map is descriptive, not a ranking/certification

Any position/shape in the profile evidence map is a communication device for repository maturity/status. It is not a standardized score, academic ranking, certification or empirical comparison.

---

## D20 — Source of truth remains repository-specific

This memory capsule is an index. A later verified repo state always supersedes a dated summary here.
