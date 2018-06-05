#coding=utf-8
import unittest
from pageobjects.dj_room06 import Room_inventory
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class land(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        """房量表"""
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.room = Room_inventory(cls.driver)


    def test_login06(self):
        '''房量表_6'''
        self.logoin.login()
        self.room.ym_dianji()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()