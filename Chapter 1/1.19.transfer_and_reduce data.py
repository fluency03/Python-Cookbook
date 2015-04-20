#!/usr/bin/python
# 1.19. Transforming and Reducing Data at the Same Time
# Problem: You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
# transform or filter the data.

nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print (s)

# --------------------------------------------------------------------

# Determine if any .py files exist in a directory
import os

path = '/home/cliu/Documents/github/Python-Cookbook/'
files = os.listdir(path)
print (files)

for f in files:
	print (f)


# Determine if any .py files exist in a directory
if any(name.endswith('.py') for name in files):
	print ('There be python!')
else: 
	print ('Sorry, no python!')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print (','.join(str(x) for x in s))

# Data reduction across fields of a data structure

portfolio = [
	{'name':'GOOG', 'shares': 50},
	{'name':'YHOO', 'shares': 75},
	{'name':'AOL', 'shares': 20},
	{'name':'SCOX', 'shares': 65}
]

min_shares = min (s['shares'] for s in portfolio)
print (min_shares)

# --------------------------------------------------------------------
# a subtle syntactic aspect of generator expressions when supplied as the 
# single argument to a function (i.e., you don’t need repeated parentheses)
s1 = sum((x * x for x in nums)) # Pass generator-expr as argument
print (s1)

s2 = sum(x * x for x in nums) # More elegant syntax
print (s2)


