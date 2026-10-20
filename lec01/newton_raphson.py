from __future__ import annotations

from collections.abc import Callable
from math import isfinite


def solve_newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-5,
    max_iter: int = 100,
    *,
    history: list[float] | None = None,
) -> float:
    """Approximate a root using x_next = x - f(x) / df(x).

    Stop at an exact zero or when abs(x_next - x) < tol. This step
    tolerance is not a guaranteed bound on the error in the root.
    If history is supplied, append x0 and every subsequent iterate to it.
    With an initially empty history, len(history) - 1 counts the updates.

    Raise ValueError for invalid inputs, a zero derivative away from a
    root, non-finite values, or exhaustion of the iteration limit.
    """
    if not isfinite(tol) or tol <= 0:
        raise ValueError("tol must be finite and positive.")
    if not isinstance(max_iter, int) or max_iter < 1:
        raise ValueError("max_iter must be a positive integer.")
    if not isfinite(x0):
        raise ValueError("The initial guess must be finite.")

    x = x0
    fx = f(x)
    if not isfinite(fx):
        raise ValueError("The function value must be finite.")
    if history is not None:
        history.append(x)

    for _ in range(max_iter):
        if fx == 0:
            return x
        dfx = df(x)
        if not isfinite(dfx):
            raise ValueError("The derivative must be finite.")
        if dfx == 0:
            raise ValueError("Derivative is zero away from a root.")

        x_next = x - fx / dfx
        if not isfinite(x_next):
            raise ValueError("The next iterate must be finite.")
        f_next = f(x_next)
        if not isfinite(f_next):
            raise ValueError("The function value must be finite.")
        if history is not None:
            history.append(x_next)
        if f_next == 0 or abs(x_next - x) < tol:
            return x_next
        x, fx = x_next, f_next

    raise ValueError("Maximum number of iterations exceeded without convergence.")
