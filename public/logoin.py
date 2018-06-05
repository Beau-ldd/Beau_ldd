#coding=utf-8
from time import sleep

class Logoin:
    def __init__(self,driver):
        """初始化"""
        self.driver=driver

    def login(self,username='liujianguo',password='1'):  # 登录的方法

        # self.driver.find_element_by_id('txtAccount').clear()  # 用于清除输入框的默认内容
        self.driver.find_element_by_id('txtAccount').send_keys(username)  # 键盘输入
        # self.driver.find_element_by_id('txtPassword').clear()
        self.driver.find_element_by_id('txtPassword').send_keys(password)
        self.driver.find_element_by_id('Log_Submit').submit()


    def decide(self):
        a = self.driver.find_element_by_id("uPid").text
        self.assertEqual(a, "刘建国")

