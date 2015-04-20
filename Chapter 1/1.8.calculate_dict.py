#!/usr/bin/python
# 1.8. Calculating with Dictionaries
# Problem
# You want to perform various calculations (e.g., minimum value, maximum value, 
# sorting, etc.) on a dictionary of data.

prices = {
	'ACME': 45.23,
	'AAPL': 612.78,
	'IBM': 205.55,
	'HPQ': 37.20,
	'FB': 10.75
}

# invert the keys and values of the dictionary using zip()
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
print (min_price)

max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
print (max_price)

# In Python 3, zip() returns an iterator instead of a list.
prices_zip = zip(prices.values(), prices.keys())
print (prices_zip)
print (list(prices_zip))

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
# 					(45.23, 'ACME'), (205.55, 'IBM'),
# 					(612.78, 'AAPL')]
print (prices_sorted)

# ------------------------------------------------------------------

print(min(prices)) # Returns 'AAPL'
print(max(prices)) # Returns 'IBM'

print(min(prices.values())) # Returns 10.75
print(max(prices.values())) # Returns 612.78

print(min(prices, key=lambda k: prices[k])) # Returns 'FB'
print(max(prices, key=lambda k: prices[k])) # Returns 'AAPL'

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)

# zip() solves the problem by “inverting” the dictionary into a
# sequence of (value, key) pairs. When performing comparisons on such tuples, 
# the value element is compared first, followed by the key.


