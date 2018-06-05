#coding=utf-8
import unittest
from pageobjects.dj_order_51 import Month_lease
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class land(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """登录方法"""
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.month_lease = Month_lease(cls.driver)
    def test_login12(self):
        '''月长租下单'''
        self.logoin.login()
        self.month_lease.ym_dianji()

        self.month_lease.ym_dianji_02()

        self.month_lease.ym_dianji_03()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()


