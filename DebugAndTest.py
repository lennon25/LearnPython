#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from functools import reduce
logging.basicConfig(level=logging.INFO)


# Python异常处理机制

# 错误处理机制 try...except...finally...
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('End!')


try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('End!')


# try...except捕获的好处，跨越多层调用
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) / 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
# 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。


# 调用栈
'''
def foo(s):
    return 10 / int('4')


def bar(s):
    return foo(s) * 2


def main():
    bar('0')


main()
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。


# 记录错误
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('End...')


def str2num(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()


def foo(s):
    n = int(s)
    print('>>> n = %d' % n)


def main():
    foo('0')


main()


# 断言 assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


# logging
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
'''


# 单元测试
# TDD 'Test-Driven Development' 测试驱动开发

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


d = Dict(a=1, b=2)
print(d['a'])


# setUp与tearDown
# 在单元测试中编写两个特殊的setUp()和tearDown()方法，这两个方法会分别在每调用一个测试方法的前后分别被执行

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if 80 <= self.score <= 100:
            return 'A'
        if 60 <= self.score < 80:
            return 'B'
        if 0 <= self.score < 60:
            return 'C'
        if self.score > 100 or self.score < 0:
            raise ValueError













