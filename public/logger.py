#coding=utf-8
import logging
import os.path
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        log_name = log_path + rq + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


#
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import os
# import time
#
# def savePngName(name):
#     #import time
#     tm = saveTime()
#     day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
#     type = ".png"
#     fp = "..\\result\\" + day + "\\image"
#     if os.path.exists(fp):
#         filename = str(fp)+"\\" + str(tm)+str("_")+str(name)+str(type)
#         print filename
#         return filename
#     else:
#         os.makedirs(fp)
#         filename = str(fp)+ "\\" + str(tm)+str("_")+str(name)+str(type)
#         print filename
#         return filename
#
# def saveTime():
#     #import time
#     #返回当前系统时间以括号中（2014-08-29-15_21_55）展示
#     return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
#
# def saveScreenshot(driver, name):
#     image = driver.save_screenshot(savePngName(name))
#     return image