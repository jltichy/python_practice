#!/usr/bin/env python

# In this exercise, the task is to write a function that picks 
# a random word from a list of words from the SOWPODS dictionary. 
# Download this file and save it in the same directory as your 
# Python code. This file is Peter Norvig's compilation of the
# dictionary of words used in professional Scrabble tournaments. 
# Each line in the file contains a single word.

# Hint: use the Python random library for picking a random word.

import numpy as np # np is the name of the matrix to be created
import random

fname = open("sowpods.txt", "w"); # This opens a file called "sowpods.txt" and will write to it (w).

fname.write("This is the first line of the text file." + '\n')

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
fname.close() # This closes the test.txt file.  Note that it is not indented, because you don't want to close the file every time a word is printed in the document.

