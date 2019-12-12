import cx_Oracle


user = "c##z"
pw = "test"
dsn = "127.0.0.1:1521/orcl"


connection = cx_Oracle.connect(user, pw, dsn, encoding = "UTF-8", nencoding = "UTF-8")

cursor = connection.cursor()
sql='insert into test1(idpm) values(:1)'
cursor.executemany(sql,[('1111',)])
connection.commit()
print("方法一插入成功")

# print("------"*10)
# cursor.executemany(sql,['1'])
# connection.commit()
# print("方法二插入成功")
