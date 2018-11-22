#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lennon'

from types import MethodType
from enum import Enum, unique

# 面向对象高级编程

# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现


class Student(object):
    pass


s = Student()
s.name = 'Lennon'
print(s.name)


# 给实例绑定方法
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)
s2 = Student()
# s2.set_age(25) 对另一个实例不起作用


# 给Class绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)


s2.set_score(99)
print(s2.score)


#  使用特殊变量__slots__，用来限制class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(object):
    pass


g = GraduateStudent()
g.score = 999
print(g.score)


# 使用@property
# @property 应用在类的定义中,让调用者写出简短的代码，同时保证对参数进行必要的检查

class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)
s.get_score()
# s.set_score(999)


# 装饰器可以动态给函数加上功能，对于类同样适用
# @property 装饰器就是负责把一个方法变成属性调用的:

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


s = Student()
s.score = 60
print(s.score)
# s.score = 999
# 对实例属性操作的时，通过getter和setter方法来实现的


# 定义读写，和只读属性
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
# birth是可读写属性，而age是一个只读属性


# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试成功')
else:
    print('测试失败！')


#  多重继承
class Animal(object):
    pass


# 大类
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 定义Runnable和Flyable类
class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def Fly(self):
        print('Flying...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Runnable):
    pass
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能


# MixIn 给一个类增加多个功能，而不是多次层的继承关系
class RunnableMinIn(object):
    pass


class FlyableMinIn(object):
    pass


class CarnivorousMinIn(object):
    pass


class HerbivoresMinIn(object):
    pass


class Dog(Mammal, RunnableMinIn, CarnivorousMinIn):
    pass


# python内置的MinIn模块
# 编写一个多进程的TCP服务
'''
class MyTCPServer(TCPServer, ForkingMinIn):
    pass


# 编写一个多线程的UDP服务
class MyUDPServer(UDPServer, ThreadingMinIn):
    pass


class MyTCPServer(TCPServer, CoroutineMinIn):
    pass
'''


# 定制类
# 内置的__xxx__命名属于特殊变量或函数，有特殊用途， 在class中可以用来定制类

# __str__
# 在类中定义__str__方法，返回一个好看的字符串
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name : %s)' % self.name
    __repr__ = __str__


print(Student('Lennon'))
s = Student('Lennon')
print(s)


# __iter__ ，该方法返回一个迭代对象，可以应用于类
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计算数

    def __iter__(self):
        return self  # 实例本身就是迭代对象

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


# __getitem__
class Fib(object):
    def __getitem__(self, n):
        a, b, = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[1])
print(f[10])
print(f[100])

print(list(range(100))[5: 10])


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[0:5])
print(f[:10])


# __getattr__方法

class Student(object):

    def __init__(self):
        self.name = 'Lennon'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99


s = Student()
print(s.name)
print(s.score)


class Student(object):

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\' %  attr')


s = Student()
print(s.age())


# 利用动态的__getattr__,可以写一个链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# __call__ 对实例进行调用(调用实例自身)
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Lennon')
print(s())


# 使用枚举类

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Fri)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)


# 把Student的gender属性改造为枚举类型
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过！')
else:
    print('测试失败！')


# 使用元类
# Type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


# 动态创建一个Hello的class对象
h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))


# 通过type创建类
def fn(self, name='World'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))


# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# 步骤：先定义metaclass，就可以创建类，最后创建实例
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)


# ORM "Object Relational Mapping" 叫做对象-关系映射，是把关系数据库的一行映射为一个对象，也就是一个类对应一个表
# 编写一个ORM框架

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()


















































