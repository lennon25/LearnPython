#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lennon'

from io import StringIO
from io import BytesIO
import pickle
import json


# 读文件

try:
    f = open('test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 在读取文件时，python引入with语句来自动调用close()方法
with open('test.txt', 'r') as f:
    print(f.read())

# for line in f.readlines():
#    print(line.strip())


# 写文件
with open('test.txt', 'w') as f:
    f.write('Hello,Lennon')

with open('test.txt', 'a') as f:
    f.write(' Hello,China')


# StringIO和BytesIO
# StringIO操作str
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world')
print(f.getvalue())


f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


# BytesIO 操作二进制数据


f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


f = BytesIO(b'\xe4\xad\xe6\x96\x87')
f.read()


# 序列化： 把变量聪内存中变为可存储或传输的过程称之为序列化，即picking
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()


# 反序列化对象 pickle.loads()
f = open('dump.txt', 'rb')
d = pickle.load(f)
print(d)


# JSON 标准数据格式
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

json_str = '{"age":20,"score":88, "name":"Bob"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

    def dict2student(d):
        return Student(d['name'], d['age'], d['score'])


print(json.dumps(s, default=lambda obj: obj.__dict__))
json_str = '{"age":20, "score":88, "name":"Bob"}'
print(json.loads(json_str, object_hook=dict2student))














