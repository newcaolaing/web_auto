import unittest
from base.web_driver import browser
from config.setting import logging
from util.send_email import inser_img,get_time

class StartEnd(unittest.TestCase):
    name=''

    @classmethod
    def setUpClass(cls):
            cls.driver = browser()
            print("打开浏览器")

    def setUp(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        logging.info("检测异常处理")

        self._testMethodName=self._testname
        for method_name, error in self._outcome.errors:  # case如果执行失败，错误会保存到_outcome.errors 中
            if error:
                case_name = self._testname  # case名，即定义好的方法名
                print(case_name)
                report_error_name =get_time()+ case_name + '.png'
                logging.error("report_error:", report_error_name)
                inser_img(self.driver,report_error_name)




    @classmethod
    def tearDownClass(cls):
        # if "end" not in cls.name:
        logging.info("用例正在结束："+cls.name)
        logging.info("关闭浏览器")
        cls.driver.quit()
