#!/usr/bin/env python

import sys

print "Enter the word that you want displayed."
word = raw_input()
number = input('Enter the number of times that you want the word displayed.')

count = 0
while (count < number):
   print "%r" % (word)
   count = count + 1

print "This will also be displayed in the test.txt file."

f = open("test.txt", "w");
print f
f.write("%r" % (word))

