import time
from BeautifulReport import BeautifulReport

from base.find_element import analytic_selector
from test_case.model.myunit import StartEnd
from config.setting import logging, report_path
import paramunittest

from util.assert_method import assert_method
from util.exl import Excel_Opertion

now = time.strftime("%Y-%m-%d %H_%M_%S")
A = Excel_Opertion()
a = A.get_data()

@paramunittest.parametrized(*a)
class TestDemo(StartEnd):
    def setParameters(self, TEST_ID,TEST_NAME,MODULE, STEP,RESULT):
        '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
        self.test_name = TEST_NAME
        self.step = STEP
        self.result = RESULT

    @BeautifulReport.add_test_img(now)
    def testcase(self):
        self._testname = self.test_name
        selector = analytic_selector(self.driver)
        assert_md = assert_method(selector,self.result)
        logging.info("开始执行用例：--------------"+self.test_name)
        selector.run(self.step)
        self.assertTrue( assert_md.run())