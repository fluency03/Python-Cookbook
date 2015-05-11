#!/usr/bin/python
# 2.5. Searching and Replacing Text
# Problem
# You want to search for and replace a text pattern in a string.

text = 'yeah, but no, but yeah, but no, but yeah'

text_new = text.replace('yeah', 'yep')
print (text), print (text_new)

# For more complicated patterns, use the sub() functions/methods in the re module.
import re

text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text2_re = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
text2_re1 = re.sub('(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
text2_re2 = re.sub(r'(\d+)/(\d+)/(\d+)', '\3-\1-\2', text2)
text2_re3 = re.sub('(\d+)/(\d+)/(\d+)', '\3-\1-\2', text2)
# The first argument to sub() is the pattern to match and the second argument is the
# replacement pattern. Backslashed digits such as \3 refer to capture group numbers in
# the pattern.
print (text2_re)
print (text2_re1)
print (text2_re2)
print (text2_re3)

# perform repeated substitutions of the same pattern, consider compiling it first
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print (datepat.sub(r'\3-\1-\2', text2))

# --------------------------------------------------------------------------

from calendar import month_abbr

def change_date(m):
	mon_name = month_abbr[int(m.group(1))]
	return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

text2_def = datepat.sub(change_date, text2)
print (text2_def)

# --------------------------------------------------------------------------
# To know how many substitutions were made in addition to getting the replacement text
newtext, n = datepat.subn(r'\3-\1-\2', text2)
print (newtext,'\n',n)

