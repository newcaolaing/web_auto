

class test():
    def __init__(self,a):
        self.__a = a

    def __abb__(self):
        print("abb")

if __name__ == '__main__':
    t = test(0)
    # 获取私有属性
    print(t._test__a)
    # 获取私有方法
    t.__abb__()