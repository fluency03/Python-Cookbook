#!/usr/bin/python
# 2.16. Reformatting Text to a Fixed Number of Columns
# Problem
# You have long strings that you want to reformat so that they fill a user-specified number
# of columns.

# textwrap module to reformat text for output
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

print (s)

import textwrap
print (textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='	'))
print(textwrap.fill(s, 40, subsequent_indent='	'))


# textwrap module is a straightforward way to clean up text for printing—especially
# if you want the output to fit nicely on the terminal. 

# On the subject of the terminal size, you can obtain it using os.get_terminal_size()
import os 

cols = os.get_terminal_size().columns
lines = os.get_terminal_size().lines
print ('columns =', cols, 'lines =', lines)
















