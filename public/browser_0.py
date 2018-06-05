#coding=utf-8

#登录的方法
from time import sleep
from selenium import webdriver

class room_yuanqi:
    def __init__(self,driver):
        '''实例化driver'''
        self.driver=driver

    def open_chrome(self):     #定义打开谷歌的方法
        self.driver = webdriver.Firefox()  # 把浏览器赋值给driver
        self.driver.maximize_window()  # 最大化浏览器
        self.driver.implicitly_wait(30)  # 设置元素等待时间
        self.url = 'http://admin.modo34.com/'
        self.driver.get(self.url)
        print(self.driver.title)   # 返回浏览器标签






