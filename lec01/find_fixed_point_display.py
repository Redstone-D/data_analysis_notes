def find_fixed_point(
    g,                       # g(x): fixed point r satisfies g(r) = r
    x0: float,               # initial guess
    tol: float = 1e-5,       # stop when |x_new - x| < tol
    max_iter: int = 100,     # safety cap on iterations
) -> float:
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        print(f"Iteration {i+1}: x = {x_new}, g(x) = {g(x_new)}")
        if abs(x_new - x) < tol:
            print(f"Converged after {i+1} iterations.")
            return x_new
        x = x_new
    raise ValueError("Fixed point not found within max_iter.")
