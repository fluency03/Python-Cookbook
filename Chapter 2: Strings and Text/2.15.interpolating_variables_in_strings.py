#!/usr/bin/python
# 2.15. Interpolating Variables in Strings
# Problem
# You want to create a string in which embedded variable names are substituted with a
# string representation of a variable’s value.


s = '{name} has {n} messages.'
message = s.format(name='Guido', n=88)
print (message)

# Alternatively, if the values to be substituted are truly found in variables, 
# use the combination of format_map() and vars()
name = 'Guido'
n = 99
mess = s.format_map(vars())
print (mess)


# vars() also works with instances
class Info:
	def __init__(self, name, n):
		self.name = name
		self.n = n

a = Info('Guido', 100)
messa = s.format_map(vars(a))
print (messa)

# format() and format_map() is that they do not deal gracefully with missing values
# s.format(name='Guido')
# Traceback (most recent call last):
  # File "2.15.interpolating_variables_in_strings.py", line 31, in <module>
    # s.format(name='Guido')
# KeyError: 'n' 

# define an alternative dictionary class with a __missing__() method
class safesub(dict):
	def __missing__(self, key):
		return '{' + key + '}'

del n 	# Make sure n is undefined
mess_miss = s.format_map(safesub(vars()))
print (mess_miss)


# hide the variable substitution process behind a small utility 
# function that employs a so-called “frame hack”
import sys

def sub(text):
	return text.format_map(safesub(sys._getframe(1).f_locals))
# sub() function uses sys._getframe(1) to return the stack frame of the caller
# f_locals attribute is accessed to get the local variables

name = 'Guido'
n = 55
print (sub('Hello {name}.'))
print (sub('You have {n} messages.'))
print (sub('Your favorite color is {color}.'))



# in Python, lack of true variable interpolation 
# Alternatively
import string

s = string.Template('$name has $n messages.')
subs = s.substitute(vars())
print (subs)

# vars():默认打印当前模块的所有属性(__dict__)，如果传一个对象参数则打印当前对象的属性 
print (vars())











