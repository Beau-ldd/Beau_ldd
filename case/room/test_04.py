#coding=utf-8
import unittest
from pageobjects.dj_room04 import Records_of_room
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class Forward_to_room(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.elems = Records_of_room(cls.driver)


    def test_login04(self):
        '''占房记录_4'''
        self.logoin.login()
        self.elems.room_records()

    @classmethod
    def tearDownClass(cls):
        '''退出浏览器'''
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()