#!/usr/bin/env python

from scipy.optimize import fmin
import numpy as np
import math
import matplotlib.pyplot as plt
import sys

# Make a vector of numbers from 0 to 10
t = np.asarray(range(0,100000))/100.

# We can make some data with noise in it
a = 2.
b = 4.
data = a + (b*t) + .5*np.random.rand(100000)



# Now suppose we new our data was sinusoidal in nature, but don't know a and b. 
# Can we solve for a and b?

def  resifunc(params):    
    anew = params[0]
    bnew = params[1]
    # Here is our model function
    modelfun = anew + (b*t)
    resi = np.sum(abs(data - modelfun)**2)
    return resi

# So we have a function that takes our data and compares it two a sine function for different parameters anew bnew

#Now see what we get with fmin



ab = fmin(resifunc,[2., 4.], xtol=10**-3, ftol=10**-19)
print ' Here are our a and b parameters ' + str(ab)

plt.plot(t,data)
plt.plot(t, ab[0]+ ab[1]*t)

plt.show()
