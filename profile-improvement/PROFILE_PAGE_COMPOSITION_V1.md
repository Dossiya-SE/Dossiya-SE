# Professional Profile Page Composition — V1

**Standard ID:** `DD-PROFILE-COMPOSITION-V1`  
**Scope:** root GitHub profile README  
**Status:** active design contract

## Purpose

The profile is a public research front door. It must reveal identity, trajectory, research programmes, mathematics, verification, repositories, and education in a deliberate order without turning the page into an unfiltered technical report.

The governing composition is

```text
identity
→ trajectory
→ research programmes
→ mathematics
→ computation
→ evidence / validation
→ repositories
→ education
→ deep technical detail on demand
```

## 1. First-frame rule

The first frame contains only:

- canonical mathematics-art header;
- compact professional identity links;
- compact page navigation;
- one concise research-identity statement;
- the evidence invariant.

Workflow-status badges, audit links, repository matrices, and long formula blocks do not belong in the hero frame.

## 2. Primary versus semantic color

Green is the public identity palette for the hero and trajectory.

Technical diagrams may retain the semantic ontology defined by the Adaptive Mathematical Visual System V4. A technical color is not recolored merely for branding when the color encodes evidence, uncertainty, dynamics, viability, hazard, interface, or decision meaning.

```text
brand color ≠ scientific semantic color
```

## 3. Visual-master rule

When a V4 adaptive master exists, the public README uses V4.

Primary public technical masters:

- `assets/math-art/profile-mathematics-universe-v4.svg`
- `assets/math-art/research-operating-system-v4.svg`
- `assets/math-art/differential-geometry-foundations-v4.svg`
- `assets/math-art/formula-evidence-lattice-v4.svg`
- `assets/math-art/evidence-maturity-map-v4.svg`
- `assets/math-art/computational-stack-v4.svg`

Legacy V3/unversioned files may remain as provenance artifacts but are not primary public render surfaces.

## 4. Visual-density rule

A full-width figure must have a clear section purpose and at least one short interpretive sentence. Avoid consecutive unexplained full-width figures.

The default public reading path should never require reading every displayed formula to understand the research identity.

## 5. Redundancy rule

Do not explain the same idea as:

1. a full-width visual;
2. a prose paragraph;
3. a second text-only flow;

unless each representation adds distinct information.

The trajectory visual plus concise prose is sufficient; the redundant text-only arrow chain is removed.

## 6. Disclosure rule

Use GitHub `<details>` for material that is rigorous but secondary to first-pass identity:

- complete profile formula atlas excerpts;
- full repository matrix;
- scientific-integrity rule list;
- standards/taxonomy references;
- repository maturity map when not needed for the primary narrative.

Disclosure is an information-architecture decision, not an evidence downgrade.

## 7. Verification-placement rule

CI/workflow badges and account-wide audit references appear in `Evidence and validation`, not directly beneath the hero.

This separates

```text
who I am
from
how the work is verified.
```

## 8. Research-programme placement

Research programmes appear before the deep mathematics sections. A visitor should understand the application questions before encountering the full mathematical machinery.

## 9. Accessibility and rendering

- SVG remains the canonical public mathematical-art format.
- Every public SVG has `<title>`, `<desc>`, `viewBox`, and adaptive light/dark tokens where required.
- Alt text describes scientific purpose rather than appearance alone.
- The public page must remain understandable if images fail to load.

## 10. Scientific non-conflation

The page composition must preserve:

```text
education ≠ equal expertise in every related field
coursework ≠ independent research
research ambition ≠ established contribution
mathematical art ≠ empirical evidence
software verification ≠ empirical validation
repository visibility ≠ evidence maturity
```

## Acceptance criteria

A release conforming to this standard must satisfy:

1. root README uses all available V4 public technical masters;
2. no workflow-status badge appears before `## Evidence and validation`;
3. hero contains compact identity links and navigation only;
4. trajectory is not duplicated by a redundant text-flow block;
5. research programmes appear before deep mathematical detail;
6. complete formulas and repository matrix remain available through disclosure sections;
7. credential and ongoing-programme controls remain unchanged;
8. profile-governance, mathematical-presentation, and adaptive-visual CI gates pass.
