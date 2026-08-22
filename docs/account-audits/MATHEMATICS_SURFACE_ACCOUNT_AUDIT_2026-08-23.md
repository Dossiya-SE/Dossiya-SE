# Account-wide mathematics-surface audit

**Account:** [Dossiya-SE](https://github.com/Dossiya-SE)  
**Audit date:** 2026-08-23  
**Tool:** `engineer-math-surfaces 1.3.0`  
**Scope:** all 16 repositories owned by the connected GitHub account  
**Release state:** `ZERO_ACTIVE_HIGH_CONFIDENCE_FINDINGS_ON_VERIFIED_BRANCHES`

## What this result means

The audit separates mathematical meaning from publication-surface correctness.
It verifies whether authored formulas are exposed to the relevant renderer,
whether deterministic repairs preserve TeX bodies and Markdown structure, and
whether extracted expressions parse with independent renderers. It does not
claim that every scientific model or equation is empirically validated.

Official contracts:

- [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
- [github/cmark-gfm](https://github.com/github/cmark-gfm)
- [MathJax accessibility components](https://docs.mathjax.org/en/latest/web/components/accessibility.html)
- [KaTeX options and strict mode](https://katex.org/docs/options)

## Account result

| Metric | Result |
|---|---:|
| Owned repositories inventoried | 16 |
| Markdown/MDX files audited | 637 |
| Confirmed active baseline findings | 323 |
| Active high-confidence findings after verified repairs | 0 |
| Preserved archival, conversation, verbatim or source-note review findings | 730 |
| Extracted formulas checked with both renderers | 1,491 |
| MathJax 4.1.3 failures | 0 |
| strict KaTeX 0.18.4 failures | 0 |

## Repository register

| Repository | Markdown/MDX | Baseline disposition | Formula gate | Release record |
|---|---:|---|---:|---|
| [africa-energy-dignity](https://github.com/Dossiya-SE/africa-energy-dignity) | 36 | 0 active findings | 38/38 pass | No source change |
| [chatbot](https://github.com/Dossiya-SE/chatbot) | 1 | 0 active findings | 1/1 pass | No source change |
| [Data-Science-an-Machine-Learning](https://github.com/Dossiya-SE/Data-Science-an-Machine-Learning) | 1 | 0 active findings | 1/1 pass | No source change |
| [Differential geometry and mathematics arts](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience) | 48 | 17 corrected | 121/121 pass | [PR #15 merged](https://github.com/Dossiya-SE/Differential-geometry-and-Mathematics-arts-for-sustainability-and-resilience/pull/15) |
| [Dossiya-SE profile](https://github.com/Dossiya-SE/Dossiya-SE) | 21 | 28 corrected | 109/109 pass | [PR #14](https://github.com/Dossiya-SE/Dossiya-SE/pull/14) |
| [Dossiya-SE-Dossiya-SE](https://github.com/Dossiya-SE/Dossiya-SE-Dossiya-SE) | 49 | 224 corrected | 234/234 pass | [PR #16](https://github.com/Dossiya-SE/Dossiya-SE-Dossiya-SE/pull/16) |
| [MScFE quantitative-finance lab](https://github.com/Dossiya-SE/Dossiya-SE-mscfe-quantitative-finance-lab) | 90 | 0 active findings | 168/168 pass | [PR #34](https://github.com/Dossiya-SE/Dossiya-SE-mscfe-quantitative-finance-lab/pull/34) |
| [dossiya-se.github.io](https://github.com/Dossiya-SE/dossiya-se.github.io) | 4 | 28 corrected | 31/31 pass | [PR #8](https://github.com/Dossiya-SE/dossiya-se.github.io/pull/8) |
| [dossiyadakou-mac-project](https://github.com/Dossiya-SE/dossiyadakou-mac-project) | 7 | 0 active findings | 129/129 pass | No source change |
| [infrastructure-interface-resilience-review](https://github.com/Dossiya-SE/infrastructure-interface-resilience-review) | 103 | 14 corrected | 347/347 pass | [PR #39](https://github.com/Dossiya-SE/infrastructure-interface-resilience-review/pull/39) |
| [Kudo-IA](https://github.com/Dossiya-SE/Kudo-IA) | 2 | 0 active findings | 4/4 pass | [PR #4](https://github.com/Dossiya-SE/Kudo-IA/pull/4) |
| [Math-Surface-Engineer-Demo](https://github.com/Dossiya-SE/Math-Surface-Engineer-Demo) | 7 | 0 active; 1 archival review preserved | 10/10 pass | No source change |
| [MSE-thesis](https://github.com/Dossiya-SE/MSE-thesis) | 166 | 12 corrected; 671 archival/verbatim reviews preserved | 291/291 pass | [PR #12](https://github.com/Dossiya-SE/MSE-thesis/pull/12) |
| [Python-for-rapid-engineering-solution](https://github.com/Dossiya-SE/Python-for-rapid-engineering-solution) | 1 | 0 active findings | 1/1 pass | No source change |
| [responsible-gold-access-network-rgan](https://github.com/Dossiya-SE/responsible-gold-access-network-rgan) | 100 | 0 active; 58 source-note/archive reviews preserved | 3/3 pass | [PR #11](https://github.com/Dossiya-SE/responsible-gold-access-network-rgan/pull/11) |
| [testasu](https://github.com/Dossiya-SE/testasu) | 1 | 0 active findings | 3/3 pass | No source change |

## Verification gates

Automatic repairs were released only after:

1. deterministic dry-run patch generation;
2. patch applicability and whitespace checks;
3. post-repair scanner execution;
4. TeX-body SHA-256 preservation records;
5. exact `cmark-gfm 0.29.0.gfm.13` structural comparison;
6. MathJax 4.1.3 and strict KaTeX 0.18.4 parsing;
7. separation of active publications from archival, conversation, source-note
   and verbatim evidence.

## Declared limitations

- Renderer success establishes syntactic compatibility, not theorem correctness,
  empirical validity or model adequacy.
- Native Quarto, MDX application compilers, notebooks and generated HTML require
  their own project-specific contracts; they were inventoried but are not
  misreported as GitHub-Markdown validations.
- GitHub Actions in the five private repositories terminated before executing
  job steps during this audit. Their hosted CI state is `UNEXECUTED`; their
  content results come from byte-preserved authenticated mirrors at recorded
  commit hashes.
- Default branches were not protected at the frozen inventory time. Repository
  rulesets remain a separate account-governance action.

## Interpretation rule

```math
G_{\mathrm{release}}
=
G_{\mathrm{syntax}}
\land G_{\mathrm{semantic}}
\land G_{\mathrm{render}}
\land G_{\mathrm{provenance}}.
```

No review-only archival item is silently promoted to a confirmed defect, and no
unexecuted gate is reported as a pass.
