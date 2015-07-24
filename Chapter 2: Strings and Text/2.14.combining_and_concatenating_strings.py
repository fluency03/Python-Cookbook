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


f = open('testfile.txt', 'w')
# Mixing I/O operations and string concatenation
chunk1 = 'chunk1'
chunk2 = 'chunk2'
# Version 1 (string concatenation)
f.write(chunk1 + chunk2 + '\n')
# Version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)
f.write('\n')

# If the two strings are small, the first version might offer much better performance due
# to the inherent expense of carrying out an I/O system call. 

# On the other hand, if the two strings are large, the second version may be more efficient, 
# since it avoids making a large temporary result and copying large blocks of memory around. 


# code as a generator function, using yield to emit fragments
def sample():
	yield 'Is'
	yield 'Chicago'
	yield 'Not'
	yield 'Chicago?'

# it makes no assumption about how the fragments are to be assembled together
# Join
print (''.join(sample()))
# redirect the fragments to I/O
for part in sample():
	f.write(part)
f.write('\n')
# hybrid scheme that’s smart about combining I/O operations
def combine(source, maxsize):
	parts = []
	size = 0
	for part in source:
		parts.append(part)
		size += len(part)
		if size > maxsize:
			yield ''.join(parts)
			parts = []
			size = 0
	yield ''.join(parts)

for part in combine(sample(), 32768):
	f.write(part)







