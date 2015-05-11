#!/usr/bin/python
# 2.7. Specifying a Regular Expression for the Shortest
# Match
# Problem
# You’re trying to match a text pattern using regular expressions, but it is identifying the
# longest possible matches of a pattern. Instead, you would like to change it to find the
# shortest possible match.

import re

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print (str_pat.findall(text1)) # ['no.']

text2 = 'Computer says "no." Phone says "yes."'
# Greedy - Longest
print (str_pat.findall(text2)) # ['no." Phone says "yes.']


str_pat = re.compile(r'\"(.*?)\"')
# Nongreedy - shortest
print (str_pat.findall(text2)) # ['no.', 'yes.']

# Adding the ? right after operators such as * or + forces the matching 
# algorithm to look for the shortest possible match instead
