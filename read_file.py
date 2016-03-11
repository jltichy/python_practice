#!/usr/bin/env python

# Instructions - Ask the user for a filename.  Read in the file.  Tell the user how many lines are included in their file of interest.  Print the first and last elements in the file.  Use the following commands - readlines(), lists, len(), and with.

# For the sake of this program, we must first create a file.

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

f.write("This is the first line of the document." + '\n')

for x in range(0, number): # This tells the for loop how many times to run (up to the user-entered number)
    f.write(word + '\n') # The \n at the end starts a new line every time the word is printed in the document.
f.close() # This closes the test.txt file.  Note that it is not indented, because you don't want to close the file every time a word is printed in the document.

# OK, here we go with this new exercise.

print "What file do you want to open?  Please enter the name of the file with the file-type extension, ex. read_me.txt."
file_name = raw_input()
print "Name of the file: ", file_name
f = open(file_name, "r");

for line in f.read().split('\n'):
   print line
f.close()

with open(file_name) as f:
   print "Your file has %d lines." % (sum(1 for _ in f))
