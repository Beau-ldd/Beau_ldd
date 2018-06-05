# # coding:utf-8
# import unittest
# class Test(unittest.TestCase):
#     def test01(self):
#         '''刞断 a == b '''
#         a = 1
#         b = 1
#         self.assertEqual(a, b)
#     def test02(self):
#         '''刞断 a in b'''
#         a = "hello"
#         b = "hello world!"
#         self.assertIn(a, b)
#     def test03(self):
#         '''刞断 a isTrue '''
#         a = True
#         self.assertTrue(a)
#     def test04(self):
#         '''失败案例'''
#         a = "上海-悠悠"
#         b = "yoyo"
#         self.assertEqual(a, b)
#     if __name__ == "__main__":
#         unittest.main()


# # coding:utf-8
# import unittest
# import time
# class Test(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("start!")
#     @classmethod
#     def tearDownClass(cls):
#         time.sleep(1)
#         print("end!")
#     def test01(self):
#         print("执行测试用例01")
#     def test03(self):
#         print("执行测试用例03")
#     def test02(self):
#         print("执行测试用例02")
#     def addtest(self):
#         print("add方法")
#     if __name__ == "__main__":
#         unittest.main()


#
# import HTMLTestRunner
# # coding:utf-8
# import unittest
# def all_case():
# # 待执行用例的目录
#     case_dir = "\\testsuits\\"
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
# # discover方法筛选出来的用例，循环添加到测试套件中
#     for test_suite in discover:
#         for test_case in test_suite:
#     #添加用例到testcase
#             testcase.addTests(test_case)
#             print(testcase)
#             return testcase
#         if __name__ == "__main__":
#     #返回实例
#             runner = unittest.TextTestRunner()
#             report_path = "\\logs\\result.html"     #储存地址
#             fp = open(report_path, "wb")
#             runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                                title=u'这是我的自动化测试报告',
#                                                description=u'用例执行情况：')
#         # run所有用例
#             runner.run(all_case())
#             fp.close()



