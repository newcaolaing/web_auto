from time import strftime, localtime

import pymysql
from twisted.enterprise import adbapi
from twisted.internet import reactor

# 数据库基本配置
db_settings = {
    'host': '192.168.11.111',
    'db': 'bf',
    'user': 'root',
    'password': '123456',
    'charset': 'utf8',
    'use_unicode': True
}
# sql语句模版
insert_sql = 'INSERT INTO `bf`.`test` (`id`) VALUES (%s); '


def go_insert(cursor, sql):
    # 对数据库进行插入操作，并不需要commit，twisted会自动帮我commit
    try:
        for i in range(100000):
            data = str(i)
            cursor.execute(sql,data)
    except Exception as e:
        print(e)


def handle_error(failure):
    # 打印错误
    if failure:
        print(failure)


def bf():
    # 41s
    # 56s
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    try:
        # 生成连接池
        db_conn = adbapi.ConnectionPool('pymysql', **db_settings)
        # 通过连接池执行具体的sql操作，返回一个对象
        query = db_conn.runInteraction(go_insert, insert_sql)
        # 对错误信息进行提示处理
        query.addCallbacks(handle_error)
    except Exception as e:
        print(e)

    # 定时，给4秒时间让twisted异步框架完成数据库插入异步操作，没有定时什么都不会做
    # reactor.callFromThread(reactor.stop,3)
    reactor.callLater(0, reactor.stop)
    reactor.run()

    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))


def zc():
    # 46s
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))
    # 普通方法插入数据
    conn = pymysql.connect(**db_settings)
    cursor = conn.cursor()
    for x in range(100000):
        cursor.execute(insert_sql, str(x))
    conn.commit()
    print(strftime("%Y-%m-%d %H:%M:%S", localtime()))

if __name__ == '__main__':
    bf()






