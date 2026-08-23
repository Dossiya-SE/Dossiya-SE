# Profile Improvement Request Protocol

**Protocol ID:** `DD-PROFILE-REQUEST-001`  
**Purpose:** preserve the user's exact intent whenever the public/professional profile is improved.

## Trigger

Use this protocol whenever the user asks to improve, redesign, correct, expand, reorganize or reposition any of the following:

- GitHub profile README;
- research portfolio website;
- professional biography;
- education narrative;
- research vision;
- repository portfolio presentation;
- CV/resume narrative;
- visual identity / mathematical art;
- project-selection display;
- skills/competency map;
- academic/research positioning.

## Required request record

For a material change, create:

```text
requests/YYYY-MM-DD_NNN_short-slug.md
```

with the following structure.

```markdown
# Profile Improvement Request

request_id: DD-PROFILE-REQ-YYYYMMDD-NNN
status: PROPOSED

## Exact user request

[Preserve the request as supplied. Do not paraphrase away constraints.]

## Intended surfaces

- [ ] GitHub profile
- [ ] portfolio website
- [ ] CV/resume
- [ ] biography
- [ ] research statement
- [ ] visual/diagram
- [ ] repository architecture
- [ ] other

## Evidence basis

List credential records, repository evidence, official sources and user-stated facts.

## Claim classification

- VERIFIED_PROFILE
- USER_STATED
- OFFICIAL_TITLE_TO_VERIFY
- ONGOING
- IMPLEMENTED_RESEARCH
- RESEARCH_AMBITION

## Proposed change

Describe the exact change before implementation.

## Files/repositories affected

List exact paths.

## Validation

- credential wording checked
- no completed/ongoing mismatch
- no research-ambition/result conflation
- links render
- SVG/XML valid if applicable
- mathematics renders
- repository claims match evidence

## Outcome

status: IMPLEMENTED | VERIFIED | RELEASED | REJECTED
commit_or_pr:
notes:
```

## Non-negotiable rules

1. **Exact user intent first.** A stylistic rewrite must not alter the requested identity or scientific meaning.
2. **Credential wording is controlled.** Never silently translate or rename a diploma where the official title is uncertain.
3. **Ongoing is not completed.** Degree status changes require explicit evidence or user instruction grounded in the official record.
4. **Ambition is not achievement.** Future mathematics/resilience goals remain `RESEARCH_AMBITION` until implemented or evidenced.
5. **One claim, one evidence class.** Do not mix profile narrative, computed evidence and external literature as if they were the same source type.
6. **Visuals inherit evidence status.** A diagram cannot strengthen a claim merely by making it look authoritative.
7. **Repository role must remain clear.** Profile improvements should reduce fragmentation, not create another competing front door.

## Future interaction shortcut

When the user says words equivalent to:

> “Use my profile-improvement folder and do this...”

interpret the new instruction against this workspace, preserve the exact request in a new request record, and use the master profile specification and credential registry as the controlling context unless the user explicitly changes them.