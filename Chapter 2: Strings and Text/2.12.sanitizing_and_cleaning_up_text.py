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
print (b.translate(cmb_chrs))

# ------------------------------------------------------------------------------------









