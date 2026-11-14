# Paper 7 — Beyond Spread: revision notes (figures pass)

**Scope of this pass:** figures only. No manuscript text, captions or numbers were changed.
Both `manuscript/main.tex` and `manuscript/supplement.tex` compile with the CVPR 2027 author kit
(`cvpr.sty`, `ieeenat_fullname.bst` are byte-identical to the kit).

## Source of truth
The two uploaded zips disagreed: the `figures/` folder in the older zip did not match the figures
shown in the latest compiled draft (e.g. Fig. 2 had 4 panels in the file, 2 in the PDF), and three
figure files were missing (`pipeline_overview`, `mnist_full_balance`, `initializer_examples`).
All 32 figures were therefore re-extracted from the latest compiled `main.pdf` / `supplement.pdf`
(`scripts_tmp`-style extraction of the embedded PDFs). The draft versions of the redrawn figures are
kept in `figures/draft_originals/`.

## Redrawn main-paper figures (same file names, so `\includegraphics` is untouched)
| Fig. | File | What changed |
|---|---|---|
| 1 | `pipeline_overview.pdf` | Rebuilt as a fully vector schematic (was PowerPoint, Aptos/Roboto sans-serif). Times lettering. Panels (A)/(B)/(C) as in the caption. Panel B point clouds are simulated with the paper's own rules (K-means regions fit on reference only; trace-ratio spread; calibrated support threshold). Criterion written as q_j⁺/p_j⁻ < ρ = 0.5 to match the caption. Panel C now shows the teacher/data decomposition from Sec. 3 and the three intervention types with their matched-budget controls. |
| 2 | `overview.pdf` | Consistent colour roles, capped 95% intervals, values printed beside each estimate, repair row highlighted, effect sizes aligned with the panel titles. |
| 3 | `support_power_main.pdf` | Mass levels now use an ordered blue ramp (light = rare) instead of four unrelated hues; exact-binomial intervals capped; curves labelled where they cross 60%. |
| 4 | `initialization_repair.pdf` | (b) rows no longer crowd each other; open markers distinguish trailing DDIM and full-moment variants; values printed. |
| 5 | `numerical_repair.pdf` | Tick labels no longer collide between panels; teacher-equality line in pixel spread. |
| 6 | `edm_solver_audit.pdf` | Calls on a log axis (3 and 7 were cramped); Heun uses the "alternative solver" colour. |
| 7 | `mnist_full_balance.pdf` | Connectors show each digit's change; reject event labelled "Reject"; (b) has a seed legend and seed means. |
| 8 | `t2i_representation_reference.pdf` | Model families by colour + marker shape; open markers kept for the alternate teacher (LCM4/1, DMD2/1.75) as the caption states. |

**Colour roles (all figures):** gray = control/baseline, blue = the repair the paper advocates,
orange = contrasting intervention, aqua = alternative solver/model. Blue/orange/aqua is the trio
that passes an all-pairs colour-blind check; marker shape is always a second encoding.

**Fonts:** `pdffonts` on every redrawn figure lists only TeX Gyre Termes (Times clone), regular/bold/italic.

## Where the plotted numbers come from
`scripts/data.py` holds every plotted value with its source. Many per-arm intervals were not printed
in the paper, so they were **recovered from the vector geometry of the draft figures**
(`scripts/recover/recover_main.py`). `scripts/recover/check_recovered.py` compares the recovered
values with every number that *is* printed in the text/tables: **35/35 agree** (to the printed precision).
Please replace the `[recovered]` values with the analysis output when convenient.

## Rebuild
```
cd scripts
python3 fig_results.py     # Figs. 2-8
python3 fig_pipeline.py    # Fig. 1
python3 -I recover/check_recovered.py
cd ../manuscript && latexmk -pdf main.tex && latexmk -pdf supplement.tex
```

## BioRender
The BioRender generation for Fig. 1 was refused: the account has 0 AI credits (5 needed).
Fig. 1 is complete without it. After a top-up, BioRender art can replace the stylised thumbnail
tiles and the network glyph in panel A (`make_tiles` / `network` in `fig_pipeline.py`), with all
lettering still typeset in Times.

## Open items for the group
1. **Page limit:** the body ends on page 9 (Sec. 5 spills ~1/6 column). This was already true of the
   uploaded draft; the redrawn figures take the same space. Needs a text cut (not done: text frozen).
2. Confirm the `[recovered]` intervals against the analysis output.
3. Supplement figures (24) are unchanged; they already use a Times clone but the older colour scheme.
   They can be restyled the same way in a second pass.
4. BioRender credits (see above).

---

# Text pass (skill checklist applied), 2026-11-13

All numbers retained: a script compared every number token in the old body with the new body.
The only numbers no longer present are three abstract roundings (20.6, 28.8, 42), whose
full-precision values remain in the body (coverage 0.206 → 0.288; 41.6%).

| Checklist item | Change |
|---|---|
| Abstract | Plain language, one message, two headline numbers (32%, 59%); no undefined terms. |
| Introduction | Problem → limitation → idea (cites Fig. 1 first, fixing figure order) → evidence → toy example (bound 0.133 re-computed: 0.1328) → "First/Second/Third" contributions → organization paragraph. |
| Related work | Already two connected paragraphs; unchanged. |
| Method (Sec. 3) | Six subsections: setting; representation & regions with **Lemma 1** (total covariance, proof); mass certificate with **Proposition 1** (simultaneous ratio intervals, proof) and **Corollary 1** (sample-size bound, proof); conditional spread; reference support; diagnosis → intervention with **Proposition 2** (Gaussian initialization/integration factorization, derivation in Supp. D–F, short proof of the refinement inequality). Covariance-start theory moved here from the CIFAR results. All constants collected in 3.7 Implementation details. Symbols defined before use. |
| Experiments (Sec. 4) | New: 4.1 Datasets, 4.2 Experimental settings, 4.3 Baselines (with a methodological reason why precision/recall/Vendi are controls, not alternatives), 4.4 Evaluation metrics (defines the Δ [ℓ, u] notation and every interval type). |
| Results (Sec. 5) | Leads with the two repairs (Tab. 1), then CIFAR, intervention location, MNIST, crossed probes, text-to-image, validation (moved out of the method), sampler choice. Figures and table are cited in numerical order. |
| Conclusion | "Discussion and conclusion" merged into one formal Conclusion that answers the intro's three questions, then limitations and future directions. |
| Tables | Tab. 1 one column, results only, short caption; definitions moved to text. |
| Captions | All shortened to "what is shown + takeaway"; interval types and settings moved to Sec. 4.4/5. No bold. |
| Names | "covariance start" / "standard start", "ordinary continuation" / "continued targeting" defined in text and used in figure labels. |
| LLM statement | Updated: adds Anthropic Claude for this revision; BioRender limited to an earlier Fig. 1. Check against the CVPR 2027 policy. |

Removed files (content moved): `cifar_experiments`, `mnist_experiments`, `t2i_experiments`,
`support_experiments`, `repair_summary`, `policy_summary`, `theory`. New: `experiments.tex`, `results.tex`.

**Page count:** body now ends on page 10 (was 9; CVPR limit 8). Expanded working draft; compress on request.
