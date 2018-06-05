#coding=utf-8
import unittest
from pageobjects.dj_room01 import elems
# from public.logger import Logger
from public import logoin_01
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

class land(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()     # 把浏览器赋值给driver
        self.driver.maximize_window()
        # 最大化浏览器)
        self.driver.implicitly_wait(30)      # 设置元素等待时间
        url = 'http://admin.modo33.com'
        self.driver.get(url)            #打开url
        print(self.driver.title)              # 返回浏览器标签
    def test_login01(self):
        logoin_01.login(self, 'liujianguo', '1')
        # mylogger.info("登录")
        elems(self.driver).ym_dianji()
        #********************************************************************************
        # a=self.driver.find_elements_by_class_name('roomtype_0')  #
        # print(a)
        # for i in range(len(a)):
        #     print(i)
        #     a[0].click()    #双击  为什么点击就可以？
        #     time.sleep(5)
        #     a = self.driver.find_elements_by_class_name('roomtype_0')  #
        # c = self.driver.find_elements_by_xpath('//*[text()=u"我的订单"]')
        # print(c)
        # ***************************************************************************************
        # ***************************************************************************************
        q = self.driver.find_elements_by_css_selector("div>.roomtype_0")                                                    # self.driver.find_elements_by_class_name('roomtype_0')
        w = self.driver.find_elements_by_xpath('//a[class="f_roomStatus"]')
        print(len(q))
        print(len(w))
        self.assertEqual(len(q),len(w))      #断言1，1是否相等
        # if len(q)== len(w):
        #     print("房间数目正确")
        # else:
        #     print("数目不正确")
        # text = self.driver.find_element_by_class_name('table_inf').text
        # print(text.startswith(u'中'))          #print  startswith  判断以什么开头，返回布尔值

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()