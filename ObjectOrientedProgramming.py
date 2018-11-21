#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Object Oriented Programming：面向对象编程 """

__author__ = 'Lennon'

import types


# 面向过程的程序：
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 88}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


# 面向对象的程序：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


# 面向对象对象的方法（Method), 给对象发消息, 实际上就是调用对象对应的关联函数
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa simpson', 87)
bart.print_score()
lisa.print_score()

# 所以，面向对象的设计思想是抽象出Class。 根据Class创建Instance。
# 数据封装、继承和多态是面向对象的三大特点。


# 面向对象最重要的概念就是类（Class）和实例（Instance），类是抽象的模板，实例是根据类创建出来的一个个具体的"对象"。
# 定义类，使用class关键字
class Student(object):
    pass


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


L = Student('Lennon', 100)
print(L)
print(L.name)
print(L.score)



# 数据封装

def print_score(std):
    print('%s: %s' % (std.name, std.score))


print_score(L)


# 可以在类的内部定义访问数据的函数，被称为封装，封装数据的函数和类本身是关联起来的，我们称为类的方法
# 通过在实例上调用方法，我们就可以操作对象内部的数据，但无需知道方法内部的实现细节。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))


print(bart.print_score())


# 给student类增加新的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print('%s : %d : %s' % (lisa.name, lisa.score, lisa.get_grade()))
print('%s : %d : %s' % (bart.name, bart.score, bart.get_grade()))




# 访问限制
# 在实例变量名前加"__", 可变为私有(private)变量. 添加获取name和score的方法
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s : %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Student('Bart Simpson', 59)
# bart.__name 外部不能调用


# Student类增加set_score方法
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s ' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


# '_xxx'定义的实例变量名虽然可以被访问，但也被视为私有变量， '__xxx'定义变量不能直接访问，但也能被解释器访问
# 如：print(bart._Student__name)，但不能这样做

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender!')


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败！')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败！')
    else:
        print('测试成功！')




# 继承和多态
# 继承
class Animal(object):
    def run(self):
        print('Animal is running...')


'''
class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()
print(dog.run())
print(cat.run())
'''


# 给子类增加方法
class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running')


dog = Dog()
cat = Cat()
print(dog.run())
print(cat.run())


# 定义class 实际是定义了一种class数据类型
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型, 也是Animal类型


# 多态的好处
def run_twice(animal):
    animal.run()
    animal.run()


print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


print(run_twice(Tortoise()))

# 多态真正的威力：调用方只管调用，不管细节
# 著名的“开闭”原则：对扩展开放：允许新增Animal子类；对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


# 判断对象类型 type()
print(type(123))
print(type('str'))
print(type(None))

print(type(abs))
print(type(b))

print(type(123)==type(345))
print(type('abc')==type('123'))
print(type('abc')== str)


# 判断一个对象是否是函数，引入import types
def fn():
    pass


print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


# 使用isinstance() , 判断是否是继承关系
class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


# 使用dir()

print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))


# 实例属性，和类属性
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性。不能对实例属性和类属性使用相同的命名。

class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


# 创建类属性
class Student(object):
    name = 'Student'


s = Student()
print(s.name)
print(Student.name)

s.name = 'Lennon'
print(s.name)
print(Student.name)

del s.name
print(s.name)


# 统计学生人数，给Student类增加一个类属性，每创建一个实例，该属性自动增加
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


if Student.count !=0:
    print('测试失败')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败！')
    else:
        lisa = Student('Lisa')
        if Student.count != 2:
            print('测试失败！')
        else:
            print('Student:', Student.count)
            print('测试通过！')







