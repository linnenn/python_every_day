import keyword
import os

class A(object):
    # 私有属性，并不是不能访问，只是约定这样，实际上可以通过a._A__a_param访问得到
    __a_param = 1
    # 普通属性
    param_a = 2
    @classmethod
    def method(cls):
        print(cls)
        print('this is classmethod isstance of class A()')
    def normal_method(self):
        print('this is method isstance of class A()')

    @staticmethod
    def static_method():
        print('this is method static_method of class A()')


class B:
    __b_param = 1
    @classmethod
    def method(cls):
        print(cls)
        print('this is classmethod isstance of class B()')

    def normal_method(self):
        print(self)
        print('this is method isstance of class B()')

    @staticmethod
    def static_method():
        print('this is method static_method of class B()')

class C:
    __c_param = 1
    @classmethod
    def method(cls):
        print(cls)
        print('this is classmethod isstance of class C()')

    def normal_method(self):
        print(self,1)
        print('this is method isstance of class C()')

    @staticmethod
    def static_method():
        print('this is method static_method of class C()')

class testA(B,A):
    count = 0
    def __init__(self):
        testA.count += 1
        print(testA.count)
        # print(self._A__a_param)
    pass

if __name__ == '__main__':
    # testA.method()
    # testA.static_method()
    a = testA()
    print(a.param_a)
    # a.method()
    # a.static_method()
    # a.normal_method()
    # 实例化才会执行__init__,来初始化一些变量
    # for i in  range(10):
    #     testA()

