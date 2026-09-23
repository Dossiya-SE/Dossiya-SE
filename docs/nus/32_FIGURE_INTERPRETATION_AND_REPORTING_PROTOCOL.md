Yes. Before interpreting each figure, we should use a **fixed scientific protocol** so that every figure is read consistently and we do not confuse description, engineering explanation, quantitative evidence, and sustainability meaning.

The central rule should be:

```math
\boxed{ \text{Figure} \rightarrow \text{What is measured} \rightarrow \text{What changes quantitatively} \rightarrow \text{Why it matters engineering-wise} \rightarrow \text{How it enters sustainability} \rightarrow \text{What conclusion is justified} }
```

# 1. Six things required for a strong figure interpretation

For every figure, extract these six layers.

| LayerQuestion                      |                                                                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Figure identity**             | What exactly is plotted? What are `x`, `y`, units, alternatives, ages, baseline?                                                     |
| **2. Quantitative result**         | What increases/decreases? By how much? Where are minima/maxima? Is the trend monotonic or nonlinear?                                 |
| **3. Engineering meaning**         | What engineering property is represented and what does the change physically mean?                                                   |
| **4. Transformation role**         | Is the figure an input, engineering output, direct sustainability output, normalized metric, sensitivity result, or decision result? |
| **5. Sustainability meaning**      | Does it concern environmental burden, economic burden, resource efficiency, performance-normalized sustainability, trade-offs, etc.? |
| **6. Evidence-bounded conclusion** | What can legitimately be concluded—and what cannot?                                                                                  |

---

# 2. Engineering logic

The engineering interpretation should answer:

```math
\boxed{ \text{material/intervention} \rightarrow \text{physical response} \rightarrow \text{engineering performance} }
```

For example, with FNS replacement:

```math
\%FNS \rightarrow \text{material/microstructural change} \rightarrow f'_c,\;UPV,\;\text{density},\ldots
```

A good engineering interpretation identifies:

- property being measured;
- functional significance;
- control/reference;
- whether performance is maintained, enhanced, or degraded;
- whether an optimum or threshold exists;
- whether the paper provides a physical explanation.

### Good wording

> “The figure shows that 10% FNS preserves 28-day compressive strength close to the control, indicating that this replacement level maintains the principal mechanical function required for subsequent sustainability normalization.”

Notice the sequence:

**result → engineering meaning → sustainability relevance.**

---

# 3. Quantitative logic

Every figure should be interrogated numerically.

At minimum record:

```math
x_{\text{control}},\quad x_{\text{best}},\quad \Delta x,\quad \%\Delta x
```

where appropriate.

For a reduction:

```math
\%\text{ reduction} = \frac{X_0-X_i}{X_0}\times100
```

For an improvement:

```math
\%\text{ improvement} = \frac{X_i-X_0}{X_0}\times100
```

But the **direction of “improvement” depends on the metric**.

For example:

- compressive strength: usually ↑ desirable;
- EE: ↓ desirable;
- GWP: ↓ desirable;
- cost: ↓ desirable;
- SI in these papers: ↓ desirable;
- EI: ↓ desirable.

This direction must be stated rather than assumed.

## Also identify the shape

Ask whether the figure is:

- monotonic;
- approximately linear;
- nonlinear;
- U-shaped;
- inverted U-shaped;
- plateauing;
- threshold-like;
- optimum-containing.

This matters enormously.

For example:

```math
\downarrow GWP \text{ continuously}
```

does **not** mean:

```math
\downarrow SI \text{ continuously}
```

because SI also depends on strength.

---

# 4. Sustainability logic

This is the most important part for your review.

Each figure should be classified according to where it lies in:

```math
\boxed{ I \rightarrow F \rightarrow S }
```

More specifically:

```math
\boxed{ \text{Inventory inputs} \rightarrow \text{Sustainability transformation} \rightarrow \text{Sustainability outcome} }
```

But engineering performance can enter the middle:

```math
\text{Engineering assessment} \rightarrow P_{\text{used}} \rightarrow F \rightarrow S
```

So classify every visual.

### Type A — Sustainability input evidence

Example: **NUS-15 Table 5**

```math
m_i,\ EE_c,\ GWP_c
```

This does not show sustainability performance itself.

It supplies the coefficients required to calculate it.

---

### Type B — Engineering output

Example: **NUS-15 Fig. 10**

```math
\%FNS \rightarrow f'_{c28d}
```

This is an engineering result.

But because `f'_{c28d}` subsequently enters SI and EI:

```math
f'_{c28d} \rightarrow SI,\;EI
```

it becomes an **engineering output used as a sustainability input**.

That dual role is important.

---

### Type C — Direct sustainability output

Examples:

- Fig. 16 → EE
- Fig. 17 → GWP

These represent:

```math
\text{inventory} \xrightarrow{\text{LCA equations}} EE,\;GWP
```

They are **absolute environmental burdens**.

---

### Type D — Integrated / normalized sustainability metric

Example:

```math
SI= \frac{GWP+0.050EE}{f'_{c28d}}
```

Fig. 18 therefore represents:

```math
\boxed{ \text{environmental burden per mechanical performance} }
```

It is conceptually different from Fig. 16 or Fig. 17.

---

### Type E — Integrated economic-performance metric

```math
EI= \frac{Cost}{f'_{c28d}}
```

Fig. 19 therefore represents:

```math
\boxed{ \text{economic burden per mechanical performance} }
```

Again, not simply “cost.”

---

### Type F — Sensitivity/robustness evidence

Example from NUS-172:

```math
\text{grinding energy assumption} \rightarrow EE/GWP\text{ recalculation}
```

This tests:

> Does the sustainability conclusion remain stable when an uncertain input changes?

That is **robustness evidence**, not another outcome category.

---

# 5. A very important concept: numerator–denominator interpretation

For SI and EI figures, never report only that the index changed.

You must ask **why**.

For NUS-15:

```math
SI= \frac{GWP+0.050EE}{f'_{c28d}}
```

So a reduction in SI can come from:

1. lower GWP;
2. lower EE;
3. higher strength;
4. combinations of these.

Likewise:

```math
EI= \frac{Cost}{f'_{c28d}}
```

EI can improve because:

- cost falls,
- strength rises,
- or both.

This decomposition is critical.

A strong interpretation says:

> “The lower SI at 10% FNS reflects the combined effect of reduced environmental burden and maintenance of 28-day mechanical performance, rather than environmental reduction alone.”

That is much stronger scientifically than:

> “10% FNS has the lowest SI.”

---

# 6. Baseline logic

Every quantitative interpretation needs a reference.

For these papers, typically:

```math
\boxed{ \text{Control} = 0\%\text{ replacement} }
```

Then distinguish:

### Absolute result

> GWP = 335.35 kg CO₂-eq/m³.

from:

### Comparative result

> GWP decreased from 488.55 to 335.35 kg CO₂-eq/m³ relative to the control.

from:

### Interpretation

> Higher FNS substitution therefore reduced the cradle-to-gate GWP within the evaluated alternatives.

These are three different statements.

---

# 7. Trade-off logic

This is especially important in sustainable engineering.

The best option for one metric may not be best overall:

```math
\boxed{ \arg\min EE \neq \arg\min SI }
```

and:

```math
\boxed{ \arg\min GWP \neq \arg\max f'_c }
```

Therefore we need to detect:

- environmental–mechanical trade-off;
- environmental–economic trade-off;
- performance–replacement trade-off;
- absolute-impact vs normalized-performance trade-off.

For NUS-15, this is precisely why Figs. 16–19 should be interpreted together.

---

# 8. Be careful with the word “correlation”

Several NUS-15 figures are titled **“Correlation between …”**.

That does not automatically mean we should report:

> “There is a statistically significant correlation.”

Unless the authors give:

```math
r,\quad R^2,\quad p
```

or another statistical analysis.

If the figure simply plots `%FNS` against EE, say:

> “Fig. 16 shows the relationship/trend between FNS replacement and embodied energy.”

Not:

> “FNS is strongly negatively correlated with EE”

unless the paper quantitatively establishes that statement.

This prevents overinterpretation.

---

# 9. Mechanism versus observation

Keep these separate.

### Observation

> “GWP decreases as FNS replacement increases.”

### Possible engineering/material explanation

> “This reduction is associated with partial replacement of Portland cement and the corresponding change in constituent environmental burdens.”

The first comes directly from results.

The second requires evidence from the paper's methodology/discussion.

Never turn:

```math
\text{association}
```

into:

```math
\text{causal mechanism}
```

without author evidence.

---

# 10. Recommended writing formula for every figure

Use this five-sentence architecture.

### Sentence 1 — Identify

> **Fig. X reports [metric] as a function of [variable] across [alternatives].**

### Sentence 2 — Quantify

> **Relative to [baseline], [alternative] changes [metric] from** **`A`** **to** **`B`****, corresponding to [Δ/%Δ], where reported/calculable.**

### Sentence 3 — Engineering interpretation

> **Engineering-wise, this indicates [performance preservation/improvement/degradation/trade-off].**

### Sentence 4 — Sustainability transformation

> **Within the sustainability assessment, this figure functions as [input/direct environmental output/engineering input/normalized sustainability output/etc.].**

### Sentence 5 — Meaning

> **Therefore, the figure supports the conclusion that [evidence-bounded conclusion].**

This is an excellent standard for the full 37-paper corpus.

---

# 11. Adaptation to each NUS-15 visual

## Table 5 — Inventory coefficients

### Concept

**Sustainability input inventory**

### Quantitative logic

Identify:

```math
EE_c,\quad GWP_c
```

for every constituent.

### Engineering logic

The mixture proportions determine how much of each constituent is consumed.

### Sustainability logic

```math
m_i\times EE_{c,i}\rightarrow EE
```

```math
m_i\times GWP_{c,i}\rightarrow GWP
```

### Best formulation

> “Table 5 provides the embodied-energy and carbon/GWP coefficients required to translate the mortar material inventory into environmental burdens. Its role is therefore upstream of the sustainability outcomes: the coefficients are transformation inputs rather than sustainability results themselves.”

---

# 12. Fig. 10 — Compressive strength

### Concept

**Engineering output → sustainability input**

### Quantitative focus

Compare:

```math
f'_{c28d,\;control}
```

versus each FNS mixture.

Known important comparison:

```math
28.27\;MPa \quad\text{vs}\quad 28.07\;MPa
```

for control and 10% FNS.

### Engineering logic

Ask:

- Is strength retained?
- Is there an optimum?
- At what substitution does deterioration become material?

### Sustainability logic

```math
f'_{c28d} \rightarrow SI,\;EI
```

### Best wording

> “Fig. 10 is not merely a mechanical-performance result. The 28-day compressive strength extracted from this figure becomes an explicit denominator in SI Eq. (7) and EI Eq. (8), creating the engineering-to-sustainability coupling used by the paper.”

That is a very important statement.

---

# 13. Fig. 16 — EE versus FNS

### Concept

**Absolute environmental burden**

### Quantitative logic

Determine:

```math
EE_0,\quad EE_i,\quad \Delta EE,\quad \%\Delta EE
```

and whether the reduction is monotonic.

### Engineering logic

EE itself is not mechanical performance.

Its engineering relevance comes from the material substitution and processing requirements.

### Sustainability logic

```math
\text{material inventory + EE coefficients} \rightarrow EE
```

### Reporting wording

> “Fig. 16 reports the embodied-energy consequence of changing FNS replacement. It represents a direct cradle-to-gate environmental output of the assessment and should therefore be interpreted as absolute energy burden, before normalization by mechanical performance.”

The phrase **before normalization** is useful.

---

# 14. Fig. 17 — GWP versus FNS

### Concept

**Absolute climate burden**

### Quantitative logic

Identify:

```math
GWP_{control}
```

and each substitution value.

Known examples include:

```math
488.55 \rightarrow 444.78 \rightarrow 335.35 \;kgCO_2eq/m^3
```

for selected alternatives.

### Sustainability logic

```math
m_i\times GWP_{c,i} \rightarrow GWP
```

### Best wording

> “Fig. 17 represents the climate-impact component of the sustainability assessment. The plotted GWP values quantify absolute cradle-to-gate greenhouse-gas burden for each FNS alternative and subsequently enter the numerator of SI Eq. (7).”

That last phrase connects the figure directly to the transformation.

---

# 15. Fig. 18 — SI versus FNS

This is probably the **most important sustainability figure** in NUS-15.

### Concept

```math
\boxed{\text{Environmental-performance efficiency}}
```

### Mathematical logic

```math
SI= \frac{GWP+0.050EE}{f'_{c28d}}
```

### Quantitative questions

We need to identify:

- control SI;
- minimum SI;
- FNS level producing the minimum;
- relative improvement;
- whether higher FNS causes SI to increase again.

Known:

```math
SI_{control}=27.71
```

```math
SI_{10\%}=25.48
```

### Interpretation

Do not say only:

> “10% has the minimum SI.”

Say:

> “Fig. 18 integrates environmental burden and engineering performance. Although increasing FNS can continue lowering absolute EE/GWP, the SI optimum occurs at the replacement level that provides the strongest balance between environmental burden and 28-day compressive strength.”

This is much deeper.

---

# 16. Fig. 19 — EI versus FNS

### Concept

```math
\boxed{\text{Economic-performance efficiency}}
```

### Mathematical logic

```math
EI= \frac{\text{Total cost}}{f'_{c28d}}
```

### Quantitative questions

Determine:

- total cost trend;
- EI control;
- minimum EI;
- replacement corresponding to minimum;
- strength contribution to that optimum.

Known minimum:

```math
EI\approx3.46\;\$/m^3/MPa
```

at 10% FNS.

### Best wording

> “Fig. 19 converts economic cost into a performance-normalized indicator by dividing the cost of 1 m³ mortar by 28-day compressive strength. The figure therefore identifies economic efficiency per unit of mechanical performance rather than the cheapest mixture alone.”

Again, this distinction is critical.

---

# 17. Final figure-reporting vocabulary

Use terms deliberately.

### For input figures/tables

- provides
- supplies
- defines
- parameterizes
- serves as an input to
- feeds the calculation

### For engineering results

- measures
- demonstrates
- reports
- maintains
- increases
- decreases
- exhibits an optimum
- preserves performance

### For sustainability transformations

- converts
- aggregates
- combines
- normalizes
- weights
- calculates
- propagates
- translates

### For outcomes

- yields
- produces
- results in
- reports
- indicates
- identifies

### For interpretation

- suggests
- indicates
- demonstrates within the evaluated alternatives
- supports
- reveals a trade-off
- distinguishes
- shows that the optimum depends on

Avoid unsupported words such as:

- proves
- causes
- guarantees
- universally optimal
- sustainable overall

unless the study truly establishes them.

---

# 18. Our protocol when we now inspect each figure

For each figure, we should produce one standardized evidence card:

### **Figure X — [exact author title]**

**1. Figure role**
Input / engineering output / transformation / sustainability outcome / sensitivity / decision integration.

**2. Variables and units**
`x=` ...
`y=` ...
Baseline = ...

**3. Quantitative evidence**
Control = ...
Alternative(s) = ...
Maximum/minimum = ...
Absolute difference = ...
Relative difference = ...

**4. Trend/form**
Monotonic / nonlinear / optimum / threshold / plateau / etc.

**5. Engineering interpretation**
What engineering phenomenon or performance change does it represent?

**6. Sustainability transformation role**

```math
\text{input} \rightarrow \text{transformation} \rightarrow \text{output}
```

**7. Sustainability interpretation**
Environmental / economic / performance-normalized / integrated / robustness.

**8. Trade-off or coupling**
What other variable must be considered before declaring an optimum?

**9. Evidence boundary**
What does the figure **not** prove?

**10. Final report sentence**
One publication-ready interpretation.

That is the framework I recommend using **figure by figure**. For NUS-15, the most logical deep-reading order is **Table 5 → Fig. 16 → Fig. 17 → Fig. 10 → Fig. 18 → Fig. 19**, because that follows the actual transformation from inputs to absolute impacts to engineering normalization to final indices.