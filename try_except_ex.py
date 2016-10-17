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
try:
  square_roots = isinstance(square_roots, int)
  not_integers = isinstance(square_roots, float)
except: 
  pass
  
print square_roots
print not_integers