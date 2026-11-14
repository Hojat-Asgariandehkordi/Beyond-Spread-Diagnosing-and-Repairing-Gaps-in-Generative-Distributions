# Review: "Beyond Spread: Diagnosing and Repairing Gaps in Generative Distributions"

## Scores
| Criterion | Score |
|---|---|
| Originality and significance | 6 |
| Technical soundness | 7 |
| Strength of evidence | 5 |
| Clarity | 4 |
| Presentation | 6 |

**Overall: 5/10 (borderline). Confidence: medium.**

## Contribution (one sentence)
The paper proposes a fixed-reference audit that certifies regional mass loss with exact binomial bounds, measures within-region spread separately, and checks reference support. It then uses each diagnosis to motivate one matched-budget intervention, illustrated by a covariance-matched starting noise for two-call CIFAR-10 DDIM and by ordinary-data continuation for a withheld MNIST digit.

## Most consequential objections
1. **The headline repair is narrow and was found by post-hoc ablation (Sec. 5.2, Table 1, Supp. F.3 l.701-706).** The frozen selector chose full-moment initialization. The covariance-only variant came from a later ablation and was then confirmed on fresh samples. The result rests on one checkpoint. After the repair, 91.29% of outputs still fall in one region that holds 35.35% of the reference mass, and 9/10 regions stay depleted. KID 0.126 is still far worse than four-call UniPC (0.069). The method is close to data-dependent priors [8] and covariance-aware sampling [33]. The cost of the teacher samples used to estimate Ĉ is not counted. *Fix:* run the covariance start on the EDM checkpoint you already use. Report the teacher-sampling cost of Ĉ. Compare against a distilled two-step generator.
2. **The paper does not show that the diagnosis adds decision value (Sec. 5.4-5.5, 5.8).** The audit-guided CIFAR choice matches KID-based selectors to within 0.0006. The MNIST "repair" fixes an overshoot that the authors created by doubling the training weight (0.1618 mass). Measured against the resolved sampler alone, the extra benefit is unresolved (−0.00331 [−0.00683, 0.00020], l.649-654). *Fix:* include at least one case where the audit's decision differs from what spread, KID, or NDB would choose, and where that decision is better on fresh samples.
3. **The regions may capture blur rather than semantic content (Sec. 3.2, 3.7, 5.2).** The regions are K=10 K-means cells in teacher pixel-PCA space for the CIFAR repair. That 97.3% of two-call outputs fall in a single cell suggests the cell captures low-energy, blurry images. If so, "regional depletion" partly restates variance contraction. The robustness check (Sec. 5.7) varies only DINO dimensions and K. *Fix:* report the semantic (classifier) audit before and after the covariance start, and show exemplars from the dominant cell.
4. **Inferential scope is overstated (Abstract, Sec. 5.6 l.658-661, Sec. 4.4).** The authors call the text-to-image reversal analysis exploratory, specified after the outcomes, and descriptive. Yet the abstract says the audit "explains why". The CIFAR intervals cover five panels from one checkpoint only. The approximate spread intervals give 4/200 false expansion flags. Table 7's Bonferroni family counts the DPM++2M and UniPC contrasts separately, although their outputs are identical. *Fix:* soften the abstract, or run a prespecified confirmation on fresh prompts. Deduplicate the contrast family.
5. **The paper is hard to follow (Sec. 4-5 throughout).** There is dense private vocabulary (arm, panel, probe, resolved probe, gate, frozen, unresolved). Four overlapping CIFAR studies are mixed together (the 22-arm original, the paired-seed ablation, the six-arm confirmation, and the external reference). Most numbers appear only in prose. The audit's core output, the per-region certificates, is never tabulated in the main paper. *Fix:* add a main-text table of certificates and spread flags per arm, a study-flow diagram, and a short glossary.

## Strengths
- The certificates are correct and their resolution can be computed in advance. I reproduced the toy bound (0.133 at n=100, α=0.025) and the threshold n=34 (ratio bound 0.488). The analytic detection rate for a 1% region at n=2,000 is 3.4%, which matches the 3.25% in Fig. 8.
- Proposition 2 is a correct, clean derivation (DDIM step = √(v_s/v_t)·cos∠). It separates initialization from integration error and correctly predicts the variance ratios at 2, 4 and 8 calls.
- Reporting is unusually transparent: every arm is retained, including unfavorable ones (CAS, output Bures). There is an untouched external reference (CIFAR-10.1, 32.7%), and the limitations are stated honestly.

## Factual / numerical / mathematical issues
- I checked Prop. 1, Cor. 1, Lemma 1, and Eqs. (7)-(8) and found no errors in them.
- Table 7 (Supp.): the DPM++2M and UniPC rows are identical, so the "five prespecified contrasts" (Sec. 4.4) are effectively four.
- Sec. 4.4 says the family has five contrasts, while Sec. 5.2/F.4 says four. These are different families, and the text should say so.
- Full-moment KID appears as 0.1405 (Fig. 3b) and as 0.1413 (Sec. 5.2). These come from different panel sets, which should be stated.
- Sec. 5.4: total variation going from 0.1461 to 0.0854 is a 41.5% reduction, but the paper reports 41.6%. This is probably rounding of the per-seed means.
- The introduction's toy example does not state that α_occ=0.025; the reader can only infer it from "97.5%".
- The abstract calls KID a "distance to real images". KID is an MMD estimate, so "discrepancy" would be more accurate.
