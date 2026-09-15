from collections.abc import Callable

def solve_newton_raphson(
        f: Callable[[float], float],
        df: Callable[[float], float],
        x0: float,
        tol: float = 1e-5,
        max_iter: int = 100
    ):
    """
    Solve f(x) = 0 using the Newton-Raphson method.
    
    Parameters:
    f : function
        The function for which we want to find the root.
    df : function
        The derivative of the function f 
    x0 : float
        Initial guess for the root.
    tol : float
        Tolerance for convergence. The iteration stops when the change is less than tol.
    max_iter : int
        Maximum number of iterations to perform. 
    
    Returns:
    float
        The approximate root of the function f.
    """