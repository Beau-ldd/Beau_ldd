#coding=utf-8
#点击房态管理中的方法
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from public.find import Base
class Room_inventory(Base):

    loc1 = ("xpath", "//*[text()='房态管理']")                   # 点击房态管理
    loc2 = ("xpath", "//*[text()='房量表']")                   #点击房量表
    loc3 = ("xpath", "//*[@id='s2id_CityID']/a/span[1]")                  #点击分店下拉框
    loc4 = ("xpath","//*[@id='select2-drop']/ul/li[2]" )        # 选择
    loc5 = ("xpath", ".//*[@id='btnSearch2']")                           #点

    def ym_dianji(self):
        """点击房量表"""
        sleep(1)
        self.click(self.loc1)
        sleep(1)
        self.click(self.loc2)
        sleep(1)
        self.click(self.loc3)
        self.click(self.loc4)
        self.click(self.loc5)