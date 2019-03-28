from selenium.webdriver.common.by import By


class LoginView(Common):
    phone=(By.ID,"com.yaobang.biaodada:id/login_user_et")
    pd=(By.ID,"com.yaobang.biaodada:id/login_password_et")
    ennter=(By.ID,"com.yaobang.biaodada:id/login_tv")

    # 我的
    wode=(By.ID,"com.yaobang.biaodada:id/main_nav_wode_rb")
    wode_phone=(By.ID,"com.yaobang.biaodada:id/wode_userphone_tv")



    def login_action(self,phones,pds):
        self.check_lbt()
        logging.info("准备登陆")
        logging.info("账号："+phones+"  "+"密码："+pds)
        self.f_e(*self.phone).send_keys(phones)
        self.f_e(*self.pd).send_keys(pds)
        self.f_e(*self.ennter).click()
        self.driver.implicitly_wait(10)
        try:
            logging.info("正在检查登录是否成功")
            self.f_e(*self.wode).click()
            phone=self.f_e(*self.wode_phone).text
            if phone == phones:
                logging.info(phone+"  账号正常登录")
                return True
            else:
                logging.warning("非指定账号登录："+phone)
        except:
            logging.error("登录失败！！！")
            self.getsceenshot("登录失败")
            return  False