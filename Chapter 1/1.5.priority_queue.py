#!/usr/bin/python
# 1.5. Implementing a Priority Queue
# Problem:
# You want to implement a queue that sorts items by a given priority and always returns
# the item with the highest priority on each pop operation.

import heapq

class PriorityQueue:
	'''A queue with priority'''
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]


class Item:
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print (q._queue)

# sort the queue based on the valus in (-priority, self._index, item)
# first check first value - -priority, is it is the same, then check the next value
# the smaller the value is, the fronter the place within the sorted queue it can be
q._queue.sort()

print (q._queue)

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))

print (a<b)
print (a<c)





