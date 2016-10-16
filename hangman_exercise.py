#!/usr/bin/env python

# In this exercise, the task is to write a function that picks 
# a random word from a list of words from the SOWPODS dictionary. 
# Download this file and save it in the same directory as your 
# Python code. This file is Peter Norvig's compilation of the
# dictionary of words used in professional Scrabble tournaments. 
# Each line in the file contains a single word.

# Hint: use the Python random library for picking a random word.

import random
from random import randint

with open('sowpods.txt', 'r') as f:
  line = f.readline().strip()
  while line:
    line = f.readline().strip()

with open('sowpods.txt', 'r') as f:
  lines = f.readlines()

file_length = len(lines)
#print file_length

random_word_index = randint(0,file_length)
#print random_word_index

#print lines[random_word_index]

print "There are %s lines in this document." % (file_length)
print "We are randoming choosing to look at line number %s." % (random_word_index)
print "The word on the line of interest is %s." % lines[random_word_index]

