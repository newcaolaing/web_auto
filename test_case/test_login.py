from base.find_element import analytic_selector
from test_case.model.myunit import StartEnd
from config.setting import logging, report_path
import paramunittest

from util.assert_method import assert_method
from util.exl import Excel_Opertion

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
        selector = analytic_selector(self.driver)
        assert_md = assert_method(selector,self.result)
        logging.info("开始执行用例：--------------"+self.test_name)
        selector.run(self.step)
        assert_md.run()



