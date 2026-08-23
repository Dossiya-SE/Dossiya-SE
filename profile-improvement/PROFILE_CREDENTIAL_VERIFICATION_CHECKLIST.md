# Profile Credential Verification Checklist

**Control ID:** `DD-PROFILE-CRED-GATE-001`  
**Purpose:** prevent public profile text from silently translating, renaming, upgrading, duplicating or prematurely completing academic credentials.

## Governing rule

A credential may appear in the public profile under a definitive official title only when its wording and status are reconciled against the authoritative record.

```text
user-stated title
    ↓
official document / official programme record
    ↓
exact-title reconciliation
    ↓
translation/equivalence note if needed
    ↓
public wording approved
```

## Credential verification fields

For each credential record, capture:

| Field | Requirement |
|---|---|
| Original-language title | Exact diploma/certificate wording |
| English public wording | Exact or explicitly identified translation |
| Awarding institution | Exact legal/institutional name |
| Country | Official jurisdiction |
| Level/type | Certificate, technical baccalaureate, diploma, licence/bachelor, master's, etc. |
| Field/specialization | Exact wording where present |
| Completion status | Completed / ongoing / expected |
| Award date | If appropriate for public use |
| Evidence source | Diploma, transcript, official portal or programme page |
| Reconciliation status | VERIFIED / NEEDS_RECONCILIATION / ONGOING |
| Public-release status | APPROVED / BLOCKED |

## Current unresolved items

### Electrical-engineering technical credentials

The following are currently `USER_STATED / OFFICIAL_TITLE_TO_VERIFY`:

1. Professional Qualification Certificate in Electricity;
2. Technical Baccalaureate of Benin — Electrical Engineering;
3. Diploma in Electrical Engineering.

**Required next evidence:** clear image/PDF/transcript or exact official text from each credential.

### Undergraduate renewable-energy credential

Two descriptions currently coexist:

- current public profile: `Licence Professionnelle, Énergies Renouvelables et Systèmes Énergétiques`;
- newer user description: `Bachelor of Physical Science in Renewable Energy and Energy Systems`.

These must not be treated as interchangeable until their relationship is established.

Required determination:

```text
same credential + translation/equivalence
OR
same programme but different public naming convention
OR
different credentials
```

Status: `RECONCILE_BEFORE_PUBLIC_CHANGE`.

### Graduate programmes

- MSE Sustainable Engineering — `ONGOING`;
- MS Financial Engineering — `ONGOING`.

They must remain explicitly ongoing until completion is supported by the official academic record.

## Translation rule

If an official credential is in French or another language, preserve the original title and, where useful, provide a clearly labelled English translation rather than replacing the original silently.

Preferred pattern:

```text
Official title — Institution
(English translation: ...)
```

when the translation materially helps an international reader.

## Prohibited transformations

Do not automatically convert:

- `Licence Professionnelle` → `Bachelor of Science`;
- technical/professional certificates → university diplomas;
- diploma titles → occupational licenses;
- ongoing master's programmes → completed degrees;
- a specialization description → a formal degree title.

## Release gate

A definitive public credential title is `APPROVED` only if:

```text
exact title verified
AND institution verified
AND completion status verified
AND translation/equivalence explicitly controlled
```

Otherwise use broader narrative language such as `electrical-engineering foundation`, `renewable-energy and energy-systems background`, or `pursuing graduate study in ...` where that wording is supported without asserting an unresolved official credential title.
