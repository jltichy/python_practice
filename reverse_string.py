#!/usr/bin/env python

# Ask the user for a string.  Write a program to reverse the words in that string

directions = raw_input("Please enter a string, aka a sentence.")
print directions

reversed_string = ' '.join(reversed(directions))
print reversed_string