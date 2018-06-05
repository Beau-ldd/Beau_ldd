#coding=utf-8
import unittest
from pageobjects.dj_room05 import The_guest_rooms
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class Forward_to_room(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.elems = The_guest_rooms(cls.driver)


    def test_login05(self):
        '''客房投放价格_5'''
        self.logoin.login()
        self.elems.room_records()

    @classmethod
    def tearDownClass(cls):
        '''退出浏览器'''
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()