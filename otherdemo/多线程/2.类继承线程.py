import  threading
from time import sleep



class threads(threading.Thread):
    # 重写run方法
    def run(self):
        for i in range(3):
            sleep(1)
            print(self.name+str(i))

def test():
    for i  in range(5):
        sleep(1)
        t = threads()
        t.start()

if __name__ == '__main__':
    test()