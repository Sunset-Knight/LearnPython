#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
if re.match(r'^\d{3}\-\d{3,8}','011-99999'):
	print('yes')
else:
	print('None')
test = '用户输入的字符串'

if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

# 切分字符串
l = 'a b  c'.split(' ')
print(l)
l = re.split(r'\s+','a b  c')
print(l)
print(re.split(r'[\s\,\;]+', 'a b  c,;d'))
t = '23:59:59'
m = re.match(r'(0[0-9]|1[0-9]|2[0-3]|[0-9])\:([0-5][0-9]|[0-9])\:([0-][0-9]|[0-9])', t)

print(m.groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# 预编译正则表达式
re_telephone = re.compile(r'(\d{3})-(\d{3,8})')
print(re_telephone.match('010-9999').groups())

# 练习1
def is_vaild_email(addr):
	re_emailaddr = re.compile(r'^([\_a-zA-Z]{1}[\_\.0-9a-zA-Z]*)\@([0-9a-zA-Z]+)\.([a-zA-Z]+)$')
	r = re_emailaddr.match(addr)
	if r:
		print(r.groups())
		return r
	else:
		print('failed')
is_vaild_email('mou222@22.com')
assert is_vaild_email('somone@gmail.com')
assert is_vaild_email('bill.gates@microsoft.com')
assert not is_vaild_email('bobb#example.com')
assert not is_vaild_email('mi-bob@example.com')
print('ok')
# 练习2
def name_of_email(addr):
	re_emailaddr = re.compile(r'^\<?([\w\s]+)|([\_a-zA-Z]{1}[\_a-zA-Z0-9]*)\>?\@([0-9a-zA-Z]+)\.([a-zA-Z]+)$')
	r = re_emailaddr.match(addr)
	if r :
		print(r.group(1))
		return r.group(1)
	else:
		print('failed.')
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
