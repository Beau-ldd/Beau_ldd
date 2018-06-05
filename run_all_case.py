# coding:utf-8
import HTMLTestRunner
import unittest
import time
# 待执行用例的目录
case_dir =("D:\\dome_true\\case")
testcase = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(case_dir,
                                        pattern="test*.py",
                                        top_level_dir=None)

if __name__ == "__main__":
    # 返回实例

    report_path = "D:\\dome_true\\result"
    now= time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = "D:\\dome_true\\result\\"+now+".html"
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'这是我的自动化测试报告',
                                           description=u'用例执行情况：',
                                           retry=1)
    runner.run(discover)
    fp.close()
    print("测试已全部完成，可前往D:\\dome_true\\result 查询测试报告")
    # run所有用例
