from selenium import webdriver
import time
driver = webdriver.Chrome()
#浏览器初始化
def driver_init():
    driver.get("https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F")
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#运行主程序
def run_main():
    driver_init()
    time.sleep(2)
    driver.find_element_by_id("J_Quick2Static").click()
    driver.find_element_by_id("TPL_username_1").send_keys("test")
    driver.find_element_by_id("TPL_password_1").send_keys("123456")
    driver.find_element_by_id("J_SubmitStatic").click()
    driver.close()

run_main()