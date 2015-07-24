#!/usr/bin/python
# 2.12. Sanitizing and Cleaning Up Text
# Problem
# Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page
# and you’d like to clean it up somehow.

s = 'pýtĥöñ\fis\tawesome\r\n'
print (s)

remap = {
	ord('\t'): ' ',
	ord('\f'): ' ',
	ord('\r'): None
}
a = s.translate(remap)
print (a)


# remove all combining characters
import unicodedata
import sys
# fromkeys() creates a new dictionary with keys from seq and values set to value
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
						 if unicodedata.combining(chr(c)))
# normalized into a decomposed form
b = unicodedata.normalize('NFD', a)
print (b)
# mapping every Unicode combining character to None
# the translate function is used to delete all of the accents.
print (b.translate(cmb_chrs))

# ------------------------------------------------------------------------------------

# Given a string representing one Unicode character, return an integer representing the Unicode code 
# point of that character. For example, ord('a') returns the integer 97 and ord('\u2020') returns 8224. 
# This is the inverse of chr().
print (ord('a'), ord('0'), ord('.'))
print (chr(88), chr(66), chr(77))

# maps all Unicode decimal digit
# characters to their equivalent in ASCII
digitmap = {
	c: ord('0') + unicodedata.digit(chr(c))
	for c in range(sys.maxunicode)
	if unicodedata.category(chr(c)) == 'Nd'
}

print (len(digitmap))
# print (digitmap)

# Arabic digits
x = '\u0661\u0662\u0665'
print (x.translate(digitmap))

# first do some preliminary cleanup of the text, and then run it through 
# a combination of encode() or decode() operations to strip or alter it
print (b.encode('ascii', 'ignore').decode('ascii'))
# print (b.encode('ascii', 'ignore'))


# As a general rule, the simpler it is, the faster it will run.
# the str.replace() method is often the fastest approach
def clean_spaces(s):
	s = s.replace('\r', '')
	s = s.replace('\t', ' ')
	s = s.replace('\f', ' ')
	return s

print (clean_spaces(a))




