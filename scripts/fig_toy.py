"""Fig. 2: the toy example from the introduction, computed (not typed).

(a) Reference P: mass 1/4, 1/2, 1/4 at -2, 0, 2.  Candidate Q: mass 1/2 at +-sqrt(2).
    Both have mean 0 and variance 2; the fixed region [-1/2, 1/2] holds 1/2 of P and 0 of Q.
(b) Certified upper bound on q/p (Proposition 1, M = 1, alpha_occ = 0.025) when n draws per
    law give n/2 reference hits and zero candidate hits.  Depletion is certified once the bound
    falls below rho = 0.5 (Corollary 1).  At n = 100 the bound is 0.133 (quoted in Sec. 1).
Run: python3 scripts/fig_toy.py   (prints the numbers used in the text)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
from scipy.stats import beta
import style as S

S.apply()
OUT = os.path.join(os.path.dirname(__file__), "..", "figures")

ALPHA, M, RHO = 0.025, 1, 0.5
EPS = ALPHA / (4 * M)


def upper_ratio(n):
    """q+/p- with zero candidate hits and n/2 reference hits out of n."""
    k = n // 2
    q_plus = 1 - EPS ** (1 / n)
    p_minus = beta.ppf(EPS, k, n - k + 1)
    return q_plus / p_minus


def main():
    ref_x, ref_p = np.array([-2, 0, 2.0]), np.array([0.25, 0.5, 0.25])
    gen_x, gen_p = np.array([-np.sqrt(2), np.sqrt(2)]), np.array([0.5, 0.5])
    for x, p in [(ref_x, ref_p), (gen_x, gen_p)]:
        assert abs((p * x).sum()) < 1e-12 and abs((p * x ** 2).sum() - 2) < 1e-12

    ns = np.arange(10, 201, 2)
    ub = np.array([upper_ratio(n) for n in ns])
    n_min = int(ns[np.argmax(ub < RHO)])
    b100 = upper_ratio(100)
    print(f"bound at n=100: {b100:.4f}; smallest even n certifying depletion: {n_min}")

    fig, axes = plt.subplots(1, 2, figsize=(S.COL_W, 1.38), gridspec_kw=dict(width_ratios=[1.0, 1.08], wspace=0.42))
    ax = axes[0]
    ax.axvspan(-0.5, 0.5, color=S.BAND, lw=0, zorder=0)
    ax.text(0.55, 0.53, r"$A$", ha="center", va="bottom", fontsize=6.8, color=S.INK2)
    ml, sl, bl = ax.stem(ref_x - 0.07, ref_p, linefmt="-", markerfmt="o", basefmt=" ")
    plt.setp(sl, color=S.REF, lw=1.6); plt.setp(ml, color=S.REF, ms=4)
    ml, sl, bl = ax.stem(gen_x + 0.07, gen_p, linefmt="-", markerfmt="s", basefmt=" ")
    plt.setp(sl, color=S.GEN, lw=1.6); plt.setp(ml, color=S.GEN, ms=3.8)
    ax.axhline(0, color=S.MUTED, lw=0.6)
    ax.set_xlim(-2.7, 2.7); ax.set_ylim(0, 0.9)
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_xticklabels(["\N{MINUS SIGN}2", "\N{MINUS SIGN}1", "0", "1", "2"])
    ax.set_yticks([0, 0.25, 0.5])
    ax.grid(axis="x", visible=False)
    ax.set_ylabel("Probability")
    ax.set_xlabel("Feature value", labelpad=1.5)
    ax.plot([], [], "o-", color=S.REF, ms=3.5, label="Reference $P$")
    ax.plot([], [], "s-", color=S.GEN, ms=3.5, label="Candidate $Q$")
    ax.legend(loc="upper left", ncol=1, handlelength=1.2, handletextpad=0.3, fontsize=6.4,
              borderaxespad=0.1, labelspacing=0.2)
    ax.set_title("(a) Equal variance, lost region", pad=4, fontsize=7.5)

    ax = axes[1]
    ax.plot(ns, ub, color=S.INK2, lw=1.4)
    ax.axhline(RHO, color=S.ADVERSE, lw=0.9, ls="--")
    ax.text(200, RHO + 0.03, r"threshold $\rho=0.5$", ha="right", va="bottom", fontsize=6.6, color=S.INK2)
    ax.axvspan(n_min, 200, color=S.HILITE, lw=0, zorder=0)
    ax.plot([100], [b100], "o", color=S.REPAIR, ms=4.2, mec="white", mew=0.5, zorder=4)
    ax.annotate(f"{b100:.3f} at $n$ = 100", (100, b100), xytext=(6, 9), textcoords="offset points",
                fontsize=6.6, color=S.INK, ha="left")
    ax.axvline(n_min, color=S.MUTED, lw=0.6, ls=":")
    ax.text(n_min + 4, 1.12, "certified for $n\\geq$%d" % n_min, fontsize=6.6, color=S.INK2, ha="left", va="center")
    ax.set_xlim(10, 200); ax.set_ylim(0, 1.25)
    ax.xaxis.set_major_locator(FixedLocator([10, 50, 100, 150, 200]))
    ax.set_yticks([0, 0.5, 1.0])
    ax.set_xlabel("Draws per law $n$", labelpad=1.5)
    ax.set_ylabel(r"Upper bound on $q/p$")
    ax.set_title("(b) Certified depletion", pad=4, fontsize=7.5)

    fig.savefig(os.path.join(OUT, "toy_example.pdf"))
    fig.savefig(os.path.join(OUT, "png", "toy_example.png"), dpi=220)
    plt.close(fig)
    return b100, n_min


if __name__ == "__main__":
    main()
