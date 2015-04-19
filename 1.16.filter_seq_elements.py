#!/usr/bin/python
# 1.16. Filtering Sequence Elements
# Problem: You have data inside of a sequence, and need to extract values or reduce the sequence
# using some criteria.


mylist = [1, 4, -5, 10, -7, 2, 3, -1]

positive_n = [n for n in mylist if n > 0]
print (positive_n)

negative_n = [n for n in mylist if n < 0]
print (negative_n)

# list comprehension might produce a large result if the original input 
# is large. If this is a concern, you can use generator expressions to 
# produce the filtered values iteratively. 

pos = (n for n in mylist if n > 0)
print (pos)

for x in pos:
	print (x, end=' ')

print ('\n')

# ------------------------------------------------------------------------

# Sometime, the filtering criteria cannot be easily expressed in a 
# list comprehension or generator expression

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

# put the filtering code into its own function and use the built-in filter()
ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']

# filter(function, iterable) is equivalent to [item for item in iterable if function(item)] 
# or, [item for item in iterable if item] if function is None.

# ------------------------------------------------------------------------

import math
seq_sqrt = [math.sqrt(n) for n in mylist if n > 0]

print (seq_sqrt)

# ------------------------------------------------------------------------
# instead of just finding positive values, you want to also clip bad values 
# to fit within a specified range

clip_neg = [n if n > 0 else 0 for n in mylist]
print (clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print (clip_pos)


# ------------------------------------------------------------------------
# itertools.compress() takes an iterable and an accompanying Boolean selector sequence as input.
# As output, it gives you all of the items in the iterable where the corresponding 
# element in the selector is True. 

addresses =[
	'5412 N CLARK',
	'5148 N CLARK',
	'5800 E 58TH',
	'2122 N CLARK'
	'5645 N RAVENSWOOD',
	'1060 W ADDISON',
	'4801 N BROADWAY',
	'1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print (more5)

comp_results = list(compress(addresses, more5))
print (comp_results)

# Like filter(), compress() normally returns an iterator. Thus, you need to use 
# list() to turn the results into a list if desired.

