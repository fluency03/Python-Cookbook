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
print('\n')

# Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and
# the queue is full, the oldest item is automatically removed. 
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print (q)

q.append(4)
print (q)

q.append(5)
print (q)

q.appendleft(4)
print (q)
q.pop()
print (q)
q.popleft()
print (q)





# Three Examples: Read each line in a file
# Example1: 
f = open("test.txt")             # 返回一个文件对象  
line = f.readline()             # 调用文件的 readline()方法  
while line:  
    print (line, end='')                 # 后面跟 ',' 将忽略换行符  
    # print(line, end = '')　　　# 在 Python 3中使用  
    line = f.readline()  

f.close()  
print('\n')

# Example2: 
for line in open("test.txt"):  
    print (line, end='')
print('\n')

# Example3: 
f = open("test.txt")  
lines = f.readlines()#读取全部内容  
for line in lines:  
    print (line, end='')
print('\n')

