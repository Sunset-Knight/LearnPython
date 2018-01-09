#!/usr/bin/env python3
# -*- coding:utf-8 -*-

f = open('/home/walter/spf13-vim.sh', 'r')
f.read()
f.close()

try:
	f = open('/home/walter/spf13-vim.sh', 'r')
	print(f.read())
finally:
	if f:
		f.close()
		
with open('/home/walter/spf13-vim.sh', 'r') as f:
	print(f.read())
	
f = open('/home/walter/spf13-vim.sh', 'r')
for line in f.readlines():
	print(line.strip()) #删除末尾的'\n'
	
with open('/home/walter/test.txt', 'a', encoding='utf-8', errors='ignore') as f:
	f.write('hello, world!2\n')