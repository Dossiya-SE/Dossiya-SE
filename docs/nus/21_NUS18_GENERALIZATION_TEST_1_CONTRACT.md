# NUS-18 — Generalization Test #1 Contract

## Paper identity

**Paper:** NUS-18  
**Title:** *An integrated energy-emergy approach to building form optimization: Use of EnergyPlus, emergy analysis and Taguchi-regression method*  
**DOI:** `10.1016/j.buildenv.2014.10.013`

Historical Frozen-37/Zotero records resolve:

```text
parent_key = BZZGBD2I
attachment_key = Z8UEF2GH
attachment_item_id = 3442
historical_pdf_sha256 = 826beba0d3973661137328c8d68ac992a8d03fa91860d69ee8c1c196010c3839
```

The historical record also confirms one local PDF for NUS-18. The PDF SHA-256 must still be freshly recomputed from the live attachment before it becomes the current execution lock.

## Test objective

NUS-18 is not another calibration paper. It is the first true generalization test of Generic NUS Evidence Engine V1.

The governing question is:

```text
Can the frozen engine process a structurally different paper correctly
without bespoke pipeline redesign?
```

## Success criterion

```text
NUS18_SUCCESS =
  correct source identity
  AND fresh live PDF SHA-256 = expected historical/current lock
  AND complete read-only extraction
  AND complete physical-surface inventory
  AND applicable T001–T047 regressions pass
  AND independent certification passes
  AND scientifically defensible adjudication
  AND no paper-specific engine redesign
```

## What may change

Only paper-specific configuration/data should normally change:

```text
paper_id
parent_key
attachment_key
expected_pdf_sha256
source-derived claim counts
surface counts
scientific evidence content
scientific conclusions
final evidence count
```

## What must not change merely because this is NUS-18

```text
nine-role ontology
focality-before-role order
provenance architecture
surface-adjudication contract
output-nature visible-comment rule
role colors
zero-tag rule
exact-author-wording rule
mutation authorization equation
transactional writer contract
independent auditor contract
T001–T047 knowledge
```

## NUS-18 paper-specific scientific risk areas to test without hard-coding

Existing historical evidence indicates the paper contains building-form variables, EnergyPlus-based operational-energy outputs, construction/resource inventories, emergy transformities, Taguchi L18 design, ANOVA, regression metamodels, emergy outputs, and optimization. These are useful **prior expectations for audit coverage only**; they must not become hard-coded scientific conclusions in the engine.

Likely structural families to test include:

```text
building-form alternatives
EnergyPlus engineering/energy simulation
emergy accounting/transformations
Taguchi/ANOVA/regression modelling
optimization/decision selection
```

The engine must derive actual focal roles, transformations, metrics, outputs, provenance, and decisions from the verified focal PDF.

## Required first-run sequence

```text
1. Resolve parent BZZGBD2I and attachment Z8UEF2GH in live Zotero
2. Verify DOI/title/parent-child relationship
3. Freshly compute PDF SHA-256
4. Compare to historical expected hash
   826beba0d3973661137328c8d68ac992a8d03fa91860d69ee8c1c196010c3839
5. Inventory live native annotations without mutation
6. Run read-only extraction
7. Construct atomic claims
8. Inventory every physical table/figure/equation
9. Run applicable T001–T047 master regressions
10. Run independent certification
11. Perform scientific adjudication
12. Human review
13. Geometry/schema/writer/auditor only after authorization
```

## Fail-closed identity rule

If the freshly computed live PDF hash differs from the historical hash, do **not** silently replace the expected hash and do not begin scientific extraction. Resolve whether the attachment bytes changed, whether the historical record refers to a different local copy, or whether a controlled new source identity must be frozen.

## Fail-closed engine rule

If NUS-18 reveals an apparent defect, classify it first:

```text
paper-specific scientific difference
vs
existing known failure class
vs
new general failure class
```

Only the third category can justify a generic engine modification.

## Anti-bespoke gate

Before adding any new code, answer:

```text
1. What exact observed failure occurred?
2. Why is it not already covered by T001–T047?
3. What paper-independent invariant does it violate?
4. What new permanent regression would reproduce it?
5. Does the proposed fix pass historical NUS-172/NUS-48 regression controls?
```

If these five questions cannot be answered, do not redesign the engine.

## Generalization metrics

Record:

```text
manual_execution_steps
manual_adjudication_actions
new_defect_count
new_general_failure_count
new_regression_count
bespoke_code_change_count
engine_files_changed
paper_config_fields_changed
```

Target:

```text
bespoke_code_change_count = 0
engine_files_changed = 0
```

for a clean first generalization pass.

## Output-nature contract for NUS-18

Visible nature is exposed only for outputs:

```text
Engineering output here is [evidence-grounded nature] : [exact author wording]
Sustainability output here is [environmental/economic/social/integrated] : [exact author wording]
```

No nature is added to PURPOSE, INTERVENTION, INPUT, ENGINEERING_METHOD, SUSTAINABILITY_TRANSFORMATION, SUSTAINABILITY_METHOD, or DECISION.

## Completion states

Possible outcomes:

```text
PASS_GENERALIZATION_NO_ENGINE_CHANGE
PASS_GENERALIZATION_WITH_NEW_GENERAL_REGRESSION
ABSTAIN_OR_FAIL_SOURCE_STATE
ABSTAIN_OR_FAIL_ENGINE
ABSTAIN_OR_FAIL_SCIENTIFIC
```

The preferred outcome is:

```text
PASS_GENERALIZATION_NO_ENGINE_CHANGE
```

That is the decisive evidence that the NUS architecture is becoming scalable.
