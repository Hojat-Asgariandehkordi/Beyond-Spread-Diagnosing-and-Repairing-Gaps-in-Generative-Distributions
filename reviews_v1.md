# Review: "Beyond Spread: Diagnosing and Repairing Gaps in Generative Distributions"

## Scores
| Criterion | Score |
|---|---|
| Originality and significance | 5 |
| Technical soundness | 6 |
| Strength of evidence | 5 |
| Clarity | 4 |
| Presentation | 6 |

**Overall: 5/10 (borderline). Confidence: medium.**

**Contribution (one sentence):** A pre-declared audit with fixed reference and fixed K-means regions. It certifies regional mass depletion or excess with exact simultaneous Clopper-Pearson ratio bounds, measures within-region spread and calibrated support departure separately, and uses each finding to motivate one controlled intervention: a covariance-matched start for two-call CIFAR-10 DDIM and ordinary continuation for withheld-digit MNIST.

## Most consequential objections
1. **The repairs are near-trivial, and the audit added little to finding them (Sec. 5.1–5.2, 5.8; Supp. Table 9).** The CIFAR deficit sits in a leading two-call grid that starts at t0=500 (L329) with a standard-normal start. That is a known schedule flaw [18], and Eq. (8) is the obvious fix. The covariance-only variant was picked from a paired-seed ablation of KID (L479–482, Supp. L702–705), not from the audit. The frozen audit chose full moments. In Supp. Table 9 the audit selector scores KID 79.0±1.9, against 78.4±1.8 for both Vendi and teacher-Fréchet. "Matches the strongest selectors" (L715) is generous. On MNIST, retraining on the full data repairs a deficit the authors created by withholding the digit. *Fix:* show a case where the audit finds a deficit that KID, NDB, or Vendi miss, and where acting on it beats baseline-guided choices.
2. **Practical significance is limited (Fig. 3b, Table 1).** The headline improvement is at KID 0.126, a quality level far from any useful two-step generator. It uses one DDPM checkpoint, and the uncertainty covers only panels from that checkpoint (L452–456). *Fix:* add a second pretrained DDPM/EDM model and a distilled one-to-two-step baseline (e.g., consistency or DMD) for context.
3. **The abstract overclaims the text-to-image results (Abstract L017–020; Sec. 5.6, 5.8).** Sec. 5.6 says the reversal analysis was specified after outcomes were available and that its intervals are descriptive. Sec. 5.8 shows no resolved benefit from audit-guided selection. *Fix:* call this part exploratory in the abstract and introduction, or pre-register it and replicate on held-out prompts.
4. **One supporting contrast includes zero but is read as support (Sec. 5.5, L624–629).** The class-mass difference −0.00331 [−0.00683, 0.00020] uses n=3 seeds and spans zero, yet it is presented as showing which repair objective improves. *Fix:* state that it is unresolved, or add seeds.
5. **Clarity: the paper is too dense to follow (Secs. 3–5).** Many undefined or late-defined terms appear ("resolved probes", "fidelity gates", "eligible", "leading/trailing", "frozen v1"). Dense numbers and supplement pointers hide the argument. Fig. 3a's y-axis ("Variance ratio" of what?) is not defined. *Fix:* add a notation table, define each pipeline stage once, move secondary numbers into tables, and state one claim per paragraph.

## Strengths
- The statistics are clean and checkable. Prop. 1, Cor. 1, and the conformal support gate are correct. Cor. 1 states sample requirements in advance, and Fig. 8 matches it (a 1%-mass region at ε=0.025/40 needs about 5,000 draws).
- Prop. 2 cleanly separates initialization from integration error. The DDIM multiplier and telescoping product check out, and the predictions match the observed regime.
- The controls are unusually honest. All arms are retained, there is an untouched CIFAR-10.1 re-evaluation, a negative control (output-covariance restoration hurts coverage, Fig. 4), and a demonstration that NDB and the certificate answer different questions at ratio = ρ (L690–698).

## Factual / numerical / mathematical checks
- **Verified:** the 0.133 bound and n≥34 (L080–084), 32.0%, 58.7%, 89.1%, 32.7%, 41.6%, 0.523+0.396=0.919, and the 525-region count.
- **Coincident values (not errors):** 24.7% (L502, L538) and KID 0.00250 (L533–534) each appear twice for different arms (Supp. Tables 12–13). Label them to avoid confusion.
- **Missing citations:** ImageReward (L436) has no citation. Teacher-feature Fréchet selection (L420) does not cite FID.
- **Ambiguous notation:** Sec. 3.4 calls z "unwhitened," but L160 says feature coordinates are scaled by their standard deviation. State which coordinates enter Eq. (4).
- **Lemma 1** is the standard law of total covariance; cite it as such.
