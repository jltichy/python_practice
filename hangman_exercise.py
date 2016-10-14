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

#fname = open("sowpods.txt",'r'); # This opens a file called "sowpods.txt"

with open('sowpods.txt', 'r') as f:
  line = f.readline().strip()
  while line:
    # do something with the 'line' variable
    line = f.readline().strip()

with open('sowpods.txt', 'r') as f:
  lines = f.readlines()

#print fname.read(10)
#print lines

file_length = len(lines)
print file_length

random_word_index = randint(0,file_length)
print random_word_index

# start here.  now that you have the index of the random word in the file,
# you can call the word with the index.

# def file_len(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1


#fname.close() # This closes the sowpods.txt file.  Note that it is not indented.

