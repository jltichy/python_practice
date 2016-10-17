#!/usr/bin/env python

# Exercise - Create a vector of random numbers.  Take the square root of every 
# number and only display the ones that are whole numbers.

import numpy as np
import random
from random import randint

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
try:
  square_root_integer = np.equal(np.mod(square_roots,1),0)
except: 
  pass
  
print square_root_integer
# Here is the reason - if you take mod 1 of an integer, you get 0

# We can then use the new square_roots array to print the values where it's 
# true.

def function():
    if square_root_integer == 'True':
        print square_roots
    elif square_root_integer == 'False':
        print('not an integer')


# Let's try another example here.
while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops!  That is not a valid number.  Try again.")
        
# still not quite getting this:
# use this webpage https://docs.python.org/3/tutorial/errors.html

  
