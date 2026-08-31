# T040 — Administrative Metadata Regression History

## Historical state

T040 was first recorded as a **candidate regression** after automated scientific adjudication found six non-scientific administrative records that had survived preprocessing.

That candidate state is preserved as part of the failure-learning chronology.

## Current authoritative state

```text
T040 = PERMANENT
Regression corpus = NUS_MASTER_FAILURE_REGRESSION_CORPUS_V17
Regression range = T001–T047
```

## Permanent failure

Scientifically non-substantive administrative fragments survived atomic-claim preprocessing, including orphaned affiliation-address tails and back-matter Data availability / Received / Accepted records.

Examples include:

```text
Tronoh, Perak 32610, Malaysia.
Box 11099, Taif 21944, Saudi Arabia.
Data availability ...
Received: 1 July 2024
Accepted: 26 November 2024
```

## Root cause

Metadata exclusion recognized complete contact/affiliation structures but did not fully cover structurally bounded administrative fragments that lack organization/contact keywords and can appear as grammatical sentences.

## Permanent invariant

Scientific claim construction must exclude structurally bounded non-scientific administrative fragments at every representation boundary, including:

```text
orphaned affiliation/address tails
Data availability administration
Received/Accepted editorial metadata
```

while preserving genuine scientific prose containing ordinary place names or dates.

## Permanent test

Synthetic and NUS-48 controls must exclude the known administrative examples while preserving true scientific prose containing place names or dates.

## Governance consequence

The earlier `CANDIDATE_REGRESSION` designation is no longer current. It remains only as historical evidence of how the failure was discovered, generalized, tested, and promoted before Generic NUS Evidence Engine V1 was frozen.
