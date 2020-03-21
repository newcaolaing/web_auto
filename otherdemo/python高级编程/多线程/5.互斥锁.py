import threading
from threading import Thread
from time import sleep

nums = 0
def work1(num):
    global nums
    for x in range(num):
        lock.acquire()
        nums+=1
        lock.release()
    print("work1:"+str(nums))


def work2(num):
    global nums
    for x in range(num):
        lock.acquire()
        nums+=1
        lock.release()
    print("work2:"+str(nums))

# 创建锁
lock = threading.Lock()


t1 = Thread(target=work1,args=(1000000,))
t1.start()
t2 = Thread(target=work2,args=(1000000,))
t2.start()

while len(threading.enumerate()) !=1:
    sleep(1)

print("最终的结果："+str(nums))