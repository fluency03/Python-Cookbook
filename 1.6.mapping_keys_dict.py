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



from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print (d)

d = defaultdict(set)











