#coding=utf-8
#点击房态管理中的方法
from time import sleep
from public.find import Base
class Change_the_price(Base):

    # loc1 = ("xpath", "//*[text()='运营系统']")                   # 点击运营系统
    # loc2 = ("xpath", "//*[text()='订单管理']")                   #点击订单管理
    loc3 = ("xpath","//*[text()='改价管理']")                    #改价管理



    def ym_dianji(self):
        """改价管理"""
        sleep(1)
        # self.click(self.loc1)
        # self.click(self.loc2)
        self.click(self.loc3)