#!/usr/bin/python
# 1.4. Finding the Largest or Smallest N Items
# Problem:
# You want to make a list of the largest or smallest N items in a collection.

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print (heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print (heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
# Similarly, if N is about the same size as the collection itself, 
# it is usually faster to sort it first and take a slice (i.e.,
# use sorted(items)[:N] or sorted(items)[-N:]).


# converting the data into a list where items are ordered as a heap
heap = list(nums)
print (heap)

heapq.heapify(heap)
print (heap)

print (heapq.heappop(heap))
print (heap)

# If you are simply trying to find the single smallest
# or largest item (N=1), it is faster to use min() and max().
print (max(heap))
print (min(heap))

# sorted() generates a new list. 
heap_sorted = sorted(heap)
print (heap_sorted)

# .sort() modify the existing list
heap.sort()
print (heap)

nums_q = str(nums)[1:-1]
print (nums_q)


portfolio = [
	{'name': 'IBM', 'shares': 100, 'price': 91.1},
	{'name': 'AAPL', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09},
	{'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YHOO', 'shares': 45, 'price': 16.35},
	{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(1, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(1, portfolio, key=lambda s: s['price'])

cheap_q = str(cheap)[1:-1]


print (cheap_q, expensive)




