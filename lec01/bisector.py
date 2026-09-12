from collections.abc import Callable


def solve_bisector(
    f: Callable[[float], float],
    a: float,
    b: float,
    max_iter: int = 100,
) -> float:
    """
    Find a fixed point of the function g using the fixed-point iteration method.

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
        The estimated fixed point of the function g.
    """
    for i in range(max_iter):
        c = (a + b) / 2 
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2 