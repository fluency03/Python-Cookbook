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

































