#!/usr/bin/python
# 2.8. Writing a Regular Expression for Multiline Patterns
# Problem
# You’re trying to match a block of text using a regular expression, but you need the match
# to span multiple lines.

import re

comment = re.compile(r'/\*(.*?)\*/')

text1 = '/* this is a comment */'
text2 = '''/* this is a
			multiline comment */ '''

print (comment.findall(text1)) # [' this is a comment ']
print (comment.findall(text2)) # []
# this is becuase  dot (.) to match any character but doesn’t match newlines

comment_n = re.compile(r'/\*((?:.|\n)*?)\*/')
print (comment_n.findall(text2)) # [' this is a\n\t\t\tmultiline comment ']

# (?:.|\n) specifies a noncapture group (i.e., it defines a group for the
# purposes of matching, but that group is not captured separately or numbered)

# re.DOTALL
comment_all = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print (comment_all.findall(text2)) # [' this is a\n\t\t\tmultiline comment ']

# Using the re.DOTALL flag works fine for simple cases, but might be problematic 
# if you’re working with extremely complicated patterns or a mix of separate regular 
# expressions that have been combined together for the purpose of tokenizing