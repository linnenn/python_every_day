"""
    test obj for python3
"""
import pandas as pd
import numpy as np
import matplotlib

class Math:
    __private_flag = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.__private_flag = self.a + self.b
    def sum(self):
        return self.__private_flag
    def mins(self):
        return self.a - self.b
    def max(self):
        if self.a > self.b :
            max = self.a
        else:
            max = self.b
        return max
    def shuff(self):
        return self.a * self.b

if __name__ == "__main__":
    a = 2
    b = 3
    param = Math(a,b)
    print(param.a,param.b,param._Math__private_flag)
