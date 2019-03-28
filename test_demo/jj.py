from test_case.model.myunit import StartEnd
import unittest
from config.setting import logging

import unittest
import paramunittest
import time
# python3.6
# 作者：上海-悠悠

@paramunittest.parametrized(
    {"user": "admin", "psw": "123", "result": "true"},
    {"user": "admin1_end", "psw": "1234", "result": "true"},
)

class TestDemo(StartEnd):
    def setParameters(self, user, psw, result):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.user = user
        self.psw = psw
        self.result = result

    def testcase(self):
        self._testMethodName = self.user
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % self.user)
        print("输入密码：%s" % self.psw)
        print("期望结果：%s " % self.result)
        time.sleep(0.5)


        self.assertTrue(self.result == "true")


if __name__ == "__main__":
    unittest.main(verbosity=2)


