# coding=utf-8
import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow import threads


# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))      #返回全路径
casepath = os.path.join(curpath, "case")                   #合并目录
if not os.path.exists(casepath):
    print("测试用例需放到‘case’文件目录下")
    os.mkdir(casepath)                                     #创建目录os.mkdir(目录)
reportpath = os.path.join(curpath, "report")
if not os.path.exists(reportpath): os.mkdir(reportpath)


def add_case(case_path="D:\\dome_true\\case", rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='ERP测试报告', log_path='report')

if __name__ == "__main__":
    # 用例集合
    cases = add_case()

    print(cases)
    for i in cases:
        print(i)
        run(i)
