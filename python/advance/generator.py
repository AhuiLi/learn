#-*- coding:utf-8 -*-

# 生成器是通过一种算法实现一边使用一边计算接下来的值的机制
# 在python中成为生成器，generator。
# 定义方式：
# 1. 列表生成式稍加修改，把[]改为()

L = [x+x for x in range(10)]
g = (x+x for x in range(10))

# print(next(g))

# 2. 复制的生成器用生成式无法表达，用函数实现

# 普通函数（斐波拉切数列）
def fib(max):
    n, a, b =  0, 0, 1
    while n<max:
        print(b)
        a, b = b, a+b
        n = n+1
    return 'done'
# fib(4)
#======================
#函数中包含yield 就不是普通函数，而是generator
def fib(max):
    n, a, b =  0, 0, 1
    while n<max:
        yield b
        a, b = b, a+b
        n = n+1
    return 'done'
f = fib(6)

for x in f:
    print('generator x:',x)

# 练习（杨辉三角）
#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1
def triangles():
    while true:
