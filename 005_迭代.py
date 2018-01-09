#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 输入一个list 返回最大值和最小值
def findMinAndMax(L):
	max = L[0]
	min = L[0]
	for i in L:
		if i < min:
			min = i
		if i > max:
			max = i
	return max, min

t = findMinAndMax([99, 891, 2, 9, 0, 3, -4, 5, 6])
print(t)

# 扬辉三角
def pascal_triangle(n):
	i, l = 0, [1]
	for x in range(n):
		print(l)
		l = [1]  + [l[i] + l[i + 1]for i in range(len(l)-1)] + [1]
		
pascal_triangle(5)