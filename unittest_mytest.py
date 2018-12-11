#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Lennon'

import unittest
from DebugAndTest import Dict
from DebugAndTest import Student
import json


class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 运行单元测试，当做正常的python脚本运行。
if __name__ == '__main__':
    unittest.main()
# 另一种方式： python -m unittest unittest_test


# 编写Student类test case
class TestStudent(unittest.TestCase):

    def setUp(self):
        pass

    def test_80_to__100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_100(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

# 基本的测试TestCase
'''
class StringTestCase(unittest.TestCase):
    def setUp(self):
        self.test_string = "this is a string"
        
    def tearDown(self):
    pass
    
    def testUp(self):
        self.assertEqual("THIS IS A STRING", self.test_string.upper())


if __name == '__main__':
    unittest.main()
'''


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
# 或 suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
# unittest.TextTestRunner(verbosity=2).run(suite)


class WeakPassWordTestCase(unittest.TestCase):
    @classmethod
    def setUp(kls):
        data_file_path = './user_data.json'
        print('before all test methods')
        with open(data_file_path) as f:
            kls.test_data = json.loads(f.read())

    def test_weak_password(self):
        for data in self.test_data:
            passwd = data['password']

            self.assertTrue(len(passwd) >=6)

            msg = "user %s has a weak password" % (data['name'])
            self.assertTrue(passwd != 'password', msg)
            self.assertTrue(passwd != 'passWord123', msg)

    def test_dummy(self):
        pass


if __name__ == '__main__':
    unittest.main()


# 文档测试
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest
    doctest.testmod()














