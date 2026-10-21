from collections.abc import Callable
from math import isfinite


def solve_bisector(
    f: Callable[[float], float],
    a: float,
    b: float,
    max_iter: int = 100,
) -> float:
    """
    Approximate a root of a continuous function by bisection.

    Require a < b and opposite endpoint signs, unless an endpoint is
    already a root. Return an exact root immediately; otherwise return
    the final interval's midpoint after max_iter halvings.

    Parameters:
    f : function
        The function for which we want to find a root.
    a : float
        The lower bound of the interval.
    b : float
        The upper bound of the interval.
    max_iter : int
        Maximum number of iterations to perform.

    Returns:
    float
        The estimated root of f.
    """
    if not isfinite(a) or not isfinite(b) or a >= b:
        raise ValueError("Require finite endpoints with a < b.")
    if not isinstance(max_iter, int) or max_iter < 0:
        raise ValueError("max_iter must be a nonnegative integer.")
    fa, fb = f(a), f(b)
    if not isfinite(fa) or not isfinite(fb):
        raise ValueError("Function values must be finite.")
    if fa == 0:
        return a
    if fb == 0:
        return b
    if (fa < 0) == (fb < 0):
        raise ValueError("Endpoint function values must have opposite signs.")

    for _ in range(max_iter):
        c = a / 2 + b / 2
        fc = f(c)
        if not isfinite(fc):
            raise ValueError("Function values must be finite.")
        if fc == 0:
            return c
        if (fa < 0) != (fc < 0):
            b = c
        else:
            a = c
            fa = fc
    return a / 2 + b / 2
