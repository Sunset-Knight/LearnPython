#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO, BytesIO

# StringIO
f = StringIO()
f.write('hello')
f.write(',')
f.write('world!')
print(f.getvalue())

f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f2.readline()
	if s == '':
		break
	print(s.strip())
	
# BytesIO
f3 = BytesIO()
f3.write('中国'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
f4.read()
print(f4.getvalue())