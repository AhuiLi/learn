## 函数
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 默认参数一定要用不可变对象

# 可变参数

def calc(*numbers):
    s = 0
    for value in numbers:
        s += value*value
    return s

print(calc(1,2,3))
# 参数numbers接收到的是一个tuple

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
L = (1,2,3,4)
print(calc(*L))

#   关键字参数

def person(name, age, **extra):
    print('name:', name, 'age', age, 'extra', extra)

person('ahui', 30)

person('ahui', 25, study='php')

person('ahui', 23, **{'study':'python'})

# 递归（移动汉诺塔，不太明白）
