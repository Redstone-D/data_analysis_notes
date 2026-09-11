from math import cos
from find_fixed_point import find_fixed_point 

# f(x) = x - 3cos(x) 
# We want to solve f(x) = 0, i.e., find the root of f(x).
# So our equation is x - 3cos(x) = 0 
# Which means that we can rewrite it as x = 3cos(x) 
# So we want to find the fixed point of the function g(x) = 3cos(x) 
def g(x):
    return 3 * cos(x) 

# Initial guess: x = 1 
x = 1 

r = find_fixed_point(g, x, tol=5e-2)
print(r) 

r = find_fixed_point(g, x, tol=1e-3)
print(r) 
