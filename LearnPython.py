#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Hello,World!")

print(100+200)

print('100+200=', 100+200)

print(1024 * 768)


# Input and Output

# name = input()
# print("Hello,",name)

# name = input("please enter your name: ")
# print("Hello,", name)


# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)


print('I\'m \"OK\"!')
print('I\'m learning\nPython.')
print('\\\n\\ ')

print('\\\t\\ ')
print(r'\\\t\\ ')

print('''line1
line2
line3''')

print(r'''hello,\n 
world''')

print(True)
print(False)
print(3 > 2)
print(3 > 5)

age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')


# 变量
a = 123
print(a)
a = 'ABC'
print(a)

x = 10
x = x*2
print(x)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 除法的计算结果为浮点数
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)

n = 123
f = 456.251
s1 = 'Hello, World'
s2 = 'Hello, \'Adam\''
s3 = 'Hello, "Bart"'
s4 = r'''Hello, 
Lennon'''

print(''' %d
%d
%s
%s
%s
%s
''', n, f, s1, s2, s3, s4)


# 字符串
print('包含中文的str')

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')


#  Format String

print('Hello, %s' % 'World')
print('Hi %s,you have $%d.' % ('Lennon', 1000000))

print('%2d-%0.2d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s, Gender: %s' % (25, True))

# format()
print('Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('%.1f%%' % r)



