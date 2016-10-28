#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The above code that includes "utf" is for text formatting.  It allows you
# to copy and paste text that may be a different font.

import sys
import this # This is the Zen of Python - it shows how to code in a Pythonic manner

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

debug = True

print("   *   ")
print("  ***  ")
print(" ***** ")
print("   *   ")
print("   *   ")
print("   *   ")

# compilers translate one computer language into another
# interpreters translate the Python code into machine code when a user runs 
# the program

x = 10
print('x = ' + str(x))
x = 20
print('x = ' + str(x))
x = 30
print('x = ' + str(x))

x = 10
print('x =', x)
x = 20
print('x =', x)
x = 30
print('x =', x)

# This is a tuple - A tuple is a comma separated list of expressions. In the 
# assignment statement x, y, z = 100, -45, 0 x, y, z is one tuple, and 100, 
# -45, 0 is another tuple
x, y, z = 100, -45, 0
print('x =', x, ' y =', y, ' z =', z)

a = 10
print('First, variable a has value', a, 'and type', type(a))
a = 'ABC'
print('Now, variable a has value', a, 'and type', type(a))

print('A\nB\nC')
# A
# B
# C
print('D\tE\tF')
# D       E       F
print('WX\bYZ')
# WYZ
print('1\a2\a3\a4\a5\a6')
# 123456

print("Did you know that 'word' is a word?")
print('Did you know that "word" is a word?')
print('Did you know that \'word\' is a word?')
print("Did you know that \"word\" is a word?")

# The above four lines look like this:
# Did you know that 'word' is a word?
# Did you know that "word" is a word?
# Did you know that 'word' is a word?
# Did you know that "word" is a word?

# There is a problem with this section - I'm getting an error:
#Traceback (most recent call last):
#  File "/home/ubuntu/workspace/python_practice/Haltermanpythonbook.py", line 62, in <module>
#    x = input()
#  File "<string>", line 1, in <module>
#NameError: name 'Hello' is not defined

#x = input('Please enter some text: ')
#print('Text entered:', x)
#print('Type:', type(x))

# Let's try using try/except because I think we have a ValueError and I am 
# throwing an exception:

# I am going to comment this out so I don't have to enter something everytime
# I run the program...

# while True:
#     try:
#         x = (raw_input("Please enter some text:"))
#         if debug:
#             print('Input: ' + str(x))
#         break
#     except:
#         print('Input: ' + str(x))


# Let's figure out some specs for this IDE.
#print sys.float_info 
#print sys.int_info
print sys.maxsize

# Write a Python program that simply emits a beep sound when run.
sys.stdout.write('\a')
sys.stdout.flush()
# This doesn't seem to be working.  It may be incompatible with Cloud9.

# Chapter 3.

print("x")
print('x')
print(x)
print("x + 1")
#print('x'+1) #This throws an error
print(x + 1)

# Here are the results of the above commands, minus the one with the error.
# x
# x
# 100
# x + 1
# 101

i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5;

print i1 + i2
print i1 / i2
print i1 // i2
print i2 / i1
print i2 // i1
print i1 * i3
print d1 + d2
print d1 / d2
print d2 / d1
print d3 * d1
print d1 + i2
print i1 / d2
print d2 / i1
print i2 / d1
print i1/i2*d1
print d1*i1/i2
print d1/d2*i1
print i1*d1/d2
print i2/i1*d1
print d1*i2/i1
print d2/d1*i1
print i1*d2/d1

# Here are the results of the above code.
# 7
# 0
# 0
# 2
# 2
# -6
# 7.0
# 0.4
# 2.5
# -1.0
# 7.0
# 0.4
# 2.5
# 2.5
# 0.0
# 0.8
# 0.8
# 0.8
# 4.0
# 5.0
# 5.0
# 5.0

print(5/3)
# This shows 1

# # Get two numbers from the user
# n1, n2 = eval(input()) # 1
# # Compute sum of the two numbers
# print(n1 + n2) # 2
# # Compute average of the two numbers
# print(n1+n2/2) # 3
# # Assign some variables
# d1 = d2 = 0 # 4
# # Compute a quotient
# print(n1/d1) # 5
# # Compute a product
# #n1*n2 = d1 # 6 # There is a problem with the syntax of this line.
# # Print result
# print(d1) # 7

x1 = 2
x2 = 2
x1 += 1
x2 -= 1
print(x1) #3
print(x2) #1

r = 0
PI = 3.14159
# Formula for the area of a circle given its radius
C = 2*PI*r
# Get the radius from the user
#r = eval(input("Please enter the circle's radius: ")
# Print the circumference
print("Circumference is", C)

# Chapter 4 Exercises:
# Request input from the user
num = eval(input("Please enter an integer in the range 0...9999: "))

# Attenuate the number if necessary
if num < 0: # Make sure number is not too small
    num = 0
if num > 9999: # Make sure number is not too big
    num = 9999

#print (end='[')

#print(end = "[") # Print left brace

# Extract and print thousands-place digit
digit = num//1000 # Determine the thousands-place digit
#print(digit, end="") # Print the thousands-place digit
num %= 1000 # Discard thousands-place digit

# Extract and print hundreds-place digit
digit = num//100 # Determine the hundreds-place digit
#print(digit, end="") # Print the hundreds-place digit
num %= 100 # Discard hundreds-place digit

# Extract and print tens-place digit
digit = num//10 # Determine the tens-place digit
#print(digit, end="") # Print the tens-place digit
num %= 10 # Discard tens-place digit

# Remainder is the one-place digit
#print(num, end="") # Print the ones-place digit

#print("]") # Print right brace