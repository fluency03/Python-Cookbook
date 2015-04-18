#!/usr/bin/python
# 1.11. Naming a Slice
# Problem: Your program has become an unreadable mess of 
# hardcoded slice indices and you want to clean it up.



###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25   ..........'  
cost = int(record[20:32]) * float(record[40:48])

print (cost)

# name the slices
SHARES = slice(20,32)
PRICE = slice(40,48)

cost = int(record[SHARES]) * float(record[PRICE])
print (cost)




items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)

print (items[2:4])
print (items[a])

items[a] = [10,11]
print (items)

del items[a]
print (items)


a = slice(5, 50, 2)
print (a.start, a.stop, a.step)


s = 'HelloWorld'
indice = a.indices(len(s))
print (indice)

for i in range(*a.indices(len(s))):
	print(s[i])

