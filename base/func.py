#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
# 内置函数
a=max(0,1,2,3,4,56,8,541,2,1,2)
print (a)
b=min(0,1,2,3,4,56,8,541,2,1,2)
print (b)
print (bool(0))
print (abs(-100))

# 把一个整数转换成十六进制表示的字符串：
print (hex(100))


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#添加默认参数
def func(a,b=0,c=0):
    s= a+b+c
    print (s)
    return math.sqrt(s)
func(2,3,0)
print (func(100,100,100))
print ('----------------')
print (func(0))

#添加可变参数
def fun(*args):
    mut=1
    for item in args:
        mut=item*mut
    print('-------------')
    print(mut)
list=(0,1,23,45,6)
fun(1,23,45,6)
# 可变参数是一个tuple
list2=(1,10,100,45)
fun(*list2)

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n + fact(n - 1)
print (fact(10))