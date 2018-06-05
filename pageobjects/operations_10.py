#coding=utf-8
#点击房态管理中的方法
from time import sleep
from public.find import Base
class Room_upgrade(Base):

    # loc1 = ("xpath", "//*[text()='运营系统']")                   # 点击运营系统
    # loc2 = ("xpath", "//*[text()='订单管理']")                   #点击订单管理
    loc3 = ("xpath","//*[text()='房型升级']")                    #点击房型升级



    def ym_dianji(self):
        """房型升级"""
        sleep(1)
        # self.click(self.loc1)
        # self.click(self.loc2)
        self.click(self.loc3)