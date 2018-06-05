#coding=utf-8
import unittest
from pageobjects.dj_room02 import Room_management
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class Forward_to_room(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.elems = Room_management(cls.driver)


    def test_login02(self):
        '''远期房态_2'''
        self.logoin.login()
        self.elems.ym_dianji()

    @classmethod
    def tearDownClass(cls):
        '''退出浏览器'''
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()