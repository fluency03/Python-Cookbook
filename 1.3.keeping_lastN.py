#!/usr/bin/python
# 1.3. Keeping the Last N Items
# Problem:
# You want to keep a limited history of the last few items seen during iteration or during
# some other kind of processing.

from collections import deque

def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
	with open('somefile.txt') as f:
		for line, prevlines in search(f, 'python', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)


