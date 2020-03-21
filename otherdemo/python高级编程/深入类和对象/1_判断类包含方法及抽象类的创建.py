


class conpany():
    def __init__(self,list):
        self.list =list

    def __len__(self):
        return len(self.list)
# 判断类型
com = conpany(["b1",'b2'])
print(hasattr(com,"__len__"))
# 方法二
from collections.abc import Sized
print(isinstance(com,Sized))


# 抽象类实现
import abc
class a(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self,key):
        pass

    @abc.abstractmethod
    def set(self,key,value):
        pass

class aa(a):

    def get(self,key):
        pass
    def set(self,key,value):
        pass

a_test = aa()