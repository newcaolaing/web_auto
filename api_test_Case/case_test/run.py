import time
import unittest

from BeautifulReport import BeautifulReport
from util.send_email import send_mail
from config.setting import report_path, api_test_dir
from base.HTMLTestRunner_cn import HTMLTestRunner

# 加载单个用例
# suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
#加载多个测试用例
discover = unittest.defaultTestLoader.discover(api_test_dir, pattern='test_login.py')

#定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_path + '/' + now + ' test_report.html'

#运行用例并生成测试报告
# with open(report_name, 'wb') as f:
#     runner = BSTestRunner(stream=f, title="Kyb Test Report", description="kyb Andriod app Test Report")
#     logging.info("start run testcase...")
#     runner.run(discover)

def create_report():
    '''
    运行所有*_test.py文件中的test,生成报告
    :param is_new: n 覆盖旧的报告，y 根据时间格式生产新报告
    :return: 根据规则生成测试报告文件名，相对路径
    '''
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="This is the 大帅哥的 report", description="关键字驱动+excel")
        runner.run(discover)
    send_mail()


def create_beautiful():
    result = BeautifulReport(discover)
    result.report(filename=now+'测试报告',report_dir=report_path,description='测试deafult报告')

if __name__ == '__main__':
    # with open(report_name, 'wb') as f:
    #     runner = HTMLTestRunner(stream=f, title="This is the 大帅哥的 report",
    #                             description="关键字驱动+excel", verbosity=2)
    #     runner.run(discover)
    create_beautiful()