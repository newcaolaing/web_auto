from threading import Thread
from time import sleep


def work1(nums):
    nums.append(44)
    sleep(1)

def work2(nums):
    print("work2:"+str(nums))

nums = [1,2,3,4,5]

t1 = Thread(target=work1,args=(nums,))
t1.start()

t2 = Thread(target=work2,args=(nums,))
t2.start()


