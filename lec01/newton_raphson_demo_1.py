from math import cos, sin

from newton_raphson import solve_newton_raphson


# Solve x**3 = sin(x), targeting the positive root from x0 = 1.
def f(x):
    return x**3 - sin(x)


def df(x):
    return 3 * x**2 - cos(x)


for tol in (5e-2, 1e-8):
    history = []
    root = solve_newton_raphson(f, df, x0=1.0, tol=tol, history=history)
    print(f"tol={tol:.0e}, x0=1, root={root:.12f}, "
          f"iterations={len(history) - 1}, residual={abs(f(root)):.3e}")
    print("iterates:", history)
