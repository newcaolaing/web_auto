import logging


class  assert_method():
    def __init__(self,selector,result):
        self.selector=selector
        self.result = result



    def run(self):
        if "||" in self.result:
            result_assert=self.result.split("||")
            logging.info("开始断言判断：" + result_assert[0])

            if result_assert[0] == 'url':
                logging.info("当前url为："+self.selector.get_url())
                logging.info("结果url为："+result_assert[1])
                return self.myassert(self.selector.get_url() , result_assert[1])
            elif self.selector.is_path(result_assert[0]):
                logging.info("正在判断："+self.result)
                self.assertTrue(self.selector.get_text(result_assert[0]) == result_assert[1])
        else:
            logging.info("本用例只需要执行不报错即可通过")
            return  True

    def myassert(self,a,b):
        try:
            assert  a == b
            return  True
        except:
            return False
