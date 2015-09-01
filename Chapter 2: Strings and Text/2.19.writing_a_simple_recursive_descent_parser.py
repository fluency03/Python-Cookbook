#!/usr/bin/python
# 2.19. Writing a Simple Recursive Descent Parser
# Problem
# You need to parse text according to a set of grammar rules and perform actions or build
# an abstract syntax tree representing the input. The grammar is small, so you’d prefer to
# just write the parser yourself as opposed to using some kind of framework.

# start by having a formal specification of the grammar in the form of a BNF or EBNF

# BNF (Backus–Naur Form)
# expr ::= expr + term
# 	 |   expr - term
# 	 |   term

# term ::= term * factor
# 	 |   term / factor
# 	 |   factor

# factor ::= ( expr )
# 	   |   NUM

# or, EBNF (Extended Backus–Naur Form)
# expr ::= term { (+|-) term }*
# term ::= factor { (*|/) factor }*
# factor ::= ( expr )
	   # |   NUM


# various parsing, 
# expr
# expr ::= term { (+|-) term }*
# expr ::= factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM { (*|/) factor }* { (+|-) term }*
# expr ::= NUM { (+|-) term }*
# expr ::= NUM + term { (+|-) term }*
# expr ::= NUM + factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM { (*|/) factor}* { (+|-) term }*
# expr ::= NUM + NUM * factor { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM * NUM { (*|/) factor }* { (+|-) term }*
# expr ::= NUM + NUM * NUM { (+|-) term }*
# expr ::= NUM + NUM * NUM

import re 
import collections

# Token specifications
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MUNIS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

# Tokenizer
Token = collections.namedtuple('Token', ['type', 'value'])

def generate_tokens(text):
	scanner = master_pat.scanner(text)
	for m in iter(scanner.match, None):
		tok = Token(m.lastgroup, m.group())
		if tok.type != 'WS':
			print (tok)
			yield tok

output = generate_tokens('+ this is a good example 000 111 !!! + - * / () (  ) ')
print (list(output)) # [Token(type='PLUS', value='+')] only the first one is detected. 



# Parser
class ExpressionEvaluator:
	"""
	Implementation of a recursive descent parser. Each method implements 
	a single grammar rule. Use the ._accept() method to test and accept 
	the current lookahead token. Use the ._expect() method to exactly match 
	and discard the next token on on the input (or raise a SyntaxError 
	if it doesn't match).
	"""

	def parse(self, text):
		self.tokens = generate_tokens(text)
		self.tok = None			# Last symbol consumed
		self.nexttok = None 	# Next symbol tokenized
		self._advance()			# Load first lookahead token
		return self.expr()
	
	def _advance(self):
		'Advance one token ahead'
		self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

	def _accept(self, toktype):
		'Test and consume the next token if it matches toktype'
		if self.nexttok and self.nexttok.type == toktype:
			self._advance()
			return True
		else:
			return False

	def _expect(self, toktype):
		'Consume next token if it matches toktype or raise SyntaxError'
		if not self._accept(toktype):
			# used for raising your own errors.
			raise SyntaxError('Expected' + toktype) 

	# Grammar rules follow

	def expr(self):
		"expression ::= term { ('+'|'-') term }*"
		exprval = self.term()
		while self._accept('PLUS') or self._accept('MINUS'):
			op = self.tok.type
			right = self.term()
			if op == 'PLUS':
				exprval += right
			elif op == 'MINUS':
				exprval -= right
		return exprval

	def term(self):
		"term ::= factor { ('*'|'/') factor }*"
		termval = self.factor()
		while self._accept('TIMES') or self._accept('DIVIDE'):
			op = self.tok.type
			right = self.factor()
			if op == 'TIMES':
				termval *= right
			elif op == 'DIVIDE':
				termval /= right
		return termval

	def factor(self):
		"factor ::= NUM | ( expr )"
		if self._accept('NUM'):
			return int(self.tok.value)
		elif self._accept('LPAREN'):
			exprval = self.expr()
			self._expect('RPAREN')
			return exprval
		else:
			raise SyntaxError('Expected NUMBER or LPAREN')

e = ExpressionEvaluator()

print (e.parse('2'))
print (e.parse('3 + 10'))
print (e.parse('2 + 6 * 4'))
print (e.parse('5 + (7 + 1) * 2'))

# print (e.parse('5 + (7 + * 2)'))
# Traceback (most recent call last):
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 152, in <module>
#     print (e.parse('5 + (7 + * 2)'))
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 89, in parse
#     return self.expr()
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 116, in expr
#     right = self.term()
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 125, in term
#     termval = self.factor()
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 140, in factor
#     exprval = self.expr()
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 116, in expr
#     right = self.term()
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 125, in term
#     termval = self.factor()
#   File "2.19.writing_a_simple_recursive_descent_parser.py", line 144, in factor
#     raise SyntaxError('Expected NUMBER or LPAREN')
# SyntaxError: Expected NUMBER or LPAREN 


# -----------------------------------------------------------------------------------

class ExpressionTreeBuilder(ExpressionEvaluator):
	def expr(self):
		"expression ::= term { ('+'|'-') term }"
		exprval = self.term()
		while self._accept('PLUS') or self._accept('MINUS'):
			op = self.tok.type
			right = self.term()
			if op == 'PLUS':
				exprval = ('+', exprval, right)
			elif op == 'MINUS':
				exprval = ('-', exprval, right)
		return exprval

	def term(self):
		"term ::= factor { ('*'|'/') factor }*"
		termval = self.factor()
		while self._accept('TIMES') or self._accept('DIVIDE'):
			op = self.tok.type
			right = self.factor()
			if op == 'TIMES':
				termval = ('*', termval, right)
			elif op == 'DIVIDE':
				termval = ('/', termval, right)
		return termval

	def factor(self):
		"factor ::= NUM | ( expr )"
		if self._accept('NUM'):
			return int(self.tok.value)
		elif self._accept('LPAREN'):
			exprval = self.expr()
			self._expect('RPAREN')
			return exprval
		else:
			raise SyntaxError('Expected NUMBER or LPAREN')


e2 = ExpressionTreeBuilder()

print (e2.parse('2'))
print (e2.parse('3 + 10'))
print (e2.parse('2 + 6 * 4'))
print (e2.parse('5 + (7 + 1) * 2'))


# Discussion ---------------------------------------------------------------------

# It must walk from left to right over each part of the grammar rule, consuming tokens in 
# the process. In a sense, the goal of the method is to either consume the rule or 
# generate a syntax error if it gets stuck.

# • If the next symbol in the rule is the name of another grammar rule (e.g., term or
	# factor ), you simply call the method with the same name. "Descent" and "Recursive". 

# • If the next symbol in the rule has to be a specific symbol (e.g., ( ), you look at the
	# next token and check for an exact match.
	# Done by _expect()

# • If the next symbol in the rule could be a few possible choices (e.g., + or - ), you have
	# to check the next token for each possibility and advance only if a match is made.
	# Done by _accept()

# • For grammar rules where there are repeated parts (e.g., such as in the rule expr ::=
	# term { ('+'|'-') term }* ), the repetition gets implemented by a while loop.

# • Once an entire grammar rule has been consumed, each method returns some kind
	# of result back to the caller.
	# E.g., the final result


# One such limitation of recursive descent parsers is that they can’t be written for 
# grammar rules involving any kind of left recursion. 

# For example, 
# items ::= items ',' item
		# | item

# class TestItems(ExpressionEvaluator):
# 	def items(self):
# 		itemsval = self.items()
# 		if itemsval and self._accept(','):
# 			itemsval.append(self.item())
# 		else:
			# itemsval = [ self.item() ]

# e3 = TestItems()

# print (e3.items()) # RuntimeError: maximum recursion depth exceeded

# it blows up with an infinite recursion error.



# ------------------------------------------------------------------------------
# Using tools given for processing more complicated ones. 

from ply.lex import lex
from ply.yacc import yacc

# Token list
t_tokens = [ 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN' ]

# Ignored characters

t_ignore = '\t\n'

# Token specifications (as regexs)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Token processing functions
def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Error handler
def t_error(t):
	print ('Bad character: {!r}'.fromat(t.value[0]))
	t.skip(1)

# Build the lexer
lexer = lex()

# Grammar rules and handler functions
def p_expr(p):
	'''
	expr : expr PLUS term
		| expr MINUS term
	'''
	if p[2] == '+':
		p[0] = p[1] + p[3]
	elif p[2] == '-':
		p[0] = p[1] - p[3]

def p_expr_term(p):
	'''
	expr : term
	'''
	p[0] = p[1]

def p_term(p):
	'''
	term : term TIMES factor
		| term DIVIDE factor
	'''
	if p[2] == '*':
		p[0] = p[1] * p[3]
	elif p[2] == '/':
		p[0] = p[1] / p[3]

def p_term_factor(p):
	'''
	term : factor
	'''
	p[0] = p[1]

def p_factor(p):
	'''
	factor : NUM
	'''
	p[0] = p[1]

def p_factor_group(p):
	'''
	factor : LPAREN expr RPAREN
	'''
	p[0] = p[2]

def p_error(p):
	print ('Syntax error.')


parser = yacc()

print (parser.parse('2'))
print (parser.parse('2+3'))
print (parser.parse('2+(3+4)*5')) 

# ImportError: No module named 'ply'










