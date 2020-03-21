

class A():
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super().__init__()

if __name__ == '__main__':
    TEST = D()