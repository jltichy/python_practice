#!/usr/bin/env python

# Ask the user for a string.  Write a program to reverse the words in that string

# This part will reverse the letters in the string.
directions = raw_input("Please enter a string, aka a sentence.")
print directions

reversed_string = ' '.join(reversed(directions))
print reversed_string

# This part will reverse the words in the string.
splitted = directions.split()
print splitted
reversed = splitted[::-1]
print reversed
result = " ".join(reversed)
print result
# result = " ".join(str.split()[::-1])
# print result


