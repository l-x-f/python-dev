#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 高阶函数
f = abs


def func(f):
    print(f(-1000))
    return False


func(f)
list = [12, 3, 4, 5, 4, 48, 44, 8, 48, 45, 48, 4]


def odd(i):
    if (i % 2 == 0):
        return i
    else:
        return '哈哈'


li = map(odd, list)
for x in li:
    if (x):
        print(x)


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
def sum(x, y):
    return x + y


lis = reduce(sum, list)
print (lis)
