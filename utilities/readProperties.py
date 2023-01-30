import configparser
import os

config= configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:

    @staticmethod
    def getBaseURL():
        url=config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def getUID():
        uid=config.get('commonInfo','UID')
        return uid

    @staticmethod
    def getPWD():
        pwd = config.get('commonInfo', 'pwd')
        return pwd

