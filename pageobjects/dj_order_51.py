#coding=utf-8
#月长租下单
from time import sleep
from public.find import Base
from selenium import webdriver


class Month_lease(Base):

    loc1 = ("css selector", ".quickbook>img")                # 点击快速下单
    loc2 = ("css selector", ".quick3>a>span")                 # 点击月长租预定
    loc3 = ("xpath", "//*[@id='s2id_BranchID']/a/span[1]")      # 点击入住分店
    loc4 = ("xpath", "//*[@id='select2-drop']/ul/li[4]")           #选择西直门
    loc5 = ("css selector", '#UserName')                         #输入客户姓名
    loc6 = ("css selector", "#UserMobile")                  #输入联系方式
    loc7 = ("xpath", "//*[@id='s2id_SourceTypeID']/a/span[1]")             #点击渠道分类
    loc8 = ("xpath", ".//*[text()='去哪儿']")                #选择去哪儿//*[@id='select2-drop']/ul/li[3]/div
    loc9 = ("xpath", "//*[@id='s2id_SourceBrandID']")                #点击渠道品牌
    loc10 = ("xpath", "//*[@id='select2-drop']/ul/li[2]")               #选择天天如家
    loc11 = ("xpath", "//*[@id='s2id_SourceID']/a/span[1]")           #点击渠道名称
    loc12 = ("xpath", "//*[@id='select2-drop']/ul/li[2]")            #选择去哪-预付
    loc13 = ("xpath", "//*[@id='startDate_0']")               #点击入住日期
    # iframe1 = self.driver.find_element_by_xpath("//*[@height='7']")           #进入iframe
    # self.driver.switch_to.frame(iframe1)
    loc14 = ("xpath", '//td[1][@valign="top"]/table/tbody/tr[6]/td[5]')    #选择2018-5-17
    loc15 = ("xpath", "//td[2][@valign='top']/table/tbody/tr[5]/td[6]")              #选择2018-6-30
    # self.driver.switch_to.default_content()  # 跳出iframe
    loc16 = ("xpath", "//*[@id='s2id_roomID_0']/a/span[1]")         #点击房间
    loc17 = ("xpath", "//*[@id='select2-drop']/ul/li[2]/div")           #现在房间
    loc18 = ("xpath", "//*[@id='averagePrice_0']")              #输入月租金
# *******************************************************************************************************
    loc19 = ("xpath", "//*[@id='btnSubmit']")  # 点击提交
    loc20 = ("css selector", ".aui_state_highlight")  # 点击保存
# **************************************************************************************************************
    loc21 = ("css selector", "#aOrderStatus_Edit")  # 点击订单处理
    # iframe2 = self.driver.find_element_by_xpath("//*[@frameborder='0']")  # 跳进iframe
    # self.driver.switch_to.frame(iframe2)
    loc22 = ("css selector", "#Remark1")  # 输入备注
    loc23 = ("css selector", "#Log_Submit")  # 点击提交




    def ym_dianji(self):
        # 月长租订单输入信息页面
        sleep(1)
        self.click(self.loc1)
        self.click(self.loc2)
        sleep(1)
        self.click_kj(self.loc3)
        self.click(self.loc4)
        self.sendKeys(self.loc5,"刘建国")
        self.sendKeys(self.loc6,"15149376446")
        sleep(1)
        self.click_kj(self.loc7)
        self.click_kj(self.loc8)
        sleep(1)
        self.click_kj(self.loc9)
        sleep(2)
        self.click_kj(self.loc10)
        sleep(1)
        self.click(self.loc11)
        self.click(self.loc12)
        self.click(self.loc13)
        iframe1 = self.driver.find_element_by_xpath("//*[@height='7']")           #进入iframe
        self.driver.switch_to.frame(iframe1)
        sleep(1)
        self.click(self.loc14)
        self.click(self.loc15)
        self.driver.switch_to.default_content()  # 跳出iframe
        sleep(1)
        self.click(self.loc16)
        self.click(self.loc17)
        self.sendKeys(self.loc18,"9000")
        sleep(1)

    def ym_dianji_02(self):
        self.click(self.loc19)
        self.click(self.loc20)
        sleep(1)


    def ruzhu(self):
        '''这里可以转入住，签合同'''
        pass


    def ym_dianji_03(self):
        sleep(1)
        self.click(self.loc21)
        iframe2 = self.driver.find_element_by_xpath("//*[@frameborder='0']")    #跳进iframe
        self.driver.switch_to.frame(iframe2)
        self.sendKeys(self.loc22,"测试数据类型")
        self.click(self.loc23)