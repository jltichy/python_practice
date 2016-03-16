#!/usr/bin/env python

# Instructions - Create an array of 1000 randomly distributed numbers.  Plot these as a timeseries from 1 to 1000.  Use numpy and matlibplot.

# This is how to install Matlibplot - sudo apt-get install python-matplotlib

import numpy as np # np is the name of the matrix to be created
import random

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt # Do not do this prior to calling use()

matrix = np.zeros((1000, 1)) # this creates a matrix of zeros with 1 column and 1000 rows
#print matrix # allows us to see what's in the matrix (all zeros at this point)
matrix = np.random.randint(0, 10, (1000, 1)) # fills the matrix of zeros with random integers from 0 to 10.  The size of the matrix doesn't change.
#print matrix # allows us to see what's in the matrix of random values

time = np.arange(1,1001)
#print time

# x = time
# y = matrix

plt.scatter(time, matrix)
#plt.show()
plt.savefig('Random Timeseries Example')
