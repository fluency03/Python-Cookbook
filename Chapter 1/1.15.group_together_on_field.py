#!/usr/bin/python
# 1.15. Grouping Records Together Based on a Field
# Problem: You have a sequence of dictionaries or instances and you want to iterate over the data
# in groups based on the value of a particular field, such as date.

from operator import itemgetter
from itertools import groupby

# To iterate over the data in chunks grouped by date. 
# First, sort by the desired field (in this case, date) and 
# then use itertools.groupby():

rows = [
	{'address': '5412 N CLARK', 'date': '07/01/2012'},
	{'address': '5148 N CLARK', 'date': '07/04/2012'},
	{'address': '5800 E 58TH', 'date': '07/02/2012'},
	{'address': '2122 N CLARK', 'date': '07/03/2012'},
	{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
	{'address': '1060 W ADDISON', 'date': '07/02/2012'},
	{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
	{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
print (rows)

#The oder of keys within the list of a dictionaries is random.  
for date, items in groupby(rows, key=itemgetter('date')):
	print(date)
	for i in items:
		print('	', i)
# The order varies not because you've added a line of code, 
# but because of hash randomization. Implementing hash randomization 
# mitigates DoS attacks using broken sequences of tens of thousands 
# of values that hash to the same value in e.g. a HTTP POST request.

from collections import defaultdict

rows_by_date = defaultdict(list)

for row in rows:
	rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
	print(r)

# For this latter example, it’s not necessary to sort the records first. 
# Thus, if memory is no concern, it may be faster to do this than to first 
# sort the records and iterate using groupby().

