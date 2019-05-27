from selenium import webdriver
from selenium.webdriver.firefox.options import Options  as fOptions
from selenium.webdriver.chrome.options import Options   as cOptions
from util.read_ini import Read_Ini
from config.setting import driver_ini_dir,logging



def browser():
    driver_ini=Read_Ini(driver_ini_dir,"driver")
    a,b=driver_ini.get_value("driver"),driver_ini.get_value("head")
    if a == "Firefox":
        if b == "False":
            options = fOptions()
            options.add_argument('-headless')  # 无头参数
            driver = webdriver.Firefox( firefox_options=options)
            logging.info("启动无头火狐")
        else:
            driver = webdriver.Firefox()
            logging.info("启动火狐")
    else:
        if b == "False":
            options = cOptions()
            options.add_argument('-headless')  # 无头参数
            driver = webdriver.Chrome(chrome_options=options,executable_path=r'chromedriver.exe')
            logging.info("启动无头谷歌")
        else:
            driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
            logging.info("启动谷歌")

    return driver



if __name__ == '__main__':
    browser()