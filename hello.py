#!/usr/bin/env python
# Remember that the shebang statement always goes first, before any comments.

# Using a for loop, create a document that has a user-inputed word printed a certain number of times (user-inputed)

# import sys
# This doesn't need to be included in this code.

print "Enter the word that you want displayed." # This will be printed on the screen.
word = raw_input() # This sets the variable "word" to be whatever the user inputs.

while True: # This statement deals with user-error.
   try:
      number = input('Enter the number of times that you want the word displayed.') # The user must enter the number, not the number written as a word (e.g. five won't work)
      break
   except NameError:
      print "Oops!  That was not a valid number.  Try again..." # This statement tells the user that s/he did something wrong.

print "This information will be displayed in the test.txt file."

f = open("test.txt", "w"); # This opens a file called "test.txt" and will write to it (w).

for x in range(0, number): # This tells the for loop how many times to run (up to the user-entered number)
    f.write(word + '\n') # The \n at the end starts a new line every time the word is printed in the document.
f.close() # This closes the test.txt file.  Note that it is not indented, because you don't want to close the file every time a word is printed in the document.

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
    
    

