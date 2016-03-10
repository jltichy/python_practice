#!/usr/bin/env python
# Remember that the shebang statement always goes first, before any comments.

# Using a for loop, create a document that has a user-inputed word printed a certain number of times (user-inputed)

# import sys
# This doesn't need to be included in this code.

print "Enter the word that you want displayed."
word = raw_input()

while True:
   try:
      number = input('Enter the number of times that you want the word displayed.') # The user must enter the number, not the number written as a word (e.g. five won't work)
      break
   except NameError:
      print "Oops!  That was not a valid number.  Try again..."

print "This information will be displayed in the test.txt file."

f = open("test.txt", "w");

for x in range(0, number):
    f.write(word + '\n')
f.close()

"""Okay,

couple of things.

Are you using import sys?  If not get rid of it.

Does your python code start with a shebang?  Move the comments to be below the shebang.

Next thing.

You need to add error handing.

What happens if someone runs your code with the following input

hello
five

does it crash?  

Figure out how to make it not crash using the following:

try

except"""
    
    

