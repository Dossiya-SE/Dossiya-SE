# Next Steps — Prioritized

This is the forward-work queue that follows from the 2026-08-21 portfolio/math-art conversation. It is not a promise that these tasks are already complete.

## Priority 0 — Preserve correctness

Before adding new visuals or technologies:

- inspect current `main` in each repository;
- ensure no new raw-LaTeX profile rendering regression;
- keep private/public repository boundaries correct;
- keep evidence statuses accurate;
- keep visual README links resolving;
- keep current CI green.

## Priority 1 — Formalize the mathematics atlas data model

The current atlas should evolve from curated conceptual nodes/edges toward a typed, provenance-bearing knowledge graph.

Recommended sequence:

1. define node classes;
2. align top-level subject nodes with MSC2020/MSC2020-SKOS;
3. define SKOS-compatible taxonomy relations;
4. define separate OWL/RDF ontology relations where justified;
5. add applied-mathematics relations for models/methods/tasks;
6. add provenance/source/version per edge;
7. introduce evidence levels;
8. reserve theorem-level `implies/proves` edges for formal/explicit proof dependencies;
9. generate the D3 graph from machine-readable JSON/RDF rather than hard-coded conceptual links;
10. add validation tests for relation type, provenance and vocabulary version.

## Priority 2 — Make mathematical art executable/reproducible

Current SVGs are version-controlled. The next rigor level is to generate more of them from deterministic code.

Suggested generators:

- Python + NumPy/SciPy/SymPy + Matplotlib/SVG;
- D3 from typed JSON graph data;
- Julia for numerical-dynamics equivalence examples;
- WebGL for continuous mathematical fields;
- Wolfram for symbolic/geometry cross-checks where appropriate.

For each generated visual preserve:

```text
input/equations
→ generator code
→ dependency versions
→ output asset
→ checksum or deterministic check
→ README inclusion
```

## Priority 3 — Move the public P–W–T–SW model from demonstrator toward scientific calibration

Correct progression:

```text
verified evidence
→ observation model
→ parameter/interface identification
→ calibration
→ out-of-sample/external validation
→ uncertainty propagation
→ viability/reachability
→ decision/control
```

Do not add “digital twin” language before this evidence chain exists.

## Priority 4 — Viability/reachability computational geometry

Implement stronger research demonstrators such as:

- two-dimensional toy viability kernel with validated benchmark;
- reachability tube;
- capture/recovery basin;
- viability-boundary sensitivity to uncertain interface parameters;
- control-feasibility field `U_V(x)`;
- design-induced deformation of viable sets.

Each new geometry should have:

- explicit definition;
- numerical method;
- convergence/error test;
- synthetic benchmark;
- epistemic-status label.

## Priority 5 — Interface uncertainty → viability uncertainty

Potential flagship research demonstrator:

```text
D_obs
→ (G_hat, theta_hat)
→ Sigma_theta
→ ensemble of coupled dynamics
→ ensemble/deformation of V_R
→ decision regret / robust control set
```

Candidate diagnostics:

- boundary displacement;
- Hausdorff-type set distance where justified;
- viable-volume loss;
- feasible-control loss;
- rank/intervention regret;
- service-continuity loss.

Define all metrics before use; do not use advanced names only for visual appeal.

## Priority 6 — Portfolio-wide evidence registry

Create a machine-readable central index that records, for every showcased artifact:

- repository;
- artifact path;
- artifact type;
- mathematical object;
- evidence class;
- source/provenance;
- generator/code path;
- CI/check name;
- last verified commit;
- validation status;
- public/private visibility.

This would make the profile itself auditable.

## Priority 7 — Repository-specific visual closure

### Profile

- keep three main visual panels concise;
- avoid adding too many badges;
- link visuals to evidence-bearing repos.

### Website

- formalize atlas graph relations;
- add reproducible math-art gallery;
- add calibrated-data section only after real evidence exists.

### Thesis

- protect detailed mathematical text;
- use visuals to summarize, not replace, derivations;
- connect master figure to executable experiments/certificates.

### AED

- link mathematical systems visual to actual registry/geospatial/model artifacts;
- expose Pareto/frontier visuals only when optimization outputs actually exist.

### Interface resilience

- connect stateful-interface visual to implemented schemas/experiments;
- maintain bounded novelty language.

### RGAN

- move from conceptual risk/valuation graphics toward prototype measurement-system analysis and field validation when data exist.

### Finance

- generate plots from committed code/data and add cross-method numerical error visualizations.

### EDA

- recover/commit the exact source that generated existing figures if rights/course rules allow;
- then change status from artifact-verifiable to source-reproducible.

### ML scaffold

- add at least one complete evidence-bearing project before promoting the repo on the main profile.

## Priority 8 — Exact-source research if the user still wants “1,000 sources”

If revisiting the mathematics-standardization research request, do it as an actual auditable study:

- define source classes and inclusion criteria;
- query official standards bodies, mathematical databases, ontology/MKM repositories and peer-reviewed literature;
- build an exact source registry;
- deduplicate;
- preserve query/date/provenance;
- categorize each source by taxonomy/ontology/proof/model/provenance role;
- publish machine-readable results;
- verify exact source count before stating it.

Until then, retain the wording **standards-first review**, not “1,000-source scrape.”

## Priority 9 — GitHub hygiene

Recheck the empty duplicate public repository `Dossiya-SE/Dossiya-SE-Dossiya-SE`.

If it still exists and is not needed, archive/delete/rename it using an authorized capability that supports repository settings. Do not create artificial commits solely to make an empty duplicate look meaningful.

## Priority 10 — Keep memory capsules current

At the end of major future work:

- update `machine_state.json` or create a new dated capsule;
- preserve exact PR/merge/CI provenance;
- record errors/corrections;
- never silently rewrite historical capsules when a new dated state is clearer.
