import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.setting import logging


class key_next(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_text(self,xpath,name):
        logging.info("正在等待元素"+xpath+":"+name)
        WebDriverWait(self.driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, xpath), name))

    def click(self):
        selector, selector_location = self.selector_path(self.actions[1])
        logging.info("正在点击" + selector_location)
        self.action_element(selector, selector_location).click()

    def open(self):
        logging.info("正在打开：" + self.actions[1])
        self.driver.get(self.actions[1])

    def input(self):
        selector, selector_location = self.selector_path(self.actions[1])
        logging.info("定位元素：" + selector_location + "--正在输入" + self.actions[2])
        self.action_element(selector, selector_location).send_keys(self.actions[2])

    def wait(self):
        selector, selector_location = self.selector_path(self.actions[1])
        self.wait_text(selector_location, self.actions[2])

    def quit(self):
        logging.info("退出浏览器")
        self.driver.quit()

    def refresh(self):
        logging.info("刷新浏览器")
        self.driver.refresh()

    def mysleep(self):
        sj = re.search('\d',self.actions[1]).group(0)
        logging.info(re.sub('\|\|','',self.key))
        time.sleep(int(sj))

    def imsleep(self):
        sj = re.search('\d',self.actions[1]).group(0)
        logging.info(re.sub('\|\|','',self.key))
        self.driver.implicitly_wait(int(sj))