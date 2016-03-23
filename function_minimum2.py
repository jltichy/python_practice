#!/usr/bin/env python

# Enter these two commands if start a new workspace:
#sudo easy_install numpy
#sudo easy_install matplotlib

from scipy.optimize import fmin
import numpy as np
import math
import sys
import matplotlib
matplotlib.use('Agg') #This is required to run matplotlib on Google Chrome.
import matplotlib.pyplot as plt

# Make a vector of numbers from 0 to 10
t = np.asarray(range(0,200))/100. # This has that same oddity -- why do the math when we could just do the range right away?

# We can make some data with noise in it
a = 2.
b = 4.
data = a*np.sin((b*t)*2*math.pi) + .5*np.random.rand(200) # The value directly in front of *np.random.rand(200) can be changed to change the data.  It started at .5
# The smaller the value in front of the np.random part of this equation, the better the data fits the sine wave curve. 
# If we change the + to a - then the data flips to the opposite side of the sine wave curve.
# The goal is to minimize the value in front of "*np.random.rand(200)"
# That would mean that you don't have much noise.


# Now suppose we new our data was sinusoidal in nature, but don't know a and b. 
# Can we solve for a and b?

def  resifunc(params):    
    anew = params[0]
    bnew = params[1]
    # Here is our model function
    modelfun = anew*np.sin((bnew*t)*2.*math.pi)
    resi = np.sum(abs(data - modelfun)**2)
    return resi

# So we have a function that takes our data and compares it two a sine function for different parameters anew bnew

#Now see what we get with fmin

ab = fmin(resifunc,[2., 4.], xtol=10**-3, ftol=10**-19)
print ' Here are our a and b parameters ' + str(ab)

plt.plot(t,data)
plt.plot(t, ab[0]*np.sin(ab[1]*t*2.*math.pi))
plt.savefig('Function Plot Number 2')