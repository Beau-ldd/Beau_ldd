#coding=utf-8
#点击房态管理中的方法
from time import sleep
from public.find import Base
class Make_out_an_invoice(Base):

    # loc1 = ("xpath", "//*[text()='运营系统']")                   # 点击运营系统
    loc2 = ("xpath", "//*[text()='发票管理']")                   #点击发票管理
    loc3 = ("xpath","//*[text()='开票信息']")                    #点击开票信息



    def ym_dianji(self):
        """开票信息"""
        sleep(1)
        # self.click(self.loc1)
        self.click(self.loc2)
        self.click(self.loc3)