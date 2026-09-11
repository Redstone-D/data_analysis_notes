from collections.abc import Callable


def find_fixed_point(
    g: Callable[[float], float],
    x0: float,
    tol: float = 1e-5,
    max_iter: int = 100,
) -> float:
    """
    Find a fixed point of the function g using the fixed-point iteration method.

    Parameters:
    g : function
        The function for which we want to find a fixed point.
    x0 : float
        Initial guess for the fixed point.
    tol : float
        Tolerance for convergence. The iteration stops when the change is less than tol.
    max_iter : int
        Maximum number of iterations to perform.

    Returns:
    float
        The estimated fixed point of the function g.
    """
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        print(f"Iteration {i+1}: x = {x_new}, g(x) = {g(x_new)}") 
        if abs(x_new - x) < tol:
            print(f"Converged after {i+1} iterations.")
            return x_new
        x = x_new
    raise ValueError("Fixed point not found within the maximum number of iterations.") 
