#!/usr/bin/python
# 2.11. Stripping Unwanted Characters from Strings
# Problem
# You want to strip unwanted characters, such as whitespace, from the beginning, end, or
# middle of a text string.


# Whitespace stripping
s = '    hello world    \n'
# By default, these methods strip whitespace, 
# but other characters can be given.
print (s.strip())
print (s.lstrip())
print (s.rstrip())

# Character stripping
t = '-----hello====='
print (t.lstrip('-'))
print (t.rstrip('='))


# stripping does not apply to any text in the middle of a string
smiddle = '   hello        world    \n'
smiddle = smiddle.strip()
print (smiddle)


# instead, you can use 'replace()' or 'sub'
print (smiddle.replace(' ', ''))

import re
ssub = re.sub('\s+', ' ', smiddle)
print (ssub)


filename = '2.10.working_with_Unicode_Characters_in_regex.py'

with open(filename) as f:
	# just creates an iterator where all of the lines produced have the 
	# space-stripping operation applied to them
	lines = (line.strip() for line in f) 
	print ('\n')
	for line in lines:
		print (line)






