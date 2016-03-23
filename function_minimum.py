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

# Make a vector of numbers from 0 to 1000 - Why do we do this math, when we could just make a range from 0 to 1000?
t = np.asarray(range(0,100000))/100.
print t

# We can make some data with noise in it
a = 2.
b = 4.
data = a + (b*t) + .5*np.random.rand(100000) # Is this vector larger than that data created in t?  What if we do this instead:
#data = a + (b*t) + .5*np.random.rand(1000) # This doesn't work -- error -- ValueError: operands could not be broadcast together with shapes (100000,) (1000,)  
print data


# Now suppose we knew our data was sinusoidal in nature, but don't know a and b. 
# Can we solve for a and b?

def  resifunc(params): # This defines a function called resifunc.  It takes in some variable called params.  I think params is a list.   
    anew = params[0] # anew will be the first element of the list called params (at index space of 0)
    bnew = params[1] # bnew will be the second element of the list called params (at index space of 1)
    # Here is our model function
    modelfun = anew + (bnew*t)
    resi = np.sum(abs(data - modelfun)**2)
    return resi

# So we have a function that takes our data and compares it two a sine function for different parameters anew bnew

# Now see what we get with fmin

ab = fmin(resifunc,[2., 4.], xtol=10**-3, ftol=10**-19) #How do you know what to set xtol and ftol to be?
print ' Here are our a and b parameters ' + str(ab)

plt.plot(t,data)
plt.plot(t, ab[0]+ ab[1]*t)
plt.savefig('Function Plot')

# I am confused by xtol and ftol, so I am trying this example:
def myFun(x):
    return (x[0]-1.2)**2 + (x[1]+3.7)**2
blah = fmin(myFun,[0,0])
print blah

def myFun1(x):
    return (x[0]-1.2)**2 + (x[1]+3.7)**2
blah1 = fmin(myFun1,[0,0], xtol=1e-12)
print blah1

def myFun2(x):
    return (x[0]-1.2)**2 + (x[1]+3.7)**2
blah2 = fmin(myFun2,[0,0], xtol=1, ftol=1e-3)
print blah2

def myFun3(x):
    return (x[0]-1.2)**2 + (x[1]+3.7)**2
blah3 = fmin(myFun3,[0,0], xtol = 1e-6, ftol = 1e-6)
print blah3