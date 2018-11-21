#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
import functools

# 函数式编程 Functional programming
# 高阶函数 Higher-order function
# 一个函数可以接受另一个函数作为参数，这种函数杯成为高阶函数, 编写高阶函数，就是让函数的参数能够接收别的函数。


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))


# map()函数
def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce()函数
# 语法：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

'''
def fn(x, y):
    return x * 10 +y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))
'''
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s))


print(str2int('13579'))


# lambda函数表示
def char2num(s):
    return digits[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# Filter函数：用于过滤序列，filter()也接收一个函数和一个序列
def is_odd(n):
    return n % 2 ==1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', 'None', 'C', '  '])))


# 用filter计算素数
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


if __name__ == '__main__':
    main()


# sorted 排序算法

print(sorted([36, 5, 76, -12, 9]))

print(sorted([26, 5, -76, -12, 9], key=abs))

print(sorted(['bob', 'about', 'Lennon', 'Zoo', 'Credit']))

print(sorted(['bob', 'about', 'Lennon', 'Zoo', 'Credit'], key=str.lower))

print(sorted(['bob', 'about', 'Lennon', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 按照学生的名字和成绩排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


def by_score(t):
    return -t[1]


L1 = sorted(L, key=by_name)
print(L1)
L2 = sorted(L, key=by_score)
print(L2)


# 返回函数 函数作为返回值

# 求和的结果
def calc_sum(*args):
    ax =0
    for n in args:
        ax = ax + n
    return ax


# 返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())


# 闭包
# 返回闭包时需注意： 返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 引用循环变量的情况
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(1)立即被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 匿名函数 lambda
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数

f=lambda x: x * x
print(f(5))


# 把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * y + y * y


print(list(filter(lambda x: x % 2 == 0, range(1, 20))))


# 装饰器（Decorator） 在代码运行期间动态增加功能的方式，被称为装饰器

def now():
    print('2018-11-20 11:13')


f =now
print(f())
print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2018-11-20 11:25')


print(now())


# 编写一个返回decorator的高阶函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s();' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('Execute')
def now():
    print('2018-11-20 11:46')


print(now())
print(now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 偏函数
print(int('12345', base=8))
print(int('12345', base=16))

'''
def int2(x, base=2):
    return int(x, base)
    
print(int2('1000000'))
print(int2('1010101'))
'''

int2 = functools.partial(int, base=2)
print(int2('100000'))
print(int2('1010101'))
print(int2('10000', base=10))



