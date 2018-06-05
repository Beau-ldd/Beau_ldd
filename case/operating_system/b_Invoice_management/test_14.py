#coding=utf-8
import unittest
from pageobjects.Invoice_14 import Tax_controller_setting
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class land(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """全局变量driver"""
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.room = Tax_controller_setting(cls.driver)


    def test_login09(self):
        '''税控器设置'''
        self.logoin.login()
        self.room.ym_dianji()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()