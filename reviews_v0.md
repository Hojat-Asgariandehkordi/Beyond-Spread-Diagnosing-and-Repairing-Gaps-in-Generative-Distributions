# Review: "Beyond Spread: Diagnosing and Repairing Gaps in Generative Distributions"

## Scores
1. Originality and significance: 5/10
2. Technical soundness: 6/10
3. Strength of evidence: 4/10
4. Clarity: 4/10
5. Presentation: 6/10

**Overall: 4/10 (borderline reject). Confidence: medium.**

## Contribution
A fixed-reference audit certifies regional mass loss with exact binomial ratio bounds and separately measures conditional spread and support. Its diagnoses motivate two matched-budget repairs: covariance-matched starting noise (2-call CIFAR-10) and ordinary-data continuation (MNIST).

## Most consequential objections
1. **The repairs work in a degenerate regime and add little (Sec. 5.2, Table 1, Fig. 3).** After the repair, two-call KID is still 0.126, 91.29% of outputs sit in one region holding 35.35% of the reference, and 9/10 regions stay depleted. Fig. 3a predicts the gain is gone by 8 calls (ratio 0.968), and the main paper reports no 4/8-call covariance-start result. The MNIST "repair" undoes an overshoot the authors caused by doubling the digit-3 weight. *Fix:* report covariance start at 4/8 calls and on EDM, and compare against the cited noise-prior methods [8,10,18,30,40] and a distilled few-step model.
2. **The uncertainty does not support the claims (Sec. 4.4, 5.5).** CIFAR intervals come from five panels of one checkpoint under a panel-effect approximation, which leaves out training variability. MNIST uses three seeds (t with df = 2). The crossed-probe difference, −0.00331 [−0.00683, 0.00020], includes zero. The spread intervals fall outside the exact guarantee (l. 306–308). *Fix:* add a second checkpoint (the paper itself names this, l. 708) and more seeds, and mark which claims are exact.
3. **No sensitivity analyses for the representation or partition (Sec. 3.2, 3.7).** Every decision depends on φ, k = 32, K = 10, ρ = 0.5 and τ, and none of these is varied in the main paper. *Fix:* report how decisions change across K, representations and ρ.
4. **The text-to-image analysis is post hoc and overstated (Sec. 5.6, Fig. 7, l. 689–691).** The decomposition was "specified after access to these outcomes" (l. 596), and the Fig. 7 intervals are descriptive. The conclusion says the matched teacher "reversed" DMD2's direction, but 0.901 [0.873, 0.929] is unresolved at the paper's own 0.9 margin. In Sec. 5.8 the audit's selection rule is no better than Vendi or Fréchet selection (KID 0.0790 vs 0.0784). *Fix:* call these results exploratory, use margin-based wording, and confirm on new prompts.
5. **The paper is hard to follow without the supplement (Sec. 4.2, 5.3–5.8).** Terms such as "22-arm study", "six-arm confirmation", "resolved probes" and "leading/trailing grids" are not defined in the main paper, and results come as dense strings of numbers. The NDB comparison at a true ratio of exactly ρ (l. 646–649) tests a different null. *Fix:* add a protocol table and one summary table per setting, and present NDB as complementary.

## Strengths
- The theory is correct and simple. Lemma 1, Prop. 1, Cor. 1 and Prop. 2 check out, and the toy example reproduces (p⁻ = 0.3726, q⁺ = 0.0495, ratio 0.133). Fig. 8 behaves as Cor. 1 predicts.
- The protocol is careful: fit, calibration and outcome pools are disjoint, comparisons are matched on budget with paired seeds, and there is an external CIFAR-10.1 check (32.7% KID reduction).
- The limitations section (l. 702–714) is candid, and the paper keeps mass change separate from fidelity.

## Errors found
- **Fig. 2 caption** says "95% intervals". Sec. 4.4 and Supp. H.2 give 97.5% for MNIST.
- **l. 543–544:** a fall from 0.1461 to 0.0854 is a 41.5% reduction, not 41.6%.
- **Abstract** says "59%", while l. 54 and l. 523 say 58.7%. Use one rounding.
- **Supp. Table 12:** the "MAD" and "Acc." column values match the F98 rates in Table 13 (for example, Euler 3 is 0.0137 in both). This looks like a column or label mix-up.
- The other numbers I checked are internally consistent: 32.0% KID, 58.7% and 89.1% MNIST reductions, 0.523 + 0.396 = 0.919, 165 evaluations, 1.6M calls.
