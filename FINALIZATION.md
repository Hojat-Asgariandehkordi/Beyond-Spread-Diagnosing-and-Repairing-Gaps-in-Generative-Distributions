# FINALIZATION — Paper 7: Beyond Spread (CVPR 2027)

Mode: **expanded working draft** (target ~9–10 pages of body; CVPR limit is 8).
Working copy: branch/worktree `Final_CVPR2027_P7_v1` (from tag `baseline-v0` = commit 0110cb6).
MAX_CYCLES = 2 (hard cap). Reviews: independent agent, stable rubric `reviews/RUBRIC.md`,
frozen PDFs with digests; reviewer never sees targets, prior scores or this file.

## Working thesis (one sentence)
Fixing a reference, regions and an effect size *before* evaluation turns "diversity" from a
pooled spread number into certifiable regional statements (lost mass, within-region contraction,
off-support departure) that tell you which single intervention to test, and two such
diagnosis-guided changes repair generators at matched budgets.

## Contributions (2–4)
1. A fixed-reference audit with finite-sample regional certificates (Prop. 1, Cor. 1) that
   separates regional mass, conditional spread and support, and states resolution in advance.
2. Diagnosis-guided repairs at matched cost: covariance start (CIFAR-10, −32.0% KID, two calls)
   and ordinary continuation (MNIST, −58.7% class-mass error, 8,000 updates).
3. An explanation of diversity reversals: pooled vs within-prompt spread, and teacher choice
   (text-to-image, DMD2 1.251 → 0.901).

## Claim → source map (central claims)
| Claim | Source in paper | Underlying source |
|---|---|---|
| KID 0.1858 → 0.1264, Δ −0.05938 [−0.06138, −0.05739] | Tab. 1, Sec. 5.2 | preserved from manuscript (Supp. F.3); not re-run |
| Coverage 0.206 → 0.288 | Tab. 1 | preserved |
| CIFAR-10.1 KID −32.7% | Sec. 5.2 | preserved (Supp. F.4) |
| MNIST class-mass error −58.7% [CI] | Tab. 1, Fig. 6 | preserved (Supp. H.2) |
| TV 0.1461 → 0.0854 | Sec. 5.4, Fig. 6 | per-seed values recovered from draft figure; means match text |
| Toy bound 0.133 | Intro | **independently recomputed** (0.1328) |
| Prop. 1 / Cor. 1 | Sec. 3.3 | proofs checked (union bound; Clopper–Pearson zero-count bound) |
| Detection 3.25% → 99.9% (1% mass) | Sec. 5.7, Fig. 8 | preserved; matches Supp. table |
| DDIM4 pooled 0.919 vs within 1.306 | Sec. 5.6, Fig. 7 | preserved; decomposition 0.523+0.396=0.919 checked |

## Initial diagnosis (own reading, before baseline review)
- The argument is correct but reads as an inventory of many studies; the payoff on page 1 is
  diluted by protocol detail and qualifiers. The novelty versus NDB / precision–recall /
  Vendi is stated only implicitly.
- Fig. 2 duplicates Table 1 (same two comparisons, same numbers): one of them is wasted space,
  while the paper's central insight (equal spread, lost region, certificate) has no visual.
- The audit procedure is spread over six subsections; no single procedural summary
  (inputs → fit/calibrate/freeze → certify → intervene → test).

## Candidate interventions (cycle 1) — subjective planning estimates
priority = [P(help)·benefit − P(harm)·downside] / cost; benefit/downside 1–3, cost 1–5.

| # | Concern | Change & location | Evidence | Success criterion | P(help) | B | P(harm)·D | Cost | Pages | Priority | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Story diluted; novelty implicit; hedging | Rewrite abstract, intro (explicit comparison with NDB, PRDC, Vendi/Scendi), lead sentence of every results subsection, concise limitations | Existing results; related work | Reviewer can state contribution in 1 sentence; clarity score not lower | high (0.7) | 3 | 0.2·2 | 3 | 0 | 0.57 | **execute** |
| C2 | Central insight has no visual; Fig. 2 duplicates Tab. 1 | Replace Fig. 2 with a code-generated toy-example figure: (a) equal-variance reference/candidate with fixed region, (b) certified upper bound vs n (Cor. 1) | Toy example (recomputed), Eq. (3) | Fig. 2 numbers equal intro numbers; no duplication of Tab. 1 | med-high (0.6) | 3 | 0.2·1 | 3 | 0 | 0.53 | **execute** |
| C3 | Procedure hard to reproduce at a glance | Algorithm 1 box in Sec. 3 (audit + intervention test) | Sec. 3.1–3.7 | All steps map to equations; ≤ 0.3 page | medium (0.5) | 2 | 0.2·1 | 2 | +0.3 | 0.40 | **execute** |
| C4 | Supplement evidence hidden | Promote a compact table of the controlled-deletion validation (NDB vs certificate vs projected rules) | Supp. C | Table numbers trace to Supp. C | medium (0.4) | 2 | 0.3·1 | 3 | +0.25 | 0.17 | defer (decide after review) |
| C5 | Fig. 3(a) legend outside wastes width | Re-layout | — | — | low | 1 | 0.1·1 | 1 | 0 | — | group with QA |

## Cycle 1 goals (fixed after v0 review; ≤3)
- **G1 Story & scoping** (C1 + v0 obj. 4, 5): confident abstract/intro with explicit novelty vs NDB/PRDC/Vendi;
  define protocol terms (22-arm, six-arm, leading/trailing, resolved probes); T2I labelled exploratory with
  margin-based wording; NDB presented as answering a different null; Sec. 5.8 framed accurately; one rounding (58.7%).
  Success: reviewer no longer flags undefined terms or overstated T2I/NDB claims.
- **G2 Evidence & visuals** (C2 + v0 obj. 1, 2, 3): toy Fig. 2 replaces duplicate overview plot; promote from supplement
  (i) the 4/8-call boundary of the initialization gain as predicted by Prop. 2 and (ii) the 9-setting
  representation/partition robustness grid; state which guarantees are exact vs approximate.
  Success: obj. 1 and 3 answered from existing evidence; no number changed.
- **G3 Procedure** (C3): Algorithm 1. Success: each step maps to an equation/section.
- Rejected/deferred: protocol table (inventory; conflicts with results-only table rule; handled as prose);
  new seeds/checkpoints/noise-prior baselines (new training/sampling runs, out of budget: next research tasks).
- v0 numerical notes: 41.6% is correct from unrounded means (14.61→8.537 = 41.57%); kept. Supp. Table 12 MAD/Acc.
  columns duplicate Table 13 F98 values per reviewer: flagged for authors, not edited.

## Cycle 2 goals (final cycle; from v1 review)
- **G1 Clarity** (v1 obj. 5): one terminology paragraph (arm, panel, probe/resolved probe, eligible, gate, frozen,
  unresolved); state which coordinates enter K-means vs Eq. (4); Fig. 3a axis names the quantity; disambiguate
  coincident values (24.7%, 0.00250). Success: terms defined once before use; no ambiguity flagged.
- **G2 Accurate scoping** (v1 obj. 1, 3, 4): abstract/intro mark text-to-image as exploratory; crossed-probe
  difference stated as unresolved; selector comparison stated exactly (0.0790 vs 0.0784); provenance of the
  covariance-only form (ablation, then fresh confirmation); attribute starting-noise mismatch to prior work [lin2024flawed etc.].
  Success: no claim exceeds its interval; prior work credited.
- **G3 References/notation** (v1 checks): cite ImageReward, FID for Fréchet selection, Lemma 1 as the law of total covariance.
- Deferred (needs new runs): second pretrained/distilled checkpoint; covariance start on EDM; head-to-head with
  noise-prior methods; a case where the audit finds a deficit KID/NDB/Vendi miss and acting on it beats baseline choices.

## Action ledger
- (setup) worktree, tag baseline-v0, frozen v0 PDFs (main db6dd188…, supp f361f11b…).
- C1/G1 abstract (58.7% one rounding), intro novelty paragraph vs PRDC/Vendi/NDB, evidence paragraph (no extra cost),
  lead sentences in 5.1/5.3/5.4/5.5/5.6, T2I exploratory, NDB complementary, Sec. 5.8 framing, conclusion DMD2 wording,
  protocol terms defined in 4.2 (leading/trailing, 22 arms, six-arm, resolved probes), exact vs approximate in 4.4,
  related work de-duplicated (inherits NDB regions; adds certificate, spread, support).
- C2/G2 Fig. 2 = toy example (scripts/fig_toy.py; 0.1328 and n ≥ 34 computed); old overview plot dropped from main;
  promoted 4/8-call boundary (Supp. Tab. 6: 92.6/37.8 vs 90.3/36.3 ×1e-3) and 9-setting robustness (Supp. C).
- C3/G3 Algorithm 1 (Sec. 3, before 3.7).
- Checks: number retention vs v0 (only '59' → 58.7 changed); new numbers traced; compile clean; pages rendered.
- Frozen v1: commit c941889, main digest c6ae6e6546d44fcd.

## Review history
| Snapshot | Commit | Digest (main) | Overall | Confidence | Notes |
|---|---|---|---|---|---|
| v2 | 1e69ab5 | d522416b40bcdf90 | **5/10** (O6 S7 E5 C4 P6) | medium | **best reviewed, retained.** Remaining: covariance-only form found by ablation, one checkpoint; no case where the audit's decision beats KID/NDB-guided choice; pixel-PCA regions may track blur; dense vocabulary; no main-text certificate table |
| v1 | c941889 | c6ae6e6546d44fcd | **5/10** (O5 S6 E5 C4 P6) | medium | kept; remaining: audit's role in choosing covariance-only; practical significance (one checkpoint); abstract T2I overclaim; crossed-probe CI spans 0; density/undefined terms; missing ImageReward/FID cites; z scaling ambiguity |
| v0 | 0110cb6 | db6dd18820aa376f | **4/10** (O5 S6 E4 C4 P6) | medium | baseline; objections: degenerate 2-call regime & no 4/8-call result; thin uncertainty; no sensitivity; T2I post hoc/overstated; undefined protocol terms; NDB null differs |

## Cycle 2 ledger
- Terminology paragraph (Sec. 4 opening); K-means vs spread vs support coordinates stated (Sec. 3.2); Lemma 1 named as the
  law of total covariance; starting-noise mismatch attributed to [lin2024flawed], priors to [lee2022priorgrad];
  covariance-only provenance (audit → full moments; ablation → covariance; six-arm fresh confirmation); crossed-probe
  difference stated as unresolved; selector gap stated exactly (0.0006); EDM coincident values labelled; ImageReward and
  FID cited; Fig. 3a y-axis "Pixel-PCA variance ratio"; abstract/intro mark text-to-image as exploratory.

## Post-review corrections → v2.1 (UNSCORED; last score 5/10 is historical, attached to v2)
- Abstract: "discrepancy from real images"; text-to-image "offers an account" (was "explains why").
- Toy example states alpha_occ = 0.025. Sec. 4.4 distinguishes the five-contrast and four-contrast families.
- Full-moment KID 0.1405 vs 0.1413 attributed to different panel sets. No numbers changed.

## Outcome
Baseline 4/10 → v1 5/10 → v2 5/10 (sub-scores up: originality 5→6, soundness 6→7). Target 7.5 not reached.
The remaining obstacle is evidential, not presentational: every reviewer's top objection asks for results that need
new runs. Best next research tasks, in order of expected value:
1. Covariance start on the EDM checkpoint already in the paper (+ report teacher-sampling cost of Ĉ): tests transfer.
2. A decision case where the audit's choice differs from KID/NDB/Vendi-guided choice and wins on fresh samples.
3. Semantic (classifier) audit of the CIFAR-10 repair before/after, with exemplars of the dominant region (blur vs content).
4. More MNIST seeds (currently 3) to resolve the crossed-probe difference.
5. A distilled two-step generator as context for the CIFAR two-call numbers.
Author items: Supp. Table 7 counts identical DPM++2M/UniPC outputs as two contrasts; Supp. Table 12 MAD/Acc. columns
duplicate Table 13 values (v0 reviewer); confirm recovered figure intervals; LLM statement vs CVPR 2027 policy.

## Final QA (re-sent prompts were byte-identical; no third cycle under Part A's cap)
- No em dashes in the manuscript sources; PDF Author empty; no identifying strings (only "University of Toronto" in the CIFAR reference).
- No undefined references or citations; no overfull boxes; body ends early on p. 11 (~10.3 pages; expanded draft).
- Citations added in cycle 2 verified against primary sources: Lin et al. (WACV 2024) state that some sampler
  implementations do not start from the last timestep; PriorGrad (ICLR 2022) uses a data-statistics prior in training and sampling.
- Title reviewed and kept: it states the thesis (beyond pooled spread; diagnose and repair regional gaps).

## Author comments round (2026-11-13, after finalization; UNSCORED, last review score is historical)
- Removed Fig. 2 (toy figure); the toy example text stays in the introduction (scripts/fig_toy.py kept as the source of 0.133 and n >= 34).
- Table 1 transposed: outcomes are columns, Control / Repair / Delta [l, u] are rows, one block per study; still one column.
- Fig. 3 (now Fig. 2): panels (a) and (b) side by side in one column-width row with one shared legend.
- Fig. 8 (detection power) moved to the supplement as Supp. Fig. 1; the main text keeps its numbers and cites Supp. Fig. 1.
- Fig. 1 scaled to 0.86 of the text width.
- Effect: body now ends on p. 10 (about 9.5 pages). No numbers changed; compile clean; main figures now Fig. 1-6.

## Material unresolved items
- Per-arm intervals recovered from draft figure geometry (35/35 printed values agree): need analysis output.
- Page limit: body ~9.3 pages (expanded draft).

## Compression map (body ≈ 10.0 pages → 8)
1. Move Sec. 5.5 (crossed probes) to the supplement, keeping two sentences in 5.4 (−0.45 p).
2. Move the EDM solver paragraph and Fig. 5 to the supplement (−0.35 p).
3. Shorten Sec. 4.2 to one paragraph; protocol details already in Supp. study map (−0.3 p).
4. Move Proposition 2's statement into prose with the equation, proof sketch only (−0.2 p).
5. Merge Sec. 5.8 into the conclusion as two sentences (−0.25 p).
6. Move the CIFAR-10 semantic and frog-reference paragraphs of 5.4 to the supplement (−0.3 p).
7. Fig. 8 (power) to half height or into the supplement with one sentence (−0.2 p).
Total ≈ −2.05 pages.
