def solve_newton_raphson(
    f,                       # function whose root we seek
    df,                      # derivative of f
    x0: float,               # initial guess
    tol: float = 1e-5,       # stop when |x_new - x| < tol
    max_iter: int = 100,     # safety cap on updates
) -> float:
    # Assume valid inputs and finite function values and iterates.
    x, fx = x0, f(x0)
    for i in range(max_iter):
        if fx == 0:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Zero derivative away from a root.")
        x_new = x - fx / dfx
        f_new = f(x_new)
        print(f"Iteration {i+1}: x = {x_new}, f(x) = {f_new}")
        if f_new == 0 or abs(x_new - x) < tol:
            print(f"Converged after {i+1} updates.")
            return x_new
        x, fx = x_new, f_new
    raise ValueError("Root not found within max_iter.")
