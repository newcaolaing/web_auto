import configparser
import os
from base.find_element import FindElement

def class_title(title):
    return "class "+title+"(StartEnd):"


def action(action,tab):
    action_=action[0]
    name=action[1:]
    if "xpath" in name:
        name.remove("xpath")
    if action_ == "open":
        driver = "self.driver.get(\"{}\")"
        return "    "*tab+driver.format(name[0])
    elif action_ =="sendkey":
        driver="self.driver.find_element_by_xpath(\"{}\").send_keys(\"{}\")"
        return "    " * tab + driver.format(name[0],name[1])
    elif action_ =="click":
        driver="self.driver.find_element_by_xpath(\"{}\").click()"
        return "    " * tab + driver.format(name[0])

def def_name(name):
    driver = "def test_{}(self):"
    return "    "  +driver.format(name)




cf = configparser.ConfigParser()  # 使用 configparser模块读取配置文件信息
cf.read("test.ini",encoding="utf-8-sig")
sections = cf.sections()
list=["from test_case.model.myunit import StartEnd"]
for sec in sections:
    list.append(class_title(sec))
    list.append(def_name(cf.get(sec, "def_name")))
    action_list=cf.options(sec)[1:]
    for option in action_list:
        actions = cf.get(sec, option).split("||")
        list.append(action(actions,2))


# for x in cf.keys():
#     if "DEFAULT" != x :
#         list.append(class_title(x))
#         cf.get(x,"1")



with open("1_判断类包含方法及抽象类的创建.py","a+",encoding="utf8") as f:
    for x in list:
        f.write(x+"\n")


# os.system('python 1_判断类包含方法及抽象类的创建.py')




