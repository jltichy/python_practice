#!/usr/bin/env python

print "Enter the word that you want displayed."
word = raw_input()
number = input('Enter the number of times that you want the word displayed.')

count = 0
while (count < number):
   print "%r" % (word)
   count = count + 1
