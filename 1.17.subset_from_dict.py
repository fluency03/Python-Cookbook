#!/usr/bin/python
# 1.17. Extracting a Subset of a Dictionary
# Problem: You want to make a dictionary that is a subset of another dictionary.

prices = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HPQ': 37.20,
	'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key:value for key, value in prices.items() if value > 200}
print (p1)

# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = {key:value for key, value in prices.items() if key in tech_names}
print (p2)

# the dictionary comprehension solution is a bit clearer and 
# actually runs quite a bit faster (TWO times faster than previous one)
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print (p3)
p4 = list((key, value) for key, value in prices.items() if value > 200)
print (p4)

# 1.6 times slower
p5 = { key:prices[key] for key in prices.keys() & tech_names }
print (p5)




