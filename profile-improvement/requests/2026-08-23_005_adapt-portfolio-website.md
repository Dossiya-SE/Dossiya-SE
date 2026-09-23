# Profile Improvement Request

request_id: `DD-PROFILE-REQ-20260823-005`  
status: `VERIFIED`

## Exact user request

> we should adapt this https://dossiya-se.github.io/

## Interpretation

Adapt the interactive public research portfolio so it expresses the same governed professional/research identity already released on the GitHub profile:

```text
2016 electrical-engineering practice
→ renewable-energy + energy systems
→ ongoing Sustainable Engineering
→ ongoing Financial Engineering
→ deeper mathematics + scientific computing
→ cross-sector sustainable-resilience research
```

The existing Power–Water–Transport–Solid-Waste browser model must remain an executable specialist research demonstrator, but must no longer define the entire public professional identity.

## Intended surfaces

- [x] `https://dossiya-se.github.io/`
- [x] `Dossiya-SE/dossiya-se.github.io/index.html`
- [x] website visual identity / CSS
- [x] machine-readable research metadata
- [x] website repository README
- [x] candidate-source verification
- [x] production-audit lifecycle

## Evidence / claim basis

- active profile architecture `DD-PROFILE-ARCH-001`;
- public profile composition standard `PROFILE_PAGE_COMPOSITION_V1`;
- mathematics-art identity standard `MATHEMATICS_ART_IDENTITY_V1`;
- public-safe credential states already frozen in the profile workspace;
- existing website browser demonstrator and its tests;
- user-stated 2016 professional electrical-engineering starting point.

## Implemented website architecture

```text
identity
→ professional/research trajectory
→ research programmes
→ mathematics architecture
→ executable infrastructure demonstrator
→ evidence / verification / validation
→ forward mathematical research
→ scientific computing + mathematical art
→ education
```

## New / revised website assets

- `assets/profile-trajectory-v1.svg`
- `assets/profile-mathematics-universe-v4.svg`
- `assets/profile-v1.css`
- `PROFILE_ALIGNMENT_V1.md`
- rewritten `index.html`
- revised `research.json`
- revised repository `README.md`
- strengthened `scripts/verify.mjs`
- migrated `scripts/verify-math-display.mjs` to V4
- revised `scripts/production-audit.mjs`
- corrected `.github/workflows/production-audit.yml` lifecycle
- package identity advanced to `0.4.0`

## Scientific / credential boundaries preserved

- `cross-sector transferability = research ambition`;
- `cross-sector transferability != established universal theory`;
- browser P–W–T–SW model remains `demonstrator`, `calibrated=false`, and not field validated;
- mathematical art does not create empirical evidence;
- Sustainable Engineering remains ongoing;
- Financial Engineering remains ongoing;
- undergraduate public title remains `Licence Professionnelle, Énergies Renouvelables et Systèmes Énergétiques`;
- earlier technical electrical credentials are represented only as the 2016 foundation while exact translated titles remain under reconciliation;
- private repository URLs remain undisclosed.

## CI diagnosis and correction

The first PR run failed because `scripts/verify.mjs` required the stale literal phrase:

```text
cross-sector ambition is a <strong>research programme</strong>
```

while the new page correctly states:

```text
This is a research programme, not an already validated universal theory.
```

The page was not weakened to satisfy the stale string. The validator was corrected to check the governed release wording.

The production-audit lifecycle was also corrected so a pull request validates candidate source rather than attempting to reject new source because the old `main` site has not yet been deployed. Deployed smoke testing remains a post-merge/manual/scheduled gate.

## Validation evidence

Website PR: `Dossiya-SE/dossiya-se.github.io#9`  
PR head validated: `1353b60aece4b7319e5ba06606d45c9b9cf9006b`  
Merge SHA: `65b6fa489d00148d1527ce76d5c55137a6949981`

Hosted CI after correction:

- Verify mathematical portfolio — run `32643158616` — `PASS`
- Production portfolio audit / source-verification — run `32643158662` — `PASS`
- PR mergeability — `PASS`

## Release state

source_release: `MERGED_TO_MAIN`  
website_pr: `https://github.com/Dossiya-SE/dossiya-se.github.io/pull/9`  
production_deployment_smoke: `POST_MERGE_GATE`

The profile repository records intent and governance; the website repository remains the source of truth for the deployed interactive implementation.
