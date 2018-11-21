#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

# python function

print(abs(12.34))
print(abs(-100))

print(max(1, 4, 7, 3, 9, 10))
print(min(4, 7, 9, 2))

# 数据类型转换
print(int('123'))
print(str(123))
print(float('12.45'))
print(str(1.56))
print(bool(1))
print(bool(''))

# 函数名赋值给变量
a = abs
print(a(-1))


# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 空函数
def nop():
    pass


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)


# 函数的参数
# def power(x):
#    return x * x

# 计算x的n次方
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))
print(power(5, 3))
print(power(5))


# 位置参数
def enroll(name, gender, age=18, city='Shenzhen'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Lennon', 'A')
enroll('Bob', 'M', 25, 'Beijing')
enroll('Adam', 'B', city='Tianjing')


# 默认参数为不可变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


def calc(numbers):
    result = 0
    for n in numbers:
        result = result + n * n
    return result


print(add_end())
print(add_end())
print(calc([1, 3, 5, 7]))
print(calc([1, 3, 5, 7, 10]))


# 可变参数,在参数前面加'*'号
def calc(*numbers):
    result = 0
    for n in numbers:
        result = result + n * n
    return result


print(calc(1, 3, 5))
print(calc(1, 5, 7, 9, 10))
print(calc(1, 2))
print(calc())

# *nums表示把nums这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]
print(nums[0], nums[1], nums[2])
print(*nums)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


person('Michael', 30)
person('Lennon', 25, city='Shenzhen')
person('CC', 24, gender='M', job='Engineer')

extra = {'city': 'Shenzhen', 'job': 'Engineer'}
person('Lennon', 27, city=extra['city'], job=extra['job'])
person('Lennon', 27, **extra)


# 命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, age, 'other:', kw)


print(person('Jack', 24, city='Beijing', addr='chaoyang', zipcode='12345'))


# 限制关键字参数名字
def person(name, age, *, city, job):
    print(name, age, city, job)


print(person('Jack', 24, city='Shenzhen', job='Engineer'))


def person(name, age, *, city='Shenzhen', job):
    print(name, age, city, job)


print(person('Jack', 24, job='Engineer'))


# 参数组合
# Python中定义函数，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


print(f1(1, 2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, args=('a', 'b'), kw={'x' : 99}))
print(f2(1, 2, d=99, ext=None))

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))


# 计算一个或多个数的乘机
def product(*args):
    x = 1
    if args == ():
        raise TypeError
    else:
        for i in args:
            x *= i
        return x


print(product(5))
print(product(5, 6))
print(product(5, 6, 7))
print(product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败！')
elif product(5, 6) != 30:
    print('测试失败！')
elif product(5, 6, 7) != 210:
    print('测试失败！')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败！')
else:
    try:
        product()
        print('测试失败！')
    except TypeError:
        print('测试成功！')


# 递归调用
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(100))


# 尾递归
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(5, 1))
print(fact_iter(4, 5))
print(fact_iter(3, 20))


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(L)















