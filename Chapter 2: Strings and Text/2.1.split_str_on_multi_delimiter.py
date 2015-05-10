#!/usr/bin/python
# 2.1. Splitting Strings on Any of Multiple Delimiters
# Problem: You need to split a string into fields, but the delimiters (and spacing around them) 
# aren’t consistent throughout the string.

# split() method of string objects is really meant for very simple cases, and 
# does not allow for multiple delimiters or account for possible whitespace 
# around the delimiters

line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
# r'[;,\s]\s*'   ; or , or ' ' plus a ' ' with amount of nature number
split_line = re.split(r'[;,\s]\s*', line)

# as shown in the solution, the separator is either a comma (,),semicolon (;), 
# or whitespace followed by any amount of extra whitespace. 
print (split_line)

new_line = line.replace(',',' ').replace(';',' ').split()
print (new_line)

# --------------------------------------------------------------------------

fields = re.split(r'(;|,|\s)\s*', line)
print (fields) # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

values = fields[0:-1:2]
delimiters = fields[1::2] + ['']

print (values) # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print (delimiters) # [' ', ';', ',', ',', ',', '']


joined = ''.join(v+d for v,d in zip(values, delimiters))
print (joined)

another_line = re.split(r'(?:,|;|\s)\s*', line)
print (another_line)