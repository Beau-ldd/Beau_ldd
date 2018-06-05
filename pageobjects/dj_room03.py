#coding=utf-8
from time import sleep
from public.find import Base
from selenium import webdriver
class Ebooking(Base):

    loc1 = ("xpath", "//*[text()='房态管理']")                   # 点击房态管理
    loc2 = ("xpath", "//*[text()='Ebooking房量表']")               #点击Ebooking房量表


    def room_records(self):
        '''Ebooking房量表'''
        sleep(1)
        self.click(self.loc1)
        sleep(1)
        self.click(self.loc2)

    def Select_query(self):
        '''
        搜索域查询，可以查询数据
        '''
        pass