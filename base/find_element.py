from base.key_next import key_next
import logging
import re
from selenium import webdriver


class analytic_selector(key_next):
    """获取元素所在位置"""

    def __init__(self, driver):
        super().__init__(driver)
        self.AC = {
            "打开":self.open,
            "点击":self.click,
            "输入":self.input,
            "退出浏览器":self.quit,
            "刷新":self.refresh,
            "正常等待":self.mysleep,
            "等待元素":self.wait,
            "隐性等待":self.imsleep,
        }

    # 获取测试步骤将其分解去除杂数据
    def one_next(self, a):
        return [re.sub("\d\.", '', x) for x in a.split("\n")]

    def step(self,key):
        self.key = key
        self.actions = key.split("||")
        self.action_head = self.actions[0]
        self.AC[self.action_head]()



    def selector_path(self, a):
        path = re.match("(.*){(.*)}", a)
        return path.groups()

    def is_path(self, path):
        selector = ["id", "name", "className", "xpath", "css"]
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

    def get_text(self, path):
        selector, selector_location = self.selector_path(path)
        return self.action_element(selector, selector_location).text

    def get_url(self):
        return self.driver.current_url

    def run(self, action):
        for next in self.one_next(action):
            self.step(next)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    a=analytic_selector(driver)
    a.run("1.打开||http://old.biaodaa.com/")