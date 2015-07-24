#!/usr/bin/python
# 2.14. Combining and Concatenating Strings
# Problem
# You want to combine many small strings together into a larger string.

import os

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
# join could come from any number of different data sequences 
# (e.g., lists, tuples, dicts, files, sets, or generators)
print (' '.join(parts))
print (','.join(parts))
print (''.join(parts))


a = 'Is Chicago'
b = 'Not Chicago?'
print ('{} {}'.format(a,b))
print (a + ' ' + b)

c = 'Hello' 'World'
print (c)

# using the + operator to join a lot of strings together is grossly inefficient 
# due to the memory copies and garbage collection that occurs

# One related (and pretty neat) trick is the conversion of data to strings 
# and concatenation at the same time using a generator expression
data = ['ACME', 50, 91.1]
print (','.join(str(d) for d in data))

# some choices
print (a + ':' + b + ':' + c)	# Ugly
print (':'.join([a, b, c])) 	#Still ugly

print (a, b , c, sep=':') 		#Better


# Mixing I/O operations and string concatenation
chunk1 = 'chunk1'
chunk2 = 'chunk2'
# Version 1 (string concatenation)
f.write(chunk1 + chunk2)
# Version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)













