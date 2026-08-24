# Account-wide repository architecture and governance audit

**Account:** Dossiya-SE  
**Audit date:** 2026-08-23  
**Scope:** all 16 repositories owned by the connected GitHub account  
**Audit class:** repository architecture, scientific-governance, portfolio structure, lifecycle and release management  
**Relationship to prior audit:** extends the existing mathematics-surface audit; it does not replace it.

## Executive conclusion

The account has evolved beyond a conventional student portfolio. It now contains a credible set of research laboratories, applied-system prototypes, mathematical-computing demonstrations, academic coursework archives and a public research portfolio. The dominant risk is no longer lack of technical content. The dominant risk is **fragmentation**: overlapping research identities, inconsistent repository naming, multiple front doors, unresolved pull-request backlog, uneven CI/release governance and insufficient account-level lifecycle control.

The recommended target architecture is:

```text
                    Dossiya-SE account
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      FRONT DOORS      RESEARCH LABS      METHODS / TOOLS
          │                │                │
   profile README      thesis / reviews    math surfaces
   portfolio site      finance / energy    math ecosystem
          │                │                │
          └──────────────┬─┴───────────────┘
                         ▼
                 APPLIED PROTOTYPES
                         │
                         ▼
                 LEARNING / ARCHIVE
```

A repository should have one primary role. Cross-links are encouraged; duplicated identities are not.

## Account inventory

At the audit snapshot the account owns **16 repositories**:

- **11 public** repositories;
- **5 private** repositories;
- **10 open pull requests** across the account at the time of the governance scan.

The prior mathematics-surface audit already established:

- 637 Markdown/MDX files audited;
- 1,491 formulas parsed with MathJax and strict KaTeX;
- zero active high-confidence mathematics-rendering findings after verified repairs;
- default branches were not protected at the frozen inventory time;
- several private-repository hosted GitHub Actions runs were `UNEXECUTED` during that audit.

Therefore this audit treats mathematical rendering as a largely controlled layer and focuses on repository-system maturity.

## Audit dimensions

Each repository is assessed against nine dimensions:

1. **Identity** — is the repository purpose immediately clear?
2. **Scientific boundary** — does it separate model, computation, observation, validation and claims?
3. **Structure** — does the directory layout support the declared purpose?
4. **Reproducibility** — can important results be reconstructed from source, data/configuration and environment?
5. **Verification / CI** — are software and scientific invariants checked automatically where appropriate?
6. **Governance** — are contribution, provenance, release and decision rules explicit?
7. **Portfolio role** — is the repository's role distinct from neighboring repositories?
8. **Lifecycle** — is the repository clearly active, experimental, frozen, legacy or archival?
9. **Publication / privacy fit** — is public/private visibility consistent with the material contained?

Maturity labels are descriptive, not certification:

```text
FLAGSHIP
SPECIALIST
APPLIED_PROTOTYPE
LEARNING
META_PLATFORM
LEGACY_CANDIDATE
```

## Repository register and disposition

| Repository | Visibility | Primary role | Audit maturity | Recommended disposition |
|---|---|---|---|---|
| `Dossiya-SE` | public | account profile + governance + mathematical presentation | FLAGSHIP FRONT DOOR | KEEP; reduce executable subproject sprawl over time |
| `dossiya-se.github.io` | public | live mathematical research portfolio | FLAGSHIP FRONT DOOR | KEEP; website only, not second governance repository |
| `africa-energy-dignity` | public | applied energy-systems research/engineering platform | FLAGSHIP RESEARCH | KEEP; continue pre-alpha evidence discipline |
| `Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience` | public | domain-neutral mathematics/resilience research platform | FLAGSHIP RESEARCH | KEEP; consider shorter repository name later |
| `MSE-thesis` | private | thesis research laboratory | FLAGSHIP RESEARCH | KEEP PRIVATE; formal release/freeze lifecycle required |
| `infrastructure-interface-resilience-review` | private | evidence synthesis + interface-resilience research | FLAGSHIP RESEARCH | KEEP PRIVATE; clarify boundary with thesis continuously |
| `Dossiya-SE-mscfe-quantitative-finance-lab` | private | MScFE programme/coursework + quantitative-finance methods | FLAGSHIP ACADEMIC LAB | KEEP PRIVATE; complete programme-wide architecture PR |
| `responsible-gold-access-network-rgan` | private | applied systems-design / competition programme | FLAGSHIP APPLIED PROJECT | KEEP PRIVATE while competition/sensitive work is active; large-history audit required |
| `Dossiya-SE-Dossiya-SE` | public | mathematics research ecosystem bootstrap/monorepo | META_PLATFORM | KEEP but RENAME; current name is ambiguous and duplicates account identity |
| `Math-Surface-Engineer-Demo` | public | reproducible mathematics-publication demo/tool | SPECIALIST TOOL | KEEP; narrow scope is a strength |
| `dossiyadakou-mac-project` | public | financial econometrics/model-risk learning and demonstrations | SPECIALIST / LEARNING | KEEP or consolidate; RENAME to purpose-based title |
| `Python-for-rapid-engineering-solution` | public | EDA/engineering coursework evidence archive | LEARNING | KEEP as bounded archive until generating source is restored; then rename |
| `testasu` | public | Solar + STEM product prototype | APPLIED_PROTOTYPE | KEEP if actively developed; RENAME immediately for discoverability |
| `Kudo-IA` | private | scholarship-platform product prototype | APPLIED_PROTOTYPE | KEEP PRIVATE while product/claims are immature |
| `Data-Science-an-Machine-Learning` | public | machine-learning learning scaffold | LEARNING | RENAME; add first validated project or consolidate later |
| `chatbot` | public | Streamlit/API integration learning artifact | LEARNING | KEEP as small demo or archive after superseding integration project exists |

## Principal strengths

### 1. Evidence boundaries are unusually explicit

Across the account, repositories repeatedly distinguish:

```text
simulation != observation
verification != validation
prototype != field evidence
model != empirical truth
source theorem != original contribution
```

This should remain the account's defining research identity.

### 2. The strongest repositories already resemble research operating systems

`MSE-thesis`, `infrastructure-interface-resilience-review`, `africa-energy-dignity`, the differential-geometry/resilience platform and the MScFE lab contain explicit methods, evidence classifications, validation gates, source provenance, reproducibility controls or machine-readable registries. These are stronger than ordinary portfolio repositories and should be treated as flagship laboratories.

### 3. Public mathematical presentation is now governed

The profile repository, live portfolio, mathematics research ecosystem and mathematics-surface demonstration have moved from decorative mathematics toward explicit provenance, renderer checks and bounded interpretation.

### 4. Visibility is mostly sensible

The most sensitive academic/research repositories are private: thesis, NUS/interface review, MScFE assessed work, RGAN competition work and Kudo product work. Public repositories generally present reusable methods, bounded prototypes or sanitized research architecture.

## Account-level findings

### A-01 — Repository identity fragmentation — HIGH

The account currently has three overlapping mathematical/meta identities:

- `Dossiya-SE` — profile + mathematical presentation + account audits + polyglot subsystem;
- `Dossiya-SE-Dossiya-SE` — Mathematics Research Ecosystem bootstrap;
- `Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience` — research platform with overlapping mathematics/resilience architecture.

These can coexist only if their contracts remain distinct:

```text
PROFILE = navigation + account governance + public identity
MATHEMATICS ECOSYSTEM = reusable mathematics knowledge/reproduction platform
DIFFERENTIAL-GEOMETRY/RESILIENCE = specific research programme
```

**Required action:** rename the mathematics ecosystem repository and publish this role separation in the profile registry.

### A-02 — Ambiguous / weak repository names — HIGH

The following names reduce professional discoverability:

- `Dossiya-SE-Dossiya-SE`
- `testasu`
- `Data-Science-an-Machine-Learning`
- `dossiyadakou-mac-project`
- `Python-for-rapid-engineering-solution`

Recommended future names:

```text
mathematics-research-ecosystem
data-science-machine-learning-lab
financial-engineering-model-risk-lab
solar-stem-ai-prototype
python-rapid-engineering-solutions
```

Renaming should preserve redirects and be done only after cross-link inventory.

### A-03 — Two public front doors need a strict contract — HIGH

`Dossiya-SE` and `dossiya-se.github.io` are both strong, but must not become duplicate portfolios.

Freeze:

```text
Dossiya-SE README
= concise identity + repository map + account governance + evidence principles

dossiya-se.github.io
= interactive public research portfolio + demonstrations + publication surfaces
```

Long technical narratives should live in research repositories or the website, not grow indefinitely in the profile README.

### A-04 — Subproject sprawl inside the profile repository — MEDIUM/HIGH

The validated `polyglot-resilience/` subsystem is now substantial enough to behave like a real scientific-computing project. Its presence in the profile repository is acceptable as a transitional state but increases coupling between profile presentation and executable research infrastructure.

**Target:** eventually extract substantial executable research subsystems into dedicated repositories when account architecture stabilizes.

### A-05 — Open pull-request backlog — HIGH

Ten open PRs were observed. They include:

- programme architecture work;
- mathematics-audit PRs;
- GWP continuity/finalization PRs;
- visual-system audit work.

Open PRs are not inherently a problem, but mixed draft, release, audit and blocked states create governance noise.

Adopt explicit PR states:

```text
DRAFT-EXPERIMENT
BLOCKED
READY-FOR-REVIEW
VALIDATED
READY-TO-MERGE
SUPERSEDED
CLOSE-NO-MERGE
```

Every long-lived PR should contain one `Next gate` field and one `Blocker` field.

### A-06 — Default-branch protection / rulesets — CRITICAL GOVERNANCE

The prior account-wide audit recorded that default branches were not protected at the frozen inventory time.

Flagship repositories should require, where technically available:

- pull request before merge;
- required status checks;
- branch up-to-date requirement for release branches where appropriate;
- no force push to `main`;
- no deletion of `main`;
- signed commits/tags where practical;
- CODEOWNERS or explicit reviewer rules for collaborative projects.

This is an account-level governance action, not a mathematics-surface action.

### A-07 — Private GitHub Actions execution reliability — HIGH

Several private repositories had Actions runs terminate before executing job steps during the prior audit. Until resolved, hosted CI must remain reported as `UNEXECUTED`, never `PASS`.

**Priority repositories:**

- `MSE-thesis`
- `infrastructure-interface-resilience-review`
- `Dossiya-SE-mscfe-quantitative-finance-lab`
- `responsible-gold-access-network-rgan`
- `Kudo-IA`

Establish one minimal `runner-smoke.yml` in each private flagship repository before relying on more complex workflows.

### A-08 — RGAN repository-size risk — HIGH

`responsible-gold-access-network-rgan` is approximately 116 MB at the repository metadata level, materially larger than other repositories in the account.

This does not prove misuse, but it requires a large-file/history audit:

- identify largest blobs;
- separate generated media from source;
- move release binaries to GitHub Releases where appropriate;
- use Git LFS only when justified;
- prevent ZIP/video/rendered-output accumulation in Git history;
- define artifact-retention policy.

### A-09 — Learning repositories lack a common lifecycle — MEDIUM

`chatbot`, `Data-Science-an-Machine-Learning`, `Python-for-rapid-engineering-solution`, `dossiyadakou-mac-project` and `testasu` represent different learning/project stages but use different naming and closure conventions.

Introduce a common lifecycle:

```text
LEARNING
→ IMPLEMENTED
→ TESTED
→ EVIDENCE-BEARING
→ FROZEN
→ ARCHIVED or PROMOTED
```

A learning repository that never reaches executable evidence can remain public, but its status must stay explicit.

### A-10 — Reproducibility gap in `Python-for-rapid-engineering-solution` — HIGH LOCAL

The repository explicitly states that outputs are artifact-verifiable but not source-reproducible because the full generating analysis is absent. This is appropriately disclosed but remains the main scientific closure gap for that repository.

Do not upgrade its maturity until the generating source, environment and deterministic regeneration path exist.

### A-11 — Product prototypes require claim registries — MEDIUM

`testasu` and `Kudo-IA` correctly distinguish implemented interface from validated impact. Formalize this further with `CLAIMS_REGISTER.yaml` containing:

```text
claim_id
claim_text
claim_type
source/evidence
status
last_verified
public_copy_location
```

This will prevent prototype copy from drifting into unsupported evidence claims.

### A-12 — Account-wide security baseline is not yet visible as one system — HIGH

For active repositories, define a common baseline:

- secret scanning / push protection where available;
- Dependabot or equivalent dependency updates;
- dependency review for high-risk changes;
- CodeQL or language-appropriate static analysis for production-facing code;
- `SECURITY.md` for public software intended for reuse;
- `.env.example`, never real secrets;
- license compatibility review for copied/generated assets;
- explicit handling of human-subject, infrastructure, competition or academic-protected data.

### A-13 — Releases and citation strategy are uneven — MEDIUM

Some repositories already expose releases, `CITATION.cff`, changelogs or version identifiers; others are effectively moving research branches without release semantics.

Use three release classes:

```text
RESEARCH-SNAPSHOT    e.g. v0.3.0
VALIDATED-DEMO       e.g. v1.0.0
FROZEN-ACADEMIC      immutable course/project release
```

A GitHub release should represent an evidence state, not simply a date.

## Target account taxonomy

### Layer 0 — front doors

- `Dossiya-SE`
- `dossiya-se.github.io`

### Layer 1 — flagship research laboratories

- `MSE-thesis` — private
- `infrastructure-interface-resilience-review` — private
- `Dossiya-SE-mscfe-quantitative-finance-lab` — private
- `africa-energy-dignity` — public
- `Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience` — public
- `responsible-gold-access-network-rgan` — private applied research/design

### Layer 2 — reusable methods / meta-platforms

- `Dossiya-SE-Dossiya-SE` → future `mathematics-research-ecosystem`
- `Math-Surface-Engineer-Demo`
- future extracted `polyglot-resilience` repository if warranted

### Layer 3 — applied prototypes

- `testasu`
- `Kudo-IA`

### Layer 4 — learning and bounded archives

- `dossiyadakou-mac-project`
- `Python-for-rapid-engineering-solution`
- `Data-Science-an-Machine-Learning`
- `chatbot`

## Account-wide repository registry contract

Create and maintain one canonical machine-readable registry in the profile repository with at least:

```yaml
repository_id:
name:
canonical_role:
visibility:
lifecycle_state:
evidence_maturity:
primary_domain:
public_entrypoint:
source_of_truth_for:
depends_on:
supersedes:
superseded_by:
release_policy:
protected_material:
next_gate:
```

The registry is governance metadata, not a scientific result.

## Recommended GitHub management architecture

### 1. Account-level `.github` repository

When practical, create a dedicated `Dossiya-SE/.github` repository for reusable community-health defaults:

- contribution template;
- security policy;
- issue templates;
- PR template;
- shared governance pointers.

Repository-specific scientific requirements must still override the defaults.

### 2. GitHub Projects v2 portfolio board

Recommended fields:

| Field | Example values |
|---|---|
| Repository | one of 16 repositories |
| Programme | Thesis / NUS / MScFE / RGAN / AED / Mathematics / Learning |
| Lifecycle | Idea / Protocol / Active / Validation / Frozen / Archived |
| Evidence maturity | Learning / Implemented / Tested / Validated / Field evidence |
| Visibility | Public / Private |
| Next gate | text |
| Risk | Low / Medium / High / Critical |
| Release target | version/date |
| Blocked | yes/no |

### 3. Cross-repository decision log

Account-level decisions such as naming, archiving, extraction, shared standards and branch rules should be recorded once in the profile governance area rather than repeated inconsistently.

## Priority action plan

### P0 — account governance

1. Configure branch protection/rulesets for flagship `main` branches.
2. Triage the 10 open PRs into merge / block / supersede / close states.
3. Resolve private GitHub Actions runner/execution reliability.
4. Publish the machine-readable repository registry.
5. Freeze the two-front-door contract: profile vs portfolio site.
6. Perform the RGAN large-history/blob audit.

### P1 — identity and lifecycle

7. Rename ambiguous repositories after cross-link inventory.
8. Add lifecycle/status headers to all READMEs.
9. Introduce common release classes and release checklists.
10. Establish account-wide security defaults.
11. Add claims registries to product prototypes.
12. Close the source-reproducibility gap in the Python engineering archive.

### P2 — consolidation and professional presentation

13. Decide whether `polyglot-resilience` should become a dedicated repository.
14. Decide whether learning repositories should remain independent or become a consolidated learning lab.
15. Reduce profile README detail by moving technical material to source repositories/portfolio site.
16. Add a public account architecture visualization generated from the registry.
17. Establish DOI/ORCID release integration for research artifacts where academically appropriate.

## Non-actions

This audit does **not** recommend automatically:

- making private research public;
- deleting historical coursework;
- merging thesis and NUS review repositories;
- presenting prototypes as validated products;
- converting every repository into a software package;
- assigning the same CI stack to every language/project;
- treating repository visibility, stars, languages or visual polish as evidence maturity.

## Account-level release criterion

A repository may be promoted as a flagship public artifact only when its declared release class satisfies the gates relevant to that artifact:

```math
G_{account-release}
=
G_{identity}
\land G_{provenance}
\land G_{verification}
\land G_{claim-boundary}
\land G_{security/privacy}
\land G_{lifecycle}.
```

Empirical validation is additionally required only for claims that depend on real-world validity; it is not falsely substituted by software verification.

## Final assessment

**Account technical depth:** strong.  
**Research-integrity framing:** strong.  
**Mathematics publication control:** strong after prior repairs.  
**Portfolio coherence:** moderate; improving.  
**Repository naming:** weak/inconsistent.  
**Account-level governance:** incomplete.  
**Branch/release discipline:** uneven.  
**Primary next challenge:** consolidation and lifecycle governance, not adding more repositories.

The account should now optimize for **coherence, traceability and release discipline** rather than repository count.
