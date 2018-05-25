#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
list=[x * x for x in range(1, 11)]
print (list)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

li={x**x   for x in range(10) if x % 2 == 0}
li2=[x**x   for x in range(10) if x % 2 == 0]
print (li)
print (li2)
L = ['Hello', 'World', 18, 'Apple', None]
child=[s.lower() for s in L if isinstance(s, str)]
print (child)

