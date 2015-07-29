#!/usr/bin/python
# 2.17. Handling HTML and XML Entities in Text
# Problem
# You want to replace HTML or XML entities such as &entity; or &#code; with their
# corresponding text. Alternatively, you need to produce text, but escape certain charac‐
# ters (e.g., < , > , or & ).

import html

s = 'Elements are written as "<tag>text</tag>".'
print (s)
print (html.escape(s))

# Disable escaping of quotes
print (html.escape(s, quote=False))

# -------------------------------------------------------------------
# emit text as ASCII and want to embed character code entities for 
# non-ASCII characters, you can use the errors='xmlcharrefreplace'
d = 'Spicy Jalapeño'
dn = d.encode('ascii', errors='xmlcharrefreplace')
print (dn)

# -------------------------------------------------------------------
from html.parser import HTMLParser
t = 'Spicy &quot;Jalape&#241;o&quot.'
p = HTMLParser()
print (p.unescape(t))


n = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print (unescape(n))


# If you’re actually processing HTML or XML, try using a proper HTML or XML parser first.









