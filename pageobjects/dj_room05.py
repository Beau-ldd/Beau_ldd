#coding=utf-8
from time import sleep
from public.find import Base
from selenium import webdriver
class The_guest_rooms(Base):

    loc1 = ("xpath", "//*[text()='房态管理']")                   # 点击房态管理
    loc2 = ("xpath", "//*[text()='客房投放价格']")               #点击客房投放价格


    def room_records(self):
        '''占房记录'''
        sleep(1)
        self.click(self.loc1)
        sleep(1)
        self.click(self.loc2)

    def Select_query(self):
        '''
        搜索域查询，可以查询数据
        '''
        pass