#!/usr/bin/env python

# Optimization routine
from scipy.optimize import fmin 
#scipy is a package for high level scientific computing, such as interpolation, integration, optimization, image processing, and statistics
#Optimization is the problem of finding a numerical solution to a minimization or equality.
#fmin is the minimum of a function


# A function 
def func(x):
    return abs(x**2 -1.) 
#def allows you to define a function of your own, in this case a function of x
#abs is absolute value
#x**2 means "x-squared"

# Forward problem: given x compute func(x)
# The value of our function at 1
print 'Here is our function at 1: ' + str(func(1.))
#one squared minus one should be zero

# Let's try it with another value:
# The value of our function at 5
print 'Here is our function at 5: ' + str(func(5))
#five squared minus one should be 24. Note that I did not include a decimal after the 5 and the answer was still correct.

# Inverse problem: given y find x such that func(x)=y
# We want to solve for where our function = 0
# -4 is the initial guess, xtol and ftol are convergence parameters
blah = fmin(func,-4., xtol=10**-9, ftol=10**-9) #this is the original code
print 'Here is the solution to our inverse problem: ' + str(blah)
#Optimization terminated successfully.                                                                                                                   
#        Current function value: 0.000000                                                                                                               
#        Iterations: 36                                                                                                                                 
#        Function evaluations: 73                                                                                                                       
#Here is the solution to our inverse problem: [-1.]  

# Let's try to start with a guess of 4 instead of -4
blah = fmin(func,4., xtol=10**-9, ftol=10**-9)
print 'Here is the solution to our inverse problem: ' + str(blah)
#Optimization terminated successfully.                                                                                                                   
#        Current function value: 0.000000                                                                                                               
#        Iterations: 36                                                                                                                                 
#        Function evaluations: 73                                                                                                                       
#Here is the solution to our inverse problem: [1.] 

# We can also plot the function to find where it's equal to 0.
import numpy as np  # Remember to install numpy as: sudo easy_install numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # Remember to install matplotlib as: sudo easy_install matplotlib
x = np.arange(-10,11)  
y = eval('func(x)')
plt.plot(x, y) 
plt.suptitle('X squared minus 1') # Figure out how to write an x with a squared symbol.
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.savefig('X squared minus 1')

# Here we go starting with Task number 3.

# For the sake of this exercise, we must first create a list that can be imported into the function.
L = [1, 2, 3, 4, 5]

print "This function will compute the sum of the squares.  Please enter the name of your list for use with this function."
list = raw_input() # In this case, the user must enter "L" since that is the name of our list for this exercise.
def func(y):
    for item in list:
return (item**2) 

# Tasks
# 1: Read about fmin and def and functions - done. see comments above
# 2: What happens when you start with a guess of 4 and not -4? done. see results above.  You get 1 instead of -1.
# 3: Write a function that takes a list and computes the sum of the squares 
# 	e.g. x(1)**2 + x(2)**2 + ... + x(n)**2
# 4: Use a list of two elements and find the minimum of the function in 3
