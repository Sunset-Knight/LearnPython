#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def trim(s):
	if s[0] == ' ':
		s = s[1:]
		print('..')
	if s[-1] == ' ':
		s = s[:-2]
	return s
s = '123 4566 '
trim(s)
print(s)