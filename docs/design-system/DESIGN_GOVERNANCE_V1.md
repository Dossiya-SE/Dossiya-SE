# Account-wide Design Governance V1

**Contract ID:** DOSS-GITHUB-DESIGN-V1  
**Status:** FROZEN FOR IMPLEMENTATION  
**Scope:** all GitHub repositories exposed through the Dossiya-SE GitHub installation.

## Governing objective

Every public artifact must communicate scientific role before decoration. Visual design is accepted only when it improves mathematical interpretation, physical mechanism, evidence state, computational role, navigation, uncertainty communication, or reproducibility.

## Canonical visual identity

| Role | RGB | Hex | Use |
|---|---:|---|---|
| Primary accent | (135,206,250) | `#87CEFA` | interface, decision, highlight, callout |
| Strong accent | (0,191,255) | `#00BFFF` | focus, hover, strong dark-surface emphasis |
| Light-background companion | (45,143,214) | `#2D8FD6` | geometry and line work |
| Light-background text | (40,120,205) | `#2878CD` | accessible accent text |
| Dark-background text | (191,232,255) | `#BFE8FF` | accessible accent text |

Gold, amber, ochre and yellow-gold are not permitted account visual roles. Warm hues require explicit scientific meaning and a documented figure manifest.

## Scientific semantic colors

- Power: red.
- Transportation: green.
- Information: blue.
- Mathematical abstraction: violet.
- Organization/coordination: magenta.
- Interface/decision/control/highlight: Light Sky Blue family.
- Critical boundary/failure: red plus a non-color cue.
- Verified/viable: green plus a label/geometry cue.

Color is never the only carrier of meaning.

## Typography

1. System sans-serif for explanatory text.
2. Mathematical serif for mathematical expressions where useful.
3. Monospace only for code, identifiers, states, hashes and computed quantities.
4. Governed SVG text must remain legible at 640 px and 980 px.
5. No canonical vector master may rasterize its text.

## SVG contract

Every governed SVG requires a canonical `viewBox`, non-empty `<title>` and `<desc>`, accessibility role where appropriate, deterministic or documented provenance, bounded layout/collision logic, and a stable figure ID for governed figure families.

## Evidence-state invariant

```text
[S] source-grounded
[D] derived
[M] model
[C] computed
[V] verified
[E] empirical
[H] hypothesis
[T] engineering/design target
```

Visualization must not upgrade epistemic status.

## Repository roles

- **FLAGSHIP_PUBLIC** — profile, portfolio, public research identity.
- **RESEARCH_LAB** — executable scientific or quantitative laboratory.
- **RESEARCH_ECOSYSTEM** — modular research infrastructure.
- **ARCHIVE_SUPPORT** — frozen evidence and support material.

Visual density and animation decrease from FLAGSHIP_PUBLIC to ARCHIVE_SUPPORT.

## Fail-closed release rule

```text
MATHEMATICS
→ SEMANTICS
→ PALETTE
→ LAYOUT
→ TYPOGRAPHY
→ ACCESSIBILITY
→ RENDER
→ REGRESSION
→ PROVENANCE
→ INTEGRATION
```

A failed mandatory gate blocks publication.
