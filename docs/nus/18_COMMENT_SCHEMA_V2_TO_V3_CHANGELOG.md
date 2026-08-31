# Comment Schema V2 → V3 Changelog

## Status

```text
V2 = SUPERSEDED
V3 = FROZEN / AUTHORITATIVE
```

## What did not change

The following remain unchanged:

```text
nine evidence roles
Q → I → M_E → P → F → M_S → S → D architecture
PURPOSE outside the chain
role colors
zero annotation tags
focality rules
citation-scope rules
provenance rules
transformation logic
physical-surface rules
exact-author-wording rule
nonredundancy rule
N_final not preset
```

## What changed

### V2 proposal

V2 proposed visible scientific nature for all nine roles:

```text
ROLE here is SCIENTIFIC NATURE : EXACT AUTHOR WORDING
```

### V3 authority

V3 narrows nature to output roles only:

```text
ENGINEERING_OUTPUT
SUSTAINABLE_OUTCOME
```

The other seven roles use simple semantic labels.

## Authoritative V3 patterns

```text
Purpose : [exact author wording]
Intervention : [exact author wording]
Input : [exact author wording]
Engineering method : [exact author wording]
Engineering output here is [engineering nature] : [exact author wording]
Sustainability transformation : [exact author wording]
Sustainability method : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
Decision : [exact author wording]
```

## Engineering-output nature expansion

V3 controlled engineering natures:

```text
mechanical
fresh-state
physical
durability
transport/permeability
thermal
structural/functional
fracture/damage
time-dependent
constructability/production
```

## Sustainability-output nature constraint

```text
environmental
economic
social
integrated
```

with:

```text
ENV + ECO + SOC ≠ INT
```

## Reason for the change

Nature is highly useful for understanding the scientific kind of an **output**, but applying a nature descriptor to every role makes visible Zotero comments unnecessarily complex and duplicates information better retained in the external ledger.

V3 therefore maximizes human interpretability while minimizing visible-comment ontology load.

## Migration impact

For new papers, V3 is the default generic-engine schema.

For already-written NUS-48 annotations, V3 does not automatically apply. The later project update states that 33 native annotations already exist under the prior authorized schema.

Changing those comments is a controlled migration, not a formatting cleanup.

## Prohibited shortcuts

Do not:

- manually edit individual existing comments;
- add a nature to a non-output role;
- infer an output nature from background discussion;
- expand author abbreviations in the exact wording suffix;
- change colors because of nature;
- add tags to represent nature;
- increase annotation count because of the new schema;
- classify `integrated` from simple multi-domain co-occurrence.

## Machine authority

```text
docs/nus/machine/comment_generation_rule_v3.json
```

Migration contract:

```text
docs/nus/machine/comment_schema_migration_contract_v1.json
```
