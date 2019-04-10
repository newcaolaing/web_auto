from base.wait import wait
from util.read_ini import Read_Ini
import logging
import re
from selenium import webdriver

class analytic_selector(wait):
    """获取元素所在位置"""

    def __init__(self, driver):
        super().__init__(driver)

    # 获取测试步骤将其分解去除杂数据
    def one_next(self,a):
        return [re.sub("\d\.",'',x) for x in a.split("\n")]

    def get_element(self, key):
        actions = key.split("||")

        if len(actions) > 1:
            action_head = actions[0]
            if action_head == "打开":
                logging.info("正在打开："+actions[1])
                self.driver.get(actions[1])

            elif action_head == "点击":
                selector, selector_location = self.selector_path(actions[1])
                logging.info("正在点击"+selector_location)
                self.action_element(selector,selector_location).click()

            elif action_head == "输入":
                selector, selector_location = self.selector_path(actions[1])
                logging.info("定位元素："+selector_location+"--正在输入"+actions[2])
                self.action_element(selector, selector_location).send_keys(actions[2])
            elif action_head == "等待":
                selector, selector_location = self.selector_path(actions[1])
                self.wait_text(selector_location,actions[2])

        elif len(actions) == 1:
            if actions[0] == "退出浏览器":
                logging.info("退出浏览器")
                self.driver.quit()
            elif actions[0] == "刷新浏览器":
                self.driver.refresh()

    def selector_path(self, a):
        path = re.match("(.*){(.*)}", a)
        return path.groups()


    def is_path(self,path):
        selector = ["id","name","className","xpath","css"]
        print(path)
        print(self.selector_path(path))
        if self.selector_path(path)[0] in selector:
            return True
        else:
            return False

    def action_element(self, by, path):
        try:
            if by == 'id':
                return self.driver.find_element_by_id(path)
            elif by == 'name':
                return self.driver.find_element_by_name(path)
            elif by == 'className':
                return self.driver.find_element_by_class_name(path)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(path)
            else:
                return self.driver.find_element_by_css(path)
        except Exception as e:
            logging.error("find_element错误信息：", e)
            return None

    def get_text(self,path):
        selector, selector_location = self.selector_path(path)
        return  self.action_element(selector, selector_location).text

    def get_url(self):
        return  self.driver.current_url



    def run(self,action):
        for next in self.one_next(action):
            self.get_element(next)





if __name__ == '__main__':
    a=analytic_selector(1)
    a.is_path('xpath{//*[@id="bs-example-navbar-collapse-1"]//a}')