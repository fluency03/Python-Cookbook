#!/usr/bin/python
# 1.10. Removing Duplicates from a Sequence while Maintaining Order
# Problem: You want to eliminate the duplicate values in a sequence, 
# but preserve the order of the remaining items.


def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

# Iterating over the list and the generator looks completely the same. 
# However, although the generator is iterable, it is not a collection, 
# and thus has no length. Collections (lists, tuples, sets, etc) keep 
# all values in memory and we can access them whenever needed. 
# A generator calculates the values on the fly and forgets them, 
# so it does not have any overview about the own result set.

a = [1, 5, 2, 1, 9, 1, 5, 10]
print (list(dedupe(a)))


print (set(a))
# this approach doesn’t preserve any kind of ordering
print (a)

# To eliminate duplicates in a sequence of unhashable types (such as dicts)
def dedupe(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

xy = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print (xy)

x = list(dedupe(a, key=lambda d: d['x']))
print (x)

with open('somefile.txt','r') as f:
	for line in dedupe(f):
		print (line)
