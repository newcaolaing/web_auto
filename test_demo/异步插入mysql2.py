import os

import cx_Oracle

import pymysql
import threading
import time
from queue import Queue
from DBUtils.PooledDB import PooledDB
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class ThreadInsert(object):
    "多线程并发MySQL插入数据"
    def __init__(self):
        start_time = time.time()
        self.pool = self.mysql_connection()
        self.data = self.getData()
        self.mysql_delete()
        self.task()
        print("========= 数据插入,共耗时:{}'s =========".format(round(time.time() - start_time, 3)))

    def mysql_connection(self):
        maxconnections = 15  # 最大连接数
        pool = PooledDB(
            pymysql,
            maxconnections,
            host='192.168.11.111',
            user='root',
            port=3306,
            passwd='123456',
            db='bf',
            use_unicode=True)
        # dsn = cx_Oracle.makedsn('127.0.0.1', 1521, sid='orcl')
        # pool = PooledDB(cx_Oracle,mincached=20,blocking=True,user='c##z',password='test',dsn=dsn)

        return pool

    def getData(self):
        st = time.time()
        # with open("10w.txt", "rb") as f:
        #     data = []
        #     for line in f:
        #         line = re.sub("\s", "", str(line, encoding="utf-8"))
        #         line = tuple(line[1:-1].split("\"\""))
        #         data.append(line)
        # orcle_data = [[str(i)] for i in range(1000000)]
        data = [str(i) for i in range(1000000)]
        n = 100000    # 按每10万行数据为最小单位拆分成嵌套列表
        result = [data[i:i + n] for i in range(0, len(data), n)]
        print("共获取{}组数据,每组{}个元素.==>> 耗时:{}'s".format(len(result), n, round(time.time() - st, 3)))
        return result

    def mysql_delete(self):
        st = time.time()
        con = self.pool.connection()
        cur = con.cursor()
        sql = "TRUNCATE TABLE test"
        cur.execute(sql)
        con.commit()
        cur.close()
        con.close()
        print("清空原数据.==>> 耗时:{}'s".format(round(time.time() - st, 3)))

    def list_util(self,x):
        nu = list()
        nu.append(x)
        return nu

    def mysql_insert(self, *args):
        con = self.pool.connection()
        cur = con.cursor()
        # oracle_sql = "INSERT INTO TEST1 (IDPM) VALUES (:1)"
        mysql_sql = "INSERT INTO test (name) VALUES (%s)"
        # oracle_args = list(map(tuple, *args))
        try:
            cur.executemany(mysql_sql,*args)
            con.commit()
        except Exception as e:
            con.rollback()  # 事务回滚
            print('SQL执行有误,原因:', e)
        finally:
            cur.close()
            con.close()

    def task(self):
        q = Queue(maxsize=10)  # 设定最大队列数和线程数
        st = time.time()
        while self.data:
            content = self.data.pop()
            t = threading.Thread(target=self.mysql_insert, args=(content,))
            q.put(t)
            if (q.full() == True) or (len(self.data)) == 0:
                thread_list = []
                while q.empty() == False:
                    t = q.get()
                    thread_list.append(t)
                    t.start()
                for t in thread_list:
                    t.join()
        print("数据插入完成.==>> 耗时:{}'s".format(round(time.time() - st, 3)))


if __name__ == '__main__':
    ThreadInsert()
