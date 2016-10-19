#!/usr/bin/env python

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
while True:
    try:
        x = (raw_input("Please enter some text:"))
        if debug:
            print('Input: ' + str(x))
        break
    except:
        print('Input: ' + str(x))

