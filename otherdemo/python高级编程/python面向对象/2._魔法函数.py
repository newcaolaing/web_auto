class test():

    def __init__(self,list):
        self.list =list

    def __str__(self):
        return ','.join(self.list)

    # 开发模式下使用
    def __repr__(self):
        return "repr"

    __repr__ = __str__

a = test(['1','2','3'])
# 调用__str__方法
print(a)



class test2(object):
    def __init__(self,lists):
        self.lists = lists

    def __add__(self, other):
        self.lists.append(other.lists[0])
        test_add = test2(self.lists)
        return test_add

    def  __str__(self):
        return  ','.join(self.lists)

a1 = test2(['1','2'])
a2 = test2(['3','4'])
# 调用__add__函数
print(a1+a2)

