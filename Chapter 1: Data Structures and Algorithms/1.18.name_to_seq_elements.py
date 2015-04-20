#!/usr/bin/python
# 1.18. Mapping Names to Sequence Elements
# Problem: You have code that accesses list or tuple elements by position, but this makes the code
# somewhat difficult to read at times. You’d also like to be less dependent on position in
# the structure, by accessing the elements by name.


from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['address', 'joined'])

sub = Subscriber('fluency.03@gmail.com', '2015-04-20')
print (sub)
print (sub.address, sub.joined)

print (len(sub))
a, b = sub

print (a, b)

# If get back a large list of tuples from a database call,
# then manipulate them by accessing the positional elements, 
# the code could break if, say, you added a new column to your table.

def compute_cost1(records):
	total = 0.0
	for rec in records:
		total += rec[1] * rec[2]
	return total


# References to positional elements often make the code a bit less 
# expressive and more dependent on the structure of the records. 

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost2(records):
	total = 0.0
	for rec in records:
		# The single star * unpacks the sequence/collection into 
		# positional arguments
		s = Stock(*rec)
		total += s.shares * s.price
	return total

# --------------------------------------------------------------------

stock_list = [
	Stock('ACME', 100, 123.45),
	Stock('B', 100, 123.45),
	Stock('C', 100, 123.45),
	Stock('D', 100, 123.45)
]

compute_result1 = compute_cost1(stock_list)
print (compute_result1)
compute_result2 = compute_cost2(stock_list)
print (compute_result2)

# large data structures involving dictionaries, use of a namedtuple will be 
# more efficient. unlike a dictionary, a namedtuple is immutable

s = Stock('ACME', 100, 123.45)

# This code is not executable
# s.shares = 75

# To change any of the attributes, it can be done using the _replace() 
# method of a namedtuple instance
s = s._replace(shares=75)
print (s)

# --------------------------------------------------------------------

Stock2 = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock2('', 0, 0.0, None, None)

def dict_to_stock(s):
	# The double star ** does the same as singe star *, 
	# only using a dictionary and thus named arguments
	return stock_prototype._replace(**s)

c = {'name': 'ACME', 'shares': 100, 'date': '12/17/2012', 'price': 123.45}
# here, the order is not relevant, e.g., the position of 'date'
stock_c = dict_to_stock(c)
print (c)
print (stock_c)

d = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
stock_d = dict_to_stock(d)
print (d)
print (stock_d)

