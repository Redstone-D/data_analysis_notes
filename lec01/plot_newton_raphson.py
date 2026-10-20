from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from newton_raphson import solve_newton_raphson


def plot_newton_raphson_iteration(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-5,
    max_iter: int = 100,
    xlim: tuple[float, float] | None = None,
    title: str | None = None,
    save_prefix: str | Path | None = None,
    show: bool = True,
) -> list[float]:
    """Plot Newton tangent steps and x_n against n using the solver's history.

    If save_prefix is given, save <prefix>_tangents.png and
    <prefix>_sequence.png. Return [x0, x1, ..., xk].
    """
    xs: list[float] = []
    solve_newton_raphson(f, df, x0, tol, max_iter, history=xs)
    if xlim is None:
        pad = max(0.1, 0.25 * (max(xs) - min(xs)))
        xlim = (min(xs) - pad, max(xs) + pad)

    xx = np.linspace(*xlim, 500)
    yy = [f(float(x)) for x in xx]
    heading = title or f"Newton-Raphson from $x_0={x0}$, tol={tol:g}"

    fig_tangents, ax = plt.subplots(figsize=(6, 4))
    ax.plot(xx, yy, color="tab:blue", label="$f(x)$")
    ax.axhline(0, color="black", linewidth=0.8)
    for i, (x, x_next) in enumerate(zip(xs, xs[1:])):
        fx = f(x)
        ax.plot([x, x], [0, fx], "--", color="gray", linewidth=0.8)
        ax.plot([x, x_next], [fx, 0], color="tab:orange",
                label="tangent steps" if i == 0 else None)
        ax.plot(x, fx, "o", color="tab:orange", markersize=4)
        ax.plot(x, 0, "o", color="tab:red", markersize=4)
        if i < 2:
            ax.annotate(f"$x_{{{i}}}$", (x, 0), xytext=(4, -16),
                        textcoords="offset points", fontsize=9)
    ax.plot(xs[-1], 0, "x", color="tab:red", markersize=7,
            label=f"final iterate {xs[-1]:.8f}")
    ax.set(xlabel="$x$", ylabel="$f(x)$", xlim=xlim, title=heading)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig_tangents.tight_layout()

    fig_sequence, ax = plt.subplots(figsize=(6, 4))
    ax.plot(range(len(xs)), xs, "-o", color="tab:blue",
            markersize=4, label="$x_n$")
    ax.axhline(xs[-1], color="tab:red", linestyle="--", linewidth=0.8,
               label=f"final iterate {xs[-1]:.8f}")
    ax.set_xticks(range(len(xs)))
    ax.set(xlabel="$n$", ylabel="$x_n$", title=heading)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")
    fig_sequence.tight_layout()

    if save_prefix is not None:
        fig_tangents.savefig(f"{save_prefix}_tangents.png", dpi=180,
                             bbox_inches="tight")
        fig_sequence.savefig(f"{save_prefix}_sequence.png", dpi=180,
                             bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig_tangents)
    plt.close(fig_sequence)
    return xs
