class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self,*args ):
        self.file.close()


with   File("1.txt" ,"r") as f:
    print(f.readline())


# 方法2
# Python 还提供了一个 contextmanager 的装饰器，
# 更进一步简化了上下文管理器的实现方式。
# 通过 yield 将函数分割成两部分，yield 之前的语句在 __enter__ 方法中执行，
# yield 之后的语句在 __exit__ 方法中执行。紧跟在 yield 后面的值是函数的返回值。

from contextlib import contextmanager

@contextmanager
def  files(path ,mode):
    f=open(path,mode)
    yield f
    f.close()

with files('1.txt','r') as f:
    print(f.readline())


