import datetime
import time
from selenium import webdriver




def is_run(list_a, list_b):
    for x in list_a:
        if x in list_b:
            return True

def is_run_1(list_a, list_b):
    for x in list_a:
        for y in list_b:
            if x == y:
                return True

if __name__ == '__main__':
    list_a = range(100000)
    list_b = range(99999, 200000)
    is_run(list_a, list_b)
    # is_run_1(list_a, list_b)
# driver.find_element_by_xpath("//*[text()='登录']").click()

# paramunittest.TestDemo_0.登录2019-03-26 17:33:09,928569
# a=datetime.datetime.now()
# print("aaa" +  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f"))
