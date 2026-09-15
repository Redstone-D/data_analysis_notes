from __future__ import annotations

from collections.abc import Callable

import matplotlib.pyplot as plt


def plot_bisector_iteration(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-5,
    max_iter: int = 100,
    title: str | None = None,
) -> list[float]:
    """
    Visualize the bisection method as a bracket-collapse plot.

    Plots the bracket sequence against the iteration index: $a_n$, $b_n$
    (upper and lower envelope, dashed) and the midpoint $c_n$ (solid),
    so the reader can see the bracket squeeze onto the root.

    Returns the sequence of midpoints [c_0, c_1, ..., c_k].
    """
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    aa, bb = a, b
    a_hist = [aa]
    b_hist = [bb]
    c_hist: list[float] = []
    for _ in range(max_iter):
        c = (aa + bb) / 2
        c_hist.append(c)
        if (bb - aa) / 2 < tol:
            break
        if f(aa) * f(c) < 0:
            bb = c
        else:
            aa = c
        a_hist.append(aa)
        b_hist.append(bb)

    ns_ab = list(range(len(a_hist)))
    ns_c = list(range(len(c_hist)))
    _, ax = plt.subplots(figsize=(6, 4))
    ax.plot(ns_ab, a_hist, "s--", color="tab:green", markersize=4, label="$a_n$")
    ax.plot(ns_ab, b_hist, "s--", color="tab:orange", markersize=4, label="$b_n$")
    ax.plot(ns_c, c_hist, "-o", color="tab:blue", markersize=4, label="$c_n$")
    ax.axhline(c_hist[-1], color="tab:red", linestyle="--", linewidth=0.8,
               label=f"final $c \\approx {c_hist[-1]:.4f}$")
    ax.set_xlabel("$n$")
    ax.set_ylabel("value")
    ax.set_title(title or f"Bracket collapse from $[{a}, {b}]$")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return c_hist
