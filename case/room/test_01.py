#coding=utf-8
import unittest
from pageobjects.dj_room01 import To_room
from public.logoin import Logoin
from public.browser_0 import room_yuanqi
class land(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """登录用户名并判断"""
        room_yuanqi.open_chrome(cls)
        cls.logoin = Logoin(cls.driver)
        cls.elems = To_room(cls.driver)


    def test_login01(self):
        '''当日房态_1'''
        self.logoin.login()
        a = self.driver.find_element_by_id("uPid").text
        self.assertEqual(a, "刘建国")
        self.elems.ym_dianji()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()