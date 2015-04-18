#!/usr/bin/python
# 1.7. Keeping Dictionaries in Order
# Problem:You want to create a dictionary, and you also want to control the order of items when
# iterating or serializing.

from collections import OrderedDict, defaultdict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 7
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
	print(key, d[key])

print (d)


import json
json.dumps(d)

print (d)
print (json.dumps(d))

# An OrderedDict internally maintains a doubly linked list that orders the keys according
# to insertion order. When a new item is first inserted, it is placed at the end of this list.
# Subsequent reassignment of an existing key doesn’t change the order.

# the size of an OrderedDict is more than twice as large as a normal 
# dictionary due to the extra linked list that’s created


d = defaultdict(int)
d['foo'] = 1
d['bar'] = 7
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
	print(key, d[key])

print (d)


import json
json.dumps(d)

print (d)
print (json.dumps(d))
