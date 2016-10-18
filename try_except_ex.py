#!/usr/bin/env python

# Exercise - Create a vector of random numbers.  Take the square root of every 
# number and only display the ones that are whole numbers.

import numpy as np
import random
from random import randint

# Here is a debug flag
debug = True

# Create a vector of length 10 of random numbers up to 10:
vector = np.random.randint(10, size=10)
print vector

# Take the square root of each value and preserve the sign:
square_roots = np.sqrt(np.abs(vector)) * np.sign(vector)
print square_roots

# Experiment with determining if a value is an integer:
result = isinstance(square_roots, int)
print result
# It looks like this gives one result for the entire vector.
# I need to figure out how to look at each value in the vector.

# Use try/except to see if each value is an integer:
# Adam gave me the code as follows:

# You are mixing your tabs between 4 space and 2 space
try:
    square_root_integer = np.equal(np.mod(square_roots,1),0)
except:
    if debug:
        print('Looks like we have a problem')
    pass
  
print square_root_integer
# Here is the reason - if you take mod 1 of an integer, you get 0

# We can then use the new square_roots array to print the values where it's 
# true.


# Let's try another example here.

# This is funy programming
while True:
    # You have a while statement that is always true
    try:
        x = int(input("Please enter a number:"))
        if debug:
            print('Here is your number: x = ' + str(x))
        # Here you are breaking out of the loop
        break
    # You were throwing an exception so the program crashes
    # Instead we will assume it is okay and not throw and exception 
    except:
        print("Oops!  That is not a valid number.  Try again.")

if debug:
    print 'There is a problem.'
       
# still not quite getting this:
# use this webpage https://docs.python.org/3/tutorial/errors.html

  
