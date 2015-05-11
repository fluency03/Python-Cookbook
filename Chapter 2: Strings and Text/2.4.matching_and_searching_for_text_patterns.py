#!/usr/bin/python
# 2.4. Matching and Searching for Text Patterns
# Problem
# You want to match or search text for a specific pattern.

text = 'yeah, but no, but yeah, but no, but yeah'

print (text.startswith('yeah'))
print (text.endswith('no'))

 # Search for the location of the first occurrence
print (text.find('no'))

# -------------------------------------------------------------------------

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# Simple matching: \d+ means match one or more digits
print (re.match(r'\d+/\d+/\d+', text1))
print (re.match(r'\d+/\d+/\d+', text2))


# Compile a regular expression pattern into a regular expression object, which 
# can be used for matching using its match() and search() methods

datepat = re.compile(r'\d+/\d+/\d+')

print (datepat.match(text1))
print (datepat.match(text2))

# -------------------------------------------------------------------------

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# The findall() method searches the text and finds all matches, returning them as a list.
text4 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print (datepat.findall(text4))

for month, day, year in datepat.findall(text4):
	print('{}-{}-{}'.format(year, month, day))

# If you want to find matches iteratively, use the finditer() method instead. For example:
for m in datepat.finditer(text4):
	print(m.groups())




m = datepat.match('11/27/2012')
print (m)
print (m.group(), m.groups())
print (m.group(0), m.group(1), m.group(2), m.group(3))
month, day, year = m.groups()
print (month, day, year)


# match starts at the begining of the string!
text5 = '11/27/2012. PyCon starts 3/13/2013.'
te = datepat.match(text5)
print (te)



