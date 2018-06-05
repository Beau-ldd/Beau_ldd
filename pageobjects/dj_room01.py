#coding=utf-8
from public.find import Base
from time import sleep
class To_room(Base):


    loc1 = ("xpath", "//*[text()='房态管理']")                   # 点击房态管理
    loc2 = ("xpath", "//*[text()='当日房态']")                   #当日房态
    loc3 = ("xpath", '//*[@id="s2id_BranchID"]/a/span[1]')        #点击分店选择框
    loc4 = ("xpath", '//*[@id="select2-drop"]/ul/li[4]')          #选择li【4】中关村店
    loc5 = ("xpath", '//*[@id="btnSearch"]')                         #点击查询按钮


    def ym_dianji(self):                    #点击当日房态的方法
        # 页面的点击事件
        sleep(1)
        self.click_kj(self.loc1)
        sleep(1)
        self.click_kj(self.loc2)
        sleep(1)
        self.click_kj(self.loc3)
        self.click(self.loc4)
        self.click(self.loc5)


    def tag_name_1(self):
        tag = self.driver.find_element_by_xpath('//*[@class="table_inf"]').tag_name
        print(tag)              #定位房间范围，打印出房间范围所有标签


