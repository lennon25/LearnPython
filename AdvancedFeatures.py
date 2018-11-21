#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
import os


# 高级特性
# 切片


L = ['Lennon', 'Michael', 'Sarah', 'Adam', 'Tracy']

print(L[0:3])
print(L[:3])
print(L[1:5])

print(L[-2:])
print(L[-4:-1])
print(L[-1])

L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])
print(L[:])

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


# 迭代（遍历）
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for key in d.values():
    print(key)

for key in d.items():
    print(key)

for i in 'ABC':
    print(i)

print(isinstance('ABC', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))


for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# 列表生成式 List Comprehensions range()

print(list(range(1, 11)))

print([x * x for x in range(1, 11)])

# 双层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录的所有文件
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'Lennon', 'Apple']
print([s.lower() for s in L])


# Test
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过！')
else:
    print('测试失败！')


# 生成器 Generator  机制：一边循环一边进行计算
# 创建一个Generator
g = (x * x for x in range(10))
print(g)
print(next(g))

for i in g:
    print(i)


# 斐波那契列数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b, = b, a+b
        n = n + 1
    return 'done'


while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break













