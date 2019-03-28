import unittest

import time

from base.find_element import analytic_selector
from test_case.model.myunit import StartEnd
from config.setting import logging, report_path
import paramunittest

from util.HTMLTestRunner import HTMLTestRunner
from util.exl import Excel_Opertion
from util.send_email import send_mail

A = Excel_Opertion()
a = A.get_data()
@paramunittest.parametrized(*a)

class TestDemo(StartEnd):
    def setParameters(self, TEST_ID,TEST_NAME,MODULE, STEP,RESULT):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.test_name = TEST_NAME
        self.step = STEP
        self.result = RESULT

    def testcase(self):
        self._testname = self.test_name
        logging.info("开始执行用例：--------------"+self.test_name)
        analytic_selector(self.driver).run(self.step)
        if "=" in self.result:
            result_assert=self.result.split("=")
            selector=analytic_selector(self.driver)
            if result_assert[0] == 'url':
                logging.info("正在判断："+self.result)
                self.assertTrue(selector.get_url() == result_assert[1])
            elif analytic_selector(1).is_path(result_assert[0]):
                logging.info("正在判断："+self.result)
                self.assertTrue(selector.get_text(),result_assert[1])
        else:
            logging.info("本用例只需要执行不报错即可通过")