#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def quadratic(a, b, c):
	if a == 0:
		return "a can't be zero"
	elif (b *b - 4* a* c) < 0:
		return "此方程无解"
	else:
		x1 = (-b + math.sqrt(b *b - 4* a* c) / (2 * a))
		x2 = (-b + math.sqrt(b *b - 4* a* c) / (2 * a))
		return x1, x2
	
print(quadratic(0,1,1))
print(quadratic(3,8,1))
print(quadratic(3,1,4))