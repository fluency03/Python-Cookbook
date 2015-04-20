#!/usr/bin/python
# 1.13. Sorting a List of Dictionaries by a Common Key
# Problem: You have a list of dictionaries and you would like to sort 
# the entries according to one or more of the dictionary values.

from operator import itemgetter

rows = [
	{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
	{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
	{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
	{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# rows is passed to sorted() function, which accepts a keyword argument key
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# The itemgetter() function can also accept multiple keys.
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
# If you give multiple indices to itemgetter(), the callable it produces 
# will return a tuple with all of the elements in it, and sorted() will 
# order the output according to the sorted order of the tuples.


rows_by_fname2 = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname2 = sorted(rows, key=lambda r: (r['lname'],r['fname']))

print (rows_by_fname2)
print (rows_by_lfname2)
# However, the solution involving itemgetter() typically runs a bit faster.


rows_min = min(rows, key=itemgetter('uid'))
rows_max = max(rows, key=itemgetter('uid'))

print (rows_min)
print (rows_max)
