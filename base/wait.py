from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.setting import logging


class wait(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_text(self,xpath,name):
        logging.info("正在等待元素"+xpath+":"+name)
        WebDriverWait(self.driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, xpath), name))