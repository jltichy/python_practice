#!/usr/bin/env python

# Instructions - Create an array of 1000 randomly distributed numbers.  Plot these as a timeseries from 1 to 1000.  Use numpy and matlibplot.

# This is how to install Matlibplot - sudo apt-get install python-matplotlib

import numpy as np # np is the name of the matrix to be created
import random
#import pprint # not necessary - used to change to string (with commas)
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt # Do not do this prior to calling use()

matrix = np.zeros((1, 1000)) # this creates a matrix of zeros with 1 column and 1000 rows
#print matrix # allows us to see what's in the matrix (all zeros at this point)
matrix = np.random.randint(0, 100, (1, 1000)) # fills the matrix of zeros with random integers from 0 to 10.  The size of the matrix doesn't change.
#pprint.pprint(matrix) # not necessary - used to change to string (with commas)
#print matrix # allows us to see what's in the matrix of random values

time = np.arange(1,1001)
#pprint.pprint(time) # not necessary - used to change to string (with commas)
#print time

# x = time
# y = matrix

plt.scatter(time, matrix, color='red')
plt.suptitle('Test Title')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
#plt.show()
plt.savefig('Random Timeseries Example')
