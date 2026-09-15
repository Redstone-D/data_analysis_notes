from math import cos
from plot_bisector import plot_bisector_iteration

# f(x) = x - cos(x)
# We want to solve f(x) = 0, i.e., find the root of f(x).
# We know that a root of f(x) exists in the interval [0, 1] because
# f(0) = -1 < 0 and f(1) = 1 - cos(1) > 0, so by IVT there is a root.
def f(x):
    return x - cos(x)

# Initial bracket: [a, b] = [0, 1]
a = 0
b = 1

# Loose tolerance: stop when the half-width of the bracket falls below 5e-2.
cs = plot_bisector_iteration(f, a, b, tol=5e-2)
print(cs)

# Tighter tolerance: stop when the half-width of the bracket falls below 1e-3.
cs = plot_bisector_iteration(f, a, b, tol=1e-3)
print(cs)
