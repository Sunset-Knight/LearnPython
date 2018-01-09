#ďź/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	return r

def bar():
	r = foo()
	if r == (-1):
		print('Error')
	else:
		pass
	
# try

try:
	print('try...')
	r = 10 / 1
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')

# 2
try:
	print('try...')
	r = 10/ int('2')
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError', e)
else:
	print('no error!')
finally:
	print('finally...')
print('END')


# 解读错误信息
def foo(s1):
	return 10/ int(s1)

def bar(s2):
	return foo(s2) *2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print('END')