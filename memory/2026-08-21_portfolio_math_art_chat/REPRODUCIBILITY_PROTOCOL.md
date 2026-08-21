# Reproducibility Protocol for Future Portfolio Work

This protocol converts the conversation’s working style into a repeatable GitHub procedure.

## 1. Repository-selection gate

Before editing, identify which public surface the user actually means.

| User-visible surface | Repository |
|---|---|
| GitHub profile | `Dossiya-SE/Dossiya-SE` |
| Research website | `Dossiya-SE/dossiya-se.github.io` |
| Thesis architecture | `Dossiya-SE/MSE-thesis` |
| AED | `Dossiya-SE/africa-energy-dignity` |
| Interface resilience / NUS controls | `Dossiya-SE/infrastructure-interface-resilience-review` |
| RGAN | `Dossiya-SE/responsible-gold-access-network-rgan` |

Never assume that changing one updates another.

## 2. Current-state gate

Before every write:

1. fetch repository metadata;
2. fetch current `main` file(s);
3. inspect relevant recent merged PRs/commits;
4. identify existing CI/workflows;
5. inspect repository-specific contribution/rigor rules where present.

## 3. Branch/PR discipline

Use:

```text
current main
→ feature branch
→ scoped commit(s)
→ compare branch vs main
→ draft PR
→ CI / review
→ ready for review
→ merge
→ re-fetch main
```

Do not write directly to `main` for normal repository updates.

## 4. Scope integrity

A visual/README PR should not silently change numerical algorithms, data, scientific results, repository visibility or unrelated files.

If numerical/source behavior changes, say so explicitly and require the corresponding tests.

## 5. Evidence chain

For every substantive scientific claim, attempt to preserve:

```text
source
→ provenance
→ definitions / units
→ assumptions
→ mathematical method
→ implementation
→ verification
→ uncertainty / sensitivity
→ validation
→ bounded conclusion
```

If a stage is missing, state the limitation next to the claim.

## 6. Epistemic-status discipline

Use explicit labels such as:

- observed;
- official/published;
- derived;
- synthetic;
- model output;
- demonstrator;
- expert judgment;
- scenario;
- design target;
- planned;
- validated empirical result.

Do not allow a more polished visualization to promote the epistemic status of its underlying data/model.

## 7. Mathematics implementation checks

Where relevant, verify:

- mathematical definitions match code;
- units/dimensions are consistent;
- weights/constraints satisfy invariants;
- numerical horizon/boundary handling is correct;
- deterministic seeds reproduce intended results;
- parameter domains are validated;
- degenerate/invalid inputs are rejected;
- threshold/event durations are time-based, not sample-count artifacts;
- independent or analytical checks exist where feasible.

## 8. Visualization checks

For every new mathematical SVG/plot:

- figure purpose is explicit;
- each shape/line has a defined semantic role;
- equations are correct and readable;
- labels fit at README scale;
- evidence status is visible or documented;
- colors do not imply unsupported certainty;
- `title`/`desc` or equivalent accessibility metadata exists;
- source is version-controlled;
- generated assets have a reproducible generator when practical.

## 9. GitHub math rendering checks

For `Dossiya-SE/Dossiya-SE` profile README:

- avoid raw `\[`, `\]`, `\(`, `\)`;
- use Unicode/plain text or SVG.

For technical repositories:

- use GitHub-supported fenced `math` blocks where appropriate;
- if a repo has Markdown rendering tests, preserve them.

## 10. Link/visibility checks

Before merge:

- public profile links should resolve for anonymous visitors;
- private repositories should be described without pretending they are publicly inspectable;
- no secret/private-user content should be exposed;
- no public page should depend on a private URL for essential evidence.

## 11. CI evidence used in this chat

The following gates were observed as PASS on the visual branches during the conversation:

- `dossiya-se.github.io`
  - Production portfolio audit
  - Verify mathematical portfolio
- `africa-energy-dignity`
  - AED application
- `Python-for-rapid-engineering-solution`
  - Evidence integrity
- `Dossiya-SE-mscfe-quantitative-finance-lab`
  - quality
- `MSE-thesis`
  - Scientific Architecture QA
  - Python package
- `infrastructure-interface-resilience-review`
  - Scientific integrity checks

Do not extrapolate those PASS results to future commits. Re-run/check current CI after new changes.

## 12. No-CI repositories

When no PR-triggered CI exists:

- inspect exact diff;
- ensure README/SVG-only scope if that is the declared scope;
- verify paths/assets exist;
- avoid claiming tests passed;
- consider adding a lightweight integrity workflow if the repository becomes evidence-bearing.

## 13. Standards-reference discipline

When mentioning standards:

- write the exact standard/reference name/version where known;
- state how it is being used;
- do not claim certification/compliance unless independently established;
- distinguish taxonomy, ontology, notation, provenance and theorem-proof layers.

## 14. External-research discipline

If a user asks for an exact source count such as 1,000 papers/websites:

1. create a source registry;
2. record query/source, URL/DOI, type, date/access, inclusion reason;
3. deduplicate;
4. verify the exact final count;
5. preserve the registry and analysis code;
6. only then claim the count.

A broad web review without such a registry must not be reported as an exact 1,000-source study.

## 15. Future-chat reproducibility

A future assistant should be able to answer:

- What was changed?
- Where is it in Git?
- What PR/commit introduced it?
- What evidence supports it?
- What tests passed?
- What remains unvalidated?
- What is the next safe action?

If those questions cannot be answered, update the memory/manifest before ending the session.

## 16. Completion report standard

After a repository operation, report:

- repository;
- branch;
- files changed;
- PR number/URL;
- CI status;
- merge commit if merged;
- post-merge verification;
- remaining limitations.

Do not say “done” if the change is only on an unmerged branch unless the user explicitly asked only for a draft.
