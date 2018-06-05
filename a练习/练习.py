#coding=utf-8
import unittest
from pageobjects.order_50 import elems_50
from public.logoin_01 import logoin_1
from selenium import webdriver
import time
class land(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome()  # 把浏览器赋值给driver
        cls.driver.maximize_window()
        cls.url = 'http://admin.modo34.com/'
        cls.driver.get(cls.url)
        print(cls.driver.title)
    @staticmethod
    def test_login50(self):
        #静态方法，不需要实例化调用也可以
        '''短租下单'''
        logoin_1(self.driver).login('liujianguo','1')
        elems_50(self.driver).ym_dianji()
        # text=self.driver.find_element_by_css_selector(".panel-heading>div").text

        elems_50(self.driver).ym_dianji_02()
        # text_2=self.driver.find_element_by_css_selector(".panel-body").text

        # self.assertEqual(text,text_2)
        elems_50(self.driver).ym_dianji_03()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()




