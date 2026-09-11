from math import cos
from plot_fixed_point import plot_fixed_point_iteration

# f(x) = x - 1.5cos(x)
# We want to solve f(x) = 0, i.e., find the root of f(x).
# So our equation is x - 1.5cos(x) = 0
# Which means that we can rewrite it as x = 1.5cos(x)
# So we want to find the fixed point of the function g(x) = 1.5cos(x)
# Note: |g'(r)| ~ 1.19 > 1 at the fixed point r ~ 0.915, so the
# iteration does not converge to r; it escapes to a stable 2-cycle.
def g(x):
    return 1.5 * cos(x)

# Initial guess: x = 1
x = 1

r = plot_fixed_point_iteration(g, x, tol=5e-2)
print(r)

r = plot_fixed_point_iteration(g, x, tol=1e-3)
print(r)
