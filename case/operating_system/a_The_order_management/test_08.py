#coding=utf-8
import unittest
from pageobjects.operations_08 import Order_review
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class land(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """全局变量driver"""
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.room = Order_review(cls.driver)


    def test_login08(self):
        '''订单审核'''
        self.logoin.login()
        self.room.ym_dianji()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()