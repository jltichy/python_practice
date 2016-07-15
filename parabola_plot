#!/usr/bin/env python

#Instructions - Create a plot of a parabola (e.g. y = x^2)
#Let's do the simple case first, where the vector x is defined and then we square each value to create a vector for y.  The two vectors will be plotted against each other.

# Enter these two commands if start a new workspace:
#sudo easy_install numpy
#sudo easy_install matplotlib

# A function 
def func(x):
    return (x**2) 
#def allows you to define a function of your own, in this case a function of x
#x**2 means "x-squared"

# Forward problem: given x compute func(x)
# The value of our function at 1
print 'Here is our function at 1: ' + str(func(1.))
#one squared should be one

# Let's try it with another value:
# The value of our function at 5
print 'Here is our function at 5: ' + str(func(5))
#five squared should be 25.

import numpy as np  # Remember to install numpy as: sudo easy_install numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # Remember to install matplotlib as: sudo easy_install matplotlib
x = np.arange(-10,11)  
y = eval('func(x)')
plt.plot(x, y) 
plt.suptitle('X squared') # Figure out how to write an x with a squared symbol.
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.savefig('X squared')

