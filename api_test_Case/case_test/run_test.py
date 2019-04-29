
import unittest

import requests

from config.setting import logging
from util.send_email import get_time


class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("setUpClass")

    def setUp(self):
        logging.info("setUp")


    def tearDown(self):

        for method_name, error in self._outcome.errors:  # case如果执行失败，错误会保存到_outcome.errors 中
            if error:
                case_name = self._testname  # case名，即定义好的方法名
                print(case_name)
                report_error_name =get_time()+ case_name
                logging.error("report_error:", report_error_name)


    @classmethod
    def tearDownClass(cls):
        logging.info("tearDownClass")

    headers = {
        "Content-Type": "application/json"
    }


    def test_login(self):
        url =  "http://api.biaodaa.com/authorize/memberLogin"
        data = '{"phoneNo":"15576361737","loginPwd":"7c222fb2927d828af22f592134e8932480637c0d","channel":"1003","clientVersion":"3.0"}'

        response = requests.post(url,data=data,headers=self.headers)
        logging.info(response.json())



if __name__ == '__main__':
    unittest.main()

