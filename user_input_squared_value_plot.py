#!/usr/bin/env python

#Instructions - Write a function that takes a number and squares it.  Then plot that function in a range from -20 to 20.

user_input = input('Please input a number.  This program will square the number and will create a plot of the function from -20 to 20.')
print(user_input)

def func(user_input):
    return (user_input**2) 
    
import numpy as np  # Remember to install numpy as: sudo easy_install numpy
import matplotlib # Remember to install matplotlib as: sudo easy_install matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  
plt.figure(1)
x = np.arange(-20,21)  
print x
y = eval('func(user_input)')
print y

z = np.full((len(x),1), y)
print z

#a = np.empty(len(x))
#for i in range(len(x)):
#    a[i] = y

plt.plot(x, z) 
plt.suptitle('User Input - X squared') # Figure out how to write an x with a squared symbol.
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.savefig('userinputXsquared')
