#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 断言 assert
# def foo(s):
# 	n = int(s)
# 	assert n != 0, 'n is zero!'
# 	return 10 / n
# 
# def main():
# 	foo('0')
# main()

# logging
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10/n)