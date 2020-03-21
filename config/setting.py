import os
import logging.config


log_file_path =os.path.join(os.path.dirname(__file__).split("web_auto")[0]+"web_auto",'config','log.conf')
logging.config.fileConfig(log_file_path)
logging = logging.getLogger()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目首路径

codeerror_path = os.path.join(base_dir,'Image','codeerror.png')  # 验证码错误图片路径
code_path = os.path.join(base_dir,'Image','code.png')  # 验证码图片保存路径

# 页面元素地址配置
config_ini_dir = os.path.join(base_dir,'config','ini.ini')  # localElement.ini 配置文件路径
driver_ini_dir = os.path.join(base_dir,'config','start_driver.ini')

# 报告目录
report_screenshot = os.path.join(base_dir,'report',"screenshot")
report_path = os.path.join(base_dir,'report',"reports")

# 用例excel存放目录
excel_path= os.path.join(base_dir,'test_case',"case_excel","test_cese.xlsx")
api_excel_path= os.path.join(base_dir,'api_test_Case',"case_excel","test_cese.xlsx")

# driver存放目录
driver_path = os.path.join(base_dir,'base',"chromedriver.exe")

# 测试用例代码目录
test_dir= os.path.join(base_dir,'test_case')
api_test_dir = os.path.join(base_dir,'api_test_Case',"case_test")
# 邮箱设置
user='179956000@qq.com'
pd='dydascollsuhbihf'
receive= ['179956000@qq.com', '179956000@qq.com',"573783387@qq.com"]

