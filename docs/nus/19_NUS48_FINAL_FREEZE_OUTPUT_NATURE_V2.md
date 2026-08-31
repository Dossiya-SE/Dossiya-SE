# NUS-48 Final Freeze — Output-Nature V2

## Governing state

```text
NUS-48 = FROZEN OUTPUT-NATURE V2
```

No further annotation, comment, geometry, color, role, tag, or ontology mutation is permitted unless a genuinely new scientific requirement is formally introduced through the controlled change process.

## Final certified annotation state

```text
Paper                     NUS-48
Annotations               33
Highlights                20
Regions                   13
Tags                       0

Comment migrations         13
Engineering outputs:
  mechanical               6

Sustainability outputs:
  environmental            4
  economic                 3
  social                   0
  integrated               0

Internal second-pass Δ     0
Idempotency                PASS
Unauthorized changes       0
PDF mutation               false
Other Zotero mutation      false
```

## Frozen visible-comment convention

```text
Engineering output here is mechanical : [ exact author wording]

Sustainability output here is environmental : [ exact author wording]

Sustainability output here is economic : [ exact author wording]
```

No unsupported social or integrated sustainability output is introduced.

The general output-nature rule is:

```text
ENGINEERING_OUTPUT
→ Engineering output here is {evidence-grounded engineering nature} : exact author wording

SUSTAINABLE_OUTCOME
→ Sustainability output here is {environmental|economic|social|integrated} : exact author wording
```

All seven other evidence roles retain their simple visible labels.

## Frozen authorities

```text
PDF SHA-256
bd27b10cb8110d7a48a0b28923e3e0cc2adc0fb2d7e416fb25714f8483db3609

Schema V2 SHA-256
ec29431fd42469679e6442314bca0b97ad22c77bb2a1c226fd29f0ebdb3688e4

Migration report SHA-256
c5eb4caa289342d6fe2f9aa8703fe5476507f208584b0dadd69f186d0e1272f0

Post-write audit SHA-256
bab0e14ee3a49b3b0c878f8f0dc997882119097c25976ba712c5e260610d930c

Freeze manifest SHA-256
e5a798f1099a76835ba964ecf1376bd69b8d5cd504c7029f08378cfd0ea90009
```

## Regression closure

The permanent failure/regression history now extends through:

```text
T001 → T047
```

T047 permanently captures the migration-state overlap defect:

```text
When schema versions differ only on a subset of records/fields,
migration phase must be classified from the discriminating subset.
Version-invariant records validate payload integrity but do not vote
on migration version.
```

## Final release chain

```text
PDF
→ scientific adjudication
→ geometry
→ schema
→ authorized write
→ output-nature migration
→ post-write audit
→ Δ=0
→ FROZEN
```

## Freeze rule

NUS-48 is no longer an active development paper. It is now a frozen calibration authority for the generic NUS Evidence Engine.

Any future NUS-48 change requires:

```text
new scientific requirement
→ formal change request
→ affected invariant(s)
→ regression impact analysis
→ explicit authorization
→ controlled mutation
→ independent audit
→ successor freeze
```

Implementation preference alone is not a valid reason to reopen NUS-48.
