#!/usr/bin/python
# 1.9. Finding Commonalities in Two Dictionaries
# Problem: You have two dictionaries and want to find out 
# what they might have in common (same keys, same values, etc.).


a = {
	'x': 1,
	'y': 2,
	'z': 3
}

b = {
	'w': 20,
	'x': 11,
	'y': 2
}

# support common set operations such as unions, intersections,and differences
# Find keys in common
common_keys = a.keys() & b.keys() # { 'x', 'y' }
print (common_keys)

# Find keys in a that are not in b
diff_keys = a.keys() - b.keys() # { 'z' }
print (diff_keys)

# Find (key,value) pairs in common
# The items() method of a dictionary returns an items-view object 
# consisting of (key,value) pairs.
common_pairs = a.items() & b.items() # { ('y', 2) }
print (common_pairs)

# alter or filter dictionary contents
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}} 
# make a new dictionary with selected keys removed
# c is {'x': 1, 'y': 2}
print (c)

 # the values() method of a dictionary does not support the set operations




