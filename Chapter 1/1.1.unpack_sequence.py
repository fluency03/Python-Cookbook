#!/usr/bin/python
# 1.1. Unpacking a Sequence into Separate Variables
# Problem:
# You have an N-element tuple or sequence that you would like to unpack into a collection
# of N variables.

p = (4,5)
x, y = p

print x, '\n', y, 'z', p, '\n'

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data

print name, shares, price, date 

s = 'Hello'
a, b, _, d, e = s

print a, b, d, e 





