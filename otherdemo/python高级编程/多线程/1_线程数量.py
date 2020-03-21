import threading
from time import sleep, ctime


def sing():
    for i in range(3):
        print("正在唱歌 {}".format(i))
        sleep(3)

def dance():
    for i in  range(3):
        print("正在跳舞 {}".format(i))
        sleep(3)

if __name__ == '__main__':
    print("开始时间：{}".format(ctime()))

    t1  = threading.Thread(target=sing)
    t2  = threading.Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        lengh = len(threading.enumerate())
        print("当前线程数为：{}个".format(lengh))
        if lengh <=1:
            break
        sleep(0.5)
