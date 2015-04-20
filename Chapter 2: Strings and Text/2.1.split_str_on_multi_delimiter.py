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

print (split_line)






