import queue
import threading
from time import sleep


def work1(num):
    sleep(10)
    print("work1:"+num)

def work2():
    # 先进先出队列
    q=queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.qsize())
    print(q.get())
    print(q.qsize())


    # 先进后出队列
    q=queue.LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.qsize())
    print(q.get())
    print(q.qsize())

    # 双向队列
    q2 = queue.deque()
    q2.append(123)
    q2.append(456)
    q2.appendleft(333)
    print(q2)



def bf():
    L=[str(i) for i in range(10)]
    q=queue.Queue(maxsize=5)
    while L:
        data = L.pop()
        t1 = threading.Thread(target=work1,args=data)
        q.put(t1)
        if q.full()   or  len(L) ==0:
            thread_list = []
            while q.empty() == False:
                t = q.get()
                thread_list.append(t)
                t.start()
                print("当前线程数："+str(len(threading.enumerate())))
            for t in thread_list:
                t.join()


if __name__ == '__main__':
    work2()