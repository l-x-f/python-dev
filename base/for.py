#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# range(1000)函数，可以生成一个整数序列 a=[0,1,2.....,998,999]
a=(range(101))
sum=0
for item in a:
    sum+=item
print (sum)


L = ['Bart', 'Lisa', 'Adam']
n=0
while n<=2:
    if n==1:
        # 在循环中，break语句可以提前退出循环
        break
    print ('hello: '+L[n])
    n=n+1
