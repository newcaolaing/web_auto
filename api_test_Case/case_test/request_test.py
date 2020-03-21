import json
import time
import unittest

import  requests
from BeautifulReport import BeautifulReport

from config.setting import report_path, test_dir

base_url = 'http://httpbin.org'
# 发送get请求
r= requests.get(base_url+'/get')
print(r.status_code)
# 发送post请求
r= requests.post(base_url+'/post')
print(r.status_code)

#get url传参
param_data = {"name":"曹亮","a":"b"}
r= requests.get(base_url+'/get',params=param_data)
print(r.url)

#post url传参
param_data = {"name":"曹亮","a":"b"}
r= requests.post(base_url+'/post',data=param_data)
print(r.url)
print(r.text)

#请求头控制
form_data ={"name":"曹亮","a":"b"}
header = {'user-agent':'request_test'}
r= requests.post(base_url+'/post',data=form_data,headers=header)
print(r.text)
print(r.json())

#cookie 设置
cookie = {"name":"caoliang"}
r = requests.get(base_url+"/cookies",cookies=cookie)
print(r.text)
r= requests.get("https://www.baidu.com")
for k,v in r.cookies.items():
    print(k+":"+v)

# 超时设置
try:
    r= requests.get(base_url+"/cookies",cookies=cookie,timeout=0.01)
except:
    print("超时了")

#文件上传
# file = {"file":open("图片","rb")}
# r = requests.post(base_url+'/post',file=file)

# 保持会话对象
s =requests.Session()
r= s.get(base_url+"/cookies/set/name/caol")
r=s.get(base_url+"/cookies")
print(r.text)

# ssl 证书认证
# r= requests.get("https://www.12306.cn",verify=False)
# print(r.text )

# 代理配置
# proxies  = {"http":"http://10.10.1.10:3128"}
# r= requests.get(base_url+"/get",proxies=proxies)
# print(r.text)

# 流式请求
r= requests.get(base_url+"/stream/10",stream=True)
if r.encoding is None:
    r.encoding="utf-8"
for line in r.iter_lines(decode_unicode=True):
    if line:
        data= json.loads(line)
        print(data["id"])


#天气接口
city = "101030100"
weather="http://t.weather.sojson.com/api/weather/city/{}"
r =requests.get(weather.format(city))
response = r.json()
print(response["data"]["forecast"][0]["high"])
print(response["data"]["forecast"][0]["week"])
print(response["data"]["forecast"][0]["ymd"])
print(response["data"]["forecast"][0]["low"])


#unitest_weather
class Weather(unittest.TestCase):
    def setUp(self):
        self.url='http://t.weather.sojson.com/api/weather/city/{}'
        print("1111111111111")

    def test_tj(self):
        data="101030100"
        r =requests.get(self.url.format(data)).json()
        self.assertEqual(r["status"],200)


    def test_error(self):
        """
        pass
        """
        data="3242423423"
        r =requests.get(self.url.format(data)).json()
        self.assertEqual(r["status"],404)

    def test_error2(self):
        data=""
        r =requests.get(self.url.format(data)).json()
        self.assertEqual(r["status"],404)

def create_beautiful():
    result = BeautifulReport(discover)
    result.report(filename=now+'测试报告',report_dir=report_path,description='测试deafult报告')

if __name__ == '__main__':
    # 加载多个测试用例
    discover = unittest.defaultTestLoader.discover(".", pattern='re*.py')
    # 定义报告的文件格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_path + '/' + now + ' test_report.html'
    create_beautiful()