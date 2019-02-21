import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")     #获取到配置文件的路径

class RedaConfig:
    def __init__(self):     #类的构造器
        self.cf = configparser.ConfigParser()       #实例化configparser类
        self.cf.read(configPath)        #读取配置值

    def get_email(self, name):      #获取配置值
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value