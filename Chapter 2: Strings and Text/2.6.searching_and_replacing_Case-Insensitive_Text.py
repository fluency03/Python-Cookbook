#!/usr/bin/python
# 2.6. Searching and Replacing Case-Insensitive Text
# Problem
# You need to search for and possibly replace text in a case-insensitive manner.

import re

text = 'UPPER PYTHON, lower python, Mixed PyThon'

findall = re.findall('python', text, flags=re.IGNORECASE)
print (findall)

sub = re.sub('python', 'snake', text, flags=re.IGNORECASE)
# This example reveals a limitation that replacing text won’t match 
# the case of the matched text.
print (sub)

# new matchcase function
def matchcase(word):
	def replace(m):
		text = m.group()
		if text.isupper():
			return word.upper()
		elif text.islower():
			return word.lower()
		else:
			temp = word[:]
			for i in range(len(text)):
				if text[i].isupper():
					temp = temp[:i] + temp[i].upper() + temp [i+1:]
			return temp
			# return word
	return replace

sub_new = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print (sub_new)

