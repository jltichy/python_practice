#!/usr/bin/env python

# Optimization routine
from scipy.optimize import fmin

# A function 
def func(x):
    return abs(x**2 -1.)

# Forward problem: given x compute func(x)
# The value of our function at 1
print 'Here is our function at 1: ' + str(func(1.))


# Inverse problem: given y find x such that func(x)=y
# We want to solve for where our function = 0
# -4 is the initial guess, xtol and ftol are convergence parameters
blah = fmin(func,-4., xtol=10**-9, ftol=10**-9)
print 'Here is the solution to our inverse problem: ' + str(blah)


# Tasks
# 1: Read about fmin and def and functions
# 2: What happens when you start with a guess of 4 and not -4?
# 3: Write a function that takes a list and computes the sum of the squares 
# 	e.g. x(1)**2 + x(2)**2 + ... + x(n)**2
# 4: Use a list of two elements and find the minimum of the function in 3
