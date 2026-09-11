from math import cos
from find_fixed_point import find_fixed_point 

# f(x) = x - cos(x) 
# We want to solve f(x) = 0, i.e., find the root of f(x).
# So our equation is x - cos(x) = 0 
# Which means that we can rewrite it as x = cos(x) 
# So we want to find the fixed point of the function g(x) = cos(x) 
def g(x):
    return cos(x) 

# Initial guess: x = 1 
x = 1 

r = find_fixed_point(g, x, tol=5e-2)
print(r) 

r = find_fixed_point(g, x, tol=1e-3)
print(r) 
