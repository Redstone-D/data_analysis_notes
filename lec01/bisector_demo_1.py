from bisector import solve_bisector 

from math import cos 

# f(x) = x - cos(x) 
def f(x):
    return x - cos(x) 

# We know that exists a root of f(x) in the interval [0, 1] 
# The interval is set as below 
a = 0
b = 1 

# Find the root using the bisector method 
r = solve_bisector(f, a, b, max_iter=10)
print(r) 

# Find the root using the bisector method with a smaller tolerance 
r = solve_bisector(f, a, b, max_iter=100)
print(r) 
