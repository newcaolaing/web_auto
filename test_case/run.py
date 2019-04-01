import time
import unittest
from util.send_email import send_mail
from config.setting import report_path, test_dir
from base.HTMLTestRunner import HTMLTestRunner

# 加载单个用例
# suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
#加载多个测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

#定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_path + '/' + now + ' test_report.html'

#运行用例并生成测试报告
# with open(report_name, 'wb') as f:
#     runner = BSTestRunner(stream=f, title="Kyb Test Report", description="kyb Andriod app Test Report")
#     logging.info("start run testcase...")
#     runner.run(discover)
if __name__ == '__main__':
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title="This is the 大帅哥的 report",
                                description="关键字驱动+excel", verbosity=2)
        runner.run(discover)

    send_mail()