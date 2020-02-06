#!/usr/bin/env python3
# 输入十个数，求和，求平均
N=10
sum = 0
count = 0
print("please input 10 numbers: ")
while count < N:
    number =float(input())
    sum = sum + number
    count = count +1
average = sum / N
print('N={},Sum={}'.format(N,sum))
print('Average = {:.2f}'.format(average)) 
