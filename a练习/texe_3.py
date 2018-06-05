# coding:utf-8
from selenium import webdriver
import time,unittest
from selenium.webdriver.support import expected_conditions as EC
class Login(unittest.TestCase):

    def setUp(self):
        url_login = "https://passport.cnblogs.com/user/signin"
        self.driver = webdriver.Firefox()
        self.driver.get(url_login)
    def test_01(self):
        '''前面输入账号密码，让正确运行刡assert返一步，断言故意设置为False丌成功'''
        try:
            self.driver.find_element_by_id("input1").send_keys(u"上海-悠悠")      #定位账号元素并输入
            self.driver.find_element_by_id("input2").send_keys("xxx")             #定位密码元素并输入
            # 登录id是错的，定位会抛异常
            self.driver.find_element_by_id("signin").click()                      #定位登录元素并点击
            # 刞断登录成功页面是否有账号："上海-悠悠"
            time.sleep(3)                                                         #等待3秒
            locator = ("id", "input1")                                  #id（‘lnk_current_user’）元素赋值给locator
            result = EC.text_to_be_present_in_element(locator,u"上海-悠悠")(self.driver)    #定位元素locator，是否等于上海悠悠     后边是全局变量
            self.assertFalse(result)                                                   #报错判断（result）？

        except Exception as msg:                                                    #exception 别名 msg
            print(u"异常原因%s"%msg)                             #打印（异常处理s%）% 错误
            # 图片名称可以加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.jpg' % nowTime)            #.get_screenshot_as_file（截图路径）
            raise
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()