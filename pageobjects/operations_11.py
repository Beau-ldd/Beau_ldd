#coding=utf-8
#点击房态管理中的方法
from time import sleep
from public.find import Base
class Butler_service(Base):

    # loc1 = ("xpath", "//*[text()='运营系统']")                   # 点击运营系统
    # loc2 = ("xpath", "//*[text()='订单管理']")                   #点击订单管理
    loc3 = ("xpath","//*[text()='服务管家']")                    #点击服务管家



    def ym_dianji(self):
        """服务管家"""
        sleep(1)
        # self.click(self.loc1)
        # self.click(self.loc2)
        self.click(self.loc3)