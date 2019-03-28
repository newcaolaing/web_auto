
class GetCode:
    """获取验证码图片，解析验证码图片并返回验证码值"""
    def __init__(self, driver):
        self.driver = driver

    # 解析图片获取验证码
    def code_online(self):

        a=input("请输入验证码:\n")
        return a

if __name__ == '__main__':
    a=GetCode(1)