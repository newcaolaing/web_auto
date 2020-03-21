class test:
    names = 'test'
    """
    name is test
    """

    def a(self):
        print(self.name)

class test2(test):
    def __init__(self,name):
        super().__init__()
        self.name = name

if __name__ == '__main__':
    a  = test2("test2")
    print(a.__dict__)
    print(test2.__dict__)
    print(test.__dict__)
    # dir信息更加多
    print(dir(test))
    print(test.__dict__)
    print(test2.names)
