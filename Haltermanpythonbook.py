#!/usr/bin/env python

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