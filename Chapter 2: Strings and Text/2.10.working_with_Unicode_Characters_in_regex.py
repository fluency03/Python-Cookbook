#!/usr/bin/python
# 2.10. Working with Unicode Characters in Regular Expressions
# Problem
# You are using regular expressions to process text, but are concerned about the handling
# of Unicode characters.

import re

num = re.compile('\d+')
#ASCII digitals
numObj = num.match('123')
if numObj:
	print ('Match --> numObj.group():', numObj.group())
else:
	print ('Not match')
# Arabic digits\
numAra = num.match('\u0661\u0662\u0663')
if numAra:
	print ('Match --> numAra.group():', numAra.group())
else:
	print ('Not match')

# -------------------------------------------------------------------
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
#ASCII digitals
araObj = arabic.match('123')
if araObj:
	print ('Match --> araObj.group():', araObj.group())
else:
	print ('Not match')
# Arabic digits\
araUni = arabic.match('\u0661\u0662\u0663')
if araUni:
	print ('Match --> araUni.group():', araUni.group())
else:
	print ('Not match')


# -------------------------------------------------------------
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
patObj = pat.match(s)
if patObj:
	print ('Match --> patObj.group():', patObj.group())
else:
	print ('Not match')

patUp = pat.match(s.upper())
if patUp:
	print ('Match --> patUp.group():', patUp.group())
else:
	print ('Not match')
print ('s.upper():', s.upper())

