# Profile Credential Verification Checklist

**Control ID:** `DD-PROFILE-CRED-GATE-001`  
**Purpose:** prevent public profile text from silently translating, renaming, upgrading, duplicating or prematurely completing academic credentials.

## Governing rule

A credential may appear in the public profile under a definitive title when the account owner has explicitly confirmed the public wording or when the wording is reconciled against an authoritative record. These are distinct evidence states and must not be conflated.

```text
user-stated / user-corrected title
    ↓
public wording control
    ↓
official document / official programme record when available
    ↓
exact-title reconciliation
    ↓
translation/equivalence note if needed
```

## Credential verification fields

For each credential record, capture:

| Field | Requirement |
|---|---|
| Original-language title | Exact diploma/certificate wording when available |
| User-confirmed public title | Account-owner correction used for public wording when explicitly supplied |
| English public wording | Exact or explicitly identified translation |
| Awarding institution | Exact legal/institutional name |
| Country | Official jurisdiction |
| Level/type | Certificate, technical baccalaureate, diploma, licence/bachelor, master's, etc. |
| Field/specialization | Exact wording where present |
| Completion status | Completed / ongoing / expected |
| Award date | If appropriate for public use |
| Evidence source | User confirmation, diploma, transcript, official portal or programme page |
| Reconciliation status | USER_CONFIRMED / VERIFIED / NEEDS_RECONCILIATION / ONGOING |
| Public-release status | APPROVED / BLOCKED |

## Current controlled items

### Electrical-engineering technical credentials

The following remain `USER_STATED / OFFICIAL_TITLE_TO_VERIFY`:

1. Professional Qualification Certificate in Electricity;
2. Technical Baccalaureate of Benin — Electrical Engineering;
3. Diploma in Electrical Engineering.

**Required next evidence:** clear image/PDF/transcript or exact official text from each credential.

### Undergraduate renewable-energy credential

The account owner explicitly corrected the public French title on 2026-09-12 to:

> **Licence, Énergies Renouvelables et Systèmes Énergétiques — Université d’Abomey-Calavi**

Status: `USER_CONFIRMED_PUBLIC_TITLE`.

This correction resolves the stale public wording. It does **not** establish an independent documentary-verification state and it does not authorize a silent English replacement.

Translation/equivalence boundary:

```text
French public title = user-confirmed
English translation/equivalence = separate evidence question
```

If an English rendering is later needed, it must be explicitly labeled and supported rather than substituted for `Licence`.

### Graduate programmes

- MSE Sustainable Engineering — `ONGOING`;
- MS Financial Engineering — `ONGOING`.

They must remain explicitly ongoing until completion is supported by the official academic record.

## Translation rule

If an official credential is in French or another language, preserve the original title and, where useful, provide a clearly labelled English translation rather than replacing the original silently.

Preferred pattern:

```text
Official/original-language title — Institution
(English translation: ...)
```

when the translation materially helps an international reader.

## Prohibited transformations

Do not automatically convert:

- `Licence` → `Bachelor of Science` or another English degree title without controlled translation/equivalence evidence;
- technical/professional certificates → university diplomas;
- diploma titles → occupational licenses;
- ongoing master's programmes → completed degrees;
- a specialization description → a formal degree title.

## Release gate

A public credential wording may be released as `USER_CONFIRMED` when the account owner explicitly corrects their own public profile wording. `VERIFIED` remains reserved for authoritative documentary or institutional evidence.

For documentary verification, the stronger state requires:

```text
exact title verified
AND institution verified
AND completion status verified
AND translation/equivalence explicitly controlled
```

Otherwise preserve the exact user-confirmed original-language wording and avoid stronger translation/equivalence claims.