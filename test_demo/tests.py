import requests
from fake_useragent import UserAgent


class A():

    name=''

    @classmethod
    def a(cls):
        print(cls.name)

    def b(self):
        A.name=222
        self.name=222


url = "http://jzsc.mohurd.gov.cn/dataservice/query/comp/list"

head= {
    "User-Agent":UserAgent().random,
    "Referer":"http://jzsc.mohurd.gov.cn/dataservice/query/comp/list"
}

data= {
    "qy_fr_name":"王",
    "$total":382,
    "qy_reg_addr":"湖南省",
    "$pgsz":15,
    "qy_region":430000,
    "$reload":0,
    "$pg":26,
}

response = requests.post(url,data=data,headers=head)
print(response.text)