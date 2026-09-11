from __future__ import annotations

from collections.abc import Callable

import matplotlib.pyplot as plt
import numpy as np


def plot_fixed_point_iteration(
    g: Callable[[float], float],
    x0: float,
    tol: float = 1e-5,
    max_iter: int = 100,
    xlim: tuple[float, float] | None = None,
    title: str | None = None,
) -> list[float]:
    """
    Visualize the fixed-point iteration x_{n+1} = g(x_n) with two figures.

    Figure 1 is a cobweb diagram: y = g(x), the diagonal y = x, and the
    staircase of iterates. Fixed points sit at intersections of the curve
    and the diagonal.

    Figure 2 plots the iterate sequence x_n against the index n.
    Converging runs level out toward a horizontal asymptote (the fixed
    point); diverging or oscillating runs stay wobbly.

    Returns the sequence of iterates [x_0, x_1, ..., x_k].
    """
    xs = [x0]
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        xs.append(x_new)
        if abs(x_new - x) < tol:
            break
        x = x_new

    # Figure 1: cobweb diagram.
    if xlim is None:
        lo, hi = min(xs), max(xs)
        pad = max(0.5, 0.2 * (hi - lo))
        xlim = (lo - pad, hi + pad)

    xx = np.linspace(xlim[0], xlim[1], 400)
    yy = np.array([g(float(v)) for v in xx])

    _, ax = plt.subplots(figsize=(6, 6))
    ax.plot(xx, yy, label="$y = g(x)$", color="tab:blue")
    ax.plot(xx, xx, "k--", linewidth=0.8, label="$y = x$")

    # First step: vertical from (x0, 0) up to the curve at (x0, x1).
    ax.plot([xs[0], xs[0]], [0, xs[1]], color="tab:orange", linewidth=1)
    for i in range(len(xs) - 1):
        # Horizontal: (x_i, x_{i+1}) -> (x_{i+1}, x_{i+1}) reflects off y = x.
        ax.plot([xs[i], xs[i + 1]], [xs[i + 1], xs[i + 1]],
                color="tab:orange", linewidth=1)
        if i + 2 < len(xs):
            # Vertical: (x_{i+1}, x_{i+1}) -> (x_{i+1}, x_{i+2}) hits the curve.
            ax.plot([xs[i + 1], xs[i + 1]], [xs[i + 1], xs[i + 2]],
                    color="tab:orange", linewidth=1)

    for i, xi in enumerate(xs):
        ax.plot(xi, xi, "o", color="tab:red", markersize=4)
        ax.annotate(f"$x_{{{i}}}$", (xi, xi),
                    textcoords="offset points", xytext=(6, -10), fontsize=8)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title or f"Fixed-point iteration from $x_0 = {x0}$")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal", adjustable="box")
    plt.tight_layout()
    plt.show()

    # Figure 2: iterate sequence x_n vs. n.
    ns = list(range(len(xs)))
    _, ax = plt.subplots(figsize=(6, 4))
    ax.plot(ns, xs, "-o", color="tab:blue", markersize=4, label="$x_n$")
    ax.axhline(xs[-1], color="tab:red", linestyle="--", linewidth=0.8,
               label=f"final $x_n \\approx {xs[-1]:.4f}$")
    ax.set_xlabel("$n$")
    ax.set_ylabel("$x_n$")
    ax.set_title(title or f"Iterates from $x_0 = {x0}$")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return xs
