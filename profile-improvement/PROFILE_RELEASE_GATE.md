# Public Profile Release Gate

**Gate ID:** `DD-PROFILE-RELEASE-001`  
**Scope:** GitHub profile README, portfolio website, public biography, CV/resume narrative, research statement and public visual identity.

## Release invariant

```math
G_{profile}
=
G_{credentials}
\land G_{status}
\land G_{evidence}
\land G_{visual}
\land G_{links}
\land G_{scope}.
```

A profile change is releasable only when every gate required for the specific change is satisfied.

## Gate 1 — Credential integrity

PASS requires:

- official credential title verified where a definitive title is used;
- institution and completion state correct;
- translation/equivalence controlled;
- no certificate/diploma/degree inflation;
- ongoing degrees remain ongoing.

If the public text uses only broad trajectory language and does not introduce unresolved credential titles, this gate may be recorded as `PASS_WITH_TITLE_RECONCILIATION_PENDING` for that specific release.

## Gate 2 — Research-evidence integrity

Every research claim must be classified as one of:

- `IMPLEMENTED_RESEARCH`;
- `VERIFIED/VALIDATED_EVIDENCE` where appropriate;
- `RESEARCH_AMBITION`;
- `LEARNING_DIRECTION`;
- `EXTERNAL_SOURCE`.

A future research direction must not be written as an existing validated contribution.

## Gate 3 — Programme-status integrity

Completed and ongoing education must remain distinguishable.

```text
pursuing / ongoing != completed / earned
```

## Gate 4 — Narrative coherence

The public story should preserve the cumulative trajectory:

```text
Electrical Engineering
→ Energy + Physical Systems
→ Sustainable Engineering
→ Financial Engineering
→ Advanced Mathematics
→ Cross-Sector Sustainable Resilience
```

The trajectory must not be rewritten into a list of unrelated qualifications.

## Gate 5 — Visual integrity

Any profile visual must:

- render as valid SVG/XML or the declared format;
- keep text inside intended regions;
- preserve evidence status;
- avoid implying mastery or validation through decorative authority;
- remain legible on GitHub light/dark themes where designed to be adaptive.

## Gate 6 — Repository and link integrity

- links resolve;
- repository role is correctly described;
- private repositories are not represented as publicly browsable evidence;
- obsolete or renamed repository links are corrected;
- the profile remains a front door, not a duplicate project monorepo.

## Gate 7 — Scope integrity

The long-term cross-sector ambition may be described as a research programme, but not as an already established universal theory.

Permitted:

> investigate reusable mathematical and computational structures for sustainable resilience across sectors

Not permitted without much stronger evidence:

> universal resilience theory

> mathematics equivalent to AI across every sector

> validated framework for all sectors

## Current release state

### Safe now

- publish a trajectory section using broad, controlled educational language;
- state that both master's programmes are ongoing;
- describe implemented repositories and research programmes with their existing evidence boundaries;
- describe discrete/differential geometry and cross-sector resilience as forward research directions;
- link to the governed profile-improvement workspace.

### Blocked pending credential reconciliation

- replacement of the current undergraduate official title;
- publication of the three technical electrical credentials under definitive English titles;
- any claim that an ongoing master's degree has been earned.

## Release record template

```text
request_id:
files_changed:
credential_gate:
programme_status_gate:
research_evidence_gate:
visual_gate:
link_gate:
scope_gate:
workflow_checks:
release_status:
commit_or_pr:
```
