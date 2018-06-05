#coding=utf-8
#短租预定
from time import sleep
from selenium import webdriver
from public.find import Base
class Short_rent(Base):

    loc1 = ("xpath", "//*[@id='quickbook']/a/img")                   #点击快速下单
    loc2 = ("css selector", ".quick2>a>span")                  #点击短租预定
    loc3 = ("css selector", '.select2-chosen')                 #点击入住分店
    loc4 = ("xpath", "//*[@id='select2-drop']/ul/li[5]")          #选择西直门
    loc5 = ("css selector", '#UserName')                        #输入客户姓名
    loc6 = ("css selector", "#UserMobile")                      #输入联系方式
    loc7 = ("xpath", "//*[@id='s2id_SourceTypeID']/a/span[1]")      #点击渠道分类
    loc8 = ("xpath", "//*[@id='select2-drop']/ul/li[3]/div")               #选择去哪了
    loc9 = ("xpath", "//*[@id='s2id_SourceBrandID']/a/span[1]")            #点击渠道品牌
    loc10 = ("xpath", "//*[@id='select2-drop']/ul/li[2]")                   #选择天天如家
    loc11 = ("xpath", "//*[@id='s2id_SourceID']/a/span[1]")         #点击渠道名称
    loc12 = ("xpath", "//*[@id='select2-drop']/ul/li[2]")           #选择去哪-预付
    loc13 = ("css selector", '#SourceBillNumber')                               #输入123456
    loc14 = ("xpath", "//*[@id='s2id_roomType_0']/a/span[1]")       #选择房型
    loc15 = ("xpath", "//*[@id='select2-drop']/ul/li[3]")               #选择豪华大床房
    loc16 = ("xpath", "//*[@id='s2id_roomID_0']/a/span[1]")             #选择房间
    loc17 = ("xpath", "//*[@id='select2-drop']/ul/li/div")              #点击第三个房间
    loc18 = ("xpath", "//*[@id='aOrderStatus_Edit']")                   #点击订单修改
    loc19 = ("css selector", "#Remark1")                                 #输入备注
    loc20 = ("css selector", "#Log_Submit")                              #点击提交


    def ym_dianji(self):
        sleep(1)
        self.click(self.loc1)
        self.click(self.loc2)
        sleep(1)
        self.click(self.loc3)
        self.click(self.loc4)
        self.sendKeys(self.loc5,"傅孟杰")
        self.sendKeys(self.loc6,"13666716051")
        self.click(self.loc7)
        self.click(self.loc8)
        sleep(1)
        self.click(self.loc9)
        self.click(self.loc10)
        self.click(self.loc11)
        self.click(self.loc12)
        self.sendKeys(self.loc13,"123456")
        self.click(self.loc14)
        self.click(self.loc15)
        sleep(1)
        self.click(self.loc16)
        self.clicks(self.loc17)

    def ym_dianji_02(self):
        self.driver.find_element_by_css_selector("#btnSubmit").click()                          #点击下单
        sleep(2)
        """以下是判断点击下单后的俩步确认过程，判断是否之前入住过，入住过会多一个确认按钮"""
        element = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button"
        t = self.driver.find_element_by_xpath(element).text
        print(t)
        if t=="确定":
            self.driver.find_element_by_xpath(element).click()
        else:
            self.driver.find_element_by_css_selector(".aui_state_highlight").click()
            sleep(1)
            self.driver.find_element_by_css_selector(".aui_state_highlight").click()



    def ym_dianji_03(self):
        '''跳出iframe'''
        sleep(2)
        self.click(self.loc18)
        self.driver.switch_to.frame(0)                               #跳出ifarme
        self.sendKeys(self.loc19,'abcdefg')
        self.click(self.loc20)

