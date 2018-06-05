#coding=utf-8
#点击房态管理中的方法
from time import sleep
from public.find import Base
class Order_center(Base):

    # loc1 = ("xpath", "//*[text()='运营系统']")                   # 点击运营系统
    # loc2 = ("xpath", "//*[text()='订单管理']")                   #点击订单管理
    # loc3 = ("xpath", "//*[text()='订单中心']")                   #点击订单中心
    loc4 = ("css selector", ".dd_mx_b5.xiangqing")                #点击详情


    def ym_dianji(self):
        """订单中心"""
        sleep(1)
        # self.click(self.loc1)
        # sleep(1)
        # self.click(self.loc2)
        # self.click(self.loc3)
        self.clicks(self.loc4)