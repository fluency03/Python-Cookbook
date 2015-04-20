#!/usr/bin/python
# 1.20. Combining Multiple Mappings into a Single Mapping
# Problem: You have multiple dictionaries or mappings that you want to logically combine into a
# single mapping to perform certain operations, such as looking up values or checking
# for the existence of keys.

from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b) # If there are duplicate keys, the values from the first mapping get used.


print (c['x'])
print (c['y'])
print (c['z'])
# a ChainMap simply keeps a list of the underlying mappings and 
# redefines common dictionary operations to scan the list
print (c, list(c.keys()), list(c.values()), len(c))

# Operations that mutate the mapping always affect the first mapping listed
c['z'] = 10
c['w'] = 40
print (c, a)

a['w'] = 30
print (c, a)

# KeyError: "Key not found in the first mapping: 'y'"
# del c['y']

# ------------------------------------------------------------------------

values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3

print (values['x'], values)
# Output: 3 ChainMap({'x': 3}, {'x': 2}, {'x': 1})


values = values.parents
print (values['x']) # Output: 2

# Discard last mapping
values = values.parents
values['x']

print (values) # Output: ChainMap({'x': 1})

# ------------------------------------------------------------------------

aa = {'x': 1, 'z': 3 }
ba = {'y': 2, 'z': 4 }

merged = dict(ba)
merged.update(aa)

print (merged, merged['x'], merged['y'], merged['z'])
# Output: {'x': 1, 'y': 2, 'z': 3} 1 2 3

# the changes don’t get reflected in the merged dictionary
a['x'] = 30
print (merged, merged['x'])
# Output: {'z': 3, 'y': 2, 'x': 1} 1