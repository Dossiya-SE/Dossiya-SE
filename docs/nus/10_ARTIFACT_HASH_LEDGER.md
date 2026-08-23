# Controlled Artifact Hash Ledger

This ledger records known authoritative or historically important artifacts mentioned during NUS-48 development. It is not a substitute for the actual files; it records names, roles, and known SHA-256 values.

## Source identity

```text
NUS-48 focal PDF
SHA-256: bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609
```

## Early extraction/preprocessing

```text
NUS48_PHASE1_READONLY_DISCOVERY_V1.txt
SHA-256: aeb6cef7ef46ce891bce11fead0583d012dda3f9a703fc8eedec5c573f7145ce

NUS48_PHASE2_ATOMIC_CLAIM_PREPROCESSOR_V1
SHA-256: 01895fa6769cfdb792923e7e5616000bfb4ef543a02929af0c01c3e1c176c3f0
```

## V2 master

```text
NUS48_MASTER_PREMUTATION_REGRESSION_HARNESS_V2
SHA-256: 00c8772cccc462c1fed6060838d257537644875b38cd69e5e376154e87b13ddd
```

## Historical one-shot / generic-engine transition artifacts

```text
NUS48_ONESHOT_PREMUTATION_READINESS_V1.txt
SHA-256: ce9ff50c745801b9fd71857733014f24f4f152b879e5c18ce6d77b2981b03250

NUS_EVIDENCE_ENGINE_V1_FOUNDATION.zip
SHA-256: 213812bef9a8bf5eed4a4585d464299c71eb399b18c1f0e1540198b902df06fa

NUS48_TO_GENERIC_ENGINE_FREEZE_PACKAGE_V1.zip
SHA-256: dbaa6771484f04ac630bfa09470ef5cbec3fee6f170bc003c2bf150ad939f6f7
```

## Repair-spec artifacts produced during development

```text
NUS48_PREMUTATION_REPAIR_SPEC_V2_4.json
SHA-256: b92e3f9b1bb5ce8e56bae357d9ffd645aea86344563468f86eba83b9be76179c

NUS48_T033_FRONTMATTER_BLOCK_REPAIR_SPEC_V3_1.json
SHA-256: 66f590bad47a57e5e185f593238484640c15365a98d3c15237d6740f6972138e

NUS48_MASTER_V2R5_DEPENDENCY_CLOSURE_FIX_AND_RUN_V1.txt
SHA-256: cbc913c2495fe6ea2baf8a0a159f9cf83e0cb01bfad6286b68f8bf6225d2ca6e

NUS48_T037_REGRESSION_DEPENDENCY_CLOSURE_REPAIR_SPEC_V1.json
SHA-256: 41935a97e424898d80cf8044decd0a49812180b23e5fe1ed6b68e5ae47a4d0dc
```

## Final V8 premutation state

```text
NUS48_ONESHOT_PREMUTATION_READINESS_BUNDLE_V8.json
SHA-256: 5359ccd275db4d4aefb1a2ab76d734a2b2e7ef547207b098f28e92ed4541d69e

NUS48_ONESHOT_PREMUTATION_READINESS_MANIFEST_V8.json
SHA-256: 646e312f7e74f878575e5cb2d6d5ec82d5023a13afce793ce5fa4086ca1dfd9e

NUS48_ONESHOT_PREMUTATION_READINESS_V8.txt
SHA-256: b4b4ba0448607e531f07eee39d30a6a114172d9f6aed3a2a080bc992f13f3988

NUS_MASTER_FAILURE_REGRESSION_CORPUS_V10.json
SHA-256: 6f75090892388582800b407c1efb8f094802fbaef72d3570f61d8d300f736ccc
```

## Automated scientific adjudication V1

```text
NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_V1.json
SHA-256: 0ac73aaaf5ca0c8d2fc418e5b4c0cd50c9e0f81f320b40260bd4c1eb7087b804

NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_REPORT_V1.md
SHA-256: 11530e457a43fe9e10c32df561814f1099b79d2cecfb359e12a8041d795b0898

NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_MANIFEST_V1.json
SHA-256: b077dc69466d97279a95a6963359c39855fd956b2f569af4248f29cda4cbfe9f

NUS48_AUTOMATED_SCIENTIFIC_ADJUDICATION_REVIEW_PACKAGE_V1.zip
SHA-256: 8e9645b3b559a278ade368b4ae6db31dc6930793d40e3965deea3f6133714093
```

## Hash-governance rules

1. Do not trust a filename as identity.
2. Verify bytes against expected SHA-256 before using an artifact as authority.
3. Do not use an embedded self-hash as sole authority.
4. Persisted artifacts and returned objects must not silently diverge.
5. Cross-component manifests must be checked against actual persisted bytes.
6. Historical artifacts are immutable evidence history; create successor versions instead of overwriting them.
