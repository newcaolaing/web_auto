import json
import re


from base.api_method import RunMethod
from config.setting import api_excel_path, logging
from util.exl import Excel_Opertion


api_excel= Excel_Opertion(api_excel_path)
test_case= api_excel.get_data()
print(test_case)


class testapi(RunMethod):
    def __init__(self):
        self.base_url='http://www.httpbin.org'
        self.headers=json.loads(test_case[0]["headers"])
        self.variate_dict={"wo":"test is 大帅哥","channel":"111111111"}



    # 定义变量获取
    def variate(self,name,response=None):
        if name :
            try:
                site,key,value  = re.split(r"[:：]=",name)

                # 请求头部添加变量信息
                if site == "header":
                    self.headers[key] = value

                # 提取response中的变量
                if site == "response-data":
                    pattern=re.findall(value, json.dumps(response.json(),ensure_ascii=False))
                    if pattern:
                        self.variate_dict.update(key=pattern)
            except:
                logging.error(name+" 变量定义失败 ")

    # 变量替换
    def judge(self,name):

        pattern =   re.findall("{{(.*?)}}",name)
        if pattern:
            for s in pattern:
                name=re.sub(r"{{"+s+"}}",self.variate_dict[s],name)
            logging.info(s+" 变量替换为"+self.variate_dict[s])
            return name.encode()
        else:
            logging.info("暂无变量替换")
            return name

    # 断言判断
    def api_assert(self,r, eqs):
        RESULT = []
        eqs==int(eqs) if type(eqs) is float else eqs
        eq = str(eqs).split(",")
        for e in eq:

            # 判断response返回码
            if e.isdigit() and len(str(e))==3:
                if r.status_code  == e:
                    RESULT.append(True)
                else:
                    RESULT.append(False)
            # 完全等于
            elif ":=" in e:
                e=e.strip(":=")
                if r.text == e:
                    RESULT.append(True)
                else:
                    RESULT.append(False)

            # 包含
            else:
                if e in r.text:
                    RESULT.append(True)
                else:
                    RESULT.append(False)

        return RESULT


    def one_test(self,case,test_case):
        # 头部变量信息获取
        self.variate(case["variate"])

        # 判断data中是否需要将变量替换
        case["data"] = self.judge(case["data"])
        logging.info(case["data"])

        r = self.run_request(case["method"], self.base_url + case["url"], data=case["data"],
                             header=self.headers)
        logging.info(r.json())

        # 采集变量信息
        self.variate(case["variate"], r)

        # 断言
        case_index = test_case.index(case)
        case["eq_result"] = self.api_assert(r, case["eq"])

        # 断言后excel更新断言状态
        logging.info("当前更新第" + str(case_index + 1) + "条用例 eq_result")
        api_excel.api_update_data(case_index + 2, 13, str(case["eq_result"]))

        # 将断言状态信息返回
        return case["eq_result"]



    def run(self):
        global test_case
        for case in test_case:
            eq_result = {}
            # 判断是否执行用例
            if case["isshow"] == "T":
                logging.info("正在执行" + case["TEST_ID"] + "用例")
                # 判断是否为测试集
                if case["test_set"]:
                    test_set=case["test_set"].split(",")
                    print(test_set)

                    # 执行测试集中的用例
                    for test in test_set:
                        for case in test_case:
                            if test == case["TEST_ID"]:
                                one_result=self.one_test(case,test_case)
                                eq_result[case["TEST_ID"]]=one_result

                    # 断言后excel更新断言状态
                    case_index = test_case.index(case)
                    logging.info("当前更新第" + str(case_index + 1) + "条用例 eq_result")
                    api_excel.api_update_data(case_index + 2, 13, str(eq_result))

                else:
                    self.one_test(case,test_case)



                    test_case=[case if x == case else x for x in test_case]
                    logging.info(test_case)





if __name__ == '__main__':
    testapi().run()

