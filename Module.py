#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A test Module"""

__author__ = 'Lennon'

# 使用模块，编写hello模块

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()


# 作用域

# public公开变量 ： abc, x123, PI
# 特殊变量： __xxx__,  __author__, __name__
# private私有变量： _xxx, __xxx,  _abc, __abc

def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) >3:
        return _private_1(name)
    else:
        return _private_2(name)


print(greeting('Lin'))


# 导入模块使用 import
# import os
# import sys
# import unittest




