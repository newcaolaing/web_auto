

class A():

    name=''

    @classmethod
    def a(cls):
        print(cls.name)

    def b(self):
        A.name=222
        self.name=222


if __name__ == '__main__':
    c=A()
    c.b()
    A.a()