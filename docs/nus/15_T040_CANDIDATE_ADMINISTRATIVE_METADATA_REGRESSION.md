# T040 Candidate — Administrative Metadata Beyond Obvious Front Matter

## Status

```text
CANDIDATE_REGRESSION
NOT_YET_PERMANENT
```

## Observed failure class

After the NUS-48 V8 preprocessing pipeline reached `58/58 PASS`, automated scientific adjudication still found six clearly non-scientific records in the atomic-claim register.

Examples included orphaned address/editorial tails such as:

```text
Tronoh, Perak 32610, Malaysia.
Box 11099, Taif 21944, Saudi Arabia.
Data availability ...
Received: 1 July 2024
Accepted: 26 November 2024
```

These records were safely excluded during adjudication, so they did not contaminate final scientific evidence.

## Why this is distinct from T033–T036

T033–T036 already protect contact/publisher/affiliation metadata and representation-boundary leakage. The new observation is that administrative metadata may survive without obvious markers such as:

```text
Department
email
DOI
publisher URL
```

The potential new generic invariant is therefore broader:

```text
Scientific claim construction must exclude structurally bounded administrative metadata,
including orphaned address tails and editorial/process metadata even when obvious affiliation/contact tokens are absent.
```

## Candidate acceptance requirements

Before promotion to permanent `T040`, a generic implementation should demonstrate:

1. exclusion of orphaned postal/address tails in front matter;
2. exclusion of editorial-process lines such as `Received`, `Accepted`, and similar administrative metadata;
3. exclusion of data-availability boilerplate when it is administrative rather than scientific evidence;
4. preservation of legitimate scientific prose containing place names, dates, addresses, or the word `data`;
5. no paper-specific university/city/country hard-coding;
6. independent negative controls against over-filtering;
7. historical regression suite remains green.

## Promotion rule

Promote `T040` from candidate to permanent only after:

```text
observed NUS-48 examples
→ generic structural rule
→ implementation
→ positive controls
→ negative controls
→ independent test
→ historical retest
```

This promotion should occur before NUS-18 generalization if the generic implementation can be validated without reopening the already adjudicated NUS-48 scientific state.

## Governance consequence

The existence of this candidate does not revoke:

```text
PASS_AUTOMATED_SCIENTIFIC_ADJUDICATION_READY_FOR_HUMAN_REVIEW
```

because the six records were explicitly identified and excluded during adjudication.

It does mean the generic engine should not be considered fully generalization-ready for NUS-18 until this candidate lesson is deliberately resolved.
