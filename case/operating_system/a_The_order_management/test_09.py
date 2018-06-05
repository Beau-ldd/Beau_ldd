#coding=utf-8
import unittest
from pageobjects.operations_09 import Change_the_price
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class land(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """全局变量driver"""
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.room = Change_the_price(cls.driver)


    def test_login09(self):
        '''改价管理'''
        self.logoin.login()
        self.room.ym_dianji()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()