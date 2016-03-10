# Using a for loop, create a document that has a user-inputed word printed a certain number of times (user-inputed)

#!/usr/bin/env python

import sys

print "Enter the word that you want displayed."
word = raw_input()
number = input('Enter the number of times that you want the word displayed.')

print "This information will be displayed in the test.txt file."

f = open("test.txt", "w");

for x in range(0, number):
    f.write("word" + '\n') #Something is wrong right here.
    
f.close()
