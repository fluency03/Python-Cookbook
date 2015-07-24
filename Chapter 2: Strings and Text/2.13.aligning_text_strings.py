#!/usr/bin/python
# 2.13. Aligning Text Strings
# Problem
# You need to format text with some sort of alignment applied.

text = 'Hello World'
print (text.ljust(20))
print (text.rjust(20))
print (text.center(20))

print (text.ljust(20, '='))
print (text.rjust(20, '*'))
print (text.center(20, '_'))

# format() function can also be used to easily align things. All you need 
# to do is use the < , > , or ^ characters along with a desired width.
print (format(text, '>20'))
print (format(text, '<20'))
print (format(text, '^20'))

# fill character other than a space
print (format(text, '=>20'))
print (format(text, '*<20'))
print (format(text, '_^20'))


# formatting multiple values
print ('{:>10} {:>10}'.format('Hello', 'World'))

# One benefit of format() is that it is not specific to strings. 
# It works with any value, making it more general purpose
x = 1.2345
print (format(x, '>10'))
print (format(x, '^10.3f'))









