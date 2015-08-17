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

import re 
import collections

# Token specifications
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MUNIS>\-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\())'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN, WS]))

# Tokenizer
Token = collections.namedtuple('Token', ['name', 'value'])














