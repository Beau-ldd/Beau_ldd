#coding=utf-8
from time import sleep
from public.find import Base
from selenium import webdriver
class Room_management(Base):

    loc1 = ("xpath", "//*[text()='房态管理']")                   # 点击房态管理
    loc2 = ("xpath", "//*[text()='远期房态']")                   #点击远期房态
    loc3 = ("xpath", '//*[@id="s2id_CityID"]/a/span[1]')        # 点击城市选择框
    loc4 = ("xpath", '//*[@id="select2-drop"]/ul/li[2]')        #选择【北京】
    loc5 = ("id", 'all')                                        #点击全选，全选取消
    loc6 = ("xpath", "//*[@id='BranchID_4']")                   #勾选中关村店
    loc7 = ("xpath", '//*[@id="btnSearch2"]')                   #点击查询按钮




    def ym_dianji(self):
        """远期房态"""
        sleep(1)
        self.click(self.loc1)
        sleep(1)
        self.click(self.loc2)
        sleep(1)
        frame = self.driver.find_element_by_id("Roomstatus")  # iframe 定位
        self.driver.switch_to_frame(frame)
        self.click(self.loc3)
        self.click(self.loc4)
        self.click(self.loc5)
        self.click(self.loc6)
        self.click(self.loc7)

    def Operating(self):
        """操作房间"""
        pass
    # def text_true(self):
    #     """for循环打印出元素，再判断......好吧，我不会写！！！！"""
    #     t = self.driver.find_element_by_xpath("//*[@class='textbox']").text    #定位房间范围，打印出房间范围所有标签
    #     for i in t:
    #         print(i)
    #     b = i.startswith(u'中')
    #     print(b)
