import requests as 请求


结果=请求.get("http://www.baidu.com")
print(结果.status_code)

def 大帅哥(形参):
    print(形参)

大帅哥("实参")


网址 = ["http://www.baidu.com","baidu.com"]

新网址  =  list(map( lambda x:x if "http://" in x else "http://www." +x ,["http://www.baidu.com","baidu.com"]))
print(新网址)