#!/usr/bin/python
# 1.14. Sorting Objects Without Native Comparison Support
# Problem: You want to sort objects of the same class, 
# but they don’t natively support comparison operations.

from operator import attrgetter

# For example, if you have a sequence of User instances in your application, 
# and you want to sort them by their user_id attribute, you would supply a 
# callable that takes a User instance as input and returns the user_id.

class User:
	def __init__(self, user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print (users) # [User(23), User(3), User(99)]

users_sorted = sorted(users, key=lambda u: u.user_id)
print (users_sorted) # [User(3), User(23), User(99)]


# However, attrgetter() is often a tad bit faster and also has the added
# feature of allowing multiple fields to be extracted simultaneously.
users_sorted2 = sorted(users, key=attrgetter('user_id'))
print (users_sorted2) # [User(3), User(23), User(99)]

# Example: by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

users_min = min(users, key=attrgetter('user_id')
users_max = max(users, key=attrgetter('user_id')







