#coding=utf-8
import unittest
from pageobjects.dj_order_50 import Short_rent
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
import time
class land(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.elems = Short_rent(cls.driver)
        # cls.username = int(time.time())         #获取时间戳  好像是需要日志的吧
        cls.logoin.login('liujianguo', '1')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login11(self):
        '''短租下单'''
        # self.logoin.login('liujianguo','1')
        self.elems.ym_dianji()       #填写信息
        self.elems.ym_dianji_02()#点击下单
        self.elems.ym_dianji_03()#订单关闭


if __name__ == '__main__':
    unittest.main()
