#!/usr/bin/python
# 2.2. Matching Text at the Start or End of a String
# Problem
# You need to check the start or end of a string for specific text patterns, such as filename
# extensions, URL schemes, and so on.

filename = 'spam.txt'

print (filename.endswith('.txt'))
print (filename.startswith('file:'))

url = 'http://www.python.org'
print (url.startswith('http:'))

# --------------------------------------------------------------------------

import os 
filenames = os.listdir('.')
print (filenames)

pyname = [name for name in filenames if name.endswith(('.py', '.h')) ]
print (pyname)

print (any(name.endswith('.py') for name in filenames))

# --------------------------------------------------------------------------

from urllib.request import urlopen

def read_data(name):
	if name.startswith(('http:', 'https:', 'ftp:')):
		return urlopen(name).read()
	else:
		with open(name) as f:
			return f.read()

# url_file = open('url.txt', 'wb')
# url_file.write(read_data(url))
# url_file.close()

# print (read_data(url)) 


# If you happen to have the choices specified in a list or set, just make sure 
# you convert them using tuple() first. 
choices = ['http:', 'ftp:', 'https:']
# url.startswith(choices)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: startswith first arg must be str or a tuple of str, not list
print (tuple(choices))
print (url.startswith(tuple(choices)))

import re
url_http = re.match('http:|https:|ftp:', url)
print (url_http)

#  this statement that checks a directory for the presence of certain kinds of files:
# if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
