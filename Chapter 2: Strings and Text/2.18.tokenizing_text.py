#!/usr/bin/python
# 2.18. Tokenizing Text
# Problem
# You have a string that you want to parse left to right into a stream of tokens.

text = 'foo = 23 + 42 * 10'
# To tokenize the string, turn the string into a sequence of pairs, like this:
tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
			('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# To do this kind of splitting, the first step is to define all of the possible tokens, 
# including whitespace, by regular expression patterns using named capture groups such as: 
import re

# the ?P<TOKENNAME> convention is used to assign a name to the pattern
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
print (master_pat)

# The scanner method is used to create a scanner object and attach it to a string. 
# This object keeps track of the current position, and moves forward after each successful match. 
# Instead of keeping track of the position yourself, just call the scanner over and over again.
scanner = master_pat.scanner('foo = 42')

# print (scanner.match())
match1 = scanner.match() 
print (match1) # <_sre.SRE_Match object; span=(0, 3), match='foo'>
print (match1.lastgroup, match1.group()) # NAME foo

match2 = scanner.match() 
print (match2) # <_sre.SRE_Match object; span=(3, 4), match=' '>
print (match2.lastgroup, match2.group()) # WS 

match3 = scanner.match()
print (match3) # <_sre.SRE_Match object; span=(4, 5), match='='>
print (match3.lastgroup, match3.group()) # EQ =

match4 = scanner.match()
print (match4) # <_sre.SRE_Match object; span=(5, 6), match=' '>
print (match4.lastgroup, match4.group()) # WS 

match5 = scanner.match()
print (match5) # <_sre.SRE_Match object; span=(6, 8), match='42'>
print (match5.lastgroup, match5.group()) # NUM 42

# match6 = scanner.match()
# print (match6) # None
# print (match6.lastgroup, match6.group()) # error


# -------------------------------------------------------------------------------------
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat,text):
	scanner = pat.scanner(text)
	for m in iter(scanner.match, None):
		yield Token(m.lastgroup, m.group())

# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
	print (tok)

# print output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')


# -------------------------------------------------------------------------------------

# filter the token stream, you can either define more generator functions or use a generator expression
# filter out all whitespace tokens
tokens = (tok for tok in generate_tokens(master_pat, text)
			if tok.type != 'WS')

for tok in tokens:
	print (tok, (tok.type, tok.value))

# print output:
# Token(type='NAME', value='foo')
# Token(type='EQ', value='=')
# Token(type='NUM', value='23')
# Token(type='PLUS', value='+')
# Token(type='NUM', value='42')
# Token(type='TIMES', value='*')
# Token(type='NUM', value='10')

# -------------------------------------------------------------------------------------

# 1. must make sure that you identify every possible text sequence that might appear in the 
# input with a correponding re pattern. If any nonmatching text is found, scanning simply stops. 
# This is why it was necessary to specify the whitespace ( WS ) token in the example.

# 2. order of tokens in the master regular expression also matters. 
# When matching, re tries to match pattens in the order specified. 

# If a pattern happens to be a substring of a longer pattern, 
# you need to make sure the longer pattern goes first. For example: 

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pattern = re.compile('|'.join([LE, LT, EQ]))  # Correct
# master_pattern = re.compile('|'.join([LT, LE, EQ])) # Incorrect

# Because it would match the text <= as the token LT followed by the token EQ, 
# not the single token LE , as was probably desired.

# 3. watch out for patterns that form substrings
PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_patt = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_patt, 'printerprintaaaa print'):
	print (tok)

# Outputs:
# Token(type='PRINT', value='print')
# Token(type='NAME', value='erprintaaaa')

# because of no whitespace in master_patt, the last print will be ignored after a space. 






