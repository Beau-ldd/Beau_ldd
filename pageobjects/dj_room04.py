#coding=utf-8
from time import sleep
from public.find import Base
from selenium import webdriver
class Records_of_room(Base):

    loc1 = ("xpath", "//*[text()='房态管理']")                   # 点击房态管理
    loc2 = ("xpath", "//*[text()='占房记录']")                   #点击占房记录


    def room_records(self):
        '''占房记录'''
        sleep(1)
        self.click(self.loc1)
        sleep(1)
        self.click(self.loc2)

    def validation(self):
        '''验证进入后，导航栏是否正确'''
        pass

    def check(self):
        '''搜索域查询'''
        pass