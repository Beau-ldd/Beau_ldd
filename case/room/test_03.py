#coding=utf-8
import unittest
from pageobjects.dj_room03 import Ebooking
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class Forward_to_room(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.elems = Ebooking(cls.driver)


    def test_login03(self):
        '''Ebooking房量表_3'''
        self.logoin.login()
        self.elems.room_records()

    @classmethod
    def tearDownClass(cls):
        '''退出浏览器'''
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()