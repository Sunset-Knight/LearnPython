#/usr/bin/env python3
# -*- coding:utf-8 -*-

names = ['Micael', 'Adam', 'Jesseca']
for name in names:
	print(name)

# for in 枚举
sum = 1
for x in range(1,101):
	sum = sum * x
	print(sum)
print(sum)

# while 循环
sum = 0
n = 99
while n > 0:
	sum = sum + n
	print(n)
	n = n-2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print(name)

while L:
	print(L[0])
	L.pop(0)
	
n = 1
while n < 100:
	if n > 10:
		break
	print(n)
	n = n + 1
	
n = 0
while n < 100:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)
	
L = []
n = 1
while n < 100:
	L.append(n)
	n = n +2

print(L)