#!/usr/bin/python
# 2.9. Normalizing Unicode Text to a Standard Representation
# Problem
# You’re working with Unicode strings, but need to make sure that all of the strings have
# the same underlying representation.

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print (s1, s2)
print (ascii(s1), ascii(s2))

import unicodedata

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print (t1, t2)
print (ascii(t1), ascii(t2))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print (t3, t4)
print (ascii(t3), ascii(t4))