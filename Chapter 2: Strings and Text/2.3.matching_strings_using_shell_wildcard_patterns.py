#!/usr/bin/python
# 2.3. Matching Strings Using Shell Wildcard Patterns
# Problem
# You want to match text using the same wildcard patterns as are commonly used when
# working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).

from fnmatch import fnmatch, fnmatchcase

print (fnmatch('foo.txt', '*.txt'))
print (fnmatch('foo.txt', '?oo.txt'))
print (fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
name_data = [name for name in names if fnmatch(name, 'Dat*.csv')]
print (name_data)

# This gives False.   
print ( fnmatch('foo.txt', '*.TXT'))

addresses = [
	'5412 N CLARK ST',
	'1060 W ADDISON ST',
	'1039 W GRANVILLE AVE',
	'2122 N CLARK ST',
	'4802 N BROADWAY',
]

ad_ST = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print (ad_ST)

ad_CLARK = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print (ad_CLARK)

