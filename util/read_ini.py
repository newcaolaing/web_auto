from config.setting import config_ini_dir
import configparser

class Read_Ini(): # 初始化
    def __init__(self,cf =None,node = None):
        self.node = node if node else 'registerElment'
        self.cf = self.load_ini(cf) if cf else self.load_ini()


    def load_ini(self,config_ini_dir=config_ini_dir):  # 加载文件
        cf = configparser.ConfigParser()  # 使用 configparser模块读取配置文件信息
        cf.read(config_ini_dir)  # 配置文件所在路径
        return cf

    def get_value(self,key): # 获取配置文件中key的value值
        data = self.cf.get(self.node,key)
        return data


if __name__ == '__main__':
    a=Read_Ini()
    a=a.get_value("register_button")
    print(a)