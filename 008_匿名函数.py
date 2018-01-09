#!/usr/bin/env python3
# -*- coding:utf-8 -*-

L1 = list(map(lambda x:x * x, [1, 2, 3, 4, 5, 6]))
print(L1)

f = lambda x:x * x
print(list(map(f, [1, 2, 3, 4])))

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
L = list(filter(lambda n: n%3 == 2, range(1, 20)))
print(L)
