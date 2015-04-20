#!/usr/bin/python
# 1.12. Determining the Most Frequently Occurring Items in a Sequence
# Problem:
# You have a sequence of items, and you’d like to determine the most frequently occurring items in the sequence.

words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]


not_counter = word_counts['not']
print (not_counter)

eyes_counter= word_counts['eyes']
print (eyes_counter)

# To increment the count manually
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
	word_counts[word] += 1

eyes_counter = word_counts['eyes']
print (eyes_counter)

word_counts.update(morewords)
eyes_counter = word_counts['eyes']
print (eyes_counter)

# Counter instances is that they can be easily combined using
# various mathematical operations
a = Counter(words)
b = Counter(morewords)

print (a)
print (b)

c = a + b
print (c)

d = a - b
print (d)

