#!/usr/bin/python
# 1.6. Mapping Keys to Multiple Values in a Dictionary
# Problem:
# You want to make a dictionary that maps keys to more than one value (a so-called
# “multidict”).

d = {
	'a' : [1, 2, 3],
	'b' : [4, 5]
}
e = {
	'a' : {1, 2, 3},
	'b' : {4, 5}
}


# To easily construct such dictionaries, 
# use defaultdict in the collections module. 
from collections import defaultdict
# it automatically initializes the first value so
# you can simply focus on adding items
d = defaultdict(list)
d['a'].append(2)
d['a'].append(3)
d['a'].append(1)
d['b'].append(4)

print (d)


d = defaultdict(set)

d['a'].add(5)
d['a'].add(6)
d['b'].add(7)

print (d)


d = {}
 # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
d['a'].append(8)

print (d)

pairs = [('h', 10), ('j', 20),('k', 30)]


d = {}
for key, value in pairs:
	if key not in d:
		d[key] = []
	d[key].append(value)
print (d)


d = defaultdict(list)
for key, value in pairs:
	d[key].append(value)
print (d)




