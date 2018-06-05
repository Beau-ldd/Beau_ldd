# coding:utf-8
import unittest
import HTMLTestRunner
import time
def all_case():
    # 待执行用例的目录
    case_dir = "D:\\dome_03\\case"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)

    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到testcase
            testcase.addTests(test_case)
            print(testcase)
    return testcase
#https://blog.csdn.net/niedongri/article/details/79045319           discover方法放入for循环去遍历
if __name__ == "__main__":
    # 返回实例
    # runner = unittest.TextTestRunner()
    now= time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = "D:\\dome_true\\result"
    report_path = "D:\\dome_true\\result\\"+now+".html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(fp,
                                           verbosity = 2,
                                           title=u'这是我的自动化测试报告',
                                           description=u'用例执行情况：')
    runner.run(all_case())
    fp.close()