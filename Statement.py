#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python Conditional Judgement Statement

age = 20
if age >= 18:
    print('Your age is', age)
    print('adult')


age = 3
if age >= 18:
    print('Your age is', age)
    print('adult')
elif age >= 6:
    print('Teenager')
else:
    print('Your age is', age)
    print('Kid')

x = 1
if x:
    print(True)

'''
s = input('Birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''

height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif 18.5 <= bmi < 25:
    print('正常')
elif 25 <= bmi < 28:
    print('过重')
elif 28 <= bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')


# Loop Statement
# for loop

names = ['Michael', 'Lennon', 'Bob', 'Tracy']
for name in names:
    print(name)

result = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = result + x
print(result)

result =0
for x in range(101):
    result = result + x
print(result)

# while loop
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


L = ['Lisa', 'Bob', 'Lennon']
for x in L:
    print('Hello,', x)



# break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('End!')


# continue
n = 0
while n <= 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)


a = 0
while a < len(L):
    print('Hello,', L[a])
    a += 1
