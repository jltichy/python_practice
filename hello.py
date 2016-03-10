#!/usr/bin/env python

import sys

print "Enter the word that you want displayed."
word = raw_input() #This defines the input as the variable called word
number = input('Enter the number of times that you want the word displayed.') #This will be the number of times that the word is displayed.

count = 0
while (count < number):
   print "%r" % (word)
   count = count + 1

print "This will also be displayed in the test.txt file."

f = open("test.txt", "w");
print f
f.write("%r" % (word))

# Here is Adam's code:
f = open('blah','w')

f.write('Hello kitty\n')

f.close()


print 'Bam bam' + str(5) + ' bam bam' + str(4.5) + '\n'

