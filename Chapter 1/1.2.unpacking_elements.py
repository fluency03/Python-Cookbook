#!/usr/bin/python
# 1.2. Unpacking Elements from Iterables of Arbitrary Length
# Problem:
# You need to unpack N elements from an iterable, but the iterable may be longer than N
# elements, causing a "too many values to unpack" exception.

def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)

def avg(number):
    total = 0
    for a in number:
        total += a
    return total/len(number)

grades = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print (drop_first_last(grades))


#-----------------------------------------------------------------------


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print (name, email, phone_numbers)


#------------------------------------------------------------------------


def avg_comparison(average, current):
	if average == current:
		return True
	else:
		return False


*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

trailing_avg = sum(trailing) / len(trailing)
print (avg_comparison(trailing_avg, current))


#------------------------------------------------------------------------


records = [
	('foo', 1, 2),
	('bar', 'hello'),
	('foo', 3, 4),
]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar',s)

for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)


#------------------------------------------------------------------------


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print ('\n', uname, homedir, sh, '\n', *fields)
#Only allow a starred expression as the last item in the exprlist. 
#This would simplify the unpacking code a bit 
#and allow for the starred expression to be assigned an iterator. 
#This behavior was rejected because it would be too surprising.


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

print (name, year)


items = [1, 10, 7, 4, 5, 9]
head, *tail = items

print (head, *tail)


#------------------------------------------------------------------------


def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head
# if tail:
#    return head + sum(tail)
# else:
#    return head

print (sum(items))










