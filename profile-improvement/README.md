# Profile Improvement Workspace

This directory is the controlled workspace for improving the public professional and research profile of **Dossiya Dakou / Dossiya-SE**.

Its purpose is to ensure that future profile edits are based on the user's **exact request**, preserve the distinction between verified credentials and narrative interpretation, and remain consistent across GitHub, the research portfolio, CV/bio text, research descriptions, diagrams, and future public-facing materials.

**Workspace status:** `ACTIVE_GOVERNING_PROFILE_WORKSPACE`  
**Architecture:** `DD-PROFILE-ARCH-001`  
**Request protocol:** `DD-PROFILE-REQUEST-001`  
**Release gate:** `DD-PROFILE-RELEASE-001`  
**Page composition:** `DD-PROFILE-COMPOSITION-V1`

## Governing principle

```text
exact user request
→ evidence / credential check
→ profile architecture
→ proposed change
→ repository-specific implementation
→ visual / mathematical QA
→ review
→ release
```

A profile statement must never be made stronger than its evidence.

## Canonical identity trajectory

The current profile architecture is intentionally cumulative:

```text
Electrical engineering practice
        ↓
Physical science + renewable-energy systems
        ↓
Sustainable engineering
        ↓
Financial engineering
        ↓
Deeper discrete / differential geometry + mathematical art
        ↓
Cross-sector mathematics for sustainable and resilient systems
```

The long-term research ambition is not to claim that one mathematical field is universally sufficient. It is to investigate whether reusable mathematical structures—geometry, dynamical systems, networks, optimization/control, inverse problems, uncertainty quantification, computation and scientific visualization—can help formulate and solve sustainability/resilience problems across multiple sectors.

The comparison with AI is therefore a **transferability ambition**, not an equivalence claim: AI is broadly reusable across domains; this research programme asks whether rigorous mathematical structures can likewise provide reusable ways to represent state, coupling, constraints, uncertainty, recovery, viability and decision across sectors.

## Files

| File | Purpose |
|---|---|
| [`PROFILE_MASTER_SPEC.md`](PROFILE_MASTER_SPEC.md) | Canonical professional/research identity and narrative boundaries |
| [`PROFILE_CREDENTIALS_REGISTRY.json`](PROFILE_CREDENTIALS_REGISTRY.json) | Machine-readable credential/status/evidence registry |
| [`PROFILE_CREDENTIAL_VERIFICATION_CHECKLIST.md`](PROFILE_CREDENTIAL_VERIFICATION_CHECKLIST.md) | Exact-title, translation/equivalence and completion-status controls |
| [`PROFILE_RELEASE_GATE.md`](PROFILE_RELEASE_GATE.md) | Public release criteria for credentials, research claims, visuals and links |
| [`PROFILE_PUBLIC_NARRATIVE.md`](PROFILE_PUBLIC_NARRATIVE.md) | Draft short, medium and research-oriented public bios |
| [`PUBLIC_PROFILE_TRAJECTORY.md`](PUBLIC_PROFILE_TRAJECTORY.md) | Strongest public-safe trajectory currently releasable without unresolved title substitution |
| [`MATHEMATICS_ART_IDENTITY_V1.md`](MATHEMATICS_ART_IDENTITY_V1.md) | Semantic/scientific contract for the green mathematical-art identity and its domain-linked equations |
| [`PROFILE_PAGE_COMPOSITION_V1.md`](PROFILE_PAGE_COMPOSITION_V1.md) | Information hierarchy, visual-density, V4-master, disclosure, navigation and verification-placement rules for the public profile |
| [`REQUEST_PROTOCOL.md`](REQUEST_PROTOCOL.md) | Exact protocol for every future profile-improvement request |
| [`requests/README.md`](requests/README.md) | Request ledger and naming convention |
| [`assets/engineering-to-mathematics-resilience-trajectory.svg`](assets/engineering-to-mathematics-resilience-trajectory.svg) | Canonical public mathematics-art trajectory |

The root README continues to use the stable public header path `assets/math-art/profile-header-v4.svg`. Under `DD-PROFILE-REQ-20260823-003`, the internal composition at that path was upgraded to the mathematics-art design while the prior master was preserved under `assets/math-art/archive/` for provenance and rollback.

Under `DD-PROFILE-REQ-20260823-004`, the public page composition is governed as a research front door rather than an unfiltered technical report. Adaptive V4 technical masters are used whenever available, workflow verification is separated from identity, and deep formula/repository material remains available through disclosure sections.

## Evidence states

- `VERIFIED_PROFILE` — already represented consistently in the current public/private profile system.
- `USER_STATED` — stated directly by the user and preserved without embellishment.
- `OFFICIAL_TITLE_TO_VERIFY` — exact diploma wording should be checked against the credential before public freezing.
- `ONGOING` — programme is currently in progress; never present as completed.
- `RESEARCH_AMBITION` — future research direction, not an achieved result.
- `IMPLEMENTED_RESEARCH` — supported by an existing repository/project.

## Public-release state

### Releasable now

- cumulative engineering → energy → sustainability → finance → mathematics trajectory;
- broad `electrical-engineering foundation` and `renewable-energy/energy-systems background` language;
- ongoing MSE Sustainable Engineering and MS Financial Engineering status;
- implemented research programmes already supported by repositories;
- discrete/differential geometry and cross-sector resilience as explicit research ambitions;
- governed mathematics-art header and trajectory SVGs;
- V4 adaptive mathematics/research/computing/evidence visuals;
- professional page hierarchy and compact navigation;
- public-safe narrative.

### Blocked pending credential reconciliation

- definitive publication of the three technical electrical credentials under translated English titles;
- silent replacement of `Licence Professionnelle, Énergies Renouvelables et Systèmes Énergétiques` by `Bachelor of Physical Science in Renewable Energy and Energy Systems`;
- any completed-degree language for ongoing master's programmes.

## Non-conflation rules

```text
education != expertise in every related subfield
coursework != independent research
research ambition != established contribution
mathematical analogy != validated transfer
visual beauty != scientific evidence
software verification != empirical validation
```

## Future-use instruction

For every new profile-improvement request, create or update a request record under `requests/` **before** changing the public profile when the change is substantial.

The request record must preserve the user's wording and identify:

1. exact request;
2. intended public surface;
3. evidence/credential basis;
4. proposed edits;
5. files/repositories affected;
6. validation required;
7. status: `PROPOSED`, `IMPLEMENTED`, `VERIFIED`, or `RELEASED`.

This directory is the source of truth for profile-improvement intent. It does not replace official credentials, institutional records, CV source documents, or research evidence.