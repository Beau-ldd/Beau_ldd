#coding=utf-8
import unittest
from pageobjects.operations_07 import Order_center
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class land(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """全局变量driver"""
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.room = Order_center(cls.driver)


    def test_login07(self):
        '''订单中心不需要点击，特殊的一个模块'''
        self.logoin.login()
        self.room.ym_dianji()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()